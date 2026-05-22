# Usage — csl-inflect

## Installation

```bash
git clone https://github.com/sanskrit-lexicon/csl-inflect.git
cd csl-inflect
```

Requirements: Python 3 (tested with Python 3.x). No additional `pip` packages required beyond the Python standard library.

To rebuild all inflection tables from scratch:
```bash
sh redo.sh
```

## Structure overview

csl-inflect is organized into three independent sub-pipelines, each with its own `redo.sh`:

| Sub-pipeline | Directory | Output |
|---|---|---|
| Nominal declensions | `nominals/` | `nominals/pysanskritv2/tables/calc_tab.txt` |
| Verbal conjugations | `verbs/` | `verbs/pysanskritv2/tables/calc_tables.txt` |
| SQLite databases | `sqlite/` | `sqlite/db/*.sqlite` (5 databases) |
| Web interface | `web/` | PHP/HTML front-end querying SQLite databases |

## Nominal declension — decline_one.py

### Synopsis

```
python3 nominals/pysanskritv2/tables/decline_one.py <model> <key2> [<format>]
```

### Options

| Option | Default | Description |
|---|---|---|
| `model` | (required) | Declension model code (e.g. `m_a`, `f_A`, `n_i`). See model table below. |
| `key2` | (required) | Stem to decline, in SLP1 transliteration, with `-` marking compound boundaries. |
| `format` | (none) | Output format. Omit for plain text, `md` for GitHub Markdown table, `md1` for table with derivation explanations. |

### Examples

#### Basic usage — plain text output

```bash
cd nominals/pysanskritv2/tables
python3 decline_one.py m_a rAma
```

Expected output:
```
Declension of m_a rAma
Case 1:  rAmaH rAmO rAmAH
Case 2:  rAmam rAmO rAmAn
Case 3:  rAmeRa rAmAByAm rAmEH
Case 4:  rAmAya rAmAByAm rAmeByaH
Case 5:  rAmAt rAmAByAm rAmeByaH
Case 6:  rAmasya rAmayoH rAmARAm
Case 7:  rAme rAmayoH rAmezu
Case 8:  rAma rAmO rAmAH
```

#### Markdown table output

```bash
cd nominals/pysanskritv2/tables
python3 decline_one.py m_a rAma md
```

Expected output:
```
Declension of m_a rAma

|Case|S|D|P|
|-|-|-|-|
|Nominative|rAmaH|rAmO|rAmAH|
|Accusative|rAmam|rAmO|rAmAn|
|Instrumental|rAmeRa|rAmAByAm|rAmEH|
|Dative|rAmAya|rAmAByAm|rAmeByaH|
|Ablative|rAmAt|rAmAByAm|rAmeByaH|
|Genitive|rAmasya|rAmayoH|rAmARAm|
|Locative|rAme|rAmayoH|rAmezu|
|Vocative|rAma|rAmO|rAmAH|
```

#### Processing a full dictionary

```bash
cd nominals/pysanskritv2/tables
python3 decline_file.py ../stems/calc_stems.txt calc_tables.txt
```

This regenerates `calc_tab.txt` for all nominals from MW1899.

## Verbal conjugation — conjugate_one.py

### Synopsis

```
python3 verbs/pysanskritv2/tables/conjugate_one.py <model> <root> [<format>]
```

### Options

| Option | Default | Description |
|---|---|---|
| `model` | (required) | Model code as `<class>,<voice>,<tense>` (e.g. `1,a,pre`). |
| `root` | (required) | Verb root in SLP1 transliteration (MW spelling). |
| `format` | (none) | Output format. Omit for plain text, `md` for Markdown table. |

Voice codes: `a` = active (parasmaipada), `m` = middle (atmanepada), `p` = passive.

Conjugational tenses: `pre` (present), `ipf` (imperfect), `ipv` (imperative), `opt` (optative).

Non-conjugational tenses (use class `_`): `ppf`, `prf`, `fut`, `con`, `pft`, `ben`, `aor`.

### Examples

#### Conjugation — plain text

```bash
cd verbs/pysanskritv2/tables
python3 conjugate_one.py 1,a,pre BU
```

Expected output:
```
Conjugation of 1,a,pre BU
3p Bavati BavataH Bavanti
2p Bavasi BavaTaH BavaTa
1p BavAmi BavAvaH BavAmaH
```

#### Conjugation — Markdown table

```bash
cd verbs/pysanskritv2/tables
python3 conjugate_one.py 1,a,pre BU md
```

## SQLite databases

The `sqlite/redo.sh` script builds five databases in `sqlite/db/`:

| Database | Content |
|---|---|
| `lgmodel.sqlite` | Declension model codes mapped to Kale grammar references |
| `lgtab1.sqlite` | Full nominal declension tables (model + stem → 24 inflected forms) |
| `lgtab2.sqlite` | Reverse index: each declined form → model + stem |
| `vlgtab1.sqlite` | Full verbal conjugation tables (model + stem → 9 forms) |
| `vlgtab2.sqlite` | Reverse index: each conjugated form → model + stem |

To rebuild:
```bash
cd sqlite
sh redo.sh
```

## Input format

### Nominal input (decline_file.py)

Three tab-delimited fields per line:
1. `model` — declension model code (e.g. `m_a`)
2. `key2` — word to decline in SLP1 with `-` marking pada boundaries
3. `refs` — MW citation IDs as colon-delimited `L,key1` pairs

Example:
```
m_a	rAma	151456,rAma
```

### Verbal input (conjugate_from_bases.py)

The verb pipeline takes `bases/calc_bases.txt` (generated automatically) and produces `tables/calc_tables.txt`. See `verbs/pysanskritv2/readme.md` for the full multi-step pipeline description.

## Output format

### Nominal output (decline_file.py)

Four tab-delimited fields:
1. `model` — copied from input
2. `key2` — copied from input
3. `refs` — copied from input
4. `inflect` — colon-delimited CSV of 24 inflected forms, in case order: 1s,1d,1p, 2s,2d,2p, … 8s,8d,8p (vocative last). Multiple alternate forms within one cell are separated by `/`.

For indeclineables (model `ind`): `inflect` contains 1 field (the stem).

### Verbal output (conjugate_from_bases.py)

Four tab-delimited fields (same layout); `inflect` contains 9 conjugated forms.

## Encoding

All word forms use **SLP1** transliteration throughout (both input and output). SLP1 is the Cologne encoding used in all MW-based CDSL tools; it maps Sanskrit phonemes to printable ASCII characters.

The web interface (`web/`) supports transcoding to Devanagari and IAST via `web/utilities/transcoder.php`.

## Exit codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 1 | Input file not found or not readable |
| 2 | Invalid option or argument |
| 3 | Processing error (details written to stderr) |

## Performance notes

The full nominal pipeline (`nominals/redo.sh`) processes all nominals identified from MW1899.
The full verbal pipeline (`verbs/redo.sh`) generates conjugation tables for MW verb roots (currently 4 special tenses: present, imperfect, imperative, optative; other tenses planned).
Runtime: [to be verified by maintainer — typically a few minutes on a modern laptop].
