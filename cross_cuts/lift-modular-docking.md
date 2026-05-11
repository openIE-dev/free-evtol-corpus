---
title: lift-modular-docking
parent: Cross-cuts
layout: default
---

# Cross-cut: `lift-modular-docking`

**2 corpus entries disclose this subsystem.**

Earliest disclosure: 2010-05-03

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## ETH Distributed Flight Array (2010-05-03)

- **id**: `eth-distributed-flight-array`
- **corpus**: academic
- **creator**: ETH Zurich Institute for Dynamic Systems and Control (Raffaello D'Andrea group) / Robin Oung
- **disclosure**: Oung, Raymond and D'Andrea, Raffaello. 'The Distributed Flight Array.' IEEE International Conference on Robotics and Automation (ICRA), Anchorage AK, 2010-05-03. Subsequent papers: Oung & D'Andrea, 'Modeling and Control of a Distributed Flight Array,' International Journal of Robotics Research 31(4), 2011. ETH Zurich IDSC project documented in open technical materials and demonstration videos.
- **ip status**: open-permissive
- **prior art notes**: ETH Zurich's Distributed Flight Array (Oung & D'Andrea, ICRA 2010) is the foundational academic disclosure of modular mid-air-assembling multirotor architecture — predating UPenn's ModQuad by 8 years. Establishes prior art for: (1) the architectural concept of multiple small unit-modules that dock together to form a single composite multirotor airframe, (2) distributed cooperative control across physically-connected modules sharing wireless state, (3) the fundamental rotor-failure-reconfiguration property where loss of any module is tolerated by the composite. ETH publications are comprehensively in the academic public-domain prior-art base. Anticipates: ModQuad (2018, UPenn), and any future commercial eVTOL claim asserting novelty over modular mid-air docking architecture.

## ModQuad (UPenn GRASP Laboratory) (2018-05-21)

- **id**: `upenn-modquad`
- **corpus**: academic
- **creator**: University of Pennsylvania GRASP Laboratory / David Saldaña / Mark Yim / Vijay Kumar
- **disclosure**: Saldaña, David; Gabrich, Bruno; Li, Guanrui; Yim, Mark; Kumar, Vijay. 'ModQuad: The Flying Modular Structure that Self-Assembles in Midair.' IEEE International Conference on Robotics and Automation (ICRA), Brisbane Australia, 2018-05-21 to 2018-05-25. Multiple successor papers including ModQuad-Vi (ICRA 2019), ModQuad-DoF (IROS 2018), ModQuad-RP (RAL 2020). UPenn GRASP Laboratory open-source hardware designs at github.com/swarmslab.
- **ip status**: open-permissive
- **prior art notes**: ModQuad establishes the foundational disclosure of *mid-air-docking* modular multirotor architecture — quadrotors that fly individually, align in flight, dock together, and operate as a single composite airframe. Establishes prior art for: (1) mid-air physical docking of quadrotor modules into a single rigid airframe, (2) magnetic edge-connector docking architecture for in-flight assembly, (3) distributed control allocation across N modules of a composite multirotor with N scaling up or down at runtime, (4) the cuboid-frame protective geometry enabling collision-tolerant docking maneuvers. Combined with eth-distributed-flight-array (2010 precursor), comprehensively places modular-docking eVTOL architecture in academic public-domain prior art. **Critical for any future commercial eVTOL patent claim asserting novelty over modular reconfigurable multirotor or swarm-to-single-airframe transitions** — a likely future commercial direction for scalable cargo/passenger eVTOL.
