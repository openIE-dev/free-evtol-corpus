---
title: "lift-modular-docking"
parent: "Invalidity Contentions"
nav_order: 27
layout: default
---

# Invalidity Contention Packet — `lift-modular-docking`

**Generated:** 2026-05-12  
**Cross-cut tag:** `lift-modular-docking`  
**Entries:** 8 (8 commons-grade, 0 draft)  
**Earliest disclosure:** 2010-05-03  
**Most recent disclosure:** 2018-08

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

### 2011-09 — University of Bologna Modular Multirotor Vehicle

- **id:** `bologna-modular-multirotor`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** University of Bologna CASY (Center for Research on Complex Automated Systems) / Roberto Naldi / Lorenzo Marconi
- **disclosure citation:** Naldi, Roberto; Marconi, Lorenzo et al. 'Modeling and Control of a Class of Modular Aerial Robots Combining Under-Actuated Air Vehicles With a Reconfigurable Mechanism.' IEEE Transactions on Robotics, subsequent to 2011 conference work. University of Bologna CASY group; papers in IEEE T-RO, IFAC, and ICRA 2011-2015.
- **disclosed subsystems:** `lift-modular-docking`, `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `cert-experimental`

**Prior art notes:**

> The University of Bologna's modular multirotor work (Naldi & Marconi, CASY group, ~2011-2015) is the Italian academic disclosure of modular-reconfigurable aerial robots combining under-actuated thrust modules with a reconfigurable connecting mechanism. Establishes Italian prior art for: (1) modular aerial vehicles where the composite achieves full actuation from individually-under-actuated parts, (2) reconfigurable inter-module mechanisms changing thrust-vector geometry. Together with the ETH and UPenn modular-aerial-robot lineages, places modular multirotor architecture in cross-national academic public-domain prior art.

**Sources:**

1. Naldi, R., Marconi, L. et al. 'Modeling and Control of a Class of Modular Aerial Robots.' IEEE Transactions on Robotics, 2011-2015 (multiple papers).
2. Naldi, R., Gentili, L., Marconi, L., Sala, A. 'Design and experimental validation of a nonlinear control law for a ducted-fan miniature aerial vehicle.' Control Engineering Practice, 2010.
3. University of Bologna CASY group publications archive.

---

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

### 2017-03-07 — Airbus Pop.Up / Pop.Up Next

- **id:** `airbus-popup`
- **corpus:** private
- **ip status:** patented
- **creator:** Airbus / Italdesign / Audi
- **disclosure citation:** Airbus Pop.Up modular ground-and-air mobility concept unveiled 2017-03-07 at the Geneva International Motor Show, by Airbus and Italdesign (Volkswagen Group / Audi subsidiary); Pop.Up Next (adding Audi as full partner) unveiled 2018-03-06 at Geneva. Documented in Airbus and Italdesign press materials and design patents. The system is a passenger capsule that docks to either a ground-vehicle skateboard module or a quadrotor air module.
- **disclosed subsystems:** `lift-modular-docking`, `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `autonomy-pilot-removed`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`

**Prior art notes:**

> Airbus Pop.Up / Pop.Up Next (Airbus + Italdesign + Audi, 2017-2018) is the foundational commercial disclosure of the modular-docking passenger-mobility concept: a passenger capsule that docks to either a ground-vehicle module or an air module (a large coaxial-octorotor frame), with the air module lifting the docked capsule mid-journey. Establishes prior art for: (1) modular passenger-capsule + interchangeable-propulsion-module architecture, (2) in-journey transfer of a passenger pod between ground and air carriers, (3) the multi-modal modular-mobility thesis. Together with xpeng-aeroht-modular (2024), bell-apt (2018), and the academic modular-aerial-robot lineage (eth-distributed-flight-array, upenn-modquad), comprehensively places modular-docking eVTOL architecture in commercial and academic prior art from 2010 forward.

**Sources:**

1. Airbus press release, 'Pop.Up: the modular ground-and-air passenger concept vehicle system,' 2017-03-07.
2. Italdesign / Audi Pop.Up Next materials, Geneva Motor Show 2018.
3. Airbus / Italdesign Pop.Up design patents, EUIPO records.

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

### 2018-08 — Bell APT (Autonomous Pod Transport)

- **id:** `bell-apt`
- **corpus:** private
- **ip status:** patented
- **creator:** Bell Textron
- **disclosure citation:** Bell APT (Autonomous Pod Transport) publicly disclosed August 2018; APT 70 (70 lb / ~32 kg payload variant) first flight 2019-08; demonstrated package delivery and NASA UTM integration trials 2020-2021. Documented in Bell Textron press materials, NASA UTM program reports, and FAA filings.
- **disclosed subsystems:** `transition-tail-sitter-pitch-up`, `lift-modular-docking`, `lift-distributed-electric-propulsion`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `autonomy-pilot-removed`, `autonomy-utm-integration`, `autonomy-bvlos-detect-and-avoid`, `cert-faa-bvlos-waiver`, `airframe-composite-monocoque`

**Prior art notes:**

> Bell APT (Autonomous Pod Transport) establishes US prior art for the modular-cargo-pod tail-sitter eVTOL — a reusable quad-rotor tail-sitter airframe carrying a swappable cargo pod mounted between the rotor booms. Establishes prior art for: (1) modular swappable cargo pod + reusable propulsion airframe architecture in tail-sitter form, (2) NASA UTM-integrated autonomous cargo eVTOL operations (2020-2021 trials), (3) the pod-as-deliverable design pattern. Together with airbus-popup (modular passenger capsule), elroy-air-chaparral (modular cargo pod), and the academic modular-aerial-robot lineage, places modular-pod eVTOL architecture in commercial prior art from 2017-2018 forward.

**Sources:**

1. Bell Textron press releases on APT, 2018-2021.
2. NASA UAS Traffic Management (UTM) program reports including Bell APT trials.
3. FAA Part 107 / BVLOS waiver records for Bell APT operations.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `d899fde`.*
