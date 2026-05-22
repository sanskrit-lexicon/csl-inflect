# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**csl-inflect** is a Sanskrit Lexicon **processing-tool** repository — part of the Cologne Digital Sanskrit Lexicon (CDSL) infrastructure.

## Repo Category

`processing-tool` — see the [tooling runbook](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-tooling-runbook.md) for category-specific conventions.

## GitHub Issue Conventions

This repository uses the **Cologne tooling-repo taxonomy**. All issues must have:
- **Exactly one type label** (9 options)
- **Exactly one severity label** (4 levels)
- **One milestone** (5 options)

### Type Labels
- `bug` — Code defect (wrong output, broken contract)
- `feature` — Net-new capability
- `enhancement` — Improvement to existing capability
- `performance` — Speed, memory, throughput optimization
- `tech-debt` — Refactoring, cleanup, dependency updates
- `security` — CVE, auth issue, credential exposure
- `documentation` — Prose docs, API docs, comments
- `infrastructure` — CI/CD, deploy, data pipelines, build tooling
- `question` — Research, proposals, open discussions

### Severity Labels
- `trivial` — Cosmetic, < 1 hour
- `minor` — Single function/component
- `major` — Multiple files, design decision
- `critical` — Blocks users, data loss/security CVE

### Milestones
- **API Stability** — performance, security, regressions
- **User Experience** — bugs, features, enhancements
- **Data Quality** — data-pipeline issues, integrity
- **Developer Experience** — tech-debt, infrastructure, docs
- **Community** — questions, proposals, discussions

## Cross-Repo Coordination

The org-level project [Tooling Roadmap](https://github.com/orgs/sanskrit-lexicon/projects/9) tracks tool work across all repositories.

## Input / output contract

**Input (nominals):** `nominals/pysanskritv2/inputs/lexnorm-all2.txt` — tab-delimited file of MW headwords with gender and inflection metadata (L, key1, key2, lexnorm). Derived from `funderburkjim/MWlexnorm`.

**Input (verbs):** `verbs/pysanskritv2/inputs/verb_cp.txt` — colon-delimited file of MW verb roots with class/voice annotations (root, Lrefs, class-voice list).

**Output (nominals):** `nominals/pysanskritv2/tables/calc_tab.txt` — four-column tab-delimited file: model, stem, refs, inflection table (24 SLP1 forms, colon-delimited, `/`-separated alternates).

**Output (verbs):** `verbs/pysanskritv2/tables/calc_tables.txt` — same layout; inflection table has 9 forms.

**Output (SQLite):** Five databases in `sqlite/db/`: `lgmodel.sqlite`, `lgtab1.sqlite`, `lgtab2.sqlite`, `vlgtab1.sqlite`, `vlgtab2.sqlite`.

**Encoding:** SLP1 throughout all input and output files. The web interface converts to Devanagari/IAST on demand.

## Key files

| Path | Purpose |
|---|---|
| `redo.sh` | Top-level rebuild script — runs nominals, verbs, and sqlite pipelines in order |
| `nominals/pysanskritv2/tables/decline_file.py` | Batch nominal declension (input file → output file) |
| `nominals/pysanskritv2/tables/decline_one.py` | Interactive single-word declension (command-line) |
| `verbs/pysanskritv2/tables/conjugate_one.py` | Interactive single-verb conjugation (command-line) |
| `verbs/pysanskritv2/tables/conjugate_from_bases.py` | Batch verbal conjugation |
| `sqlite/redo.sh` | Builds all five SQLite databases from the calc_tables files |
| `web/getWord.php` | Web API endpoint: given a word in any encoding, returns paradigm data |

## Common commands

```bash
# Rebuild everything from scratch
sh redo.sh

# Decline a single nominal (SLP1 stem, model code)
cd nominals/pysanskritv2/tables
python3 decline_one.py m_a rAma

# Conjugate a single verb root
cd verbs/pysanskritv2/tables
python3 conjugate_one.py 1,a,pre BU

# Rebuild only the SQLite databases (after re-running nominals/verbs pipelines)
cd sqlite && sh redo.sh
```

## Known edge cases

- Certain nominal categories are excluded from the main pipeline and require special handling: participles, pronouns, irregular nouns, and headwords whose citation form is a dual or plural. See `nominals/pysanskritv2/inputs/readme.md` for details.
- The verbal pipeline currently covers only the 4 special tenses (present, imperfect, imperative, optative). Other tenses (perfect, aorist, future, etc.) are partially stubbed in `pysanskrit_work/` but not yet integrated.
- `pysanskrit_work/` is an incomplete rewrite and is **not** used in the production pipeline.
- Duplicate model-stem pairs are assumed to be removed before the SQLite build step (see comments in `sqlite/readme.md`).
