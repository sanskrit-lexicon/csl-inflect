# csl-inflect Pipeline Manual

_Created: 11-07-2026 · Last updated: 11-07-2026_

The operator manual for csl-inflect: rebuilding the declension and
conjugation tables from their MW/Huet inputs, loading the five SQLite
databases, and running the "inflected forms" PHP lookup app — end-to-end,
without reading the source. The repo bridges two scholarly paradigm datasets
(Gérard Huet's Sanskrit Heritage conjugation data and a declension engine
descended from Deshpande's work) to CDSL/Monier-Williams headwords.

Companion metadoc: [docs/PIPELINE_MANUAL.meta.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/docs/PIPELINE_MANUAL.meta.md).

---

## 1. Cheat-sheet — the whole pipeline on one screen

```bash
# 0. ONLY when Huet republishes his data (~monthly) — refresh the Huet import:
cd huetdata/download
curl https://sanskrit.inria.fr/DATA/XML/SL_morph_dtd.txt -o SL_morph.dtd
curl https://sanskrit.inria.fr/DATA/XML/SL_morph.xml.gz -o SL_morph.xml.gz
gunzip SL_morph.xml.gz            # SL_morph.xml is ~large and NOT committed
cd ..
sh redo.sh                        # 8 tenses: extract/ + MW-respelled mapextract/

# 1. Full rebuild (nominals → verbs → sqlite), from the repo root:
sh redo.sh

# 2. Run the lookup app locally (needs PHP; DBs must exist in sqlite/db/):
cd web && php -S localhost:8080   # open http://localhost:8080/index.php
```

`redo.sh` at each level just chains the level below — every stage can be run
alone from its own directory with its own `redo.sh`, which is how you rerun
one stage after touching one input.

## 2. Data-flow diagram

```
INPUTS (three independent sources)
│
├─ MW nominals: nominals/pysanskritv2/inputs/lexnorm-all2.txt
│    (copied from funderburkjim/MWlexnorm step2 — L-number, headword,
│     compound-marked headword, gender/stem hints)
│
├─ MW verb roots: verbs/pysanskritv2/inputs/verb_cp_orig.txt
│    (MW's class-pada "cp" data) + mw_genuine_roots.txt filter
│
└─ Huet: huetdata/download/SL_morph.xml   ← downloaded, NOT in git
     │  sh huetdata/redo.sh  (= redo_one.sh × aor prf prs fut pef cnd ben inj)
     │    verbs_tp.py / verbs-prim-prs.py  → extract/huet_{stems,conj_tables}_*.txt
     │    huet_mw_map.py + the 678-entry curated crosswalk huet_mw_map_data.py
     ▼         (Huet root spelling → MW root spelling)
   huetdata/mapextract/huet_conj_tables_*.txt
     │  (hand-reconciled into…)
     ▼
   verbs/pysanskritv2/manual/tables_*.txt  (per-tense "manual" model tables)

NOMINAL CHAIN  (nominals/pysanskritv2/, 2 stages)
  stems/   stems.py → remove_dups.py → remove_gdups.py → stem_model_diff.py
             lexnorm-all2.txt ──────────────────────────→ calc_stems.txt
  tables/  decline_file.py → corrections.py (+ correction_inventory.txt)
             calc_stems.txt ───────────────────────────→ calc_tables.txt

VERB CHAIN  (verbs/pysanskritv2/, 4 stages: inputs → models → bases → tables)
  inputs/  clean.py → genuine_filter.py → verb_cp.txt (root:Lrefs:class-voice)
           verb_cp_manual.py + manual/tables_{aorist,aorist_passive,prf}.txt
  models/  root_model.py per tense (present passive fut pft con ben inj ppf
           aor aor_passive prf) → cat → calc_models.txt
  bases/   bases_test2.py (mines pysanskritv1/test2.py, the elispsanskrit
           port) → calc_bases.txt
  tables/  conjugate_from_bases.py + manual_tables_inventory.txt
             ──────────────────────────────────────────→ calc_tables.txt

SQLITE  (sqlite/, 5 databases → sqlite/db/*.sqlite, NOT committed)
  lgmodel   model code → description + "Kale N" grammar reference
  lgtab1    nominal calc_tables.txt   (model, stem, MW refs, 24-form table)
  lgtab2    inverted index: each declined form → (model, stem)   [make_input.py]
  vlgtab1   verb calc_tables.txt      (model, stem, MW refs, 9-form table)
  vlgtab2   inverted index: each conjugated form → (model, stem) [make_input.py]

WEB  (web/, PHP)
  index.php + getWord.php + dal.php (+ utilities/transcoder)
  lookup of an inflected form: vlgtab2/lgtab2 → full table from vlgtab1/lgtab1
  → grammar reference via lgmodel; input transcoded to SLP1 first
  dal.php hardcodes the DB location: ../sqlite/db/{name}.sqlite
```

## 3. Step-by-step operator walkthrough

### 3.1 Huet refresh (`huetdata/`) — only when Huet's data changes

Huet recomputes his database at the end of a month
([huetdata/readme.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/readme.md)).
Download per the cheat-sheet (§1, step 0 — instructions also in
[huetdata/download/readme.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/download/readme.md)),
then:

```bash
cd huetdata
sh redo.sh            # all 8 tenses; or one at a time:
sh redo_one.sh aor    # aor | prf | prs | fut | pef | cnd | ben | inj
```

Each `redo_one.sh <tense>` run:

1. extracts that tense's paradigms from `download/SL_morph.xml` with
   [verbs_tp.py](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/verbs_tp.py)
   (most tenses) or
   [verbs-prim-prs.py](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/verbs-prim-prs.py)
   (`prs`, `pef`) → `extract/huet_stems_<tense>.txt` +
   `extract/huet_conj_tables_<tense>.txt`;
2. rewrites root spellings to MW conventions with
   [huet_mw_map.py](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/huet_mw_map.py)
   reading the hand-curated 678-entry crosswalk
   [huet_mw_map_data.py](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/huet_mw_map_data.py)
   → `mapextract/huet_conj_tables_<tense>.txt`.

This crosswalk is the repo's reason to exist: Huet's root spellings and
CDSL/MW headword spellings disagree often enough that a naive join misses
entries. Table-line format (9 fields = 3s 3d 3p 2s 2d 2p 1s 1d 1p,
alternatives `/`-separated, all SLP1):

```
kfz aor 4P:[akArkzIt/akrAkzIt akArzwAm/akrAzwAm … akArkzma/akrAkzma]
```

The `mapextract/` tables were reconciled (a manual act, not a script) into
`verbs/pysanskritv2/manual/` — that is how Huet data reaches the verb chain.
[huetdata/nominals/](https://github.com/sanskrit-lexicon/csl-inflect/tree/main/huetdata/nominals)
(`nouns.py`) similarly extracts Huet's noun stems + genders for comparison.

### 3.2 Nominal declensions (`nominals/pysanskritv2/`)

```bash
cd nominals && sh redo.sh     # or run stems/ and tables/ separately
```

**Stage 1 — `stems/`** (from `../inputs/lexnorm-all2.txt`, a copy of
[funderburkjim/MWlexnorm step2](https://github.com/funderburkjim/MWlexnorm/blob/master/step2/lexnorm-all2.txt)):
`stems.py` derives the initial stem+model list, then two dedup passes
(`remove_dups.py` for same model + un-hyphenated stem, `remove_gdups.py` for
feminine same-stem duplicates — each writes a `*_log.txt` audit), then
`stem_model_diff.py` splits off `stems_problem.txt` → **`calc_stems.txt`**.

**Stage 2 — `tables/`**: `decline_file.py` declines every stem per its model
→ `calc_tables0.txt`, then `corrections.py` applies
`correction_inventory.txt` (the hand-maintained fix list) →
**`calc_tables.txt`** — one line per (model, stem): MW refs + the 24-form
table (1 form for `ind` indeclinables). The standalone engine in
[nominals/pydecl/](https://github.com/sanskrit-lexicon/csl-inflect/tree/main/nominals/pydecl)
(`decline.py`, `decline_f.py`, `decline_irr.py`, …) is the algorithm library
this pipeline draws on.

### 3.3 Verb conjugations (`verbs/pysanskritv2/`) — 4 stages

```bash
cd verbs && sh redo.sh        # = inputs → models → bases → tables, in order
```

1. **`inputs/`** — `clean.py` normalizes MW's class-pada data
   (`verb_cp_orig.txt`), `genuine_filter.py` keeps only
   `mw_genuine_roots.txt` roots → **`verb_cp.txt`**
   (`root:Lrefs:class-voice`, e.g. `BU:151456:1a,1m`); `verb_cp_manual.py`
   builds the aorist/aorist-passive/perfect input lists against the
   `manual/` tables (the Huet-derived ones from §3.1).
2. **`models/`** — `root_model.py` is run once per tense family (present,
   passive, fut, pft, con, ben, inj, ppf from Deshpande-305, aor,
   aor-passive, prf), each writing `calc_models_<t>.txt`; the stage ends
   with `cat calc_models_*.txt > calc_models.txt`. **The stage starts with
   `rm calc_models_*.txt`** — never keep hand-edits inside that directory
   under a `calc_` name; they are deleted on the next run (`calc_` = always
   recomputed, by convention).
3. **`bases/`** — `bases_test2.py` mines conjugation *bases* out of
   [verbs/pysanskritv1/](https://github.com/sanskrit-lexicon/csl-inflect/tree/main/verbs/pysanskritv1)'s
   `test2.py` (the surviving core of funderburkjim/elispsanskrit) →
   `calc_bases.txt`. `pysanskritv1` is kept *only* to feed this stage;
   `pysanskrit_work/` is an unfinished rewrite, used by nothing.
4. **`tables/`** — `conjugate_from_bases.py` combines bases with ending
   tables, consulting `manual_tables_inventory.txt` for overrides →
   **`calc_tables.txt`** (model, stem, MW refs, 9-form table).

### 3.4 SQLite load (`sqlite/`)

```bash
cd sqlite && sh redo.sh       # loops: lgmodel lgtab1 lgtab2 vlgtab1 vlgtab2
```

Each subdirectory's `redo_<name>.sh` drops any old `.sqlite`, runs
`sqlite3 <name>.sqlite < <name>.sql` (the `.sql` does a tab-separated
`.import` of the source file and prints the row count — **watch that count**,
it is the stage's only self-check), and moves the result to `sqlite/db/`.
The two `*tab2` databases first run their `make_input.py` to invert the
`*tab1` data into a form → (model, stem) index — that inversion is what makes
form-based lookup possible. Sources, per
[sqlite/readme.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/sqlite/readme.md):

| DB | Source | Content |
|---|---|---|
| `lgmodel` | `lgmodel/lgmodel_input.txt` | model code → description + Kale Higher Sanskrit Grammar page ref |
| `lgtab1` | `nominals/pysanskritv2/tables/calc_tables.txt` | declension tables |
| `lgtab2` | inverted from lgtab1 | declined form → (model, stem) |
| `vlgtab1` | `verbs/pysanskritv2/tables/calc_tables.txt` | conjugation tables |
| `vlgtab2` | inverted from vlgtab1 | conjugated form → (model, stem) |

`sqlite/db/` holds only a readme in git — **the built `.sqlite` files are
local artifacts**; a fresh clone must run the pipeline (or copy them from a
deployment) before the web app works.

### 3.5 The lookup app (`web/`)

A no-framework PHP app ("inflected form lookup"): `index.php` (UI) →
`getWord.php` (accepts `?word=…` in any transliteration, converts to SLP1 via
`utilities/transcoder`) → `dal.php` (queries `../sqlite/db/{name}.sqlite`,
path hardcoded). Lookup path: form → `lgtab2`/`vlgtab2` → full table from
`lgtab1`/`vlgtab1` → grammar reference via `lgmodel`. `getWord.php` also runs
from the CLI (`php getWord.php rAmaH`) — the quickest smoke test. Local
serving: `cd web && php -S localhost:8080`. Deployment is the Cologne-server
copy of this same layout — `web/` and `sqlite/db/` must travel together.

## 4. Environment & prerequisites

- **python3** on PATH (plain scripts, no third-party packages, no build step).
- **sqlite3** CLI (the `.sql` loaders use `.import`).
- **sh** — every driver is a Bourne-shell script; on Windows run them from
  Git Bash, not PowerShell.
- **PHP** (CLI or any web server) — only for `web/`.
- **curl + gunzip** — only for the Huet refresh (§3.1).
- **Data prerequisite:** `huetdata/download/SL_morph.xml` is not in git;
  without it only the `huetdata/` stage is blocked (its committed
  `extract/`/`mapextract/` outputs keep the rest of the pipeline runnable).

## 5. Symptom → cause → cure

| Symptom | Cause | Cure |
|---|---|---|
| `huetdata/redo.sh` prints `Unknown htense=ben` (and for `prf`) | Real defect in [redo_one.sh](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/redo_one.sh): the line `elif [ $htense == "ben" ] [ $htense == "prf" ]` is missing its `\|\|`, so the test errors out and both tenses fall through to the `else` | Fix the script (add `\|\|`); until then run those tenses by editing the branch — the committed `extract/`/`mapextract/` ben/prf files predate the bug's visibility |
| `redo_one.sh` fails with "can't open download/SL_morph.xml" | Huet data never downloaded (not committed) | §3.1 / [download/readme.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/download/readme.md) |
| Web app renders but every lookup returns nothing | `sqlite/db/*.sqlite` missing (fresh clone) — dal.php's `../sqlite/db` path finds no files | Run `cd sqlite && sh redo.sh` (needs both calc_tables.txt built first), or copy the DBs from a deployment |
| A `select count(*)` printed during `sqlite/redo.sh` is 0 or tiny | The upstream `calc_tables.txt` is missing/truncated — the `.import` silently loads whatever is there | Rebuild the owning chain (§3.2 / §3.3) and re-run the loader |
| Hand-edited a `calc_models_*.txt` and the edit vanished | `models/redo.sh` starts with `rm calc_models_*.txt`; every `calc_` file is recomputed by contract | Put the change in the stage's *inputs* (`manual/tables_*.txt`, `verb_cp_extra.txt`) or in `root_model.py`, never in a `calc_` output |
| Declension output wrong for a known-irregular stem | Fix belongs in the corrections layer | Add a row to `nominals/pysanskritv2/tables/correction_inventory.txt`, rerun the tables stage |
| A nominal missing entirely | Dropped in the stems stage — check the audit logs `calc_stems_dup_log.txt` / `calc_stems_gdup_log.txt` / `stems_problem.txt` | If wrongly deduped/probleme'd, adjust the stems stage inputs; the logs name each dropped stem |
| A Huet verb table not attaching to its MW root | Root spelling not in the crosswalk | Add/curate the entry in `huetdata/huet_mw_map_data.py` (678 entries as of 07-2026), rerun `redo_one.sh <tense>` |
| `redo.sh` scripts do nothing / `cd` errors on Windows PowerShell | They are `sh` scripts | Run from Git Bash |
| `lgtab1`/`vlgtab1` redo scripts mention `../../outputs/nominals/stem_model_tab.txt` which doesn't exist | Vestigial `smfile=` variable, unused — the `.sql` file names the real source | Ignore (or delete the dead lines); nothing reads `smfile` |

## 6. Glossary

| Term | Meaning |
|---|---|
| SLP1 | The ASCII transliteration all data files use (`BU` = bhū) |
| model | A paradigm code naming *how* a stem inflects; `lgmodel` links each to a page of Kale |
| Kale | M. R. Kale, *A Higher Sanskrit Grammar* — the reference grammar the lookup app cites |
| cp / class-voice | MW's conjugation-class + pada data (`1a,1m` = class 1 active + middle) |
| P / A / Q | parasmaipada (active) / ātmanepada (middle) / passive, in Huet table IDs |
| tense codes | aor aorist · ben benedictive · cnd/con conditional · fut simple future · inj injunctive · pef/pft periphrastic future · prf perfect · ppf periphrastic perfect · prs present system (present, imperfect, imperative, optative). Both `cnd/con` and `pef/pft` spellings occur (huetdata vs verbs models) — same tense, two codes |
| lexnorm | MWlexnorm's per-headword inflection hint (`m:f#I:n` gender/stem info or `LEXID=…` for pronouns/numerals) |
| L-number / Lrefs | Cologne record id(s) of a headword/root in the MW digitization |
| `calc_*` | "Computed — never hand-edit" file-naming convention; every stage may delete and rewrite them |
| 24-form / 9-form table | Nominals: 8 cases × 3 numbers; verbs: 3 persons × 3 numbers |
| base | The stage-3 verb intermediate: stem-like string a tense's ending table attaches to |

## 7. Maintainer appendix

- **Per-directory division of labor:** `huetdata/` = Huet import + crosswalk
  (rerun monthly at most); `nominals/` + `verbs/` = the two calculation
  engines (rerun when inputs/corrections change); `sqlite/` = load (rerun
  after either engine); `web/` = read-only consumer. Root
  [redo.sh](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/redo.sh)
  deliberately does **not** run `huetdata/` — the Huet refresh is a separate,
  manual, data-download-gated act.
- **Invariants:** every computed file is `calc_*` and disposable; every stage
  is idempotent (safe to rerun); `sqlite/db/*.sqlite` and
  `huetdata/download/SL_morph.xml` never enter git; the web app's only
  coupling to the pipeline is the `../sqlite/db` path in
  [web/dal.php](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/web/dal.php).
- **Observed defects (found 11-07-2026 while writing this manual):**
  1. the `ben`/`prf` branch bug in `huetdata/redo_one.sh` (§5, row 1) —
     a full `huetdata/redo.sh` run silently skips two of eight tenses
     (no `set -e`, so the loop continues);
  2. vestigial `smfile=` variables in `sqlite/lgtab1/redo_lgtab1.sh` and
     `sqlite/vlgtab1/redo_vlgtab1.sh` pointing at a nonexistent `outputs/`
     tree (§5, last row);
  3. the `cnd/con` and `pef/pft` tense-code spelling split between
     `huetdata/` and `verbs/pysanskritv2/models/` (§6) — harmless today
     because the two namespaces never join mechanically, but a trap for any
     future script that tries.
- **Where a correction belongs** (the most common maintainer question):
  wrong *declension* → `correction_inventory.txt` (nominal tables stage);
  wrong *conjugation* → `manual/tables_*.txt` or `manual_tables_inventory.txt`
  (verb stages 2/4); wrong *root spelling join* → `huet_mw_map_data.py`;
  wrong *grammar reference* → `sqlite/lgmodel/lgmodel_input.txt`. Dictionary
  *text* corrections do not belong in this repo at all — they go through the
  org correction workflow
  ([csl-corrections/docs/correction-workflow.md](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md)).
- **Ancestry:** `pysanskritv1` (verbs) and `pydecl` (nominals) both descend
  from [funderburkjim/elispsanskrit](https://github.com/funderburkjim/elispsanskrit);
  `bases_test2.py` is the only live consumer of v1. `pysanskrit_work/` is an
  abandoned rewrite — do not build on it.
- **Issue taxonomy:** processing-tool category, one type + one severity +
  one milestone — see
  [CLAUDE.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/CLAUDE.md).

---

_Dr. Mārcis Gasūns_
