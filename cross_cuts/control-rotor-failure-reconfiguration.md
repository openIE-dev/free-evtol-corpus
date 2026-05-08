---
title: control-rotor-failure-reconfiguration
parent: Cross-cuts
layout: default
---

# Cross-cut: `control-rotor-failure-reconfiguration`

**9 corpus entries disclose this subsystem.**

Earliest disclosure: 1991-12-23

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Kaman K-MAX (1991-12-23)

- **id**: `kaman-k-max`
- **corpus**: private
- **creator**: Kaman Aircraft Corporation
- **disclosure**: Kaman K-MAX first flight 1991-12-23; FAA Type Certificate Part 27 (restricted category) granted 1994-08-30. Optionally-Piloted Aircraft (OPA) variant flown autonomously by U.S. Marine Corps in Afghanistan 2011-2014 (the first deployed unmanned heavy-lift helicopter).
- **ip status**: patented
- **prior art notes**: Kaman K-MAX is the modern descendant of HH-43 intermeshing-rotor architecture and the first heavy-lift helicopter deployed for unmanned cargo operations in combat (Afghanistan, 2011-2014). Establishes prior art for: (1) modern certified intermeshing-rotor helicopter (extends HH-43 prior art into the 1990s-2010s with documented operational performance), (2) optionally-piloted heavy-lift cargo VTOL (Lockheed Martin retrofit), (3) Part 27 certification basis for intermeshing rotor.

## NASA GL-10 Greased Lightning (2014-08)

- **id**: `nasa-gl-10`
- **corpus**: academic
- **creator**: NASA Langley Research Center
- **disclosure**: Fredericks, William J. et al. 'Aerodynamic Characteristics of an Electric Distributed Propulsion Wind Tunnel Model.' AHS International Forum 70, May 2014; subsequent flight test reports through 2015 documented in NASA TM-2017-219653 and related.
- **ip status**: public-domain
- **prior art notes**: GL-10 is NASA's foundational disclosure of distributed electric propulsion (DEP) applied to tilt-wing VTOL. Establishes prior art for: (1) ten-rotor wing-distributed electric lift architecture, (2) hybrid genset+battery propulsion topology for VTOL, (3) DEP-specific control allocation including rotor-failure reconfiguration. NASA's publication of GL-10 design and test data is comprehensive and CC-licensed by virtue of being U.S. government work. Anticipates: lift-plus-cruise commercial eVTOLs that use DEP across a wing (Beta Alia, Wisk Cora variants), and any DEP-specific control allocation patents filed post-2014. Combined with X-57 Maxwell, GL-10 places DEP comprehensively in the public domain.

## PX4 VTOL flight stack (2014-09)

- **id**: `px4-vtol`
- **corpus**: open
- **creator**: PX4 / Dronecode Foundation / Lorenz Meier et al.
- **disclosure**: PX4 VTOL framework first merged 2014-09 (canonical PX4 git history at github.com/PX4/PX4-Autopilot); foundational paper Meier, L. et al. 'PX4: A Node-Based Multithreaded Open Source Robotics Framework for Deeply Embedded Platforms,' ICRA 2015.
- **ip status**: open-permissive
- **prior art notes**: PX4 is the BSD-licensed reference flight stack for VTOL aircraft, used in commercial products and academic research worldwide. Establishes prior art for: (1) modular VTOL transition state machine with named airframe types (Standard, Tail-sitter, Tilt-rotor), (2) EKF2-based state estimation across regime transitions, (3) open-source rotor-failure handling. Like ArduPilot, the BSD license lets PX4 disclosures function unambiguously as prior art.

## ArduPilot QuadPlane VTOL (2015-04)

- **id**: `ardupilot-quadplane`
- **corpus**: open
- **creator**: ArduPilot Project / Andrew Tridgell et al.
- **disclosure**: ArduPilot QuadPlane functionality first merged into ArduPlane main branch 2015-04 (commit history available at github.com/ArduPilot/ardupilot); first general public release with QuadPlane support: ArduPlane 3.5.0, 2015-12-14.
- **ip status**: open-copyleft
- **prior art notes**: ArduPilot QuadPlane is the GPL-licensed reference implementation of generic VTOL flight control. Establishes prior art (under GPL, but the architectural disclosure is unencumbered as prior art for patent purposes) for: (1) generic transition controller for lift+cruise, tilt-rotor, tilt-wing, and tail-sitter VTOLs, (2) rotor-failure detection and reconfiguration in multirotor lift, (3) Q_ASSIST transitional thrust assist algorithms. The git commit history provides timestamped disclosure of every subsystem-level innovation. Filed against any post-2015 patent claim on basic VTOL transition control or rotor-failure reconfiguration in multirotor lift, this is anticipating prior art.

## Aurora Flight Sciences LightningStrike XV-24A (2016-03-03)

- **id**: `aurora-lightningstrike-xv-24a`
- **corpus**: academic
- **creator**: Aurora Flight Sciences (Boeing subsidiary) / DARPA
- **disclosure**: Aurora Flight Sciences LightningStrike XV-24A awarded DARPA VTOL X-Plane Phase 3 contract 2016-03-03; sub-scale demonstrator first hover 2017-04. Program subsequently de-scoped without full-scale first flight, but Aurora's design and test data were extensively published in DARPA reports and AIAA papers.
- **ip status**: patented
- **prior art notes**: Aurora LightningStrike XV-24A is the most architecturally similar prior art to Lilium Jet's 36-fan ducted-fan-array eVTOL — also a tilt-wing distributed-electric-propulsion configuration with embedded ducted lift fans. The XV-24A's 24 ducted fans (2016) anticipate Lilium's 36 (2019) configuration by 3 years and DARPA-funded design publication is fully in the public domain. Establishes US prior-art lineage for: (1) high-multiplicity tilt-wing ducted-fan-array, (2) turbine-electric hybrid powerplant for VTOL, (3) the very-high-rotor-count distributed-electric-propulsion architecture. Filed against any post-2016 patent claim on similar ducted-fan-array tilt-wing configurations, this is anticipating prior art.

## EHang EH216-S (2018-02-05)

- **id**: `ehang-eh216`
- **corpus**: private
- **creator**: EHang Holdings
- **disclosure**: EHang 184 / 216 platform first publicly disclosed at CES 2016; EH216 designation first used 2018-02-05 in EHang corporate filings; EH216-S type certificate granted by CAAC 2023-10-13 (TC No. ETC-G-2023-101). Production certificate granted 2024-04-07.
- **ip status**: patented
- **prior art notes**: EHang EH216-S is the first eVTOL to receive a full type certificate from a major civil aviation authority (CAAC, 2023-10-13). The TC documentation is publicly available and constitutes a comprehensive engineering disclosure under SC-VTOL-like framework. Establishes commons-grade disclosure of: (1) eight-coaxial-pair 16-rotor lift architecture, (2) production autonomous-passenger eVTOL flight management system, (3) the CAAC SC-VTOL certification basis itself (the regulation and applied airworthiness criteria are public). Together with volocopter-vc1, places multirotor passenger eVTOL architecture comprehensively in the public domain as of 2018.

## Jetson ONE (2018-09)

- **id**: `jetson-one`
- **corpus**: private
- **creator**: Jetson AB (Italy / Sweden joint operation)
- **disclosure**: Jetson AB founded 2018-09 by Tomasz Patan (Polish-Swedish) and Peter Ternström (Swedish); Jetson ONE design unveiled 2020-04-21; first manned flight 2020-09; first customer deliveries 2023-09.
- **ip status**: patented
- **prior art notes**: Jetson ONE is the leading consumer ultralight-class single-seat eVTOL — the Swedish/Italian/Polish realization of the open-frame multirotor design originally disclosed by Curtiss-Wright VZ-7 (1958). Operates under FAA Part 103 ultralight rules with no pilot license required. Establishes Northern European prior-art lineage for consumer-grade ultralight eVTOL with open-rotor architecture and rotor-failure reconfiguration.

## Volocopter VoloCity (2019-08-14)

- **id**: `volocopter-volocity`
- **corpus**: private
- **creator**: Volocopter GmbH
- **disclosure**: VoloCity production-design unveiling 2019-08-14 at Helsinki ITS World Congress; precursor VC-200 first manned flight 2013-11-17; first public manned demo at Singapore 2019-10-22. EASA SC-VTOL certification process actively pursued; targeted operations Paris 2024 / 2026 commercial rollouts.
- **ip status**: patented
- **prior art notes**: Volocopter VoloCity is the production design descending from e-volo VC1 (2011, first manned multicopter flight). 18-rotor circular-ring multirotor architecture, EASA SC-VTOL certification basis. Establishes the German prior-art lineage from e-volo through Volocopter for circular-ring multirotor passenger eVTOL — foundational and predates EHang in manned-flight precedence.

## DJI FlyCart 30 (2023-08-16)

- **id**: `dji-flycart-30`
- **corpus**: private
- **creator**: SZ DJI Technology Co Ltd (Shenzhen)
- **disclosure**: DJI FlyCart 30 publicly unveiled 2023-08-16 in Shenzhen; CAAC type certification application 2023; commercial deliveries to Chinese and international markets 2024. DJI is the world's largest drone manufacturer and holds an extensive multirotor patent estate.
- **ip status**: patented
- **prior art notes**: DJI FlyCart 30 is the entry of the world's largest drone manufacturer into the heavy-cargo eVTOL category. DJI's massive patent estate and operational scale (millions of multirotor flights/day globally) constitute foundational prior-art coverage for: (1) coaxial-pair multirotor manufacturing at scale, (2) autonomous multirotor cargo delivery, (3) consumer-priced multirotor architecture migration to commercial cargo class. Establishes Chinese prior-art lineage for heavy-payload multirotor cargo eVTOL with explicit Beyond Visual Line of Sight (BVLOS) operational basis.
