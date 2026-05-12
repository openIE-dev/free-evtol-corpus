---
title: "control-differential-thrust-attitude"
parent: "Invalidity Contentions"
nav_order: 15
layout: default
---

# Invalidity Contention Packet — `control-differential-thrust-attitude`

**Generated:** 2026-05-11  
**Cross-cut tag:** `control-differential-thrust-attitude`  
**Entries:** 30 (30 commons-grade, 0 draft)  
**Earliest disclosure:** 1922  
**Most recent disclosure:** 2024-04-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `control-differential-thrust-attitude`.

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

### 1922 — Pescara helicopter

- **id:** `pescara-helicopter`
- **corpus:** academic
- **ip status:** patented
- **creator:** Raúl Pateras Pescara de Castelluccio
- **disclosure citation:** Pescara helicopter No.3 (later 3F) developed at Issy-les-Moulineaux, France; set FAI distance world record 736 m on 1924-04-18 with Pescara at controls. Pescara holds Spanish patent ES86,124 (1920) and French patents covering biplane coaxial counter-rotating rotor design with cyclic and collective pitch control.
- **disclosed subsystems:** `cert-experimental`, `control-differential-thrust-attitude`, `lift-coaxial-rotor`

**Prior art notes:**

> Pescara is the foundational Argentine/Spanish disclosure of practical coaxial counter-rotating rotor lift with cyclic+collective pitch control. Contemporaneous with de Bothezat's quadrotor (1922) but in coaxial geometry rather than X-frame. Establishes prior art for: (1) coaxial counter-rotating rotor architecture for torque cancellation without tail rotor (foundational to modern Kamov Ka-line and to coaxial-pair lift modules in eVTOL such as Beta Alia, Wisk Cora, EHang EH216), (2) the cyclic + collective pitch control invention. Combined with verne-albatross (1886) and de-bothezat-quadrotor (1922), provides multi-architecture 1880–1922 prior art base. The Pescara patents (ES86,124 et seq.) have been expired for over 80 years.

**Sources:**

1. Liberatore, E.K. Helicopters Before Helicopters. Krieger, 1998.
2. Charnov, Bruce H. From Autogiro to Gyroplane: The Amazing Survival of an Aviation Technology. Praeger, 2003, chapter on Pescara.
3. FAI archives, world record file 1924-04-18.
4. Pescara, Raúl. Spanish Patent ES86,124, 1920.

---

### 1922-12-18 — de Bothezat helicopter

- **id:** `de-bothezat-quadrotor`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** George de Bothezat / U.S. Army Air Service (McCook Field)
- **disclosure citation:** U.S. Army Air Service report on first manned flight of the de Bothezat helicopter at McCook Field, Dayton, Ohio, 1922-12-18; documented in NACA technical literature and McCook Field records.
- **disclosed subsystems:** `cert-experimental`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`

**Prior art notes:**

> First manned multirotor heavier-than-air vehicle to achieve sustained hover (approximately 100 flights between 1922 and 1924). Establishes prior art for: (1) X-frame quadrotor airframe geometry, (2) differential-thrust attitude control between independently-controlled lift rotors, (3) multi-rotor mechanical lift platform. The 1922 disclosure is referenced in nearly every modern academic survey of multirotor history and is foundational to invalidity arguments against any post-1922 quadrotor airframe-geometry or attitude-allocation claims. Although the propulsion is mechanical rather than electric, the architectural decomposition (lift via plural independent rotors, attitude via differential thrust) is identical to modern electric multirotor designs. Combined with verne-albatross (1886), this entry blocks any patent attempt to claim the basic multirotor architectural pattern as novel.

**Sources:**

1. de Bothezat, George. 'Helicopter for the United States Army Air Service.' McCook Field Report, 1923.
2. Liberatore, E.K. Helicopters Before Helicopters. Krieger, 1998.
3. Leishman, J. Gordon. Principles of Helicopter Aerodynamics, 2nd ed. Cambridge University Press, 2006, chapter 1.
4. U.S. Army Air Service / McCook Field photographic and report archives, NARA.

---

### 1924-05-04 — Oehmichen No.2 helicopter

- **id:** `oehmichen-helicopter`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Étienne Oehmichen
- **disclosure citation:** Oehmichen No.2 set FAI absolute closed-circuit helicopter distance record 1924-05-04: 1,100 m at Valentigney, France, piloted by Oehmichen. The first rotorcraft to fly a kilometer closed-circuit course. Documented in FAI record archives and Oehmichen's contemporary publications.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `cert-experimental`

**Prior art notes:**

> Étienne Oehmichen's No.2 helicopter is contemporaneous with the de Bothezat quadrotor (1922) but with explicit attitude control through dedicated small rotors. Establishes additional French prior art (with Cornu 1907) for: (1) compound multi-rotor lift + dedicated-attitude-rotor architecture, (2) the first practical demonstration of sustained closed-circuit rotorcraft flight. Oehmichen's published descriptions document his thinking explicitly: lift via primary rotors, attitude via auxiliary rotors. The architectural pattern anticipates modern eVTOL with separate lift and yaw effectors.

**Sources:**

1. Oehmichen, Étienne. 'L'Hélicoptère: ses progrès et ses possibilités.' Société des Ingénieurs Civils de France, 1925.
2. FAI absolute helicopter record, 1924-05-04.
3. Liberatore, E.K. Helicopters Before Helicopters. Krieger, 1998.

---

### 1936-06-26 — Focke-Wulf Fa 61

- **id:** `focke-wulf-fa-61`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Henrich Focke / Focke-Wulf Flugzeugbau
- **disclosure citation:** Focke-Wulf Fa 61 first flight 1936-06-26 at Bremen by test pilot Ewald Rohlfs. Set multiple FAI helicopter world records 1937-1938 including duration, altitude, and distance. Famously demonstrated indoors by Hanna Reitsch at the Deutschlandhalle Berlin 1938-02. Documented in Focke-Wulf company archives, Allied technical intelligence, and Smithsonian collections.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `cert-experimental`

**Prior art notes:**

> The Focke-Wulf Fa 61 is generally regarded as the first fully-practical helicopter — sustained controlled flight with all stability and control axes properly engineered. Establishes prior art for: (1) lateral side-by-side twin-rotor architecture (architectural ancestor of Mil V-12 and any modern eVTOL using lateral rotor pairs), (2) production-grade cyclic + collective + differential control across two rotors, (3) the first rotorcraft to set FAI records in every major category. Captured by Allied forces 1945; design materials in CIOS technical intelligence reports. Henrich Focke's subsequent Focke-Achgelis Fa 223 Drache was the first production helicopter to enter service.

**Sources:**

1. Focke, Henrich. 'Die Entwicklung der Hubschrauber.' Jahrbuch 1939 der WGL.
2. Allied CIOS reports on Focke-Wulf rotorcraft, post-1945.
3. Smith and Kay. German Aircraft of the Second World War. Putnam, 1972.

---

### 1956 — Convertawings Model A Quadrotor

- **id:** `convertawings-model-a`
- **corpus:** academic
- **ip status:** patented
- **creator:** Convertawings Inc / D. H. Kaplan
- **disclosure citation:** Convertawings Model A Quadrotor first flight 1956 at Amityville NY; designed by D. H. Kaplan. The first quadrotor with full cyclic and collective pitch control on each of the four rotors. U.S. Army / Navy evaluated; program ended ~1960 for lack of orders. Documented in contemporary aviation press and rotorcraft histories.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `cert-experimental`

**Prior art notes:**

> Convertawings Model A is the foundational quadrotor with full cyclic + collective control on each rotor — a direct architectural precursor of modern quadrotor eVTOL. Establishes prior art for: (1) the H-frame four-rotor configuration with cross-shafted multi-engine drive, (2) attitude control via per-rotor cyclic pitch (the de Bothezat 1922 design used differential collective only). Convertawings' 1950s patents are long expired. Combined with de-bothezat-quadrotor (1922), curtiss-wright-vz-7 (1958), and piasecki-vz-8-airgeep (1958), comprehensively places quadrotor architecture in mid-20th-century public-domain prior art.

**Sources:**

1. Liberatore, E.K. Helicopters Before Helicopters. Krieger, 1998.
2. Markman and Holder. Straight Up. Schiffer, 2000.
3. Aviation Week coverage of Convertawings Model A, 1956-1959.

---

### 1958 — Curtiss-Wright VZ-7

- **id:** `curtiss-wright-vz-7`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Curtiss-Wright / U.S. Army Transportation Research Command
- **disclosure citation:** U.S. Army Transportation Research Command 'Flying Jeep' program; VZ-7 first flight 1958. Documented in TRC test reports and Markman & Holder, Straight Up (Schiffer 2000).
- **disclosed subsystems:** `cert-military`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`

**Prior art notes:**

> The VZ-7 is one of three contemporaneous U.S. Army 'flying jeep' programs (with the Chrysler VZ-6 and Piasecki VZ-8) that disclosed the modern open-rotor quadrotor architecture in 1958, controlled by differential rotor thrust at the four corners of an X-frame. Establishes a 1958 anchor for: (1) corner-mounted open-rotor quad configuration, (2) cross-shafted single-engine drive of four lift rotors (mechanical analogue of modern electric quadrotors with DC-link power sharing), (3) differential-thrust attitude allocation. Combined with de-bothezat-quadrotor (1922), this places the basic open-rotor quadrotor lift architecture in the public domain a full half-century before any modern multirotor patent attempt. The Hoversurf S3 and Aerofex hover bike as well as Jetson ONE all sit downstream of this disclosure.

**Sources:**

1. Markman, Steve and Holder, Bill. Straight Up. Schiffer, 2000.
2. U.S. Army Transportation Research Command VZ-7 test reports, available DTIC.
3. Lambert, Mark (ed.). Jane's All The World's Aircraft 1959–60.

---

### 1958-10-12 — Piasecki VZ-8 Airgeep

- **id:** `piasecki-vz-8-airgeep`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Piasecki Aircraft Corporation / U.S. Army Transportation Research Command
- **disclosure citation:** Piasecki VZ-8 Airgeep first flight 1958-10-12 at Piasecki Pennsylvania facility. Sister U.S. Army 'flying jeep' program to Curtiss-Wright VZ-7 and Chrysler VZ-6. Documented in TRC test reports.
- **disclosed subsystems:** `cert-military`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`

**Prior art notes:**

> Piasecki VZ-8 Airgeep is the third major U.S. Army 'flying jeep' program of 1958 (with Curtiss-Wright VZ-7 and Chrysler VZ-6), establishing prior art for: (1) tandem fore-and-aft open-rotor architecture (precursor to Aerofex Aero-X hover-bike geometry by 50 years), (2) cross-coupled twin-piston-engine drive with engine-out continued lift. The hover-bike architecture descends directly from this 1958 disclosure.

**Sources:**

1. U.S. Army Transportation Research Command VZ-8 reports.
2. Piasecki Aircraft Corporation archives.
3. Markman and Holder. Straight Up. Schiffer, 2000.

---

### 2008-10 — Aerofex Aero-X

- **id:** `aerofex-aero-x`
- **corpus:** private
- **ip status:** patented
- **creator:** Aerofex Corporation (Manhattan Beach, California)
- **disclosure citation:** Aerofex first concept demonstrator publicly unveiled October 2008; Aero-X full-scale prototype publicly demonstrated 2014-04-30. Founded by Mark De Roche, ex-Boeing/NASA; Aerofex hold patents on ducted-rotor stability augmentation.
- **disclosed subsystems:** `cert-part-103-ultralight`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`

**Prior art notes:**

> Aerofex Aero-X is the canonical disclosure of the modern hover-bike architecture: rider-straddle platform with twin large lift rotors fore and aft. Establishes prior art for: (1) personal hover-bike form factor, (2) intuitive lean-to-bank stability control mapping rider body input to differential rotor thrust, (3) the open-rotor straddle motorcycle-like operational paradigm. Anticipates Hoversurf S3, JetPack Aviation Speeder, and any subsequent hover-bike patent attempt.

**Sources:**

1. De Roche, Mark. US Patent 8,083,173, 2011.
2. Aerofex press releases and demonstration materials 2008–2017.
3. Popular Science and Wired coverage 2010–2014.

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

### 2011-10-21 — e-volo VC1 (Volocopter precursor)

- **id:** `volocopter-vc1`
- **corpus:** private
- **ip status:** patented
- **creator:** e-volo GmbH (later Volocopter GmbH)
- **disclosure citation:** e-volo / Stephan Wolf, Thomas Senkel, Alexander Zosel: first manned multicopter flight, 2011-10-21 at Karlsruhe-Forchheim airfield; documented in DLR aviation news and academic press.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-experimental`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`, `power-li-po`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`

**Prior art notes:**

> The e-volo VC1 is the first manned electric multicopter to achieve flight, predating EHang, Joby S2/S4, and Volocopter VoloCity. Establishes prior art for: (1) electric manned multicopter passenger air-mobility architecture, (2) sixteen-rotor circular lift configuration with differential-thrust attitude control, (3) the underlying Volocopter patent family (DE102010032217 and continuations). Anticipates virtually all current commercial electric multirotor air-taxi claims (EHang EH216, Volocopter VoloCity, Hyundai Supernal multirotor configurations).

**Sources:**

1. Senkel, T., Zosel, A., Wolf, S. e-volo flight test reports, 2011.
2. Volocopter GmbH patent family, esp. DE102010032217.
3. DLR magazine coverage 2011–2012 of first manned multicopter flight.

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

### 2013-01-31 — Bitcraze Crazyflie

- **id:** `bitcraze-crazyflie`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Bitcraze AB
- **disclosure citation:** Bitcraze Crazyflie 1.0 publicly released 2013-01-31 as open hardware (BSD/CERN-OHL licensed); subsequent Crazyflie 2.X (2016) widely adopted in academic robotics research. Hardware design files openly published at github.com/bitcraze. Founded by Arnaud Taffanel, Tobias Antonsson, and Marcus Eliasson.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `propulsion-bldc-direct-drive`, `cert-experimental`

**Prior art notes:**

> Bitcraze Crazyflie is the canonical open-hardware micro-quadrotor reference platform — used in 1000+ academic papers and hundreds of university research labs worldwide as the standard small-quadrotor experimental platform. Establishes Swedish prior art for open-hardware quadrotor design and substantially places small-quadrotor architecture in the open-hardware public domain via CERN-OHL/BSD/GPL licensing. Combined with ardupilot-quadplane and px4-vtol, comprehensively places open-source / open-hardware multirotor design in prior art.

**Sources:**

1. Bitcraze AB Crazyflie repository, github.com/bitcraze.
2. Honegger, D. et al. 'An Open Source Indoor Visual Odometry.' ICRA 2013.
3. Multiple academic papers using Crazyflie as research platform 2013-2024.

---

### 2014-07 — H3 Dynamics HyFly hydrogen-electric eVTOL

- **id:** `h3-dynamics-hyfly`
- **corpus:** private
- **ip status:** patented
- **creator:** H3 Dynamics (Singapore) / H3 Dynamics SAS (France)
- **disclosure citation:** H3 Dynamics founded 2014-07 in Singapore by Taras Wankewycz; hydrogen fuel-cell UAS commercialized starting 2019; H3 Dynamics demonstrated long-endurance hydrogen UAS at Singapore Airshow 2022 and 2024.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `propulsion-hydrogen-fuel-cell`, `propulsion-bldc-direct-drive`, `control-differential-thrust-attitude`, `cert-easa-special-condition-vtol`

**Prior art notes:**

> H3 Dynamics establishes Singapore prior art for hydrogen-fuel-cell VTOL UAS. The Singapore/France dual-headquarters structure is increasingly common for aerospace startups operating across multiple regulatory regimes. Adds Singapore to the eVTOL OEM map and establishes hydrogen-electric VTOL architecture prior art alongside AMSL Vertiia (AU passenger-class hydrogen).

**Sources:**

1. H3 Dynamics press releases 2014-2024.
2. Singapore Airshow 2022 and 2024 exhibitor materials.

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

### 2017-04-28 — Hoversurf Scorpion-3

- **id:** `hoversurf-s3`
- **corpus:** private
- **ip status:** patented
- **creator:** Hoversurf Inc (Russia / United States)
- **disclosure citation:** Hoversurf Scorpion-3 prototype publicly unveiled 2017-04-28 in Moscow; first paying customer (Dubai Police) publicly disclosed 2017-10-13; FAA Part 103 Special Light-Sport Aircraft compliance evaluation 2018. Hoversurf founded 2014 by Alexander Atamanov.
- **disclosed subsystems:** `cert-part-103-ultralight`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`

**Prior art notes:**

> Hoversurf Scorpion-3 is the leading commercial hover-bike — Russian-founded company with US operations, sold to Dubai Police as the first operational hover-bike patrol vehicle (2017). Establishes Russian prior-art lineage for the hover-bike form factor and confirms operational deployment pre-2018.

**Sources:**

1. Hoversurf press releases 2017–2024.
2. Dubai Police adoption announcement 2017-10-13.
3. FAA Part 103 ultralight registration records.

---

### 2017-10-09 — Workhorse SureFly

- **id:** `workhorse-surefly`
- **corpus:** private
- **ip status:** patented
- **creator:** Workhorse Group / Moog Aircraft Group
- **disclosure citation:** Workhorse SureFly publicly unveiled 2017-10-09 at AOPA Norman OK; first tethered hover 2018-05-09 at Wilmington OH. Workhorse spun off SureFly to Moog Aircraft Group 2019-10. Program effectively shelved 2020. Documented in Workhorse SEC filings (NASDAQ: WKHS) 2017-2020.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `propulsion-hybrid-series`, `power-hybrid-genset`, `propulsion-bldc-direct-drive`, `control-differential-thrust-attitude`, `safety-ballistic-parachute`, `airframe-composite-monocoque`, `cert-part-23`

**Prior art notes:**

> Workhorse SureFly establishes US prior art for hybrid-electric octocopter with ballistic recovery parachute as integrated standard equipment (2017). Although the program effectively shelved by 2020, the public disclosures (2017-10-09 unveiling, 2018-05-09 hover, Workhorse SEC filings) establish the prior-art date. SureFly's coaxial-pair-on-cruciform geometry anticipates Honda eVTOL and other hybrid-electric multirotor configurations filed post-2017.

**Sources:**

1. Workhorse Group Form 10-K SEC filings 2017-2020.
2. Workhorse press releases 2017-2019.
3. AOPA SureFly unveiling materials 2017-10-09.

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

### 2018-07-12 — Pivotal Helix (formerly Opener BlackFly)

- **id:** `pivotal-blackfly`
- **corpus:** private
- **ip status:** patented
- **creator:** Opener Inc / Pivotal LLC
- **disclosure citation:** Opener / BlackFly publicly unveiled 2018-07-12 with first flight video and FAA Part 103 ultralight categorization; subsequent customer deliveries 2022 (Pivotal Helix branding 2023).
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-part-103-ultralight`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `transition-tail-sitter-pitch-up`

**Prior art notes:**

> Pivotal Helix (formerly Opener BlackFly) is a single-pilot tail-sitter eVTOL operating under FAA Part 103 ultralight rules — the first commercially-delivered eVTOL in the U.S. market. Architecturally a tail-sitter (descended from XFY-1 Pogo, 1954) with eight distributed electric rotors. Establishes prior art for: (1) eight-rotor tail-sitter eVTOL geometry, (2) Part 103 ultralight-class commercial eVTOL deployment basis, (3) the design tradeoff of pilot pitch reorientation as an alternative to tilt-rotor or tilt-wing transition mechanisms.

**Sources:**

1. Opener Inc press releases 2018-07-12 onward.
2. Pivotal LLC product disclosures and FAA Part 103 ultralight registrations.
3. Page, Marcus et al. US Patent 11,066,162 (Opener).

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

### 2018-12 — SkyDrive SD-05

- **id:** `skydrive-sd-05`
- **corpus:** private
- **ip status:** patented
- **creator:** SkyDrive Inc
- **disclosure citation:** SkyDrive SD-03 (precursor demonstrator) public manned flight 2020-08-25 at Toyota Test Field; SD-05 production design unveiled 2021-09; Japan Civil Aviation Bureau type-certification application accepted 2021-10. SkyDrive founded 2018-12 (incorporation date), spinning out from CARTIVATOR volunteer eVTOL project (founded 2012).
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `control-differential-thrust-attitude`, `lift-coaxial-rotor`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `safety-ballistic-parachute`, `safety-redundant-bus`

**Prior art notes:**

> SkyDrive SD-05 is Japan's lead passenger eVTOL, with Japan Civil Aviation Bureau type-certification application accepted 2021-10. The 12-motor coaxial-pair architecture is similar to EHang EH216-S; the program establishes Japanese prior-art lineage for multirotor passenger eVTOL and the JCAB SC-VTOL-equivalent certification approach. Originated in the volunteer CARTIVATOR project (2012), one of the earliest organized open-development eVTOL efforts.

**Sources:**

1. SkyDrive Inc press releases 2018–2024.
2. Japan Civil Aviation Bureau type-certification application docket.
3. Toyota Motor Corporation investor disclosures (Toyota is a SkyDrive backer).

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

### 2024-04-04 — XPENG AeroHT Land Aircraft Carrier

- **id:** `xpeng-aeroht-modular`
- **corpus:** private
- **ip status:** patented
- **creator:** AeroHT (XPENG flying car subsidiary)
- **disclosure citation:** XPENG AeroHT Land Aircraft Carrier publicly unveiled 2024-04-04 at Beijing Auto Show; production target 2026. Combines a road-legal 6x6 ground vehicle ('Mothership') containing a fold-out manned eVTOL drone.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-easa-special-condition-vtol`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-redundant-bus`

**Prior art notes:**

> XPENG AeroHT Land Aircraft Carrier is the most ambitious modular drive+fly transformer architecture publicly disclosed: a separate ground vehicle that carries and deploys a manned eVTOL. Establishes Chinese prior-art lineage for modular vehicle-eVTOL architectures, distinct from integrated transformer-eVTOL designs (ASKA A5, AeroMobil) where one vehicle physically transforms. Anticipates future modular-carrier patent filings.

**Sources:**

1. XPENG AeroHT Beijing Auto Show 2024-04-04 unveiling materials.
2. AeroHT / XPENG technical disclosures 2024.
3. Reuters and South China Morning Post coverage 2024-04-04.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `bff4888`.*
