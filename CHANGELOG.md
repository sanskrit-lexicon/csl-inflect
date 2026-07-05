# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Mobile viewport support: viewport meta tag + `max-width:700px` breakpoint stacking the
  three absolute-positioned panes so the inflected-form lookup is usable on phones
  (desktop layout above 700px untouched); before/after screenshots for PR #17.
- "Go" button for the lookup form (#14).
- `CLAUDE.md`, `CITATION.cff`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, tooling `README.md`
  via the tooling-repo runbook; Dependabot config + auto-merge workflow.
- Declension-table correction facility (#11); `decline_one.py` now shows a correction
  alongside the algorithmic declension when one exists.

### Fixed
- XSS security fix; transcoder ignore-warning fix.
- PHP 8.2 dynamic-variable deprecation fix.
- Declension of `viSvasfj` corrected for neuter only; nominals ending in `j` removed from
  `stems_problem.txt` (now computed algorithmically); `a-sfj` shown as a compound in
  `lexnorm-all2.txt`; annoying stray print statement removed from `pydecl/decline_pco.py`.
