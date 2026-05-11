---
title: "lift-modular-docking"
parent: "Invalidity Contentions"
nav_order: 20
layout: default
---

# Invalidity Contention Packet — `lift-modular-docking`

**Generated:** 2026-05-11  
**Cross-cut tag:** `lift-modular-docking`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2010-05-03  
**Most recent disclosure:** 2018-05-21

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `lift-modular-docking`.

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

### 2018-05-21 — ModQuad (UPenn GRASP Laboratory)

- **id:** `upenn-modquad`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** University of Pennsylvania GRASP Laboratory / David Saldaña / Mark Yim / Vijay Kumar
- **disclosure citation:** Saldaña, David; Gabrich, Bruno; Li, Guanrui; Yim, Mark; Kumar, Vijay. 'ModQuad: The Flying Modular Structure that Self-Assembles in Midair.' IEEE International Conference on Robotics and Automation (ICRA), Brisbane Australia, 2018-05-21 to 2018-05-25. Multiple successor papers including ModQuad-Vi (ICRA 2019), ModQuad-DoF (IROS 2018), ModQuad-RP (RAL 2020). UPenn GRASP Laboratory open-source hardware designs at github.com/swarmslab.
- **disclosed subsystems:** `lift-modular-docking`, `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `autonomy-pilot-removed`, `cert-experimental`

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

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `7e83101`.*
