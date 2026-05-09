---
title: "Volocopter patent estate"
parent: "Invalidity Contentions"
nav_order: 103
layout: default
---

# Invalidity Contention Packet — Volocopter patent estate

**Target:** Volocopter GmbH (formerly e-volo GmbH) and its asserted patents around manned electric multicopter passenger eVTOL.

**Representative patents:**

- **DE 10 2010 032 217 / WO2011050822** — foundational Multicopter aircraft patent (e-volo, 2010) — basis for the entire Volocopter patent family
- **EP 2 511 173** and continuations covering the 18-rotor circular-ring multirotor architecture
- Multiple Volocopter patents 2010-2024 covering battery topology, redundant electrical bus, autonomous flight management, and EASA SC-VTOL certification basis

This packet maps the architectural claim domains of the Volocopter patent estate to corpus entries that anticipate each domain.

---

## How to use this packet

1. Identify the architectural domain of the Volocopter claim being challenged (manned multirotor passenger architecture, circular-ring rotor arrangement, electric BLDC multicopter, etc.).
2. Read the relevant section below.
3. Each cited entry's `prior_art_notes` is element-by-element 102/103 anticipation analysis.

**Critical priority note:** Volocopter's foundational patent DE 10 2010 032 217 was filed 2010-07-26. Volocopter is itself prior art (volocopter-vc1 first manned flight 2011-10-21). However, the architectural claims of "manned electric multirotor with N rotors arranged on a circular frame" require careful attention to the priority date of the specific claims being challenged.

---

## Domain 1 — Manned multirotor passenger architecture

**Volocopter claim area:** manned passenger-carrying multi-rotor electric VTOL with N>=4 lift rotors.

**Anchor 102 prior art:**

- **1886** — `verne-albatross` — Distributed electric multi-rotor lift architecture. Foundational anticipation by 124 years (predating DE 10 2010 032 217 filing).
- **1907** — `cornu-helicopter` — First manned free-flight rotorcraft. Establishes the basic concept of human-carrying rotorcraft.
- **1922** — `de-bothezat-quadrotor` — First manned multi-rotor heavier-than-air vehicle to achieve sustained hover. Establishes prior art for multi-rotor manned lift architecture.
- **1922** — `pescara-helicopter` — Coaxial counter-rotating manned rotorcraft.
- **1924** — `oehmichen-helicopter` — Manned 4-rotor + 8-control-rotor compound architecture.
- **1958** — `de-bothezat-quadrotor` parallel: `curtiss-wright-vz-7` (1958), `piasecki-vz-8-airgeep` (1958) — manned multi-rotor flying-jeep architectures with cross-shafted single-engine drive.

**103 obviousness chain:** Verne (1886) + de Bothezat (1922) + Curtiss-Wright VZ-7 (1958) + electric DC motor and battery technology of the 1990s-2000s would have made manned electric multirotor obvious to a person of ordinary skill in the art well before 2010.

---

## Domain 2 — Circular-ring rotor arrangement

**Volocopter claim area:** the 18 rotors arranged around a circular frame (VoloCity production design).

**Anchor 102 prior art:**

- **1886** — `verne-albatross` — *The* foundational anticipation: thirty-seven pairs of lift airscrews (74 total) distributed across an airframe. Verne's specific multi-rotor count and distribution dwarfs Volocopter's 18-rotor arrangement; the architectural pattern is identical.
- **1922** — `de-bothezat-quadrotor` — X-frame multi-rotor with rotors at frame extremities.
- **1924** — `oehmichen-helicopter` — Cross-pattern + 8-control-rotor distribution.
- **2011** — `volocopter-vc1` — Volocopter's own predecessor (16 rotors, circular-ring concept). The transition from 16 to 18 rotors is design choice, not architectural novelty.

The circular-ring rotor arrangement has no architectural novelty separately from the multi-rotor concept itself, which was disclosed in 1886.

---

## Domain 3 — BLDC direct-drive multirotor

**Volocopter claim area:** brushless DC motors directly driving fixed-pitch propellers in multi-rotor configuration.

**Anchor 102 prior art:**

BLDC motors and direct-drive propeller architecture are universal in modern multirotor design and were not novel in 2010. Anchored by:

- **1886** — `verne-albatross` — explicit electric drive for distributed lift airscrews
- **2008-2010** — Open-source drone projects (ArduCopter, predecessors of `ardupilot-quadplane`) — open-source BLDC multirotor reference designs

Industrial/maker BLDC quadrotor designs are public-domain pre-2010 in massive variety. The DJI Phantom 1 (2013) — and its many predecessors documented in academic papers and open-hardware projects — comprehensively place BLDC direct-drive multirotor architecture in pre-Volocopter prior art.

---

## Domain 4 — Differential-thrust attitude control

**Volocopter claim area:** attitude control via differential thrust between rotors.

**Anchor 102 prior art:**

- **1922** — `de-bothezat-quadrotor` — First demonstration of differential-thrust attitude control between independent lift rotors. Foundational disclosure.
- **1924** — `oehmichen-helicopter` — Compound differential-thrust architecture with dedicated attitude rotors.
- **1958** — `curtiss-wright-vz-7`, `piasecki-vz-8-airgeep` — Cross-shafted multi-rotor with differential-thrust attitude.

Differential-thrust attitude control for multirotor is foundational prior art from 1922.

---

## Domain 5 — EASA SC-VTOL certification basis

**Volocopter claim area:** EASA Special Condition VTOL (SC-VTOL) compliance methodology.

The EASA SC-VTOL framework itself is regulatory text published 2019-07 by EASA, comprehensively in the public domain. Patent claims cannot encompass the regulatory framework. Implementations of compliance with the framework cite the framework, not the other way around.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on use, citation, copying, or redistribution.

---

*Hand-written contention packet. Maintained alongside auto-generated subsystem packets by `tools/contention_packets.py`. Architectural domains and patent estate references documented in Volocopter GmbH (now Volocopter Holding) DPMA filings, EPO European patent records, and EASA SC-VTOL public docket.*
