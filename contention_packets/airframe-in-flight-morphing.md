---
title: "airframe-in-flight-morphing"
parent: "Invalidity Contentions"
nav_order: 3
layout: default
---

# Invalidity Contention Packet — `airframe-in-flight-morphing`

**Generated:** 2026-05-14  
**Cross-cut tag:** `airframe-in-flight-morphing`  
**Entries:** 3 (3 commons-grade, 0 draft)  
**Earliest disclosure:** 2017-08  
**Most recent disclosure:** 2018-12

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `airframe-in-flight-morphing`.

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

### 2017-08 — EPFL origami folding drone

- **id:** `epfl-folding-drone`
- **corpus:** academic
- **ip status:** patented
- **creator:** EPFL Laboratory of Intelligent Systems (Dario Floreano) / Stefano Mintchev
- **disclosure citation:** Mintchev, Stefano; Floreano, Dario. 'A pocket sized foldable quadrotor for collaborative missions.' (and related papers). EPFL Laboratory of Intelligent Systems, 2017; published IEEE Robotics and Automation Letters and ICRA/IROS 2017-2019. Origami-inspired quadrotor that folds into a compact package for storage/transport and self-deploys for flight.
- **disclosed subsystems:** `airframe-in-flight-morphing`, `lift-distributed-electric-propulsion`, `cert-experimental`

**Prior art notes:**

> EPFL's origami folding drone (Mintchev & Floreano, 2017) establishes prior art for foldable / self-deploying multirotor airframes — arms that collapse into a compact transport package and deploy for flight. Establishes prior art for: (1) origami-inspired collapsible quadrotor arm architecture, (2) spring-loaded or motor-driven self-deployment. Together with uzh-foldable-drone (active mid-flight folding) and univ-tokyo-dragon (in-flight multilink transformation), comprehensively places morphing / folding aerial-robot architecture in academic public-domain prior art.

**Sources:**

1. Mintchev, S., Floreano, D. 'A pocket sized foldable quadrotor for collaborative missions.' Related EPFL LIS publications 2017-2019.
2. Mintchev, S., Daler, L., L'Eplattenier, G., Saint-Raymond, L., Floreano, D. 'Foldable and Self-Deployable Pocket Sized Quadrotor.' ICRA 2015.
3. EPFL Laboratory of Intelligent Systems publications archive.

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

### 2018-12 — UZH RPG foldable drone

- **id:** `uzh-foldable-drone`
- **corpus:** academic
- **ip status:** patented
- **creator:** University of Zurich Robotics and Perception Group (Davide Scaramuzza) / Davide Falanga / Kevin Kleber / Stefano Mintchev / Dario Floreano
- **disclosure citation:** Falanga, Davide; Kleber, Kevin; Mintchev, Stefano; Floreano, Dario; Scaramuzza, Davide. 'The Foldable Drone: A Morphing Quadrotor That Can Squeeze and Fly.' IEEE Robotics and Automation Letters 4(2), 2018 / presented ICRA 2019. University of Zurich Robotics and Perception Group (with EPFL LIS collaboration). A quadrotor that actively folds its arms in flight to change its morphology and pass through narrow gaps.
- **disclosed subsystems:** `airframe-in-flight-morphing`, `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `cert-experimental`

**Prior art notes:**

> UZH's Foldable Drone (Falanga, Kleber, Mintchev, Floreano, Scaramuzza, RAL 2018 / ICRA 2019) is the foundational disclosure of in-flight repeatable airframe morphing — a quadrotor that actively folds its arms to change its geometry mid-flight (X → H → O shape) and adapts its control allocation in real time. Establishes prior art for: (1) servo-actuated repeatable in-flight airframe reconfiguration, (2) real-time control-allocation adaptation to changing rotor geometry, (3) morphology-driven obstacle traversal. Together with univ-tokyo-dragon (multilink transformation) and epfl-folding-drone (one-shot deployment), comprehensively places morphing aerial-robot architecture in academic public-domain prior art — directly relevant to any modular or reconfigurable eVTOL claim involving in-flight geometry change.

**Sources:**

1. Falanga, D., Kleber, K., Mintchev, S., Floreano, D., Scaramuzza, D. 'The Foldable Drone: A Morphing Quadrotor That Can Squeeze and Fly.' IEEE RAL 4(2), 2018.
2. University of Zurich Robotics and Perception Group publications archive.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `04cd8e0`.*
