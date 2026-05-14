---
title: "control-rotor-failure-reconfiguration"
parent: "Invalidity Contentions"
nav_order: 18
layout: default
---

# Invalidity Contention Packet — `control-rotor-failure-reconfiguration`

**Generated:** 2026-05-14  
**Cross-cut tag:** `control-rotor-failure-reconfiguration`  
**Entries:** 20 (20 commons-grade, 0 draft)  
**Earliest disclosure:** 1991-12-23  
**Most recent disclosure:** 2023-11

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `control-rotor-failure-reconfiguration`.

To use it:

1. Identify the patent claim element being challenged.
2. Match the element against the entries below in chronological order (earliest
   first). The earliest entry that discloses the element is the strongest 102
   anticipation candidate.
3. For 103 obviousness contentions, identify the closest two-or-more entries
   that together disclose all claim elements.
4. Each entry's **prior_art_notes** field is element-by-element 102/103
   anticipation analysis — citable as-is.
5. Verify the timestamp authority via the procedures in the corpus repo's
   release artifacts (FreeTSA RFC 3161, DigiCert RFC 3161, OpenTimestamps
   Bitcoin-anchored).

The Free eVTOL Corpus is licensed CC0 1.0; no permission is required to
cite, copy, or redistribute these contentions.

---

## Entries (chronological)

### 1991-12-23 — Kaman K-MAX

- **id:** `kaman-k-max`
- **corpus:** private
- **ip status:** patented
- **creator:** Kaman Aircraft Corporation
- **disclosure citation:** Kaman K-MAX first flight 1991-12-23; FAA Type Certificate Part 27 (restricted category) granted 1994-08-30. Optionally-Piloted Aircraft (OPA) variant flown autonomously by U.S. Marine Corps in Afghanistan 2011-2014 (the first deployed unmanned heavy-lift helicopter).
- **disclosed subsystems:** `autonomy-pilot-removed`, `cert-part-27`, `control-rotor-failure-reconfiguration`, `lift-coaxial-rotor`

**Prior art notes:**

> Kaman K-MAX is the modern descendant of HH-43 intermeshing-rotor architecture and the first heavy-lift helicopter deployed for unmanned cargo operations in combat (Afghanistan, 2011-2014). Establishes prior art for: (1) modern certified intermeshing-rotor helicopter (extends HH-43 prior art into the 1990s-2010s with documented operational performance), (2) optionally-piloted heavy-lift cargo VTOL (Lockheed Martin retrofit), (3) Part 27 certification basis for intermeshing rotor.

**Sources:**

1. Kaman Aerospace press releases and FAA TC dossier 1994.
2. U.S. Marine Corps K-MAX OPA mission reports, declassified excerpts.
3. Lockheed Martin / Kaman OPA program technical materials.

---

### 2010-05-03 — ETH Distributed Flight Array

- **id:** `eth-distributed-flight-array`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** ETH Zurich Institute for Dynamic Systems and Control (Raffaello D'Andrea group) / Robin Oung
- **disclosure citation:** Oung, Raymond and D'Andrea, Raffaello. 'The Distributed Flight Array.' IEEE International Conference on Robotics and Automation (ICRA), Anchorage AK, 2010-05-03. Subsequent papers: Oung & D'Andrea, 'Modeling and Control of a Distributed Flight Array,' International Journal of Robotics Research 31(4), 2011. ETH Zurich IDSC project documented in open technical materials and demonstration videos.
- **disclosed subsystems:** `lift-modular-docking`, `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `autonomy-pilot-removed`, `cert-experimental`

**Prior art notes:**

> ETH Zurich's Distributed Flight Array (Oung & D'Andrea, ICRA 2010) is the foundational academic disclosure of modular mid-air-assembling multirotor architecture — predating UPenn's ModQuad by 8 years. Establishes prior art for: (1) the architectural concept of multiple small unit-modules that dock together to form a single composite multirotor airframe, (2) distributed cooperative control across physically-connected modules sharing wireless state, (3) the fundamental rotor-failure-reconfiguration property where loss of any module is tolerated by the composite. ETH publications are comprehensively in the academic public-domain prior-art base. Anticipates: ModQuad (2018, UPenn), and any future commercial eVTOL claim asserting novelty over modular mid-air docking architecture.

**Sources:**

1. Oung, R. and D'Andrea, R. 'The Distributed Flight Array.' ICRA 2010.
2. Oung, R. and D'Andrea, R. 'Modeling and Control of a Distributed Flight Array.' IJRR 31(4), 2011.
3. ETH Zurich IDSC project archive, multiple demonstration videos.

---

### 2010-11 — UPenn cooperative grasping and transport with multiple quadrotors

- **id:** `upenn-cooperative-grasping`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** University of Pennsylvania GRASP Laboratory / Daniel Mellinger / Michael Shomin / Nathan Michael / Vijay Kumar
- **disclosure citation:** Mellinger, Daniel; Shomin, Michael; Michael, Nathan; Kumar, Vijay. 'Cooperative Grasping and Transport using Multiple Quadrotors.' International Symposium on Distributed Autonomous Robotic Systems (DARS), Lausanne, November 2010; published Springer Tracts in Advanced Robotics, 2013. UPenn GRASP Laboratory; demonstration videos widely circulated 2010-2012.
- **disclosed subsystems:** `lift-modular-docking`, `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `autonomy-pilot-removed`, `cert-experimental`

**Prior art notes:**

> UPenn's cooperative-grasping work (Mellinger, Shomin, Michael, Kumar, DARS 2010) is the closest conceptual ancestor of ModQuad within the GRASP Laboratory — multiple quadrotors rigidly coupling to a shared body and cooperatively controlling it as a single composite multirotor. Establishes prior art for: (1) rigid in-air coupling of N independent quadrotors into a single controlled composite, (2) distributed cooperative control allocation across the coupled set, (3) cooperative aerial transport / manipulation. Combined with eth-distributed-flight-array (2010) and upenn-modquad (2018), comprehensively places modular / cooperatively-coupled multirotor architecture in academic public-domain prior art.

**Sources:**

1. Mellinger, D., Shomin, M., Michael, N., Kumar, V. 'Cooperative Grasping and Transport using Multiple Quadrotors.' DARS 2010 / STAR 2013.
2. Michael, N., Fink, J., Kumar, V. 'Cooperative manipulation and transportation with aerial robots.' Autonomous Robots 30(1), 2011.
3. UPenn GRASP Laboratory project archive.

---

### 2014-06 — Malloy Aeronautics Hoverbike / US Army JTARV

- **id:** `malloy-aeronautics-hoverbike`
- **corpus:** private
- **ip status:** patented
- **creator:** Malloy Aeronautics (United Kingdom; founder Chris Malloy, Australian) — later partnered with SURVICE Engineering / U.S. Army; acquired by BAE Systems 2024
- **disclosure citation:** Malloy Aeronautics publicly unveiled the Hoverbike (a quadcopter straddle vehicle) at Paris Air Show 2014; partnered with SURVICE Engineering for the U.S. Army's Joint Tactical Aerial Resupply Vehicle (JTARV) programme 2015; the cargo variant became the TRV-150 Tactical Resupply UAS for the U.S. Marine Corps. Malloy Aeronautics acquired by BAE Systems 2024. Documented in Malloy materials and U.S. Army/USMC contract records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `autonomy-pilot-removed`, `cert-military`

**Prior art notes:**

> Malloy Aeronautics' Hoverbike / U.S. Army JTARV / USMC TRV-150 establishes prior art for the four-ducted-rotor hover-bike-and-cargo-quad family that reached U.S. military service — the crewed Hoverbike and the uncrewed TRV-150 cargo variant on a shared four-ducted-rotor airframe. Establishes prior art for: (1) ducted-rotor hover-bike architecture, (2) crewed-and-uncrewed variants on a common airframe, (3) operational military deployment of a hover-bike-class platform. Acquired by BAE Systems 2024. Together with aerofex-aero-x (2008), hoversurf-s3 (2017), jetpack-aviation-speeder (2021), and the historical personal-platform anchors, comprehensively places hover-bike architecture in commercial and military prior art. (Note: the Malloy TRV-150 is closely related to but distinct from the Skyways/Orb Aerospace TRV-150 lineage — both used the 'TRV-150' designation for USMC tactical-resupply VTOL.)

**Sources:**

1. Malloy Aeronautics Hoverbike / TRV-150 technical materials 2014-2024.
2. U.S. Army JTARV / USMC TRV-150 Tactical Resupply UAS contract records.
3. BAE Systems acquisition of Malloy Aeronautics, 2024.

---

### 2014-08 — NASA GL-10 Greased Lightning

- **id:** `nasa-gl-10`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** NASA Langley Research Center
- **disclosure citation:** Fredericks, William J. et al. 'Aerodynamic Characteristics of an Electric Distributed Propulsion Wind Tunnel Model.' AHS International Forum 70, May 2014; subsequent flight test reports through 2015 documented in NASA TM-2017-219653 and related.
- **disclosed subsystems:** `cert-experimental`, `control-rotor-failure-reconfiguration`, `lift-distributed-electric-propulsion`, `lift-tilt-wing`, `power-hybrid-genset`, `propulsion-bldc-direct-drive`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> GL-10 is NASA's foundational disclosure of distributed electric propulsion (DEP) applied to tilt-wing VTOL. Establishes prior art for: (1) ten-rotor wing-distributed electric lift architecture, (2) hybrid genset+battery propulsion topology for VTOL, (3) DEP-specific control allocation including rotor-failure reconfiguration. NASA's publication of GL-10 design and test data is comprehensive and CC-licensed by virtue of being U.S. government work. Anticipates: lift-plus-cruise commercial eVTOLs that use DEP across a wing (Beta Alia, Wisk Cora variants), and any DEP-specific control allocation patents filed post-2014. Combined with X-57 Maxwell, GL-10 places DEP comprehensively in the public domain.

**Sources:**

1. Fredericks, W.J. et al. AHS International Forum 70, May 2014.
2. Fredericks, W.J., Moore, M.D., Busan, R.C. NASA TM-2017-219653.
3. Rothhaar, P.M. et al. 'NASA Langley Distributed Propulsion VTOL Tiltwing Aircraft Simulation Modeling.' AIAA SciTech 2014.

---

### 2014-09 — PX4 VTOL flight stack

- **id:** `px4-vtol`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** PX4 / Dronecode Foundation / Lorenz Meier et al.
- **disclosure citation:** PX4 VTOL framework first merged 2014-09 (canonical PX4 git history at github.com/PX4/PX4-Autopilot); foundational paper Meier, L. et al. 'PX4: A Node-Based Multithreaded Open Source Robotics Framework for Deeply Embedded Platforms,' ICRA 2015.
- **disclosed subsystems:** `cert-experimental`, `control-fly-by-wire-triplex`, `control-rotor-failure-reconfiguration`, `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `transition-tail-sitter-pitch-up`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> PX4 is the BSD-licensed reference flight stack for VTOL aircraft, used in commercial products and academic research worldwide. Establishes prior art for: (1) modular VTOL transition state machine with named airframe types (Standard, Tail-sitter, Tilt-rotor), (2) EKF2-based state estimation across regime transitions, (3) open-source rotor-failure handling. Like ArduPilot, the BSD license lets PX4 disclosures function unambiguously as prior art.

**Sources:**

1. Meier, L., Honegger, D., Pollefeys, M. 'PX4: A Node-Based Multithreaded Open Source Robotics Framework for Deeply Embedded Platforms.' ICRA 2015.
2. PX4 Autopilot project, github.com/PX4/PX4-Autopilot.
3. PX4 user guide: docs.px4.io.

---

### 2015-04 — ArduPilot QuadPlane VTOL

- **id:** `ardupilot-quadplane`
- **corpus:** open
- **ip status:** open-copyleft
- **creator:** ArduPilot Project / Andrew Tridgell et al.
- **disclosure citation:** ArduPilot QuadPlane functionality first merged into ArduPlane main branch 2015-04 (commit history available at github.com/ArduPilot/ardupilot); first general public release with QuadPlane support: ArduPlane 3.5.0, 2015-12-14.
- **disclosed subsystems:** `cert-experimental`, `control-differential-thrust-attitude`, `control-fly-by-wire-triplex`, `control-rotor-failure-reconfiguration`, `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> ArduPilot QuadPlane is the GPL-licensed reference implementation of generic VTOL flight control. Establishes prior art (under GPL, but the architectural disclosure is unencumbered as prior art for patent purposes) for: (1) generic transition controller for lift+cruise, tilt-rotor, tilt-wing, and tail-sitter VTOLs, (2) rotor-failure detection and reconfiguration in multirotor lift, (3) Q_ASSIST transitional thrust assist algorithms. The git commit history provides timestamped disclosure of every subsystem-level innovation. Filed against any post-2015 patent claim on basic VTOL transition control or rotor-failure reconfiguration in multirotor lift, this is anticipating prior art.

**Sources:**

1. ArduPilot project, github.com/ArduPilot/ardupilot, ArduPlane git history.
2. Tridgell, Andrew. 'ArduPilot QuadPlane' presentation, ArduPilot DevConf, multiple years.
3. ArduPilot wiki: ardupilot.org/plane/docs/quadplane-overview.html.

---

### 2016-03-03 — Aurora Flight Sciences LightningStrike XV-24A

- **id:** `aurora-lightningstrike-xv-24a`
- **corpus:** academic
- **ip status:** patented
- **creator:** Aurora Flight Sciences (Boeing subsidiary) / DARPA
- **disclosure citation:** Aurora Flight Sciences LightningStrike XV-24A awarded DARPA VTOL X-Plane Phase 3 contract 2016-03-03; sub-scale demonstrator first hover 2017-04. Program subsequently de-scoped without full-scale first flight, but Aurora's design and test data were extensively published in DARPA reports and AIAA papers.
- **disclosed subsystems:** `cert-military`, `control-rotor-failure-reconfiguration`, `lift-distributed-electric-propulsion`, `lift-ducted-fan-array`, `lift-tilt-wing`, `power-hybrid-genset`, `propulsion-hybrid-series`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Aurora LightningStrike XV-24A is the most architecturally similar prior art to Lilium Jet's 36-fan ducted-fan-array eVTOL — also a tilt-wing distributed-electric-propulsion configuration with embedded ducted lift fans. The XV-24A's 24 ducted fans (2016) anticipate Lilium's 36 (2019) configuration by 3 years and DARPA-funded design publication is fully in the public domain. Establishes US prior-art lineage for: (1) high-multiplicity tilt-wing ducted-fan-array, (2) turbine-electric hybrid powerplant for VTOL, (3) the very-high-rotor-count distributed-electric-propulsion architecture. Filed against any post-2016 patent claim on similar ducted-fan-array tilt-wing configurations, this is anticipating prior art.

**Sources:**

1. Aurora Flight Sciences DARPA VTOL X-Plane technical white papers, 2014–2018.
2. DARPA VTOL X-Plane program reports, available DTIC.
3. AIAA SciTech / Aviation Forum papers from Aurora team 2014–2018.

---

### 2017 — Alauda Aeronautics Airspeeder (Mk3 / Mk4)

- **id:** `alauda-airspeeder`
- **corpus:** private
- **ip status:** patented
- **creator:** Alauda Aeronautics / Airspeeder (Adelaide, Australia) / Matthew Pearson
- **disclosure citation:** Alauda Aeronautics (founded 2016 in Adelaide by Matthew Pearson) developed the Airspeeder racing eVTOL — the Mk3 (uncrewed remote-piloted racer, first flew 2021, raced in the 'EXA Series' 2022) and the Mk4 (crewed racer, unveiled 2022, designed for the manned Airspeeder Grand Prix). The world's first eVTOL racing series. Documented in Alauda/Airspeeder materials and Australian CASA filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> Alauda Aeronautics' Airspeeder (Mk3 uncrewed 2021, Mk4 crewed 2022) establishes Australian prior art for the racing eVTOL — a high-power-to-weight single-seat (or uncrewed) octocopter designed for close-formation pylon racing, the world's first eVTOL racing series. Establishes prior art for: (1) racing-tuned eVTOL flight envelope and aggressive-maneuvering control, (2) the racing-eVTOL operational concept, (3) crewed/uncrewed variants on a racing airframe. Together with amsl-vertiia (AU, hydrogen passenger eVTOL), deepens Australia's eVTOL footprint. The racing-eVTOL niche is a distinct application alongside passenger air taxi, cargo, personal, and military eVTOL — and Airspeeder is its foundational disclosure.

**Sources:**

1. Alauda Aeronautics / Airspeeder Mk3 / Mk4 technical materials 2017-2024.
2. Airspeeder EXA Series race records 2022.
3. Australian CASA (Civil Aviation Safety Authority) Airspeeder filings.

---

### 2018-02-05 — EHang EH216-S

- **id:** `ehang-eh216`
- **corpus:** private
- **ip status:** patented
- **creator:** EHang Holdings
- **disclosure citation:** EHang 184 / 216 platform first publicly disclosed at CES 2016; EH216 designation first used 2018-02-05 in EHang corporate filings; EH216-S type certificate granted by CAAC 2023-10-13 (TC No. ETC-G-2023-101). Production certificate granted 2024-04-07.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-bvlos-detect-and-avoid`, `autonomy-pilot-removed`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `lift-coaxial-rotor`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `safety-ballistic-parachute`, `safety-redundant-bus`, `sensing-lidar-terrain`

**Prior art notes:**

> EHang EH216-S is the first eVTOL to receive a full type certificate from a major civil aviation authority (CAAC, 2023-10-13). The TC documentation is publicly available and constitutes a comprehensive engineering disclosure under SC-VTOL-like framework. Establishes commons-grade disclosure of: (1) eight-coaxial-pair 16-rotor lift architecture, (2) production autonomous-passenger eVTOL flight management system, (3) the CAAC SC-VTOL certification basis itself (the regulation and applied airworthiness criteria are public). Together with volocopter-vc1, places multirotor passenger eVTOL architecture comprehensively in the public domain as of 2018.

**Sources:**

1. EHang Holdings Form 20-F annual report 2023 (NASDAQ: EH).
2. CAAC Type Certificate ETC-G-2023-101, public registry.
3. Wang, Hu et al. 'EH216 design and certification basis' EHang technical white paper, 2022.

---

### 2018-05 — DRAGON (University of Tokyo JSK Laboratory)

- **id:** `univ-tokyo-dragon`
- **corpus:** academic
- **ip status:** patented
- **creator:** University of Tokyo JSK Laboratory (Masayuki Inaba) / Moju Zhao / Tomoki Anzai / Fan Shi
- **disclosure citation:** Zhao, Moju; Anzai, Tomoki; Shi, Fan; Chen, Xiangyu; Okada, Kei; Inaba, Masayuki. 'Design, Modeling, and Control of an Aerial Robot DRAGON: A Dual-Rotor-Embedded Multilink Robot With the Ability of Multi-Degree-of-Freedom Aerial Transformation.' IEEE Robotics and Automation Letters 3(2), 2018; presented ICRA 2018. University of Tokyo JSK Laboratory. DRAGON = 'Dual-rotor embedded multilink Robot with the Ability of multi-deGree-of-freedom aerial transformatioN'.
- **disclosed subsystems:** `airframe-in-flight-morphing`, `lift-modular-docking`, `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `autonomy-pilot-removed`, `cert-experimental`

**Prior art notes:**

> The University of Tokyo JSK Laboratory's DRAGON (Zhao, Anzai, Shi, Chen, Okada, Inaba, RAL 2018 / ICRA 2018) is the foundational disclosure of the multilink transforming aerial robot — a serially-connected chain of thrust-vectoring modules with actuated joints, able to change its whole-body shape in flight (line, curve, loop, gap-thread) and perform whole-body aerial manipulation by wrapping around objects. Establishes Japanese prior art for: (1) modular serially-linked aerial-robot architecture, (2) in-flight whole-body transformation with real-time control allocation across the changing kinematic chain, (3) whole-body aerial grasping/manipulation. Together with eth-distributed-flight-array, upenn-modquad, and the morphing-drone lineage (epfl-folding-drone, uzh-foldable-drone), comprehensively places modular / transforming / reconfigurable aerial-robot architecture in academic public-domain prior art across Swiss, US, and Japanese research lineages. **Directly anticipates any future commercial eVTOL claim involving in-flight reconfiguration of a multi-module airframe.**

**Sources:**

1. Zhao, M., Anzai, T., Shi, F., Chen, X., Okada, K., Inaba, M. 'Design, Modeling, and Control of an Aerial Robot DRAGON.' IEEE RAL 3(2), 2018.
2. Anzai, T., Zhao, M., Murooka, M., Shi, F., Okada, K., Inaba, M. 'Aerial Grasping Based on Shape Adaptive Transformation by HALO.' ICRA 2018.
3. University of Tokyo JSK Laboratory publications archive.

---

### 2018-05-21 — ModQuad (UPenn GRASP Laboratory)

- **id:** `upenn-modquad`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** University of Pennsylvania GRASP Laboratory / David Saldaña / Mark Yim / Vijay Kumar
- **disclosure citation:** Saldaña, David; Gabrich, Bruno; Li, Guanrui; Yim, Mark; Kumar, Vijay. 'ModQuad: The Flying Modular Structure that Self-Assembles in Midair.' IEEE International Conference on Robotics and Automation (ICRA), Brisbane Australia, 2018-05-21 to 2018-05-25. Multiple successor papers including ModQuad-Vi (ICRA 2019), ModQuad-DoF (IROS 2018), ModQuad-RP (RAL 2020). UPenn GRASP Laboratory open-source hardware designs at github.com/swarmslab.
- **disclosed subsystems:** `airframe-collision-resilient-cage`, `autonomy-pilot-removed`, `cert-experimental`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `lift-distributed-electric-propulsion`, `lift-modular-docking`

**Prior art notes:**

> ModQuad establishes the foundational disclosure of *mid-air-docking* modular multirotor architecture — quadrotors that fly individually, align in flight, dock together, and operate as a single composite airframe. Establishes prior art for: (1) mid-air physical docking of quadrotor modules into a single rigid airframe, (2) magnetic edge-connector docking architecture for in-flight assembly, (3) distributed control allocation across N modules of a composite multirotor with N scaling up or down at runtime, (4) the cuboid-frame protective geometry enabling collision-tolerant docking maneuvers. Combined with eth-distributed-flight-array (2010 precursor), comprehensively places modular-docking eVTOL architecture in academic public-domain prior art. **Critical for any future commercial eVTOL patent claim asserting novelty over modular reconfigurable multirotor or swarm-to-single-airframe transitions** — a likely future commercial direction for scalable cargo/passenger eVTOL.

**Sources:**

1. Saldaña, D., Gabrich, B., Li, G., Yim, M., Kumar, V. 'ModQuad: The Flying Modular Structure that Self-Assembles in Midair.' ICRA 2018.
2. Saldaña, D. et al. 'ModQuad-Vi: A Vision-Based Self-Assembling Modular Quadrotor.' ICRA 2019.
3. Gabrich, B. et al. 'Design and Control of ModQuad-DoF.' IROS 2018.
4. Li, G. et al. 'A Modular Aerial Robot Platform: ModQuad-RP.' IEEE RAL, 2020.
5. UPenn GRASP Laboratory ModQuad project archive, github.com/swarmslab.

---

### 2018-09 — Jetson ONE

- **id:** `jetson-one`
- **corpus:** private
- **ip status:** patented
- **creator:** Jetson AB (Italy / Sweden joint operation)
- **disclosure citation:** Jetson AB founded 2018-09 by Tomasz Patan (Polish-Swedish) and Peter Ternström (Swedish); Jetson ONE design unveiled 2020-04-21; first manned flight 2020-09; first customer deliveries 2023-09.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-part-103-ultralight`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `lift-coaxial-rotor`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`

**Prior art notes:**

> Jetson ONE is the leading consumer ultralight-class single-seat eVTOL — the Swedish/Italian/Polish realization of the open-frame multirotor design originally disclosed by Curtiss-Wright VZ-7 (1958). Operates under FAA Part 103 ultralight rules with no pilot license required. Establishes Northern European prior-art lineage for consumer-grade ultralight eVTOL with open-rotor architecture and rotor-failure reconfiguration.

**Sources:**

1. Jetson AB press releases 2018–2024.
2. Jetson ONE technical specifications, jetsonaero.com.
3. FAA Part 103 ultralight registration records (Jetson ONE customer aircraft).

---

### 2018-10-25 — LIFT Aircraft Hexa

- **id:** `lift-aircraft-hexa`
- **corpus:** private
- **ip status:** patented
- **creator:** LIFT Aircraft Inc (Austin, Texas)
- **disclosure citation:** LIFT Aircraft Hexa publicly unveiled 2018-10-25; first crewed flights 2019; FAA Part 103 ultralight category (no pilot license required); public 'flight experiences' / training-flight programme launched 2021-2024. Documented in LIFT Aircraft press materials, FAA Part 103 registrations, and U.S. Air Force AFWERX Agility Prime contracts.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `control-simplified-vehicle-operations`, `cert-part-103-ultralight`, `airframe-composite-monocoque`

**Prior art notes:**

> LIFT Aircraft Hexa establishes US prior art for the maximally-redundant single-seat multirotor eVTOL — eighteen independent rotors each with its own battery and motor (full distributed redundancy, tolerates loss of six rotors), single-joystick fly-by-wire simplified vehicle operations, FAA Part 103 ultralight operation. Establishes prior art for: (1) per-rotor-independent battery/motor architecture with deep failure tolerance, (2) consumer-grade single-joystick SVO for an 18-rotor eVTOL, (3) Part 103 ultralight commercial flight-experience deployment. Together with pivotal-blackfly, jetson-one, ehang-eh216, and volocopter-volocity, comprehensively places single-seat / small-pax multirotor eVTOL in commercial prior art.

**Sources:**

1. LIFT Aircraft press releases and FAA Part 103 registrations 2018-2024.
2. U.S. Air Force AFWERX Agility Prime contract records (LIFT Hexa).

---

### 2019 — teTra Mk-5

- **id:** `tetra-mk-5`
- **corpus:** private
- **ip status:** patented
- **creator:** teTra Aviation Corporation (Tokyo, Japan) / Tasuku Nakai
- **disclosure citation:** teTra Aviation Corporation (founded 2018 in Tokyo, an outgrowth of GoFly Prize-competing students) revealed the Mk-3 personal eVTOL (2020, GoFly Prize 'Pratt & Whitney Disruptor Award' winner) and subsequently the production Mk-5 single-seat personal eVTOL (2021); first crewed flights and FAA Special Airworthiness Certificate process underway. Documented in teTra materials and GoFly Prize records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `transition-mode-shutdown`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-103-ultralight`

**Prior art notes:**

> teTra Mk-5 establishes Japanese prior art for the high-rotor-count single-seat personal eVTOL — a fixed-wing airframe with 32 small distributed lift rotors for hover redundancy plus wing lift for cruise efficiency. A GoFly Prize-derived design. Establishes prior art for: (1) very-high-rotor-count (~32) personal eVTOL with fixed wings, (2) the GoFly Prize lineage of personal-flight designs. Together with skydrive-sd-05 (JP, multirotor air taxi), aska-a5 (JP/US, drive+fly), honda-evtol (JP, hybrid), and the Japanese fictional VTOL anchors, deepens Japan's eVTOL footprint. Together with lift-aircraft-hexa (US, 18-rotor) and ehang-eh216 (CN, 16-rotor), places high-rotor-count personal/small eVTOL architecture in prior art.

**Sources:**

1. teTra Aviation Mk-3 / Mk-5 technical materials 2019-2024.
2. GoFly Prize competition records (teTra Mk-3, Pratt & Whitney Disruptor Award).

---

### 2019-08-14 — Volocopter VoloCity

- **id:** `volocopter-volocity`
- **corpus:** private
- **ip status:** patented
- **creator:** Volocopter GmbH
- **disclosure citation:** VoloCity production-design unveiling 2019-08-14 at Helsinki ITS World Congress; precursor VC-200 first manned flight 2013-11-17; first public manned demo at Singapore 2019-10-22. EASA SC-VTOL certification process actively pursued; targeted operations Paris 2024 / 2026 commercial rollouts.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`

**Prior art notes:**

> Volocopter VoloCity is the production design descending from e-volo VC1 (2011, first manned multicopter flight). 18-rotor circular-ring multirotor architecture, EASA SC-VTOL certification basis. Establishes the German prior-art lineage from e-volo through Volocopter for circular-ring multirotor passenger eVTOL — foundational and predates EHang in manned-flight precedence.

**Sources:**

1. Volocopter press releases 2013–2024.
2. EASA SC-VTOL filings, public docket.
3. Vertical Flight Society Forum technical papers from Volocopter 2014–2024.

---

### 2019-10-30 — Volocopter VoloDrone

- **id:** `volocopter-volodrone`
- **corpus:** private
- **ip status:** patented
- **creator:** Volocopter GmbH (Bruchsal, Germany)
- **disclosure citation:** Volocopter VoloDrone publicly demonstrated 2019-10-30 at the Volocopter facility in Bruchsal, Germany — a heavy-cargo unmanned variant of the Volocopter 18-rotor multirotor architecture. Subsequently demonstrated for DB Schenker cargo logistics and at the Volocopter Hamburg test campaign. Documented in Volocopter press materials and EASA filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `autonomy-pilot-removed`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`, `safety-redundant-bus`

**Prior art notes:**

> Volocopter VoloDrone establishes German prior art for the cargo-variant-of-passenger-multirotor pattern — unmanned heavy-cargo operations on the same 18-rotor airframe as the VoloCity passenger eVTOL, with up to 200 kg payload. Establishes prior art for: (1) shared-airframe passenger/cargo eVTOL family architecture, (2) underslung cargo and swappable container variants of a multirotor passenger eVTOL. Adds the cargo dimension to the Volocopter prior-art lineage (alongside the passenger volocopter-vc1 / volocopter-volocity).

**Sources:**

1. Volocopter VoloDrone press materials and demonstrations 2019-2024.
2. DB Schenker / Volocopter cargo logistics partnership records.

---

### 2022-06 — Doroni H1 / H1-X

- **id:** `doroni-h1`
- **corpus:** private
- **ip status:** patented
- **creator:** Doroni Aerospace (Fort Lauderdale, Florida) / Doron Merdinger
- **disclosure citation:** Doroni Aerospace (founded 2016 by Doron Merdinger) unveiled the H1 two-seat personal eVTOL in 2022; first crewed test flight 2023-05; received an FAA Special Airworthiness Certificate (Experimental) 2023; developing the H1-X for FAA Part 23 certification. Designed to fit in a two-car garage and operate from driveways under (intended) Part 103 ultralight or LSA rules. Documented in Doroni materials and FAA filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `control-simplified-vehicle-operations`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> Doroni H1 establishes US prior art for the garage-storable enclosed-rotor two-seat personal eVTOL — eight ducted lift rotors housed within the airframe body (not on exposed booms), small fixed wings, car-like footprint, driveway operation. Establishes prior art for: (1) fully-enclosed-within-body lift rotors on a personal eVTOL, (2) garage-storable / driveway-operable two-seat personal eVTOL form factor. Together with pivotal-blackfly, jetson-one, lift-aircraft-hexa, alef-model-a, and the historical personal-platform anchors, comprehensively places small-personal eVTOL architecture in prior art.

**Sources:**

1. Doroni Aerospace H1 / H1-X technical materials 2022-2024.
2. FAA Special Airworthiness Certificate dossier (Doroni H1).

---

### 2023-08-16 — DJI FlyCart 30

- **id:** `dji-flycart-30`
- **corpus:** private
- **ip status:** patented
- **creator:** SZ DJI Technology Co Ltd (Shenzhen)
- **disclosure citation:** DJI FlyCart 30 publicly unveiled 2023-08-16 in Shenzhen; CAAC type certification application 2023; commercial deliveries to Chinese and international markets 2024. DJI is the world's largest drone manufacturer and holds an extensive multirotor patent estate.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-bvlos-detect-and-avoid`, `autonomy-pilot-removed`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `lift-coaxial-rotor`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`

**Prior art notes:**

> DJI FlyCart 30 is the entry of the world's largest drone manufacturer into the heavy-cargo eVTOL category. DJI's massive patent estate and operational scale (millions of multirotor flights/day globally) constitute foundational prior-art coverage for: (1) coaxial-pair multirotor manufacturing at scale, (2) autonomous multirotor cargo delivery, (3) consumer-priced multirotor architecture migration to commercial cargo class. Establishes Chinese prior-art lineage for heavy-payload multirotor cargo eVTOL with explicit Beyond Visual Line of Sight (BVLOS) operational basis.

**Sources:**

1. DJI press releases and product disclosures 2023–2024.
2. CAAC type certification dossier (DJI FlyCart 30).
3. DJI patent estate, USPTO and CNIPA records.

---

### 2023-11 — Sarla Aviation Shunya

- **id:** `sarla-aviation-shunya`
- **corpus:** private
- **ip status:** patented
- **creator:** Sarla Aviation (Bangalore, India)
- **disclosure citation:** Sarla Aviation (founded 2023 in Bangalore by Adrian Schmidt, Rakesh Gaonkar, and Shivam Chauhan; named after Sarla Thakral, India's first woman pilot) unveiled the Shunya eVTOL air taxi in November 2023, with production targeted for ~2028 in Indian cities (Bangalore, Mumbai, Delhi, Pune); sub-scale prototype work 2024. Documented in Sarla materials and Indian DGCA engagement records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-23`, `airframe-composite-monocoque`

**Prior art notes:**

> Sarla Aviation Shunya establishes additional Indian prior art for the urban-air-taxi multirotor eVTOL — a five-seat eVTOL designed for short hops in dense Indian cities, the second major Indian eVTOL OEM after ePlane. Establishes Indian depth alongside eplane-company-e200 (IN, lift+cruise) and the Indian fictional flight anchor (Krrish). Together with ehang-eh216 (CN), volocopter-volocity (DE), and the global multirotor air-taxi cluster, places urban-air-taxi multirotor eVTOL architecture in prior art across US, EU, China, India, Japan, Korea, and Brazil lineages.

**Sources:**

1. Sarla Aviation Shunya technical materials 2023-2024.
2. Indian DGCA (Directorate General of Civil Aviation) UAM engagement records.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `04cd8e0`.*
