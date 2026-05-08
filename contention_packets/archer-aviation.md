---
title: "Archer Aviation patent estate"
parent: "Invalidity Contentions"
nav_order: 101
layout: default
---

# Invalidity Contention Packet — Archer Aviation patent estate

**Target:** Archer Aviation, Inc. (NYSE: ACHR) and its asserted and pending patent claims around hybrid lift+cruise / tilt-rotor distributed-electric-propulsion eVTOL.

**Representative patent estate:**

- Archer Aviation patent estate, multiple US, PCT, and continuation filings 2020–2025 in CPC B64C 29/00 (VTOL aircraft) and B64D 27/24 (electric aircraft propulsion).
- Archer's distinctive claim area is the 6+6 hybrid architecture: six wing-leading-edge tilting propellers and six aft-boom-mounted lift-only propellers (stop and feather in cruise).

This packet maps the architectural claim domains of the Archer patent estate to corpus entries that anticipate each domain.

---

## How to use this packet

1. Identify the architectural domain of the Archer claim being challenged (hybrid lift+cruise architecture, six-tilt-six-lift configuration, transition through partial-tilt regimes, BLDC direct-drive, etc.).
2. Read the relevant section below.
3. Each cited entry's `prior_art_notes` is element-by-element 102/103 anticipation analysis.

---

## Domain 1 — Hybrid lift+cruise architecture (separate lift rotors + separate cruise propulsion)

**Archer claim area:** dedicated lift rotors that operate in hover and stop in cruise, plus separate tilting propellers that function as both lift in hover and cruise propulsion.

**Anchor 102 prior art:**

- **1923** — `cierva-autogyro` — Foundational disclosure of compound rotorcraft: forward thrust separate from rotor lift; tractor propeller for cruise + autorotating top rotor.
- **1943** — `doblhoff-wnf-342` — Tip-jet rotor with cruise mode where rotor autorotates and forward thrust comes from a separate tractor propeller. The architectural pattern of separate lift propulsion + separate cruise propulsion in one aircraft.
- **1959** — `kamov-ka-22-vintokryl` — Soviet hybrid: wingtip lift rotors + tractor propellers for cruise. Specifically anticipates Archer's split-mode propulsion topology.
- **1958** — `fairey-rotodyne` (compound rotorcraft anchor) — tip-jet driven rotor with cruise propellers.
- **2014** — `nasa-gl-10` — Modern DEP tilt-wing with mode-switching of lift rotors in different flight regimes.
- **2018** — `wisk-cora` — Boeing/Wisk autonomous lift+cruise (12+1) with mode-shutdown transition.
- **2020** — `beta-alia-250` — Production-scale lift+cruise architecture with mode-shutdown transition: lift rotors stop and shut down in cruise, separate pusher provides forward propulsion.

**103 obviousness chain:** Cierva (1923) + Doblhoff (1943) + Beta Alia (2020) together disclose the entire architectural pattern of split lift / cruise propulsion that Archer's 6+6 hybrid implements.

---

## Domain 2 — Distributed electric propulsion with mixed-function rotors

**Archer claim area:** some rotors function as both lift in hover and cruise propulsion (the six tilting); others function only as lift (the six lift-only).

**Anchor 102 prior art:**

- **1886** — `verne-albatross` — Distributed electric lift airscrews + horizontal cruise propellers decoupled from lift. Foundational disclosure of mixed-function rotor architecture.
- **1977** — `bell-xv-15` — Tilt-rotor in which prop-rotors function as lift in hover and cruise propulsion in horizontal flight (the foundational mixed-function rotor disclosure).
- **2014** — `nasa-gl-10` — Modern DEP tilt-wing with explicit different rotor states in different regimes.
- **2016** — `aurora-lightningstrike-xv-24a` — DARPA VTOL X-Plane: 24 ducted lift fans embedded in wing and canard, turbine-electric hybrid. Specifically anticipates high-multiplicity DEP claims.

**103 obviousness chain:** Verne (1886) + XV-15 (1977) + GL-10 (2014) + LightningStrike (2016) together disclose every architectural element Archer claims around mixed-function distributed electric rotors.

---

## Domain 3 — Six tilt + six lift configuration specifically

**Archer claim area:** the specific 6+6 hybrid architecture (six tilting + six lift-only).

**Anchor 102 prior art:**

- **2014** — `nasa-gl-10` — Ten-rotor wing-distributed DEP architecture (eight wing + two horizontal-tail). The specific multiplicity is different but the architectural pattern (multi-rotor wing-distributed DEP with optional control of individual rotor states) is identical.
- **2018** — `joby-s4` — Six-tilt-rotor architecture (4+2). Specifically anticipates the "six tilt" subset of Archer's 6+6.
- **2018** — `wisk-cora` — Twelve-rotor wing-and-boom architecture; the lift-only sub-configuration is identical to Archer's six lift-only.
- **2020** — `beta-alia-250` — Five-rotor lift+cruise (4 lift + 1 pusher) with mode-shutdown.

The specific 6+6 multiplicity is a design choice, not a novel architectural concept. The combination is anticipated by GL-10 + Joby S4 + Beta Alia in 103 obviousness terms.

---

## Domain 4 — BLDC direct-drive electric propulsion

**Archer claim area:** brushless DC motors directly driving propellers without geared reduction.

**Anchor 102 prior art:**

- **2011** — `volocopter-vc1` — First manned electric BLDC multicopter. The fundamental BLDC-direct-drive disclosure for manned eVTOL.
- **2014** — `nasa-gl-10` — BLDC direct-drive wing-distributed propulsion.
- **2014** — `px4-vtol` and **2015** — `ardupilot-quadplane` — Open-source flight control with explicit BLDC motor control libraries supporting any number of direct-drive lift rotors.

BLDC direct-drive for VTOL is so widely-disclosed in 2011-2015 prior art that any patent claim asserting novelty over it is anticipated.

---

## Domain 5 — Triplex fly-by-wire / Part 23 SVO certification basis

(Same as Joby Domain 5 / Domain 6.) See [`joby-aviation.md`](joby-aviation.md) for the FBW + SVO contention domain. The architectural prior art is identical: Short SC.1 (1957) for triplex FBW, and the cumulative SVO disclosures in fictional + ultralight-class entries from 1962 forward.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on use, citation, copying, or redistribution.

---

*Hand-written contention packet. Maintained alongside auto-generated subsystem packets by `tools/contention_packets.py`. Architectural domains and patent estate references cited above are documented in Archer Aviation S-1 SEC filing (2021-06-10), 10-K filings 2022–2025, and USPTO records.*
