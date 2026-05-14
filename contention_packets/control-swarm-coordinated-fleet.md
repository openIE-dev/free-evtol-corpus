---
title: "control-swarm-coordinated-fleet"
parent: "Invalidity Contentions"
nav_order: 20
layout: default
---

# Invalidity Contention Packet — `control-swarm-coordinated-fleet`

**Generated:** 2026-05-14  
**Cross-cut tag:** `control-swarm-coordinated-fleet`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 2011-12-02  
**Most recent disclosure:** 2016-11-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `control-swarm-coordinated-fleet`.

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

### 2011-12-02 — ETH Flight Assembled Architecture

- **id:** `eth-flight-assembled-architecture`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** ETH Zurich Gramazio Kohler Research / Raffaello D'Andrea (flying machine control) / FRAC Centre Orléans
- **disclosure citation:** Flight Assembled Architecture installation, FRAC Centre, Orléans, France, 2011-12-02 to 2012-02-19. ETH Zurich Gramazio Kohler Research (Fabio Gramazio, Matthias Kohler) with flying-machine control by Raffaello D'Andrea's group. Quadrotors autonomously assembled a 6-meter tower from 1,500 foam modules. Documented in academic publications and the book 'Flight Assembled Architecture' (Editions HYX, 2013).
- **disclosed subsystems:** `lift-modular-docking`, `control-swarm-coordinated-fleet`, `autonomy-pilot-removed`, `cert-experimental`

**Prior art notes:**

> ETH Zurich's Flight Assembled Architecture (Gramazio Kohler + D'Andrea, 2011-2012) is the foundational disclosure of autonomous aerial robots constructing load-bearing structures by coordinated assembly of modular components. Establishes prior art for: (1) coordinated multi-quadrotor fleet assembly of structures from modular building blocks, (2) the concept of on-demand aerially-assembled structures (directly relevant to 'a flying structure built on demand from individual modules'), (3) autonomous pick-and-place aerial manipulation at fleet scale. Combined with eth-distributed-flight-array (2010), upenn-cooperative-grasping (2010), and upenn-modquad (2018), comprehensively places modular-aerial-assembly architecture in academic public-domain prior art.

**Sources:**

1. Willmann, J., Augugliaro, F., Cadalbert, T., D'Andrea, R., Gramazio, F., Kohler, M. 'Aerial Robotic Construction: Towards a New Field of Architectural Research.' International Journal of Architectural Computing 10(3), 2012.
2. Gramazio, F., Kohler, M., D'Andrea, R. (eds). Flight Assembled Architecture. Editions HYX, 2013.
3. Augugliaro, F. et al. 'The Flight Assembled Architecture installation: Cooperative construction with flying machines.' IEEE Control Systems Magazine 34(4), 2014.

---

### 2012-01-31 — KMel Robotics / UPenn nano-quadrotor swarm

- **id:** `kmel-nano-quadrotor-swarm`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** KMel Robotics (UPenn GRASP Laboratory spinout) / Alex Kushleyev / Daniel Mellinger / Vijay Kumar
- **disclosure citation:** Kushleyev, Alex; Mellinger, Daniel; Powers, Caitlin; Kumar, Vijay. 'Towards a swarm of agile micro quadrotors.' Robotics: Science and Systems (RSS), Sydney, 2012; published Autonomous Robots 35(4), 2013. The famous '20 nano quadrotors flying in formation' video was released by the UPenn GRASP Lab / KMel Robotics 2012-01-31 (viewed tens of millions of times). KMel Robotics later acquired by Qualcomm.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-swarm-coordinated-fleet`, `control-differential-thrust-attitude`, `autonomy-pilot-removed`, `cert-experimental`

**Prior art notes:**

> The KMel Robotics / UPenn GRASP nano-quadrotor swarm (Kushleyev, Mellinger, Powers, Kumar, RSS 2012) is the foundational public disclosure of large-scale agile multirotor swarm coordination — the famous '20 nano quadrotors' video. Establishes prior art for: (1) tightly-coordinated 3D formation flight of N independent multirotors, (2) dynamic in-flight reconfiguration of swarm formations, (3) coordinated passage through constrained openings while maintaining formation. Combined with intel-shooting-star (2016) and collmot-drone-show (2014), comprehensively places multi-drone coordinated-fleet control in pre-2017 prior art. The 'fleet acting as one system' concept central to modern modular/swarm eVTOL is anticipated here.

**Sources:**

1. Kushleyev, A., Mellinger, D., Powers, C., Kumar, V. 'Towards a swarm of agile micro quadrotors.' RSS 2012 / Autonomous Robots 35(4), 2013.
2. UPenn GRASP Laboratory / KMel Robotics video, 'A Swarm of Nano Quadrotors,' 2012-01-31.

---

### 2014 — CollMot Robotics drone-show swarm

- **id:** `collmot-drone-show`
- **corpus:** private
- **ip status:** patented
- **creator:** CollMot Robotics / CollMot Entertainment (Budapest, Hungary) / Gábor Vásárhelyi / Tamás Vicsek
- **disclosure citation:** CollMot Robotics founded 2014 in Budapest by Gábor Vásárhelyi (with roots in Tamás Vicsek's collective-motion research group at Eötvös Loránd University); decentralized outdoor drone-swarm flight published in Vásárhelyi, G. et al. 'Optimized flocking of autonomous drones in confined environments,' Science Robotics 3(20), 2018. CollMot Entertainment performs commercial drone-light shows worldwide.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-swarm-coordinated-fleet`, `autonomy-pilot-removed`, `cert-experimental`

**Prior art notes:**

> CollMot Robotics establishes Hungarian prior art for decentralized outdoor drone-swarm coordination — distinct from motion-capture-based indoor swarms (UPenn nano-quad, Intel Shooting Star) by operating outdoors at scale with onboard GPS and decentralized self-organizing flocking. Rooted in Tamás Vicsek's foundational collective-motion physics (the Vicsek model, 1995). The Science Robotics 2018 paper (Vásárhelyi et al.) is a comprehensive disclosure. Adds Hungary to the eVTOL / aerial-robotics prior-art map. Together with kmel-nano-quadrotor-swarm and intel-shooting-star, places multi-drone coordinated-fleet control in continuous prior-art coverage.

**Sources:**

1. Vásárhelyi, G., Virágh, C., Somorjai, G., Nepusz, T., Eiben, A.E., Vicsek, T. 'Optimized flocking of autonomous drones in confined environments.' Science Robotics 3(20), 2018.
2. Vicsek, T. et al. 'Novel type of phase transition in a system of self-driven particles.' Physical Review Letters 75(6), 1995.
3. CollMot Robotics / CollMot Entertainment technical materials.

---

### 2016-11-04 — Intel Shooting Star drone-light-show system

- **id:** `intel-shooting-star`
- **corpus:** private
- **ip status:** patented
- **creator:** Intel Corporation
- **disclosure citation:** Intel Shooting Star drone-light-show system publicly demonstrated 2016-11-04 (500-drone Guinness World Record, Krailling Germany); subsequently scaled to 1,218 drones (PyeongChang Olympics opening ceremony 2018-02-09) and 2,018+ drones (Folsom CA, 2018-07). Intel filed multiple patents on swarm light-show choreography and coordinated multi-drone control. Publicly disclosed via Intel press materials and Guinness World Records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-swarm-coordinated-fleet`, `autonomy-pilot-removed`, `cert-experimental`

**Prior art notes:**

> Intel Shooting Star establishes US commercial prior art for large-scale single-operator coordinated drone-fleet control — 500 drones (2016), 1,218 drones (PyeongChang 2018 Olympics), 2,018+ drones (2018). Establishes prior art for: (1) one operator controlling a fleet of N independent multirotors as a single coordinated system, (2) choreography-software-driven fleet trajectory generation at scale, (3) the 'fleet flies as one system' control paradigm directly relevant to any modular / swarm-coordinated eVTOL claim. Together with kmel-nano-quadrotor-swarm (2012) and collmot-drone-show (2014), comprehensively places coordinated-multi-drone control in 2012-2018 prior art across US academic, US commercial, and Hungarian commercial lineages.

**Sources:**

1. Intel Corporation press releases on Shooting Star, 2016-2020.
2. Guinness World Records, 'Most unmanned aerial vehicles (UAVs) airborne simultaneously,' 2016-11-04 and 2018-07.
3. PyeongChang 2018 Olympic Winter Games opening ceremony, 2018-02-09.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `04cd8e0`.*
