# Integration — csl-inflect

Which CDSL systems consume this tool, how it is invoked, and what output it produces.

## How csl-inflect fits in the CDSL pipeline

`csl-inflect` is a **standalone computational library**, not a per-dictionary processing script.
It operates on data extracted from the Monier-Williams dictionary (MW1899) to generate
inflection and conjugation tables for Sanskrit nominals and verbs.

Its outputs (the five SQLite databases in `sqlite/db/`) are consumed by the CDSL web
interface to display paradigm tables alongside dictionary entries.

No invocation of csl-inflect was found in the `csl-pywork` per-dictionary build scripts,
because this tool is dictionary-independent: it processes MW headword data once and produces
shared database files used across the site.

## Dictionaries that use csl-inflect outputs

| Consumer | How used | Notes |
|---|---|---|
| CDSL web interface (`web/`) | Queries `lgtab1`, `lgtab2`, `vlgtab1`, `vlgtab2`, `lgmodel` SQLite files | PHP scripts `dal.php` + `getWord.php` return inflected forms for a queried word |
| Sanskrit Lexicon website | Displays nominal declension and verbal conjugation paradigms | Uses the `web/` PHP front-end bundled in this repo |
| MW (Monier-Williams) | Source of headwords, stems, and verb roots | Input is derived from MW1899 via `funderburkjim/MWlexnorm` |

## Data sources

| Source | Role |
|---|---|
| `funderburkjim/MWlexnorm` — `lexnorm-all2.txt` | Primary input: MW headwords with gender and inflection metadata |
| `verbs/pysanskritv2/inputs/verb_cp.txt` | Verb roots with class/voice data extracted from MW |
| `huetdata/` | Huet's Heritage dictionary data used for cross-validation and comparison |

## Invocation from csl-pywork

csl-inflect is **not** invoked by csl-pywork per-dictionary scripts.
It is built independently using its own top-level `redo.sh`:

```bash
# Rebuild all inflection tables and SQLite databases
cd csl-inflect
sh redo.sh
```

The three sub-pipelines run in order:
```bash
cd nominals && sh redo.sh && cd ..   # → nominals/pysanskritv2/tables/calc_tab.txt
cd verbs    && sh redo.sh && cd ..   # → verbs/pysanskritv2/tables/calc_tables.txt
cd sqlite   && sh redo.sh            # → sqlite/db/*.sqlite  (5 databases)
```

## Output consumed by

| Downstream repo | How the output is used |
|---|---|
| `web/` (bundled in this repo) | PHP web interface queries the SQLite databases for on-demand paradigm lookup |
| CDSL website deployment | The `sqlite/db/*.sqlite` files are deployed to the server alongside the `web/` scripts |
| [to be verified] `csl-sqlite` | May import or reference these databases — check with maintainer |

## SQLite database schema

All five databases live in `sqlite/db/`.

### lgtab1.sqlite — nominal declension tables

| Column | Type | Description |
|---|---|---|
| `model` | text | Declension model code (e.g. `m_a`) |
| `stem` | text | Word stem in SLP1 |
| `refs` | text | MW source record citations |
| `data` | text | Colon-delimited inflection table (1 field for indeclineables, 24 fields otherwise) |

### lgtab2.sqlite — nominal reverse index

| Column | Type | Description |
|---|---|---|
| `key` | text | A single declined form in SLP1 |
| `model` | text | Source declension model |
| `stem` | text | Source stem |

### vlgtab1.sqlite — verbal conjugation tables

| Column | Type | Description |
|---|---|---|
| `model` | text | Conjugation model code (e.g. `1,a,pre`) |
| `stem` | text | Verb root in SLP1 |
| `refs` | text | MW source citations |
| `data` | text | Colon-delimited conjugation table (9 forms) |

### vlgtab2.sqlite — verbal reverse index

Same structure as `lgtab2.sqlite` but for conjugated forms.

### lgmodel.sqlite — model reference

| Column | Type | Description |
|---|---|---|
| `model` | text | Model code |
| `descr` | text | Human-readable description |
| `ref` | text | Reference to Kale Higher Sanskrit Grammar (format: `Kale N`) |

## Version compatibility

| csl-inflect version | Notes |
|---|---|
| current (`master`) | No formal versioned releases. Tied to MW1899 data from `MWlexnorm`. |

## Known incompatibilities

- The verbal pipeline currently covers only 4 special tenses (present, imperfect, imperative, optative). Periphrastic and reduplicative forms are planned but not yet implemented.
- `pysanskrit_work/` is an incomplete rewrite and is not currently used in the production pipeline.
- Certain nominal categories are excluded from the main pipeline: participles (`lexnorm-all2-part.txt`), dual/plural citation forms (`lexnorm-all2-inflectid.txt`), pronouns (`lexnorm-all2-pron.txt`), and irregular nouns (`lexnorm-irregular.txt`). These require special handling not yet implemented.
