# csl-inflect

_Created: 26-11-2019 · Last updated: 11-07-2026_

CDSL **processing-tool** repository in the Sanskrit Lexicon project: it generates
declension and conjugation tables for Sanskrit headwords and serves them through an
"inflected forms" lookup web app.

## Why this repo exists

A CDSL dictionary entry gives a headword and a gloss, but not the inflected forms a
reader actually meets in a text — a verb root like *bhū* appears in a passage as
*bhavati*, *babhūva*, *bhaviṣyati*, never as the bare root. Two independent scholarly
datasets already encode how Sanskrit inflects (Gérard Huet's verbal-conjugation data
from the Sanskrit Heritage project, and a nominal-declension engine descended from
Deshpande's work), but neither is keyed to CDSL headwords out of the box: Huet's root
spellings and CDSL's (largely Monier-Williams-derived) headword spellings disagree
often enough that a naive join misses entries. This repo bridges that gap — a
hand-curated root-spelling crosswalk reconciles the two conventions, the paradigm
engines calculate the tables, five SQLite databases index them, and a PHP app looks up
the inflected forms for a given headword.

## Documentation

- [docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/docs/PIPELINE_MANUAL.md)
  — **operator manual**: the full rebuild (`redo.sh` chain: Huet import + root-spelling
  crosswalk → nominal/verb table calculation → 5-database SQLite load → the PHP
  inflected-form lookup app), environment, symptom→cause→cure, and a glossary. Read this
  before rebuilding anything. Companion metadoc:
  [docs/PIPELINE_MANUAL.meta.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/docs/PIPELINE_MANUAL.meta.md).

## Layout

| Path | Purpose |
|---|---|
| [huetdata/](https://github.com/sanskrit-lexicon/csl-inflect/tree/main/huetdata) | Huet verbal-conjugation import. `huet_mw_map.py` respells Huet roots to MW headwords using the `huet_mw_map` dict in `huet_mw_map_data.py`; `extract/` holds Huet stems + conjugation tables per tense/mood (aor, ben, cnd, fut, inj, pef, prf, prs), and `mapextract/` the same tables after the crosswalk is applied. |
| [nominals/](https://github.com/sanskrit-lexicon/csl-inflect/tree/main/nominals) | Declension engines: `pydecl/` (standalone Python decliner — `decline.py`, `decline_1cons.py`, `decline_f.py`, `decline_irr.py`, `decline_pco.py`, `sandhi_nR.py`) and `pysanskritv2/` (second-generation stems→analysis→tables pipeline). |
| [verbs/](https://github.com/sanskrit-lexicon/csl-inflect/tree/main/verbs) | Conjugation engines: `pysanskrit_work/`, `pysanskritv1/`, and `pysanskritv2/` (inputs→bases→tables). |
| [sqlite/](https://github.com/sanskrit-lexicon/csl-inflect/tree/main/sqlite) | Loads the calculated tables into five SQLite databases — `lgmodel`, `lgtab1`, `lgtab2`, `vlgtab1`, `vlgtab2`. |
| [web/](https://github.com/sanskrit-lexicon/csl-inflect/tree/main/web) | PHP lookup app (`index.php`, `dal.php`, `getWord.php`, `main.js`, `main.css`) with a bundled transcoder under `utilities/`. |
| [docs/](https://github.com/sanskrit-lexicon/csl-inflect/tree/main/docs) | Operator manual + metadoc. |

## The root-spelling crosswalk

[huetdata/huet_mw_map.py](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/huet_mw_map.py)
rewrites a Huet paradigm-table file, replacing each Huet root with its mapped MW
headword via the `huet_mw_map` dict in
[huetdata/huet_mw_map_data.py](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/huet_mw_map_data.py)
— a curated set of 34 spelling overrides (e.g. `'dIv':'div'`, `'gE':'gA'`) for the
roots where the Huet and MW conventions differ; roots not in the dict pass through
unchanged. The annotated reference file
[huetdata/huet_mw_map_data.txt](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/huet_mw_map_data.txt)
(678 lines) records the `HU=`/`MW=` gloss comparison behind each mapping decision. The
input tables it operates on look like this:

```
$ head -3 huetdata/extract/huet_stems_prs.txt
aMSa:11P,_Q
akz:1P,5P,_Q
agada:11P
```

Each `root:tp,parm` line's root is looked up in the crosswalk; when the Huet spelling
and the MW headword differ, `write()` in `huet_mw_map.py` counts the substitution
(`hrec.root != hrec.mw`) before emitting the MW-keyed table into `mapextract/`.

## Rebuild

From the repo root, [redo.sh](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/redo.sh)
chains the whole calculation: `nominals` → `verbs` → `sqlite`. Every stage has its own
`redo.sh` and can be rerun in isolation from its own directory. The Huet import
(`huetdata/redo.sh`) is refreshed separately, only when Huet republishes his data. See
the [pipeline manual](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/docs/PIPELINE_MANUAL.md)
for environment requirements and the step-by-step run.

## Tech stack

- **Runtime**: Python 3 (table calculation) + PHP (lookup web app), plain scripts, no build step
- **Input**: CDSL/MW headwords + Huet/Deshpande paradigm data
- **Storage**: five SQLite databases in `sqlite/`
- **Output**: per-headword declension / conjugation tables, served by `web/`

## GitHub issue conventions

`processing-tool` category of the
[Cologne tooling-repo taxonomy](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-tooling-runbook.md).
Every issue carries exactly one type label (9 options: `bug`, `feature`, `enhancement`,
`performance`, `tech-debt`, `security`, `documentation`, `infrastructure`, `question`),
one severity (`trivial`, `minor`, `major`, `critical`), and one milestone (API
Stability, User Experience, Data Quality, Developer Experience, Community). Domain
labels scoped here: `domain:morphology`, `domain:normalization`, `domain:lookup`. Org
project: [Tooling Roadmap](https://github.com/orgs/sanskrit-lexicon/projects/9). Full
conventions live in
[CLAUDE.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/CLAUDE.md).

Snapshot 2026-05-29 (12 open, unchanged as of 2026-07-11): by milestone, 8 User
Experience / 3 Developer Experience / 1 Community; by type, 7 enhancement / 3
documentation / 1 feature / 1 question.

---

_Dr. Mārcis Gasūns_
