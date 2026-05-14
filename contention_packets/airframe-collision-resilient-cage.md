---
title: "airframe-collision-resilient-cage"
parent: "Invalidity Contentions"
nav_order: 1
layout: default
---

# Invalidity Contention Packet — `airframe-collision-resilient-cage`

**Generated:** 2026-05-14  
**Cross-cut tag:** `airframe-collision-resilient-cage`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2014-09  
**Most recent disclosure:** 2018-05-21

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `airframe-collision-resilient-cage`.

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

### 2014-09 — EPFL GimBall

- **id:** `epfl-gimball`
- **corpus:** academic
- **ip status:** patented
- **creator:** EPFL Laboratory of Intelligent Systems (Dario Floreano) / Adrien Briod (later Flyability SA)
- **disclosure citation:** Briod, Adrien; Kornatowski, Przemyslaw; Zufferey, Jean-Christophe; Floreano, Dario. 'A Collision-resilient Flying Robot.' Journal of Field Robotics 31(4), 2014. EPFL Laboratory of Intelligent Systems; won the UAE Drones for Good Award 2015; commercialized as Flyability Elios via the Flyability SA spinout.
- **disclosed subsystems:** `airframe-collision-resilient-cage`, `lift-coaxial-rotor`, `lift-distributed-electric-propulsion`, `cert-experimental`

**Prior art notes:**

> EPFL's GimBall (Briod, Kornatowski, Zufferey, Floreano, JFR 2014) is the foundational disclosure of the gimbaled protective-cage flying-robot architecture — a freely-rotating outer cage that decouples collision impacts from the inner flight system, enabling collision-tolerant flight. Establishes prior art for: (1) rotating protective-cage airframe geometry, (2) collision-tolerant operation enabling contact-based maneuvers (including docking). The protective-cage concept is directly antecedent to ModQuad's cuboid-frame docking architecture. Commercialized as Flyability Elios for industrial confined-space inspection.

**Sources:**

1. Briod, A., Kornatowski, P., Zufferey, J.-C., Floreano, D. 'A Collision-resilient Flying Robot.' Journal of Field Robotics 31(4), 2014.
2. EPFL Laboratory of Intelligent Systems publications archive.
3. Flyability SA technical materials.

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

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `674103d`.*
