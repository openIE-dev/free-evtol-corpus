# Free eVTOL Corpus

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20092536.svg)](https://doi.org/10.5281/zenodo.20092536)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

A structured prior art commons covering eVTOL aircraft and eVTOL-adjacent
flying machines: passenger air taxis, cargo eVTOL, jetpacks, hover bikes,
personal VTOL, tilt-rotor and tilt-wing demonstrators, military VTOL,
ducted-fan and vectored-thrust craft, drive+fly transformers, and the science
fiction and academic literature that anticipated all of them.

Coverage is global and deep: 217 entries spanning ~2,500 years from the
Pushpaka Vimana (Sanskrit Ramayana, ~5th c BCE) and the 1001 Nights flying
carpet (~9th c CE) through Verne's *Albatross* (1886, 74 distributed lift
airscrews — the foundational engineering anticipation of distributed-electric-
propulsion) and the deep helicopter-pioneer base (Cornu 1907, Oehmichen
1924, Focke Fa 61 1936, Sikorsky VS-300 1939, Flettner Fl 282 1941, Bell
Model 30 1942), the Cold War VTOL demonstrators (XV-3 1955, X-13 Vertijet
1957, X-14 1957, VZ-2 1957, X-18 1959, P.1127 1960, X-22 1966, XV-15 1977,
V-22 1989, Yak-141 1987, F-35B 2008), and the modern commercial eVTOL
ecosystem (Joby, Archer, Beta, Wisk, Volocopter, Lilium, Vertical, EHang,
AutoFlight, AeroHT, Hyundai Supernal, Eve, AMSL, ePlane, Zuri, Crisalion,
Manta, AeroMobil, Klein Vision, PAL-V, Pivotal, Jetson, AIR, ASKA, etc.)
through 2024.

**29 countries on six populated continents** — US, FR, JP, DE, GB, RU, CH, CN,
CA, IT, AT, IN, AU, KR, SE, AR, BR, ES, IL, NL, SG, SK, ZA, CZ, EG, GE, HU, IE, NZ.
All 20 lift-architecture categories are populated, including `fictional_repulsor`
(Star Wars repulsorlift 1977, Back to the Future Part II hoverboard 1989, The
Fifth Element 1997), `cyclorotor` (Kirsten-Boeing cyclogiro 1922 → D-Dalus 2011
→ CycloTech 2022), `buoyant_hybrid` (LTA Pathfinder 1, Airlander 10, Flying
Whales, Aeros Aeroscraft), `ground_effect_hybrid` (Soviet ekranoplans 1966,
Wigetworks AirFish, REGENT seaglider), and `coleopter` (Heinkel Lerche II 1945
→ SNECMA Coléoptère 1959).

The corpus also covers the adjacent lineages that bound any future commercial
eVTOL patent claim: modular / transforming / swarming / self-assembling aerial
robots (ETH Distributed Flight Array 2010, UPenn ModQuad 2018, University of
Tokyo DRAGON 2018, KMel/UPenn nano-quad swarm 2012, Intel Shooting Star 2016,
Airbus Pop.Up and Bell APT modular-pod concepts 2017-2018); fully-actuated
omnidirectional multirotors (ETH Omnicopter 2016, Voliro 2018, CycloTech 2022);
historical personal-VTOL platforms (Hiller VZ-1 Pawnee 1955, de Lackner HZ-1
Aerocycle 1955, Williams X-Jet 1982, SoloTrek XFV 2001); compound rotorcraft
(Fairey Rotodyne 1957, Eurocopter X3 2010, Airbus RACER 2024, Sikorsky/DARPA
X-Wing 1986); electric airships and WIG craft (LTA Pathfinder 1 2023, Hybrid
Air Vehicles Airlander 10 2012, Flying Whales LCA60T 2012, REGENT seaglider
2021); and drive+fly transformers across folding-wing, modular-capsule,
whole-body-rotation, and autogyro variants (Terrafugia Transition 2009, Klein
Vision AirCar 2020, Alef Model A 2022, Airbus Pop.Up 2017, PAL-V Liberty 2024).

Hand-written invalidity-contention packets target the Joby Aviation, Archer
Aviation, Beta Technologies, and Volocopter patent estates by mapping their
architectural claim domains to corpus entries that anticipate each.
Auto-generated subsystem packets cover 50 distinct architectural / certification
/ safety / autonomy / modular-docking / morphing / swarm / omnidirectional /
buoyant-hybrid / stopped-rotor domains.

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
