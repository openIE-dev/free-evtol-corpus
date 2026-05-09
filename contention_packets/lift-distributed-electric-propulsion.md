---
title: "lift-distributed-electric-propulsion"
parent: "Invalidity Contentions"
nav_order: 17
layout: default
---

# Invalidity Contention Packet — `lift-distributed-electric-propulsion`

**Generated:** 2026-05-09  
**Cross-cut tag:** `lift-distributed-electric-propulsion`  
**Entries:** 60 (60 commons-grade, 0 draft)  
**Earliest disclosure:** 1886  
**Most recent disclosure:** 2024-04-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `lift-distributed-electric-propulsion`.

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

### 1886 — Albatross (Robur the Conqueror)

- **id:** `verne-albatross`
- **corpus:** fictional
- **ip status:** public-domain
- **creator:** Jules Verne
- **disclosure citation:** Verne, Jules. Robur le Conquérant. J. Hetzel et Cie, Paris, 1886.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`

**Prior art notes:**

> Foundational prior art for distributed electric propulsion (DEP) lift architectures. Verne explicitly describes thirty-seven pairs of vertical lift airscrews electrically driven, distributing lift across many independent rotors with horizontal cruise propellers decoupled from lift. This anticipates the entire architectural pattern of modern multirotor and lift+cruise eVTOL aircraft: many small electric lift rotors, redundancy through multiplicity, and separation of hover-lift propulsion from cruise propulsion. Any patent claim asserting novelty over 'plurality of electrically-driven lift rotors arranged across an airframe' filed after 1886 is anticipated by this disclosure. The 1886 publication date predates by 36 years the de Bothezat quadrotor and by 130+ years all current eVTOL companies.

**Sources:**

1. Verne, Jules. Robur le Conquérant. Paris: J. Hetzel et Cie, 1886.
2. Verne, Jules. The Clipper of the Clouds. Sampson Low, London, 1887 (English translation).
3. Standard scholarly editions catalog the lift-rotor count at 74; e.g., Butcher, William. Jules Verne: The Definitive Biography (2006).

---

### 1907-11-13 — Cornu helicopter

- **id:** `cornu-helicopter`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Paul Cornu
- **disclosure citation:** Cornu helicopter first untethered free flight 1907-11-13 at Coquainvilliers, Normandy, by Paul Cornu — 20 cm altitude for 20 seconds. The first manned heavier-than-air rotorcraft to leave the ground in free flight. Documented in Cornu's contemporary technical papers and FAI archives.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `cert-experimental`

**Prior art notes:**

> Paul Cornu's 1907 helicopter is the first free-flying piloted heavier-than-air rotorcraft in human history — predating the de Bothezat quadrotor by 15 years. Establishes prior art for: (1) twin-rotor manned rotorcraft architecture with cross-belt single-engine drive, (2) the foundational concept of practical vertical lift via airfoil-type rotors. Cornu's design materials are in the French public domain (creator died 1944, copyright in design specifications long expired). Combined with verne-albatross (1886) and pescara-helicopter (1922), comprehensively places multi-rotor manned VTOL in pre-1925 prior art.

**Sources:**

1. Cornu, Paul. 'Hélicoptère.' L'Aérophile, December 1907.
2. FAI archives, first free-flight rotorcraft record.
3. Liberatore, E.K. Helicopters Before Helicopters. Krieger, 1998.

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

### 1932-08-14 — TsAGI 1-EA

- **id:** `tsagi-1-ea`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** TsAGI (Central Aerohydrodynamic Institute) / Alexei Cheremukhin
- **disclosure citation:** TsAGI 1-EA helicopter set unofficial world altitude record 1932-08-14: 605 m piloted by Alexei Cheremukhin (the existing FAI record was 18 m). Documented in TsAGI archives, RGAE archives, and Mikheyev's Russian-language history of Soviet rotorcraft.
- **disclosed subsystems:** `cert-experimental`, `lift-distributed-electric-propulsion`

**Prior art notes:**

> TsAGI 1-EA is the foundational Soviet rotorcraft disclosure (1930-1934 test program). Establishes Russian/Soviet prior art for: (1) multi-rotor anti-torque architecture (one main lift rotor + four small anti-torque rotors at outriggers — an unusual lift-and-attitude split that anticipates modern eVTOL designs with separate lift and yaw rotors). Soviet government work, fully in the public domain post-1991. Often overlooked in Western rotorcraft histories despite predating practical Western helicopters by years.

**Sources:**

1. Mikheyev, Vadim. Stranitsy istorii TsAGI [TsAGI History]. TsAGI Press, multiple editions.
2. Cheremukhin, A.M. archives, TsAGI Library.
3. Liberatore, E.K. Helicopters Before Helicopters. Krieger, 1998.
4. RGAE (Russian State Archive of Economy) Soviet Aviation Industry collections.

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

### 1939-09-14 — Sikorsky VS-300

- **id:** `sikorsky-vs-300`
- **corpus:** academic
- **ip status:** patented
- **creator:** Igor Sikorsky / Vought-Sikorsky Aircraft
- **disclosure citation:** Sikorsky VS-300 first tethered hover 1939-09-14 at Stratford CT, by Igor Sikorsky himself; first untethered free flight 1940-05-13. Direct ancestor of the Sikorsky R-4 (first production single-rotor helicopter) and the entire Sikorsky helicopter dynasty. Documented in Sikorsky archives and Smithsonian collections (the VS-300 itself is at the Henry Ford Museum).
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `cert-experimental`

**Prior art notes:**

> Sikorsky VS-300 is the foundational disclosure of the single-main-rotor + tail-rotor helicopter architecture that subsequently dominated heavier-than-air rotorcraft for 80+ years. Establishes prior art for: (1) the simple single-rotor + small-anti-torque-rotor architecture, (2) the iterative design methodology of progressive simplification from compound multi-rotor to canonical single-rotor configuration. Igor Sikorsky's foundational patents are long expired. Although not strictly an eVTOL, VS-300 is foundational vertical-lift prior art that anticipates any helicopter-derived eVTOL.

**Sources:**

1. Sikorsky, Igor. The Story of the Winged-S. Dodd Mead, multiple editions 1938-1958.
2. Sikorsky Aircraft Corporation archives, United Technologies Hartford.
3. Henry Ford Museum / Greenfield Village VS-300 collection.

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

### 1962-09-23 — Jetsons family aerocar

- **id:** `jetsons-aerocar`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Hanna-Barbera Productions
- **disclosure citation:** The Jetsons, episode 1 'Rosey the Robot', original air date 1962-09-23, ABC.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`

**Prior art notes:**

> The Jetsons aerocar establishes in the 1962 cultural baseline the family-sized urban-air VTOL passenger pod with four lift propulsors and a transparent canopy — the exact form factor commercial eVTOL companies (Joby S4, Archer Midnight, Wisk Cora, Lilium Jet, Volocopter VoloCity, EHang EH216) are now claiming as differentiating product design. Anticipates: small-pax-count urban-air-mobility VTOL with multiple lift propulsors, transparent-canopy passenger compartment, ground-and-air drive+fly transformer mode (precedent for AeroMobil, PAL-V Liberty, ASKA A5). The fictional nature does not weaken this as 102/103 reference: courts have repeatedly held that fictional disclosures of specific configurations anticipate later patent claims (cf. Heinlein 'waldoes' as prior art for teleoperated manipulators).

**Sources:**

1. The Jetsons, original Hanna-Barbera ABC broadcast, 1962-09-23.
2. Solomon, Charles. The Art of Hanna-Barbera. Crown, 1989.
3. Anderson, Christopher. The Jetsons: A Family History. Pocket Books reference, 1995.

---

### 1968-06-27 — Mil V-12 (Mi-12)

- **id:** `mil-v-12`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Mil Moscow Helicopter Plant
- **disclosure citation:** Mil V-12 first hover 1968-06-27; first horizontal flight 1969-02-10. Set FAI absolute payload world record 1969-08-06: 40,204.5 kg lifted to 2,255 m. The world record stands unbroken. Documented in Mil OKB archives and in Gunston's Soviet aircraft references.
- **disclosed subsystems:** `cert-experimental`, `lift-distributed-electric-propulsion`

**Prior art notes:**

> The V-12/Mi-12 is the largest helicopter ever built and the canonical disclosure of side-by-side lateral lift-rotor architecture at scale. Establishes prior art for: (1) twin-side-by-side lateral lift-rotor geometry (architectural ancestor of any eVTOL with lateral twin-rotor lift), (2) cross-shafted multi-engine drive of lateral rotor pair (engine-out continued lift), (3) record-scale heavy-lift VTOL operations. Soviet government work, comprehensively in the public domain post-1991. Although not electric, the lateral-rotor architectural pattern is anticipated for any commercial eVTOL claiming novelty over twin-side-by-side lift rotor configurations.

**Sources:**

1. Mikheyev, Vadim. Mil V-12 / Mi-12: The World's Largest Helicopter. Polygon, 2002.
2. Gunston, Bill. The Osprey Encyclopedia of Russian Aircraft. Osprey, 1995.
3. FAI absolute world record archive, 1969-08-06.

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

### 2016-06-17 — NASA X-57 Maxwell

- **id:** `nasa-x-57-maxwell`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** NASA Armstrong Flight Research Center / Empirical Systems Aerospace (ESAero)
- **disclosure citation:** NASA X-57 Maxwell publicly designated 2016-06-17; foundational design papers by Borer, Patterson et al. published 2014–2018. Program experimental flight test cancelled before powered flight 2023-06-23 due to budget constraints, but design and ground-test data are comprehensively documented in NASA TM and TP series.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-experimental`

**Prior art notes:**

> NASA X-57 Maxwell is the foundational disclosure of distributed electric propulsion (DEP) for fixed-wing aircraft — the 'high-lift blown-wing' approach where many small electric propellers along the wing leading edge augment wing circulation. Although STOL rather than VTOL, X-57 establishes prior art for: (1) high-multiplicity DEP architecture (12 leading-edge propellers + 2 wingtip), (2) BLDC direct-drive propulsion at scale, (3) lithium-ion battery propulsion at certified-aircraft scale. Combined with NASA GL-10 (2014, VTOL DEP), comprehensively places DEP architecture in U.S. government public-domain prior art for both fixed-wing and VTOL applications. Cited extensively in commercial eVTOL technical white papers as the canonical DEP design reference.

**Sources:**

1. Borer, N.K., Patterson, M.D. et al. 'Design and Performance of the NASA SCEPTOR Distributed Electric Propulsion Flight Demonstrator.' AIAA SciTech 2016.
2. NASA TM-2017-219653, NASA TP-2018-219898, and many other X-57 / SCEPTOR papers.
3. NASA Armstrong Flight Research Center X-57 program archive.

---

### 2017-03 — Zuri eVTOL

- **id:** `zuri-evtol`
- **corpus:** private
- **ip status:** patented
- **creator:** Zuri s.r.o (Prague, Czech Republic)
- **disclosure citation:** Zuri founded 2017-03 by Michal Illich, Stanislav Saling, and Daniel Hadacek; first sub-scale prototype publicly demonstrated 2018-09; full-scale Zuri 2.0 prototype unveiled 2021-10-12 in Pisek and reached first hover 2023-09-22. EASA Special Condition VTOL certification dialogue 2022 onward.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `lift-distributed-electric-propulsion`, `power-hybrid-genset`, `propulsion-bldc-direct-drive`, `propulsion-hybrid-series`, `safety-ballistic-parachute`, `safety-redundant-bus`, `transition-mode-shutdown`

**Prior art notes:**

> Zuri eVTOL is the lead Czech (and Central European) commercial eVTOL — hybrid-electric lift+cruise distinct from pure-battery competitors in its 700 km range targeting. Establishes Czech prior-art lineage for hybrid-electric eVTOL and adds to the global hybrid-eVTOL prior-art base alongside Honda eVTOL, AMSL Aero Vertiia, and Elroy Air Chaparral.

**Sources:**

1. Zuri press releases and technical materials 2017–2024.
2. Czech Civil Aviation Authority engagement records.
3. Aviation Week and Vertical magazine coverage 2018–2023.

---

### 2017-04-26 — Wingcopter 198

- **id:** `wingcopter-198`
- **corpus:** private
- **ip status:** patented
- **creator:** Wingcopter GmbH (Weiterstadt, Germany)
- **disclosure citation:** Wingcopter founded 2017-04-26; Wingcopter 178 first commercial flights 2018-09 (vaccine delivery to Vanuatu islands with UNICEF); Wingcopter 198 production-design unveiled 2020-04-21. EU type certification (CS-LURS / EASA Special Condition) in process. Wingcopter holds the Tilt-Rotor Mechanism patent family (EP3260370, US10913529).
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-bvlos-detect-and-avoid`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `lift-distributed-electric-propulsion`, `lift-tilt-rotor`, `power-li-po`, `propulsion-bldc-direct-drive`, `safety-redundant-bus`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Wingcopter 198 is Germany's lead unmanned tilt-rotor cargo eVTOL — operational since 2018 (medical delivery to Pacific islands with UNICEF). Establishes prior art for: (1) small-airframe tilt-rotor cargo eVTOL with single-axis tilt mechanism (Wingcopter Tilt-Rotor Mechanism patent family), (2) the cargo / payload-delivery use case for tilt-rotor eVTOL distinct from passenger air taxi. Anticipates cargo eVTOL claims asserting novelty over single-axis tilt actuation.

**Sources:**

1. Wingcopter GmbH press releases 2017–2024.
2. Wingcopter Tilt-Rotor Mechanism patents EP3260370 / US10913529.
3. UNICEF Pacific islands medical delivery program reports 2018.

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

### 2018 — ASKA A5

- **id:** `aska-a5`
- **corpus:** private
- **ip status:** patented
- **creator:** ASKA / NFT Inc (Mountain View, California / Nagoya, Japan)
- **disclosure citation:** ASKA / NFT Inc founded 2018 by Guy Kaplinsky and Maki Kaplinsky; A5 production-design unveiled at CES 2023 (2023-01-04); FAA Special Airworthiness Certificate (Experimental) granted 2023-06-29 for flight testing. NHTSA-approved street-legal road operation pending.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-part-23`, `lift-distributed-electric-propulsion`, `lift-tilt-rotor`, `power-hybrid-genset`, `propulsion-hybrid-series`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> ASKA A5 is the leading drive+fly transformer eVTOL with documented FAA experimental-category certification. Establishes prior art for: (1) folding-wing tilt-rotor transformer architecture, (2) hybrid-electric powerplant for transformer range extension, (3) dual-certification basis (FAA + NHTSA road-legal). Anticipates: PAL-V Liberty, AeroMobil 4.0, Klein Vision AirCar, and any modern drive+fly patent claim.

**Sources:**

1. ASKA / NFT Inc press releases 2018–2024.
2. FAA Special Airworthiness Certificate dossier (ASKA A5).
3. ASKA technical white papers and patent filings.

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

### 2018-05-09 — EmbraerX eVTOL concept (2018)

- **id:** `embraerx-evtol-concept`
- **corpus:** private
- **ip status:** patented
- **creator:** EmbraerX (Embraer S.A. internal venture)
- **disclosure citation:** Embraer publicly unveiled its eVTOL air taxi concept design at the Uber Elevate Summit, Los Angeles, 2018-05-09. EmbraerX (Embraer's internal venture launched 2017-10) led the design. The 2018 concept preceded Eve UAM Solutions (Embraer subsidiary, 2020-10-08) and Eve Holding spinoff (NYSE: EVEX SPAC merger, 2022-05-09).
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-23`, `airframe-composite-monocoque`, `safety-redundant-bus`

**Prior art notes:**

> EmbraerX 2018 is the original Brazilian disclosure of the lift+cruise architecture that subsequently became Eve Air Mobility's production design. Establishes Brazilian / Latin American prior-art lineage two years earlier than the 2020 Eve Air Mobility entity. The Uber Elevate Summit 2018 unveiling makes this a publicly-dated Embraer corporate disclosure with documented engineering depth in subsequent Embraer technical materials. Combined with eve-air-mobility (2020), provides a multi-year Embraer lineage for the 8+1 lift+cruise architecture.

**Sources:**

1. Uber Elevate Summit, Los Angeles, 2018-05-09 (live-streamed; archived video).
2. EmbraerX press releases 2018-2020.
3. Embraer S.A. corporate archives and 20-F SEC filings 2018-2020.

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

### 2018-12-20 — Joby Aviation S4

- **id:** `joby-s4`
- **corpus:** private
- **ip status:** patented
- **creator:** Joby Aviation
- **disclosure citation:** Joby S4 unveiling and first flight: Joby first publicly disclosed S4 prototype 2018-12-20 (Joby press release); first untethered transition flight 2017-08 (predecessor S2); S4 Production Prototype first transition flight reported in Joby Aviation S-1 SEC filing 2020-08, full disclosure in 10-K filings 2021–2025.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-part-23`, `control-fly-by-wire-triplex`, `control-simplified-vehicle-operations`, `lift-distributed-electric-propulsion`, `lift-tilt-rotor`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`, `sensing-lidar-terrain`, `sensing-radar-altimeter`, `transition-conversion-corridor`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The Joby S4 is the lead commercial tilt-rotor electric eVTOL. Direct architectural descendant of bell-xv-15 (1977) and v-22-osprey (1989) — Joby's tilt geometry, conversion corridor, and gimbaled prop-rotor topology are classical tilt-rotor architecture with electric distributed propulsion substituted for cross-shafted turboshaft. Establishes prior art for: (1) six-rotor tilt-rotor with stop-in-cruise props, (2) BLDC direct-drive tilt-rotor propulsion, (3) Part 23 SVO certification basis. Joby's patent estate (US 10,994,841 et seq.) covers specific implementations but is anticipated on the architectural level by XV-15 and V-22 disclosures.

**Sources:**

1. Joby Aviation S-1 (2020-08) and 10-K filings 2021–2025, SEC EDGAR.
2. Bevirt, JoeBen et al. US Patent 10,994,841 and US Patent 11,377,217.
3. Joby Aviation press releases 2018-12-20 (S4 unveil) and subsequent.
4. Vertical Flight Society Forum technical papers from Joby engineering staff 2019–2024.

---

### 2019-01-07 — Bell Nexus 4EX

- **id:** `bell-nexus-4ex`
- **corpus:** private
- **ip status:** patented
- **creator:** Bell (Textron Inc)
- **disclosure citation:** Bell Nexus design publicly unveiled 2019-01-07 at CES Las Vegas; Nexus 4EX revised four-rotor variant unveiled 2020-01-07. Program wound down circa 2022; design materials and filings remain in the public record.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-part-23`, `lift-distributed-electric-propulsion`, `lift-tilt-duct`, `power-hybrid-genset`, `propulsion-hybrid-series`, `safety-redundant-bus`, `sensing-radar-altimeter`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Bell Nexus is one of the Uber-Elevate-era US passenger eVTOL concepts (2019). Although the program wound down, the public design disclosures remain prior art for: (1) hybrid-electric tilting-ducted-fan eVTOL architecture, (2) Bell's specific tilt-duct geometry distinct from Joby's open-rotor tilt-rotor approach. Establishes additional US prior-art lineage for tilt-duct passenger eVTOL (with bell-x-22 from 1966).

**Sources:**

1. Bell / Textron press releases 2019–2022.
2. CES 2019 and CES 2020 Bell Nexus unveilings.
3. Bell Nexus patent filings, USPTO records.

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

### 2019-02-05 — Cargo VTOL (Wandering Earth)

- **id:** `wandering-earth-cargo-vtol`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Frant Gwo / Liu Cixin (original story) / China Film Group
- **disclosure citation:** The Wandering Earth (流浪地球), directed by Frant Gwo, theatrical release 2019-02-05 in China; based on Liu Cixin's 2000 novella. Production design materials documented in The Art of The Wandering Earth (Renmin University Press, 2019). Sequel The Wandering Earth 2 (2023) expanded the depiction with detailed cargo-VTOL deployment scenes.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The Wandering Earth establishes 2019 Chinese cinematic prior art for heavy-cargo VTOL atmospheric transport in extreme-environment operation. Combined with the existing Chinese commercial eVTOL prior-art base (EHang, AutoFlight, AeroHT XPENG, TCab, Geely Aerofugia), establishes China's substantial multi-decade cultural and industrial VTOL footprint. Adds Chinese fictional anchor distinct from the Japanese-dominated Asian fictional prior-art base.

**Sources:**

1. Gwo, Frant (dir.). The Wandering Earth (流浪地球). China Film Group, 2019.
2. Liu, Cixin. The Wandering Earth (流浪地球). Sichuan Science and Technology Press, 2000 (novella).
3. The Art of The Wandering Earth. Renmin University Press, 2019.

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

### 2019-05-16 — Lilium Jet (7-seat)

- **id:** `lilium-jet`
- **corpus:** private
- **ip status:** patented
- **creator:** Lilium GmbH
- **disclosure citation:** Lilium Jet 5-seat prototype unveiled and first hover flight 2019-05-16 at Manching; 7-seat production design unveiled 2021-03-30. Disclosures continued through Lilium SPAC merger Form S-4 2021-09 and subsequent NASDAQ filings until bankruptcy 2024-10.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `lift-distributed-electric-propulsion`, `lift-ducted-fan-array`, `lift-tilt-duct`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`, `sensing-radar-altimeter`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Lilium Jet establishes prior art for the high-multiplicity ducted-fan-array eVTOL: 36 small embedded ducted fans tilting in flap-segment groupings to provide both lift and cruise. Architecturally a hyper-distributed extension of Bell X-22 (4 tilt-ducts) and Doak VZ-4 (2 tilt-ducts). Although Lilium filed for bankruptcy in October 2024, the patent estate (now in receivership / likely auctioned) covers specific implementations of the 36-fan ducted-array geometry and EASA SC-VTOL certification basis approaches. The fundamental architecture (multiple ducted fans in a tilting flap arrangement) is anticipated by Bell X-22 (1966).

**Sources:**

1. Lilium Jet technical white paper 2021 (Munich, public download).
2. Lilium GmbH SPAC merger Form S-4 SEC filing 2021.
3. Wendel et al. 'Lilium Jet propulsion architecture' technical papers 2020–2022.

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

### 2019-10-03 — Kitty Hawk Heaviside

- **id:** `kittyhawk-heaviside`
- **corpus:** private
- **ip status:** patented
- **creator:** Kitty Hawk Corporation / Larry Page
- **disclosure citation:** Kitty Hawk Heaviside publicly unveiled 2019-10-03 at TED Conference / Wired25 Festival; first manned flight 2019-09. Kitty Hawk Corporation (funded by Larry Page) ceased operations 2022-09-21. Documented in Kitty Hawk press releases and the public technical paper 'Heaviside: A Single-Pilot eVTOL Aircraft' (Vertical Flight Society, 2020).
- **disclosed subsystems:** `lift-tilt-rotor`, `lift-distributed-electric-propulsion`, `transition-thrust-borne-to-wing-borne`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-103-ultralight`

**Prior art notes:**

> Kitty Hawk Heaviside establishes US prior art for ultralight-class single-pilot tilt-rotor eVTOL with explicit low-noise design optimization. Although Kitty Hawk Corporation ceased operations 2022, the Heaviside disclosure is comprehensive — Larry Page-funded program with VFS Forum technical paper publication and Kitty Hawk's continued patent portfolio licensable through successor entities. Kitty Hawk also produced Cora (which became Wisk Aero after the Boeing JV, covered separately).

**Sources:**

1. Kitty Hawk Corporation press releases 2019-2022.
2. Vertical Flight Society Forum 76 paper, 'Heaviside,' 2020.
3. TED Talk archive, Page/Kitty Hawk presentations 2018-2020.

---

### 2020-03-10 — Beta Technologies Alia-250

- **id:** `beta-alia-250`
- **corpus:** private
- **ip status:** patented
- **creator:** Beta Technologies
- **disclosure citation:** Beta Technologies / Kyle Clark publicly unveiled Alia-250 design 2020-03-10; first hover flight 2020-05; first full transition flight 2021-04; multiple cross-country flights 2022–2024 publicly documented.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-part-23`, `control-fly-by-wire-triplex`, `lift-coaxial-rotor`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`, `sensing-lidar-terrain`, `sensing-radar-altimeter`, `transition-mode-shutdown`

**Prior art notes:**

> Beta Alia-250 is the canonical commercial lift+cruise eVTOL: lift rotors stop and shut down in cruise, with a separate pusher providing forward propulsion. Architecturally simpler than tilt-rotor (no transition envelope coupling between lift and cruise), at cost of cruise drag from stopped lift rotors. Establishes prior art for: (1) production-scale lift+cruise architecture with mode-shutdown transition, (2) coaxial lift-pair geometry with single pusher cruise. Cited extensively by NASA Langley as the lift+cruise reference design.

**Sources:**

1. Beta Technologies press releases 2020–2024.
2. Vertical Flight Society Forum technical papers from Beta 2021–2023.
3. FAA Part 23 / Special Conditions for VTOL filings.

---

### 2020-04 — Manta Aircraft ANN2

- **id:** `manta-aircraft-ann2`
- **corpus:** private
- **ip status:** patented
- **creator:** Manta Aircraft S.A. (Lugano, Switzerland / Varese, Italy)
- **disclosure citation:** Manta Aircraft ANN2 design publicly unveiled April 2020 at AERO Friedrichshafen; sub-scale prototype hover testing 2021. Manta Aircraft founded 2018 by Lucas Marchesini (Italian-Swiss aerospace engineer).
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `lift-distributed-electric-propulsion`, `lift-tilt-rotor`, `power-hybrid-genset`, `propulsion-hybrid-series`, `safety-ballistic-parachute`, `safety-redundant-bus`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Manta Aircraft ANN2 is the lead Italian-Swiss commercial eVTOL — hybrid-electric tilt-rotor with twin-fuselage geometry. Adds Italian prior-art lineage for hybrid-electric eVTOL alongside Leonardo AW609 (production tilt-rotor) and complements the Slovak (Klein Vision, AeroMobil) and Dutch (PAL-V) drive+fly Central European base.

**Sources:**

1. Manta Aircraft press releases 2018–2024.
2. AERO Friedrichshafen 2020 unveiling materials.
3. EASA SC-VTOL engagement records.

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

### 2020-10-08 — Eve Air Mobility eVTOL

- **id:** `eve-air-mobility`
- **corpus:** private
- **ip status:** patented
- **creator:** Eve Holding Inc (Embraer S.A. spinoff)
- **disclosure citation:** Eve UAM Solutions launched as Embraer subsidiary 2020-10-08; spun off as standalone Eve Holding via SPAC merger 2022-05-09 (NYSE: EVEX). Aircraft design publicly unveiled 2022; first prototype unveiled 2024.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-part-23`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`, `sensing-radar-altimeter`, `transition-mode-shutdown`

**Prior art notes:**

> Eve Air Mobility is Brazil's lead commercial eVTOL, backed by Embraer's 100+-year aerospace heritage. The 8+1 lift+cruise architecture is architecturally similar to Beta Alia and AutoFlight Prosperity I; establishes Brazilian / Latin American prior-art lineage for commercial lift+cruise eVTOL. Eve has the deepest commercial aerospace certification experience among any eVTOL company by virtue of Embraer parentage.

**Sources:**

1. Embraer / Eve Holding 20-F SEC filings 2022–2024.
2. Eve Air Mobility press releases 2020–2024.
3. ANAC (Agência Nacional de Aviação Civil) eVTOL certification framework filings.

---

### 2021-03 — AMSL Aero Vertiia

- **id:** `amsl-vertiia`
- **corpus:** private
- **ip status:** patented
- **creator:** AMSL Aero Pty Ltd (Bankstown, Australia)
- **disclosure citation:** AMSL Aero Vertiia design publicly unveiled March 2021; sub-scale prototype hover testing 2022; first hover flight 2023-02-15. AMSL Aero founded 2017 by Andrew Moore (former CSIRO and Boeing engineer) and Siobhan Lyndon. Targeted at hydrogen-fuel-cell-powered eVTOL ambulance and regional connectivity missions.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-part-23`, `lift-distributed-electric-propulsion`, `propulsion-bldc-direct-drive`, `propulsion-hydrogen-fuel-cell`, `safety-ballistic-parachute`, `safety-redundant-bus`, `sensing-radar-altimeter`, `transition-mode-shutdown`

**Prior art notes:**

> AMSL Aero Vertiia is Australia's lead commercial eVTOL with a distinctive commitment to hydrogen-fuel-cell propulsion for 1,000 km range — addressing the energy-density limitation of pure-battery eVTOL. Establishes Australian prior-art lineage for hydrogen-eVTOL and for long-range regional eVTOL distinct from short-range urban air taxi. Anticipates other hydrogen-fuel-cell eVTOL claims (e.g., Joby's post-acquisition H2 program, Airbus ZEROe rotorcraft).

**Sources:**

1. AMSL Aero press releases 2021–2024.
2. Australian Civil Aviation Safety Authority (CASA) eVTOL framework filings.
3. Vertical Flight Society Forum 2023 papers from AMSL.

---

### 2021-06-10 — Archer Aviation Midnight

- **id:** `archer-midnight`
- **corpus:** private
- **ip status:** patented
- **creator:** Archer Aviation
- **disclosure citation:** Archer Aviation S-1 SEC filing 2021-06-10; Archer Midnight design publicly unveiled 2022-11-16; Maker demonstrator first hover flight 2021-12; first full transition 2023-06.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-part-23`, `control-fly-by-wire-triplex`, `lift-distributed-electric-propulsion`, `lift-tilt-rotor`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`, `sensing-lidar-terrain`, `sensing-radar-altimeter`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Archer Midnight is a hybrid lift+cruise / tilt-rotor architecture with six tilting and six lift-only propellers. Architecturally descends from the NASA GL-10 DEP tilt-wing concept and the XV-15 tilt-rotor, with the lift+cruise split providing lower hover-prop disk loading at the cost of cruise drag from idle lift props. Disclosures in SEC filings make this a commons-grade entry. Establishes prior art for: (1) 6+6 hybrid tilt-and-lift-only DEP architecture, (2) feathering cruise props with fixed-cruise disk.

**Sources:**

1. Archer Aviation S-1 (2021-06-10) and 10-K filings 2022–2025, SEC EDGAR.
2. Archer Aviation press releases including 2022-11-16 Midnight unveil.
3. Vertical Flight Society Forum 2023 technical paper from Archer engineering.

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

### 2021-09-14 — Geely Aerofugia AE200

- **id:** `geely-aerofugia-ae200`
- **corpus:** private
- **ip status:** patented
- **creator:** Aerofugia (Geely Holding Group eVTOL subsidiary)
- **disclosure citation:** Geely Holding Group launched Aerofugia subsidiary 2021-09-14 in Chengdu; AE200 design publicly unveiled at Beijing Air Show 2022-02-10; sub-scale prototype hover 2023-04. Geely also acquired Terrafugia (US) 2017-11 and uses combined IP base for AE200.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `lift-distributed-electric-propulsion`, `lift-tilt-rotor`, `power-li-ion-pouch`, `power-solid-state`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Geely Aerofugia AE200 is China's third major commercial passenger eVTOL (with EHang and AutoFlight). Distinctive: Geely's parallel ownership of Terrafugia (US flying car company since 2017) provides cross-Pacific patent integration. Establishes additional Chinese tilt-rotor prior-art lineage alongside TCab E20.

**Sources:**

1. Aerofugia / Geely press releases 2021-2024.
2. Beijing Air Show 2022 unveiling materials.
3. Geely Holding Group investor disclosures.

---

### 2021-09-21 — Airbus CityAirbus NextGen

- **id:** `airbus-cityairbus-nextgen`
- **corpus:** private
- **ip status:** patented
- **creator:** Airbus Helicopters (Donauwörth, Germany) / Airbus Defence and Space
- **disclosure citation:** Airbus CityAirbus NextGen design publicly unveiled 2021-09-21 at Airbus Summit; first scaled prototype hover 2024-09. EASA SC-VTOL type-certification process initiated 2022. Predecessor CityAirbus demonstrator first hover 2019-05-03.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `control-fly-by-wire-triplex`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`, `safety-ballistic-parachute`, `safety-redundant-bus`, `autonomy-utm-integration`

**Prior art notes:**

> Airbus CityAirbus NextGen is the production-track lift+cruise successor to the Vahana research program. Establishes German industrial prior-art lineage for production-scale lift+cruise passenger eVTOL with V-strut lift-rotor mounting geometry distinct from boom-mounted competitors (Beta Alia, Eve, Wisk). Airbus's industrial certification scale and EASA insider position make this a particularly important commons-grade entry.

**Sources:**

1. Airbus Helicopters press releases 2019–2024.
2. Airbus Summit 2021 unveiling materials.
3. EASA SC-VTOL public docket.

---

### 2021-09-29 — Vertical Aerospace VX4

- **id:** `vertical-vx4`
- **corpus:** private
- **ip status:** patented
- **creator:** Vertical Aerospace Ltd (Bristol, United Kingdom)
- **disclosure citation:** Vertical Aerospace VX4 unveiled 2021-09-29 at SPAC announcement / investor presentation; first tethered hover 2022-09-26; first untethered transition 2024-12. SPAC merger with Broadstone Acquisition (NYSE: EVTL) completed 2021-12. Lead investors include Microsoft / Avolon / American Airlines / Honeywell / Rolls-Royce.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `control-fly-by-wire-triplex`, `lift-distributed-electric-propulsion`, `lift-tilt-rotor`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`, `sensing-radar-altimeter`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Vertical Aerospace VX4 is the United Kingdom's lead commercial eVTOL — the post-Hawker British vectored/tilt VTOL inheritance translated into electric propulsion. The 4+4 tilt-and-lift hybrid is architecturally between Joby S4 (6 tilt) and Archer Midnight (6+6 hybrid). Establishes UK prior-art lineage for commercial tilt-rotor eVTOL; Rolls-Royce propulsion subsystem involvement provides direct industrial-scale supplier coverage.

**Sources:**

1. Vertical Aerospace 20-F SEC filings 2021–2024.
2. Vertical Aerospace press releases including 2021-09-29 SPAC announcement.
3. Honeywell Avionics and Rolls-Royce eVTOL-program technical disclosures.

---

### 2021-09-30 — Honda eVTOL

- **id:** `honda-evtol`
- **corpus:** private
- **ip status:** patented
- **creator:** Honda Motor Company / Honda Aircraft Company
- **disclosure citation:** Honda Motor Company eVTOL program publicly disclosed 2021-09-30 at 'Honda Dream Loop' announcement; design materials and target specifications subsequently disclosed in Honda investor briefings 2022–2024. Targeted commercial operation 2030.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-part-23`, `lift-distributed-electric-propulsion`, `power-hybrid-genset`, `power-solid-state`, `propulsion-bldc-direct-drive`, `propulsion-hybrid-series`, `safety-ballistic-parachute`, `safety-redundant-bus`, `sensing-radar-altimeter`, `transition-mode-shutdown`

**Prior art notes:**

> Honda eVTOL establishes prior art for hybrid-turbine-electric passenger eVTOL — Honda's specific architecture decision is to use a gas-turbine genset (leveraging HondaJet experience) for range extension. Anticipates other turbine-hybrid eVTOL claims (Elroy Air Chaparral, AMSL Aero Vertiia variants).

**Sources:**

1. Honda 'Dream Loop' announcement, 2021-09-30.
2. Honda Motor Company investor disclosures 2021–2024.
3. Honda Aircraft Company technical materials.

---

### 2021-10-04 — AIR ONE (eVTOL)

- **id:** `air-one`
- **corpus:** private
- **ip status:** patented
- **creator:** AIR Mobility Ltd (Pardes Hanna, Israel)
- **disclosure citation:** AIR ONE publicly unveiled 2021-10-04 in San Francisco; first untethered manned hover flight 2023-06-19 at AIR Pardes Hanna test site, Israel. AIR Mobility founded by Rani Plaut and Chen Rosen, 2018.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-part-23`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `transition-mode-shutdown`

**Prior art notes:**

> AIR ONE is Israel's lead consumer-grade eVTOL — distinct from CityHawk (commercial ducted-fan) by addressing the personal-recreational segment. Lift+cruise architecture targeting Part 23 certification with consumer operability emphasis. Establishes Israeli prior-art lineage for consumer/recreational eVTOL distinct from passenger air taxi.

**Sources:**

1. AIR Mobility press releases 2021–2024.
2. Globes (Israeli business newspaper) coverage of 2023-06-19 flight test.
3. Vertical Flight Society Forum 2023 papers from AIR engineering.

---

### 2021-12-13 — AutoFlight Prosperity I

- **id:** `autoflight-prosperity-i`
- **corpus:** private
- **ip status:** patented
- **creator:** AutoFlight (Shanghai)
- **disclosure citation:** AutoFlight Prosperity I publicly unveiled 2021-12-13; first untethered hover flight 2022-04; full-scale prototype transition flight 2023-02-23 at Kunshan; cross-Pearl River Delta demonstration flight Hong Kong → Macau 2024-04-29. AutoFlight founded by Tian Yu (former co-founder of EHang).
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`, `transition-mode-shutdown`

**Prior art notes:**

> AutoFlight Prosperity I is the leading Chinese lift+cruise eVTOL — architectural sibling to Beta Alia-250 with eight rather than four lift rotors. The 250 km Hong Kong-Macau demonstration flight (2024-04-29) is the longest eVTOL flight publicly documented as of mid-2024. Establishes Chinese prior-art lineage for lift+cruise architecture and supports EASA SC-VTOL certification basis dual-track with EHang's CAAC certification.

**Sources:**

1. AutoFlight press releases 2021–2024.
2. China Daily and Xinhua coverage of 2024-04-29 Hong Kong-Macau flight.
3. AutoFlight technical white papers (Chinese and English editions).

---

### 2022-08 — ePlane Company e200

- **id:** `eplane-company-e200`
- **corpus:** private
- **ip status:** patented
- **creator:** The ePlane Company (IIT Madras spinout)
- **disclosure citation:** The ePlane Company e200 unveiled 2022-08; first sub-scale prototype hover flight 2022-12; full-scale prototype rolled out 2023-09 at IIT Madras Research Park. Founded 2017 by Prof. Satya Chakravarthy. Awarded Anjani Mashelkar Inclusive Innovation Award 2023.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-part-23`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `transition-mode-shutdown`

**Prior art notes:**

> ePlane e200 is India's lead commercial eVTOL — IIT Madras research spinout with explicit design constraint for compact urban Indian airspace. Establishes Indian prior-art lineage for commercial lift+cruise eVTOL and the design philosophy of compact-footprint operation in dense urban environments. Targeted at DGCA (Directorate General of Civil Aviation, India) certification.

**Sources:**

1. Chakravarthy, Satya. ePlane Company technical white papers, 2022–2024.
2. Indian DGCA eVTOL certification framework filings.
3. IIT Madras Research Park ePlane Company disclosures.

---

### 2022-09-08 — Crisalion Mobility Integrity

- **id:** `crisalion-integrity`
- **corpus:** private
- **ip status:** patented
- **creator:** Crisalion Mobility S.L. (Tecnalia Research and Innovation spinoff)
- **disclosure citation:** Crisalion Mobility Integrity design publicly unveiled 2022-09-08 at Madrid; sub-scale demonstrator hover 2023. Crisalion Mobility spun off from Tecnalia Research and Innovation (Basque Country research center). Documented in Crisalion press materials and Tecnalia research disclosures.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `lift-tilt-rotor`, `transition-thrust-borne-to-wing-borne`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`

**Prior art notes:**

> Crisalion Mobility Integrity is Spain's lead commercial eVTOL — Tecnalia Research and Innovation (Basque Country) spin-off establishes Spanish industrial prior-art lineage for tilt-rotor distributed-electric passenger eVTOL. Adds Spain to the European eVTOL OEM map alongside Germany (Volocopter, Lilium, Wingcopter, Airbus CityAirbus), Italy (Leonardo, Manta), Netherlands (PAL-V), Slovakia (Klein Vision, AeroMobil), Czech Republic (Zuri), Sweden (Jetson).

**Sources:**

1. Crisalion Mobility press releases 2022-2024.
2. Tecnalia Research and Innovation public technical disclosures.

---

### 2022-12-07 — TCab Tech E20

- **id:** `tcab-tech-e20`
- **corpus:** private
- **ip status:** patented
- **creator:** TCab Tech (Shanghai TCab)
- **disclosure citation:** TCab Tech E20 sub-scale technology demonstrator first transition flight 2022-12-07 at Tianjin; full-scale E20 prototype unveiled 2023-09-13. TCab founded 2021 in Shanghai by Yon Wui Ng; technical leadership from former Volocopter and Lilium engineers.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `lift-distributed-electric-propulsion`, `lift-tilt-rotor`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> TCab Tech E20 is China's lead tilt-rotor passenger eVTOL — architectural sibling to Joby S4 with the same 4+2 tilt-rotor configuration. Establishes Chinese-lineage prior art for the tilt-rotor electric eVTOL category, ensuring the architectural pattern is disclosed across at least four geographic prior-art bases (US, EU, China, Italy).

**Sources:**

1. TCab Tech press releases and technical white papers 2022–2024.
2. Vertical Flight Society Forum 2023 papers including TCab Tech engineering.
3. South China Morning Post and Caixin coverage 2022–2024.

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

### 2024-01-09 — Hyundai Supernal S-A2

- **id:** `hyundai-supernal-sa2`
- **corpus:** private
- **ip status:** patented
- **creator:** Supernal LLC (Hyundai Motor Group eVTOL subsidiary)
- **disclosure citation:** Hyundai Supernal S-A2 unveiled at CES 2024 (Las Vegas), 2024-01-09. Predecessor S-A1 design unveiled at CES 2020 (2020-01-07). Supernal LLC incorporated under Hyundai Motor Group, headquartered in Washington DC with engineering in Irvine CA, but the design lineage and corporate ownership are South Korean.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-part-23`, `lift-distributed-electric-propulsion`, `lift-tilt-rotor`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`, `sensing-radar-altimeter`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Hyundai Supernal S-A2 is Korea's lead commercial eVTOL program, backed by Hyundai Motor Group's automotive industrial scale. The 4+4 tilt-rotor configuration is architecturally between Joby S4 (4+2) and tilt-wing designs. Establishes Korean prior-art lineage for tilt-rotor commercial eVTOL; targets FAA Part 23 certification and 2028 commercial operation.

**Sources:**

1. Supernal CES 2024 press materials, 2024-01-09.
2. Hyundai Motor Group investor disclosures.
3. FAA Part 23 / Special Conditions for VTOL filings.

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

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `b4393b4`.*
