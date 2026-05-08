---
title: "Joby Aviation patent estate"
parent: "Invalidity Contentions"
nav_order: 100
layout: default
---

# Invalidity Contention Packet — Joby Aviation patent estate

**Target:** Joby Aviation, Inc. (NYSE: JOBY) and its asserted and pending patent claims around tilt-rotor distributed-electric-propulsion eVTOL.

**Representative patents:**

- **US 10,994,841 B2** (Bevirt et al., "Aircraft hover stability") — issued 2021-05-04
- **US 11,377,217 B2** (Bevirt et al., "Vertical take-off and landing aircraft") — issued 2022-07-05
- **US 11,505,304** (Bevirt et al.) and continuation chain
- Plus the broader Joby patent estate (50+ issued US patents 2014–2025) covering tilt-rotor electric distributed propulsion, simplified vehicle operations, prop-rotor variable pitch, conversion-corridor control, and Part 23 SVO certification basis.

This packet maps the architectural claim domains of the Joby patent estate to corpus entries that anticipate each domain. It is not a substitute for claim-chart preparation against specific claims — it is a structured starting point.

---

## How to use this packet

1. Identify the architectural domain of the Joby claim being challenged (tilt-rotor geometry, transition control, distributed electric propulsion, variable-pitch propellers stop-in-cruise, simplified vehicle operations, etc.).
2. Read the relevant section below. Each section maps the domain to corpus entries in chronological order, with the earliest as the strongest 102 anticipation candidate.
3. For 103 obviousness contentions, identify the smallest subset of entries that together disclose every claim element. Joby's electric-distributed-propulsion specific implementations are anticipated by the architectural disclosures of XV-15 (1977) plus the DEP disclosures of NASA GL-10 (2014) plus the variable-pitch-stop-in-cruise disclosures of XC-142 / Bell XV-15.
4. Each cited entry's `prior_art_notes` is element-by-element 102/103 anticipation analysis, citable as-is.

CC0 1.0. No permission required to cite, copy, or redistribute.

---

## Domain 1 — Tilt-rotor architecture (wingtip-mounted, gimbaled prop-rotor, cyclic+collective)

**Joby claim area:** wingtip-mounted tilting prop-rotors with cyclic and collective blade pitch control; nacelle rotation between vertical (hover) and horizontal (cruise).

**Anchor 102 prior art (chronological):**

- **1922** — `pescara-helicopter` — Coaxial counter-rotating rotor with cyclic and collective pitch control. Foundational disclosure of the rotor-pitch-control concept used by all subsequent rotorcraft including Joby's prop-rotors. Pescara's Spanish patent ES86,124 (1920) has been expired for over a century.
- **1959** — `kamov-ka-22-vintokryl` — Wingtip-mounted lift-rotor + cruise-propeller architecture predating Bell XV-3 in some configurations. Soviet-era disclosure, public domain since USSR dissolution.
- **1977** — `bell-xv-15` — *The* foundational disclosure of modern tilt-rotor architecture: wingtip-mounted gimbaled prop-rotor with cyclic and collective pitch, conversion-corridor envelope explicitly mapped and published by Bell/NASA, cross-shafted twin-engine drive of dual prop-rotors with engine-out continued lift in hover. Hundreds of NASA reports document the design completely (NASA SP-2000-4517).
- **1989** — `v-22-osprey` — Production-grade triplex fly-by-wire tilt-rotor flight control, cross-shafted prop-rotor drive with single-engine emergency operation in hover, operational conversion corridor with explicit nacelle-angle commanded transition. Bell V-22-era patents largely now expired.
- **2003** — `leonardo-aw609` — World's first civil-certified tilt-rotor (Italy/US, descendant of XV-15 and V-22).
- **1985** — `mil-mi-30` — Soviet tilt-rotor design materials, fully in the public domain.

**103 obviousness chain:** XV-15 + V-22 + NASA GL-10 (2014, distributed electric propulsion) together disclose every architectural element of Joby's tilt-rotor + electric DEP combination.

---

## Domain 2 — Distributed electric propulsion (DEP)

**Joby claim area:** plurality of independently-controlled electric prop-rotors providing both lift and (in tilted configuration) cruise thrust; lift redundancy via multiplicity.

**Anchor 102 prior art:**

- **1886** — `verne-albatross` — *The* foundational anticipation of distributed electric propulsion. Verne explicitly describes thirty-seven pairs of vertical lift airscrews electrically driven, distributing lift across many independent rotors with horizontal cruise propellers decoupled from lift. Predates by 36 years the de Bothezat quadrotor and 130+ years all current eVTOL companies. Public domain (Verne died 1905).
- **1922** — `de-bothezat-quadrotor` — First manned multi-rotor lift in history. Mechanical (not electric) but the architectural pattern (many independent lift rotors, attitude via differential thrust) is identical to modern DEP.
- **2011** — `volocopter-vc1` — First manned electric multicopter to achieve flight. Volocopter's foundational patent family DE102010032217.
- **2014** — `nasa-gl-10` — NASA's foundational disclosure of distributed electric propulsion (DEP) applied to tilt-wing VTOL. Ten BLDC-driven rotors on wing-distributed electric lift architecture, comprehensively published in NASA TM-2017-219653 and AIAA papers. U.S. government work, fully in the public domain.
- **2016** — `aurora-lightningstrike-xv-24a` — DARPA VTOL X-Plane: 24 ducted lift fans embedded in wing and canard, turbine-electric hybrid powerplant. Aurora's design and test data extensively published in DARPA reports and AIAA papers.

**103 obviousness chain:** Verne (1886) + de Bothezat (1922) + NASA GL-10 (2014) together disclose every claim element of DEP architecture from the most general (multi-rotor lift) to the most specific (wing-distributed BLDC electric lift). Anything Joby claims as novel over DEP is anticipated.

---

## Domain 3 — Conversion-corridor transition control

**Joby claim area:** coordinated nacelle tilt and prop-pitch transition between hover and cruise; transition envelope ("conversion corridor") explicitly modeled in flight control.

**Anchor 102 prior art:**

- **1954** — `convair-xfy-pogo` — *The* foundational disclosure of full VTOL transition: vertical takeoff, transition to horizontal cruise, transition back to vertical, and vertical landing — all in one flight, by Coleman 1954-11-02.
- **1957** — `ryan-x-13-vertijet` — First jet aircraft to demonstrate complete tail-sitting VTOL transition.
- **1958** — `doak-vz-4` — First successful tilt-duct VTOL aircraft; tilt-duct transition methodology with reaction-control supplementation in hover.
- **1964** — `ltv-xc-142` — Most thoroughly documented tilt-wing aircraft, with full conversion-corridor flight test envelope published in NASA TM-X-1842.
- **1966** — `bell-x-22` — Most thoroughly tested tilt-duct VTOL aircraft, providing 800+ flight hours of transition envelope data in NASA TN D-7095.
- **1977** — `bell-xv-15` — Conversion corridor envelope explicitly mapped and published. NASA SP-2000-4517 documents the entire envelope.

**103 obviousness chain:** XV-15 + V-22 disclose tilt-rotor conversion control; XC-142 + X-22 disclose tilt-wing and tilt-duct conversion control. Together they anticipate any conversion-corridor claim Joby asserts as novel.

---

## Domain 4 — Variable-pitch prop-rotor stopping in cruise

**Joby claim area:** prop-rotors with variable pitch that can be stopped (feathered) in cruise to reduce drag, with different rotors actively powered in different flight regimes.

**Anchor 102 prior art:**

- **1923** — `cierva-autogyro` — Articulated rotor with flapping-hinge blades autorotating from forward airflow generated by a tractor combustion engine. Foundational disclosure of rotor blade autorotation + auxiliary cruise propulsion architecture.
- **1943** — `doblhoff-wnf-342` — Compound rotorcraft architecture switching between hover (rotor powered) and cruise (rotor autorotates, forward thrust via tractor propeller). The mode-switching of lift rotors for different flight regimes.
- **1958** — `fairey-rotodyne` (referenced) — tip-jet driven rotor with mode shutdown in cruise.
- **2014** — `nasa-gl-10` — Modern DEP tilt-wing with rotor-failure reconfiguration and explicit control of differential rotor states in different flight regimes.

**103 obviousness chain:** Cierva (1923) + Doblhoff (1943) + NASA GL-10 (2014) disclose the architectural concept of differential rotor activation across flight regimes that Joby's stop-in-cruise variable-pitch prop-rotors implement in electric form.

---

## Domain 5 — Triplex fly-by-wire control

**Joby claim area:** triplex (three-channel redundant) electronic fly-by-wire flight control system.

**Anchor 102 prior art:**

- **1957** — `short-sc-1` — *The* foundational disclosure of triplex-redundant fly-by-wire control. The Short SC.1 was the first aircraft worldwide to use a triplex fly-by-wire system. UK Ministry of Aviation public-domain disclosure.
- **1989** — `v-22-osprey` — Production-grade triplex FBW for tilt-rotor flight control.
- **2003** — `leonardo-aw609` — Triplex FBW descended from V-22 program for civil tilt-rotor.

Triplex FBW is so deeply rooted in the prior art (1957) that any modern claim asserting novelty over its application to tilt-rotor or eVTOL is anticipated.

---

## Domain 6 — Simplified vehicle operations (SVO)

**Joby claim area:** reduced pilot workload via automation; single-stick or simplified-control interface mapping pilot intent to coordinated multi-effector commands.

**Anchor 102 prior art:**

- **1962** — `jetsons-aerocar` — Fictional but specific cinematic disclosure of single-stick pilot input for VTOL passenger transport. Anticipates the user-interface design pattern of simplified VTOL piloting.
- **1982** — `bladerunner-spinner` — Vectored-thrust transition under simplified pilot control with voice interaction.
- **2018** — `pivotal-blackfly` — First commercial single-axis pilot-input eVTOL operating under FAA Part 103.
- **2018** — `joby-s4` *(target itself)* — Joby's S4 cites simplified vehicle operations as design intent; this is the intent, not the novel implementation.

The SVO concept as applied to VTOL is anticipated by 1962 fictional and 2018 ultralight-class commercial prior art.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on use, citation, copying, or redistribution.

---

*Hand-written contention packet. Maintained alongside auto-generated subsystem packets by `tools/contention_packets.py`. The architectural domains and patent numbers cited above are documented in Joby Aviation S-1 SEC filing (2020-08), 10-K filings 2021–2025, and USPTO records.*
