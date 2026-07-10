# PIPELINE_MANUAL.md — metadoc

_Created: 11-07-2026 · Last updated: 11-07-2026_

Companion record for
[docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/docs/PIPELINE_MANUAL.md).

## Purpose

The operator manual for the csl-inflect morphology pipeline: Huet import +
root-spelling crosswalk, the nominal (2-stage) and verb (4-stage) calculation
chains, the five-database SQLite load, and the PHP inflected-form lookup app.
The test is operational: a newcomer rebuilds everything from the manual alone.

## Audience

- An operator rerunning the pipeline after a Huet monthly refresh or an
  input correction.
- A new contributor locating where a wrong form gets fixed (the §7
  "where a correction belongs" map).
- A maintainer of the Cologne-server deployment of `web/`.

## Provenance

Authored 11-07-2026 by Fable 5 (`claude-fable-5`) under handoff
[H507-Fable_csl-inflect_morphology_pipeline_manual_10.07.26](https://github.com/gasyoun/Uprava/blob/main/handoffs/H507-Fable_csl-inflect_morphology_pipeline_manual_10.07.26.md)
(the H501–H531 per-repo manuals programme, Litpam-Indexator MANUAL.md gold
standard). Every command and file path read from the actual `redo*.sh`
scripts, `.sql` loaders, per-directory readmes, and `web/dal.php` — none
invented; the three §7 defects were observed in the committed scripts.

## Ranked improvement backlog

| # | Item | Status |
|---|---|---|
| 1 | Fix the `ben`/`prf` missing-`\|\|` bug in [huetdata/redo_one.sh](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/redo_one.sh) (two of eight tenses silently skipped by a full run) | open |
| 2 | Add `set -e` (or explicit exit-code checks) to the `redo.sh` chain — today a failed stage scrolls past and the run "succeeds" | open |
| 3 | Delete the vestigial `smfile=` lines in `sqlite/lgtab1/redo_lgtab1.sh` + `sqlite/vlgtab1/redo_vlgtab1.sh` | open |
| 4 | Unify the `cnd/con` and `pef/pft` tense-code spellings (or document the mapping in code) | open |
| 5 | A row-count regression check for the sqlite load (assert counts within tolerance of last run, instead of eyeballing the printed `count(*)`) | open |

## Known limitations

- The Cologne-server deployment specifics (exact URL, sync mechanism for
  `web/` + `sqlite/db/`) are not documented in the repo and are described
  only structurally (§3.5); the deployed-copy update ritual is
  upstream-maintainer territory.
- The internals of `root_model.py`'s mode arguments (`5,present`, `4,ppf`, …)
  are not decoded beyond what `models/redo.sh` shows; `models/readme.org`
  has partial notes.

## Related documents

- [README.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/README.md) — repo overview + verified crosswalk usage example
- Per-directory readmes: [huetdata](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/readme.md) · [nominals](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/nominals/readme.md) · [verbs](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/verbs/readme.md) · [sqlite](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/sqlite/readme.md) · [download](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/huetdata/download/readme.md)
- [CLAUDE.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/CLAUDE.md) — issue taxonomy

## Revision history

| Date | Change | By |
|---|---|---|
| 11-07-2026 | Initial version (H507) | Fable 5 (`claude-fable-5`) |

---

_Dr. Mārcis Gasūns_
