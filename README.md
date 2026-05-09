# Free eVTOL Corpus

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20092536.svg)](https://doi.org/10.5281/zenodo.20092536)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

A structured prior art commons covering eVTOL aircraft and eVTOL-adjacent
flying machines: passenger air taxis, cargo eVTOL, jetpacks, hover bikes,
personal VTOL, tilt-rotor and tilt-wing demonstrators, military VTOL,
ducted-fan and vectored-thrust craft, drive+fly transformers, and the science
fiction and academic literature that anticipated all of them.

Coverage is global: 114 entries spanning 1886 (Verne *Albatross* — 74 lift
airscrews, the foundational distributed-electric-propulsion prior art) through
2024, across 24 countries on six continents.

Latin America is represented by Brazil (Embraer EmbraerX 2018 concept,
Eve Air Mobility 2020 production) and Argentina (Pescara helicopter 1922
academic, Eternauta 1957 fictional). The genuinely thin homegrown OEM
footprint elsewhere in Latin America reflects the current state of the
field rather than a corpus omission — the corpus tracks design disclosures,
not airline-operator partnerships.

Hand-written invalidity-contention packets target the Joby Aviation and
Archer Aviation patent estates by mapping their architectural claim domains
to corpus entries that anticipate each. Auto-generated subsystem packets
cover 40 distinct architectural / certification / safety / autonomy domains.

**The corpus IS the prior art commons.** Every entry, at the moment of
timestamped commit and quarterly release, is a defensive publication. There
is no separate commons layer above this catalog — the structured data here,
combined with the cryptographic timestamping in `releases/`, is itself the
invalidity-contention material.

## License

CC0-1.0. Public domain dedication. See [LICENSE](LICENSE).

## What's in here

```
SCHEMA.md           — schema spec (currently v0.1)
TIMESTAMPING.md     — release ceremony for cryptographic timestamping
RELEASE_RUNBOOK.md  — step-by-step first-release procedure
README.md           — this file

corpus.jsonl        — master corpus (one JSON object per line)
private.jsonl       — generated mirror, entries with corpus="private"
open.jsonl          — generated mirror
fictional.jsonl     — generated mirror
academic.jsonl      — generated mirror

CORPUS_INDEX.md     — generated alphabetical index
lineage.json        — generated ancestor/descendant DAG

cross_cuts/         — generated per-subsystem prior art views
  INDEX.md          — table of all cross-cuts with counts
  <tag>.md          — chronological view of all entries disclosing <tag>

tools/
  validate.py       — schema and quality-bar enforcement
  index.py          — generates CORPUS_INDEX.md, lineage.json, per-corpus mirrors
  cross_cuts.py     — generates cross_cuts/

release.sh          — quarterly release ceremony with timestamping
```

## Quick start

```bash
# Validate the corpus passes structural and quality-bar checks
python3 tools/validate.py corpus.jsonl --strict

# Regenerate all derived artifacts after editing corpus.jsonl
python3 tools/index.py .
python3 tools/cross_cuts.py

# Run a quarterly release with cryptographic timestamping
./release.sh 2026.Q3
```

## Quality bar

An entry is commons-grade (not `draft: true`) when:

1. `disclosure_citation` resolves to a primary source verifiable by a
   third party.
2. `first_disclosure_date` is the earliest verifiable public disclosure,
   defensible against challenge.
3. `prior_art_notes` reads as a 102/103 anticipation analysis someone
   unrelated to us could cite without rewriting.
4. `sources` cite primary references.
5. For patented entries, `ip_citations` lists actual patent numbers.

Entries that don't yet clear this bar are merged with `draft: true` and
have explicit work items in their `notes` field.

## Cross-cuts as the working tool

The cross-cut files (`cross_cuts/<tag>.md`) are the operational form of the
commons. Each file lists every entry disclosing a given subsystem, in
chronological order, with their `prior_art_notes` and `disclosure_citation`
inline.

Use these when assessing patent claims:

- A claim about distributed electric propulsion? Open
  `lift-distributed-electric-propulsion.md` — anchored at Verne's
  *Albatross* (1886, ~74 vertical lift rotors), through de Bothezat (1922),
  Curtiss-Wright VZ-7 (1958), to modern multirotor air taxis.
- A claim about tilt-rotor transition? Open `lift-tilt-rotor.md` — anchored
  at Bell XV-3 (1955) and XV-15 (1977), through V-22 Osprey (1989), to
  Joby S4 and Archer Midnight.
- A claim about vectored-thrust VTOL? Open `lift-vectored-thrust.md` —
  Hawker P.1127 (1960), AV-8B Harrier (1985), Yak-141 3-bearing swivel
  duct (1987), F-35B (2008), Lilium ducted-fan array.

## Contributing

Contributions are welcome under CC0-1.0. By submitting an entry you
dedicate the contribution to the public domain.

A good entry is one that holds up as defensive publication. The
contribution guide ([CONTRIBUTING.md](CONTRIBUTING.md)) covers what that
means in practice. Briefly:

- Cite primary sources, not Wikipedia.
- Identify specific subsystems disclosed using the taxonomy in SCHEMA.md.
- Write `prior_art_notes` as element-by-element anticipation analysis.
- For patented entries, point back at academic, military, or fictional
  prior art that anticipates the claims.

If unsure, mark the entry `draft: true` and document the work needed to
clear the quality bar.

## Provenance

Originated within Open Interface Engineering (OpenIE) as a sister project
to the Free Humanoid Corpus, applying the same defensive-publication
methodology to a different patent-thicket-formation field. The corpus
serves the entire eVTOL and personal aerial mobility field, not any
specific platform.
