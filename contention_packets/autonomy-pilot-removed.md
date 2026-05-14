---
title: "autonomy-pilot-removed"
parent: "Invalidity Contentions"
nav_order: 5
layout: default
---

# Invalidity Contention Packet — `autonomy-pilot-removed`

**Generated:** 2026-05-14  
**Cross-cut tag:** `autonomy-pilot-removed`  
**Entries:** 29 (29 commons-grade, 0 draft)  
**Earliest disclosure:** 1991-12-23  
**Most recent disclosure:** 2023-08-16

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `autonomy-pilot-removed`.

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

### 2003-03-06 — Bell Eagle Eye TR918

- **id:** `bell-eagle-eye`
- **corpus:** private
- **ip status:** patented
- **creator:** Bell Helicopter Textron / U.S. Coast Guard / U.S. Army
- **disclosure citation:** Bell Eagle Eye first hover 2003-03-06; first transition flight 2003-08-22; full-scale TR918 unveiled at HAI Heli-Expo 2005. U.S. Coast Guard Deepwater program cancellation 2007 ended production but Bell continues design work. Documented in Bell technical papers and Coast Guard procurement records.
- **disclosed subsystems:** `lift-tilt-rotor`, `transition-thrust-borne-to-wing-borne`, `autonomy-pilot-removed`, `cert-military`

**Prior art notes:**

> Bell Eagle Eye is the unmanned-scale tilt-rotor descended from the V-22 program — establishes prior art for: (1) tilt-rotor architecture in unmanned tactical UAV scale, (2) autonomous tilt-rotor mission operation. Together with bell-xv-15, v-22-osprey, bell-v-280-valor, and aerovironment-skytote, places tilt-rotor architecture across the full scale spectrum from small unmanned to large troop transport in comprehensive prior-art coverage.

**Sources:**

1. Bell Helicopter Eagle Eye technical papers, AHS Forum 2003–2008.
2. U.S. Coast Guard Deepwater program records, declassified portions.

---

### 2003-04 — AeroVironment SkyTote

- **id:** `aerovironment-skytote`
- **corpus:** academic
- **ip status:** patented
- **creator:** AeroVironment Inc / U.S. Air Force Research Laboratory
- **disclosure citation:** AeroVironment SkyTote first untethered hover April 2003 at Edwards AFB; demonstrated transition flight 2004. AFRL Materiel Command Phase 2 SBIR contract. Documented in AFRL technical reports and AeroVironment publications.
- **disclosed subsystems:** `transition-tail-sitter-pitch-up`, `lift-coaxial-rotor`, `autonomy-pilot-removed`, `cert-military`

**Prior art notes:**

> AeroVironment SkyTote is the foundational small-scale unmanned tail-sitter VTOL — establishes prior art for the tail-sitter architecture in modern UAV scale (2003) with autonomous flight control. Combined with convair-xfy-pogo (1954) and pivotal-blackfly (2018), comprehensively places tail-sitter VTOL in continuous prior-art coverage from 1954 through 2024.

**Sources:**

1. AFRL technical reports on SkyTote, AFRL/MN-WR-TR-2004-001 series.
2. AeroVironment publications and patent estate.
3. AHS Forum papers from AeroVironment 2003–2008.

---

### 2005 — DLR ARTIS / SuperARTIS

- **id:** `dlr-superartis`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Deutsches Zentrum für Luft- und Raumfahrt (DLR) Institute of Flight Systems / Stephan Adolf / Florian-Michael Adolf
- **disclosure citation:** DLR ARTIS (Autonomous Rotorcraft Testbed for Intelligent Systems) first flight 2005; SuperARTIS (larger 24 kg variant) entered service ~2010 at DLR Braunschweig. The German Aerospace Center's autonomous-rotorcraft research platform. Foundational reference paper: Adolf, F.M., Andert, F. 'Onboard mission management for a VTOL UAV using sequence and supervisory control.' AHS Forum, 2011. Subsequent papers through 2015-2020 expanded ARTIS / SuperARTIS capability.
- **disclosed subsystems:** `autonomy-pilot-removed`, `autonomy-bvlos-detect-and-avoid`, `sensing-lidar-terrain`, `cert-experimental`

**Prior art notes:**

> DLR ARTIS / SuperARTIS (2005-) is the German Aerospace Center's autonomous-rotorcraft research platform — adds DLR (the German national aerospace research agency) to the academic aerial-robotics prior-art base alongside the existing US (UPenn GRASP, MIT, Harvard, NASA Langley/Ames/Armstrong), Swiss (ETH, EPFL, UZH), Japanese (Tokyo JSK), Dutch (TU Delft), Italian (Bologna), Austrian (IAT-21, CycloTech), Australian (ArduPilot), and Swiss-academic (Crazyflie at Bitcraze) anchors. The DLR ARTIS publications (F.M. Adolf, F. Andert, et al.) document mission-management, sense-and-avoid, and autonomous-rotorcraft control through 2005-2020.

**Sources:**

1. Adolf, F.M., Andert, F. 'Onboard mission management for a VTOL UAV using sequence and supervisory control.' AHS Forum, 2011.
2. DLR Institute of Flight Systems publications archive (Braunschweig).
3. Andert, F., Adolf, F.M. et al. ARTIS / SuperARTIS technical reports 2005-2020.

---

### 2005-04 — Schiebel Camcopter S-100

- **id:** `schiebel-camcopter-s-100`
- **corpus:** private
- **ip status:** patented
- **creator:** Schiebel Aircraft GmbH
- **disclosure citation:** Schiebel Camcopter S-100 publicly disclosed April 2005; entered service with Royal Australian Navy 2010 and Italian Navy 2011; deployed by 30+ naval forces worldwide. One of the most-deployed naval VTOL UAVs in history. Documented in Schiebel technical materials and naval procurement records.
- **disclosed subsystems:** `lift-coaxial-rotor`, `autonomy-pilot-removed`, `cert-military`

**Prior art notes:**

> Schiebel Camcopter S-100 is the most-deployed naval VTOL UAV in the world (30+ navies, 30,000+ hours of operational flight). Establishes Austrian industrial prior-art lineage for autonomous shipborne VTOL UAS. Although conventional single-rotor architecture (not eVTOL specifically), the operational disclosure of autonomous shipboard VTOL operations is comprehensive and applicable to eVTOL claims around naval deployment.

**Sources:**

1. Schiebel Aircraft GmbH press releases 2005-2024.
2. Royal Australian Navy / Italian Navy procurement records.

---

### 2007 — Saab Skeldar V-200

- **id:** `saab-skeldar-v-200`
- **corpus:** private
- **ip status:** patented
- **creator:** UMS Skeldar (Saab AB / UMS Aero joint venture)
- **disclosure citation:** Saab Skeldar (originally Saab IsoMatic / Saab AERTEC) first flight 2007; in service with Spanish Armada 2018 and German Bundeswehr 2020. UMS Skeldar joint venture established 2015. Documented in Saab and UMS technical materials and naval procurement disclosures.
- **disclosed subsystems:** `autonomy-pilot-removed`, `cert-military`

**Prior art notes:**

> Saab Skeldar V-200 is Sweden's lead naval VTOL UAV — competitor to Schiebel Camcopter S-100 with similar architectural pattern but Swedish industrial provenance. Adds Saab as Swedish defense industrial prior-art anchor alongside jetson-one (Sweden consumer eVTOL).

**Sources:**

1. Saab AB and UMS Skeldar press releases 2007-2024.
2. Spanish Armada and German Bundeswehr procurement records.

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

### 2017 — Orb Aerospace Nomad

- **id:** `orb-aerospace-nomad`
- **corpus:** private
- **ip status:** patented
- **creator:** Orb Aerospace / Skyways Inc
- **disclosure citation:** Skyways Inc founded ~2017 in Austin, Texas. Skyways A22 autonomous VTOL cargo aircraft publicly demonstrated for USMC Naval Air Systems Command (NAVAIR) starting 2019; awarded USMC Tactical Resupply Vehicle (TRV-150) contract 2020. Orb Aerospace product line including the Orb Nomad publicly disclosed via Air Force AFWERX program records, Skyways press materials, and U.S. defense contracting disclosures. Distinct architectural commitment to industrial / defense / emergency-response cargo missions rather than urban passenger air taxi.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-hybrid-series`, `power-hybrid-genset`, `propulsion-bldc-direct-drive`, `autonomy-pilot-removed`, `autonomy-bvlos-detect-and-avoid`, `cert-faa-bvlos-waiver`, `airframe-composite-monocoque`

**Prior art notes:**

> Orb Aerospace / Skyways establishes US prior art for the industrial / defense / emergency-response cargo eVTOL category — distinct architectural and operational commitment from urban passenger air taxi. The USMC TRV-150 contract (2020) is among the earliest production-track autonomous VTOL cargo deployments in U.S. military service. Establishes prior art for: (1) hybrid-electric autonomous cargo eVTOL specifically designed for unprepared / austere site operations, (2) the industrial-first eVTOL deployment thesis (cargo and defense use cases preceding consumer urban air taxi). Together with elroy-air-chaparral, pyka-pelican, sabrewing-rhaegal-a, volansi-vbat, wingcopter-198, dji-flycart-30, and amsl-vertiia, comprehensively places autonomous hybrid-electric cargo eVTOL architecture in 2017-2024 commercial prior art across US, DE, AU, and CN industrial lineages.

**Sources:**

1. Skyways Inc press releases and product materials 2017-2024.
2. USMC NAVAIR / TRV-150 contract award records.
3. U.S. Air Force AFWERX program disclosures.
4. Orb Aerospace public technical materials.
5. https://go.skyways.com/ — corporate landing page.

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

### 2018-01-31 — Airbus A^3 Vahana

- **id:** `airbus-vahana`
- **corpus:** private
- **ip status:** patented
- **creator:** Acubed (Airbus Silicon Valley) / Airbus SAS
- **disclosure citation:** Airbus A^3 Vahana sub-scale demonstrator first untethered hover 2018-01-31 at Pendleton OR (Acubed test site); first transition flight 2018-05-15. Vahana flight-test program completed 2019-11 with 138 successful flights. Acubed published Vahana technical papers and design data openly.
- **disclosed subsystems:** `lift-tilt-wing`, `lift-distributed-electric-propulsion`, `transition-thrust-borne-to-wing-borne`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `autonomy-pilot-removed`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> Airbus Vahana is the first fully-autonomous tilt-wing eVTOL to achieve transition flight (2018) — a distinct architectural achievement combining tilt-wing geometry with BLDC distributed electric propulsion and full-autonomy control, all flying 138+ missions in 2018-2019. Establishes prior art for: (1) tilt-wing passenger eVTOL with eight-rotor configuration, (2) full-autonomy transition control across the conversion corridor, (3) production-ready electric tilt-wing flight-control architecture. Acubed published Vahana data openly, putting comprehensive engineering disclosure in the public domain.

**Sources:**

1. Acubed / Airbus A^3 press releases 2018–2019.
2. Vahana flight-test technical papers, Vertical Flight Society Forum 2019–2020.
3. Smith, Zach. 'Vahana: Lessons Learned.' Acubed publication, 2019-11.

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

### 2018-03-13 — Wisk Aero Cora / Gen 6

- **id:** `wisk-cora`
- **corpus:** private
- **ip status:** patented
- **creator:** Wisk Aero LLC (Boeing / Kitty Hawk joint venture)
- **disclosure citation:** Cora aircraft publicly unveiled 2018-03-13 by Kitty Hawk; first untethered hover earlier in 2017 (test campaign in New Zealand); Wisk Aero JV with Boeing announced 2019-12-19; Gen 6 production design unveiled 2022-10-03; Boeing acquired Kitty Hawk's interest 2023-05, making Wisk a Boeing subsidiary.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-bvlos-detect-and-avoid`, `autonomy-pilot-removed`, `autonomy-utm-integration`, `cert-part-23`, `control-fly-by-wire-triplex`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`, `sensing-lidar-terrain`, `sensing-radar-altimeter`, `transition-mode-shutdown`

**Prior art notes:**

> Wisk Cora / Gen 6 is the leading US autonomous (no on-board pilot) passenger eVTOL — distinct architectural commitment to autonomy from Joby, Archer, Beta. Lift+cruise architecture with 12+1 propulsor count. Establishes US prior-art lineage for autonomous-passenger commercial lift+cruise eVTOL targeting FAA Part 23 / Special Conditions.

**Sources:**

1. Wisk Aero press releases 2018–2024.
2. Boeing investor disclosures regarding Wisk acquisition 2023-05.
3. FAA Part 23 / Special Conditions for VTOL filings (Wisk).

---

### 2018-04 — Volansi VBAT

- **id:** `volansi-vbat`
- **corpus:** private
- **ip status:** patented
- **creator:** Volansi Inc / Martin UAV (acquired by Shield AI 2021)
- **disclosure citation:** Volansi VBAT autonomous tail-sitter cargo VTOL publicly disclosed April 2018; Volansi delivered medical and military supplies operationally 2019-2022. Acquired by Shield AI 2021-08. Volans-i original company ceased independent operation 2022 after acquisition by Shield AI.
- **disclosed subsystems:** `transition-tail-sitter-pitch-up`, `lift-ducted-fan-array`, `autonomy-pilot-removed`, `autonomy-bvlos-detect-and-avoid`, `cert-faa-bvlos-waiver`

**Prior art notes:**

> Volansi VBAT is the leading autonomous tail-sitter cargo VTOL deployed operationally for medical/military supply runs 2019-2022. Establishes prior art for: (1) ducted-fan tail-sitter cargo VTOL architecture, (2) operational FAA BVLOS waiver framework for autonomous tail-sitter UAS. Together with aerovironment-skytote and pivotal-blackfly, comprehensively places tail-sitter VTOL architecture in modern operational coverage.

**Sources:**

1. Volans-i / Volansi press releases 2018-2022.
2. Shield AI acquisition disclosures 2021.
3. FAA Part 137 / UAS operational approvals public records.

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

### 2018-08 — Pyka Pelican Cargo

- **id:** `pyka-pelican`
- **corpus:** private
- **ip status:** patented
- **creator:** Pyka (Oakland, California)
- **disclosure citation:** Pyka founded 2018; Egret (predecessor agricultural eVTOL) operational since 2019; Pelican Cargo unveiled 2022-06-21; FAA Part 137 ag operations approval (Pelican Spray) 2023-04. Pyka's autonomy stack documented in open technical white papers.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-bvlos-detect-and-avoid`, `autonomy-pilot-removed`, `autonomy-utm-integration`, `cert-part-23`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-redundant-bus`, `sensing-lidar-terrain`, `transition-mode-shutdown`

**Prior art notes:**

> Pyka Pelican is the leading US autonomous cargo eVTOL targeting agricultural and middle-mile logistics. Establishes prior art for: (1) autonomous lift+cruise cargo eVTOL operating under Part 137 / Part 23, (2) electric agricultural-spray eVTOL (Pelican Spray variant operational since 2023). Distinct architectural commitment from passenger eVTOL: prioritizes payload, range, and short-strip operation over hover endurance.

**Sources:**

1. Pyka technical white papers 2020–2024.
2. FAA Part 137 / Special Conditions filings 2023.
3. Pyka press releases including 2022-06-21 Pelican unveil.

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

### 2019-01-30 — Elroy Air Chaparral C1

- **id:** `elroy-air-chaparral`
- **corpus:** private
- **ip status:** patented
- **creator:** Elroy Air Inc (San Francisco)
- **disclosure citation:** Elroy Air founded 2016 by David Merrill and Kofi Asante; sub-scale Chaparral demonstrator publicly unveiled 2019-01-30; full-scale C1 first hover flight 2023-11-12 at Camarillo, CA. Air Force AFWERX / USAF Agility Prime contracts 2021-09 onward.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-bvlos-detect-and-avoid`, `autonomy-pilot-removed`, `autonomy-utm-integration`, `cert-part-23`, `lift-distributed-electric-propulsion`, `power-hybrid-genset`, `propulsion-bldc-direct-drive`, `propulsion-hybrid-series`, `safety-redundant-bus`, `sensing-lidar-terrain`, `transition-mode-shutdown`

**Prior art notes:**

> Elroy Air Chaparral establishes prior art for: (1) hybrid-electric (turbine-genset + battery) cargo eVTOL, distinct from pure-battery designs by extending range to 500+ km, (2) modular swappable cargo-pod architecture decoupled from aircraft turnaround. Hybrid powerplant anticipates similar claims on series-hybrid eVTOL propulsion topology.

**Sources:**

1. Elroy Air press releases and technical white papers 2019–2024.
2. USAF Agility Prime program disclosures.
3. FAA filings related to autonomous cargo operations.

---

### 2019-04 — Sabrewing Rhaegal-A

- **id:** `sabrewing-rhaegal-a`
- **corpus:** private
- **ip status:** patented
- **creator:** Sabrewing Aircraft Company
- **disclosure citation:** Sabrewing Aircraft Rhaegal-A unveiled April 2019; sub-scale prototype hover trials 2020. Designed for 4,500 lb (2,040 kg) cargo capacity in unmanned configuration. Documented in Sabrewing technical materials and FAA filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `lift-ducted-fan-array`, `transition-mode-shutdown`, `propulsion-hybrid-series`, `power-hybrid-genset`, `autonomy-pilot-removed`, `cert-part-23`

**Prior art notes:**

> Sabrewing Rhaegal-A establishes US prior art for heavy-cargo (2-ton class) hybrid-electric eVTOL with ducted-fan architecture. Distinct from Elroy Air Chaparral by larger payload and ducted-fan rather than open-rotor lift. Anticipates other heavy-cargo eVTOL claims filed post-2019.

**Sources:**

1. Sabrewing Aircraft technical materials 2019-2024.
2. FAA Part 23 / Special Conditions filings.

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

### 2020-09 — Manna Air Delivery drone

- **id:** `manna-air-delivery`
- **corpus:** private
- **ip status:** patented
- **creator:** Manna Drone Delivery Ltd
- **disclosure citation:** Manna Drone Delivery Ltd founded 2018 in Dublin by Bobby Healy; operational food delivery service launched September 2020 in Oranmore, Galway; expanded to multiple Irish towns and UK 2021-2024. Documented in Irish Aviation Authority (IAA) operational approvals and Manna press materials.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `autonomy-pilot-removed`, `autonomy-bvlos-detect-and-avoid`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`

**Prior art notes:**

> Manna Air Delivery establishes Ireland's lead commercial drone-delivery OEM with operational deployment 2020-2024 across Irish towns. Distinctive: tethered cargo drop without landing (architectural variant of cargo delivery distinct from DJI FlyCart's set-down approach). Adds Ireland to the Western European eVTOL ecosystem.

**Sources:**

1. Manna Drone Delivery press releases 2020-2024.
2. Irish Aviation Authority operational approvals public record.
3. Reuters and Irish Times coverage 2020-2024.

---

### 2021-07-16 — XPENG AeroHT X2

- **id:** `aeroht-xpeng-x2`
- **corpus:** private
- **ip status:** patented
- **creator:** AeroHT (XPENG flying car subsidiary)
- **disclosure citation:** XPENG Voyager X2 publicly unveiled 2021-07-16 at XPENG Tech Day; first untethered manned flight 2022-10-10 at Dubai. AeroHT subsequently unveiled X3 (2023) and the modular Land Aircraft Carrier (2024). AeroHT holds Chinese patents on coaxial multirotor and modular drive+fly architecture.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-bvlos-detect-and-avoid`, `autonomy-pilot-removed`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `control-differential-thrust-attitude`, `lift-coaxial-rotor`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `safety-redundant-bus`, `sensing-lidar-terrain`

**Prior art notes:**

> AeroHT (XPENG flying car subsidiary) is one of three lead Chinese passenger eVTOL programs (with EHang and AutoFlight). The X2 establishes Chinese prior art for coaxial-pair multirotor passenger eVTOL with autonomous + pilot-override flight management. AeroHT's subsequent X3 and modular Land Aircraft Carrier (2024) extend to drive+fly transformer geometry.

**Sources:**

1. XPENG Tech Day 2021-07-16 announcement materials.
2. Reuters and South China Morning Post coverage of 2022-10-10 Dubai flight.
3. AeroHT product disclosures and Chinese patent filings.

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

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `04cd8e0`.*
