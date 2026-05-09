---
title: "cert-experimental"
parent: "Invalidity Contentions"
nav_order: 6
layout: default
---

# Invalidity Contention Packet — `cert-experimental`

**Generated:** 2026-05-09  
**Cross-cut tag:** `cert-experimental`  
**Entries:** 33 (33 commons-grade, 0 draft)  
**Earliest disclosure:** 1907-11-13  
**Most recent disclosure:** 2018-01-31

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `cert-experimental`.

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

### 1923-01-09 — Cierva C.4 autogyro

- **id:** `cierva-autogyro`
- **corpus:** academic
- **ip status:** patented
- **creator:** Juan de la Cierva y Codorníu
- **disclosure citation:** Cierva C.4 first sustained autorotation flight 1923-01-09 at Getafe airfield, Madrid, by Lieutenant Alejandro Gómez Spencer. Cierva published design in Spanish Royal Academy of Sciences proceedings (1923) and held Spanish and British patents covering articulated rotor blade architecture.
- **disclosed subsystems:** `cert-experimental`, `lift-compound-rotorcraft`

**Prior art notes:**

> Cierva's C.4 is the foundational disclosure of articulated rotor blades with flapping hinges — the fundamental enabling invention without which modern rotorcraft (and any eVTOL with articulated blade roots) would not function. Establishes prior art for: (1) flapping-hinge articulated rotor blade design (the patent that made all subsequent rotorcraft possible), (2) compound rotorcraft architecture (forward thrust separate from rotor lift, anticipating modern compound rotorcraft like Fairey Rotodyne, Jaunt Journey, and Sikorsky Raider/Defiant). Cierva patents are long expired; the architectural disclosure is in the public domain.

**Sources:**

1. Cierva, Juan de la. Wings of Tomorrow. McBride, 1931.
2. Brooks, Peter W. Cierva Autogiros: The Development of Rotary-Wing Flight. Smithsonian, 1988.
3. Charnov, Bruce H. From Autogiro to Gyroplane. Praeger, 2003.

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

### 1942-12 — Bell Model 30

- **id:** `bell-model-30`
- **corpus:** academic
- **ip status:** patented
- **creator:** Arthur Young / Bell Aircraft Corporation
- **disclosure citation:** Bell Model 30 Ship 1A first hover December 1942 at Gardenville NY; first untethered free flight 1943-06-26. Direct ancestor of Bell 47 (1945, first civil-certified helicopter). Arthur Young's stabilizer-bar-equipped two-bladed teetering rotor became the foundational architecture for the Bell helicopter dynasty. Documented in Bell company archives and the Smithsonian National Air and Space Museum (Ship 1A is preserved).
- **disclosed subsystems:** `lift-coaxial-rotor`, `cert-experimental`

**Prior art notes:**

> Bell Model 30 (Arthur Young's design) is the foundational disclosure of the two-bladed teetering rotor with gyroscopically-coupled stabilizer bar — the architecture that made small helicopters practical and produced the Bell 47 (1946 first civil-certified helicopter, immortalized in M*A*S*H). Establishes prior art for: (1) two-bladed teetering rotor head architecture, (2) gyroscopic stabilizer-bar control augmentation. Arthur Young's foundational patents (US 2,415,148 et seq.) have been expired for over 50 years. Although not eVTOL, Bell Model 30 lineage is foundational vertical-lift prior art.

**Sources:**

1. Young, Arthur M. The Bell Notes: A Journey from Metaphysics to Mechanics. Robert Briggs, 1979.
2. Bell Helicopter / Textron archives, Fort Worth TX.
3. Smithsonian NASM Bell Ship 1A collection.

---

### 1955-08-11 — Bell XV-3

- **id:** `bell-xv-3`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Bell Helicopter / U.S. Air Force / U.S. Army
- **disclosure citation:** Bell XV-3 first flight 1955-08-11 at Hurst TX; first complete transition from helicopter to airplane mode 1958-12-18 — the first tilt-rotor in history to achieve full conversion. NACA / NASA / Army joint research program. Documented exhaustively in NASA SP-2000-4517 (which is primarily the XV-15 history but includes detailed XV-3 lineage discussion).
- **disclosed subsystems:** `lift-tilt-rotor`, `transition-thrust-borne-to-wing-borne`, `transition-conversion-corridor`, `cert-experimental`

**Prior art notes:**

> Bell XV-3 is the foundational disclosure of the tilt-rotor architecture — *the* original tilt-rotor predating Bell XV-15 by 22 years. Critically: the XV-3 is the first aircraft in history to achieve complete tilt-rotor transition from helicopter mode to airplane mode (1958-12-18, by Bill Quinlan). Establishes prior art for: (1) the entire tilt-rotor architectural concept (cross-shafted single-engine wingtip prop-rotors with nacelle tilt), (2) the conversion-corridor envelope methodology, (3) the lineage that produces XV-15 → V-22 → AW609 → Joby S4 → Archer Midnight → Vertical VX4 → Hyundai Supernal → Geely Aerofugia → Bell V-280 Valor. NACA/NASA/U.S. Army joint research program; comprehensively in the public domain. **Filed against any tilt-rotor patent claim asserting novelty over the basic wingtip-tilting prop-rotor architecture, this 1955-1958 disclosure is the deepest US public-domain anchor available.**

**Sources:**

1. Maisel, M.D., Giulianetti, D.J., Dugan, D.C. The History of the XV-15 Tilt Rotor Research Aircraft. NASA SP-2000-4517, 2000 (detailed XV-3 lineage chapter).
2. NASA TN D-2538, 'Performance Tests of the Bell XV-3 Tilt-Rotor Aircraft,' 1965.
3. Bell Helicopter XV-3 program archives.

---

### 1957-02-19 — Bell X-14

- **id:** `bell-x-14`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Bell Aircraft / U.S. Air Force / NASA Ames
- **disclosure citation:** Bell X-14 first hover 1957-02-19; first transition 1958-05-24. Operated by USAF and NASA Ames as a research testbed continuously 1957-1981. Documented in NASA TN, USAF Flight Test Center reports, and Smithsonian collections.
- **disclosed subsystems:** `lift-vectored-thrust`, `transition-thrust-borne-to-wing-borne`, `cert-experimental`

**Prior art notes:**

> Bell X-14 is the foundational US vectored-thrust VTOL testbed (1957) — predates Hawker P.1127 by 3 years. Establishes US prior-art lineage for deflected-jet vectored-thrust VTOL with reaction-control hover attitude. Distinct from Short SC.1 (1957) by using vane deflection rather than swivel nozzles. NASA Ames operated X-14 as a research testbed until 1981 — 24 years of accumulated public-domain flight data. Combined with hawker-p-1127, yak-36-freehand, dornier-do-31, vfw-fokker-vak-191b, and short-sc-1, comprehensively places vectored-thrust VTOL architecture in 1957-1971 prior art across US, UK, Soviet, and German lineages.

**Sources:**

1. NASA TN D-1859, 'Flight Tests of the X-14 Aircraft,' 1963.
2. Markman and Holder. Straight Up. Schiffer, 2000.
3. Bell Aircraft / Bell Aerosystems X-14 program archives.

---

### 1957-08-13 — Boeing-Vertol VZ-2

- **id:** `boeing-vertol-vz-2`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Vertol (later Boeing-Vertol) / U.S. Army Transportation Research Command
- **disclosure citation:** Vertol 76 / VZ-2 first hover 1957-08-13; first complete transition from hover to wing-borne flight 1958-07-15. The first aircraft in history to achieve complete tilt-wing transition. Documented in U.S. Army TRC reports and NASA Langley archives (the VZ-2 was extensively flight-tested at Langley 1959-1965).
- **disclosed subsystems:** `lift-tilt-wing`, `transition-thrust-borne-to-wing-borne`, `cert-experimental`

**Prior art notes:**

> Boeing-Vertol VZ-2 is the foundational disclosure of the tilt-wing architecture — *the* first tilt-wing aircraft in history to fly and to achieve complete transition. Predates LTV XC-142 (1964) by seven years and Canadair CL-84 (1965) by eight years. Establishes prior art for: (1) the entire tilt-wing architectural concept (whole wing rotates with engines), (2) cross-shafted single-engine drive of dual propellers with engine-out lift continuation, (3) the tilt-wing conversion corridor methodology. U.S. Army public-domain disclosure. **Anticipates every modern tilt-wing claim including NASA GL-10 (2014), Aurora LightningStrike (2016), and Airbus Vahana (2018).**

**Sources:**

1. U.S. Army Transportation Research Command VZ-2 reports.
2. NASA Langley Research Center VZ-2 flight test memoranda 1959-1965.
3. Markman and Holder. Straight Up. Schiffer, 2000.

---

### 1957-11-06 — Fairey Rotodyne

- **id:** `fairey-rotodyne`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Fairey Aviation Company / British European Airways
- **disclosure citation:** Fairey Rotodyne first flight 1957-11-06 at Boscombe Down; first transition (helicopter mode to autorotation cruise) 1958-04-10. Set FAI compound-rotorcraft world speed record 307 km/h on 1959-01-05. Program cancelled 1962. Documented in BEA / Fairey company archives and U.K. Ministry of Aviation reports.
- **disclosed subsystems:** `lift-compound-rotorcraft`, `lift-tip-jet-rotor`, `propulsion-tip-jet`, `cert-experimental`

**Prior art notes:**

> The Fairey Rotodyne is the UK's foundational compound-rotorcraft + tip-jet disclosure — production-scale (48-passenger) tip-burner rotor with autorotation cruise mode, holding the world compound-rotorcraft speed record. Establishes prior art for: (1) production-scale compound-rotorcraft architecture, (2) tip-burner rotor with auxiliary turboprop cruise, (3) the conversion-mode-shutdown (rotor powered in hover, autorotates in cruise) pattern that modern lift+cruise eVTOL adopt in electric form. Combined with doblhoff-wnf-342 and mil-v-7-tarakan, comprehensively places tip-jet rotor compound-rotorcraft in 1943-1957 prior art.

**Sources:**

1. Wood, Derek. The Project Cancelled: The Disaster of Britain's Abandoned Aircraft Projects. Macdonald & Jane's, 1975.
2. BEA / Fairey Aviation archives.
3. Markman and Holder. Straight Up. Schiffer, 2000.

---

### 1957-12-20 — Mil V-7 Tarakan

- **id:** `mil-v-7-tarakan`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Mil Moscow Helicopter Plant
- **disclosure citation:** Mil V-7 first ground-test 1957-12-20; first piloted hover trials 1959-04. Cancelled after instabilities discovered. Documented in Mil OKB declassified archives, RGAE collections, and Gunston's Soviet aviation references.
- **disclosed subsystems:** `cert-experimental`, `lift-tip-jet-rotor`, `propulsion-tip-jet`

**Prior art notes:**

> Mil V-7 is the Soviet contemporary tip-jet helicopter — a parallel-track development to Doblhoff/McDonnell tip-jet programs in the West. Establishes Soviet prior-art lineage (1957–1959) for tip-jet rotor architecture in passenger-transport configuration. Soviet government work, fully in the public domain.

**Sources:**

1. Mikheyev, Vadim. Mil M.L.: Helicopter Pioneer. Polygon, multiple editions.
2. Gunston, Bill. The Osprey Encyclopedia of Russian Aircraft. Osprey, 1995.

---

### 1959-06-15 — Kamov Ka-22 Vintokryl

- **id:** `kamov-ka-22-vintokryl`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Kamov Design Bureau (OKB-2)
- **disclosure citation:** Ka-22 Vintokryl first hover 1959-06-15; first transition flight 1961-08-12. Set FAI world records 1961-11-07 (speed 356.3 km/h, payload-to-altitude 16,485 kg). Documented in Mikheyev's history of Kamov design bureau and in FAI record archives.
- **disclosed subsystems:** `cert-experimental`, `lift-compound-rotorcraft`, `lift-tilt-rotor`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The Ka-22 Vintokryl is the Soviet contemporaneous answer to U.S. tilt-rotor demonstrators. Establishes Soviet-bloc prior art (1959–1961) for: (1) wingtip-mounted lift-rotor + cruise-propeller architecture (parallel to but predating Bell XV-3 and XV-15 in some configurations), (2) record-setting heavy-payload VTOL operation. Soviet design documentation, declassified in the post-1991 era, is in the public domain by virtue of being USSR state work. Provides invalidity anchor for tilt-rotor-with-cruise-propeller hybrid claims that try to assert novelty over the basic split-propulsion approach.

**Sources:**

1. Mikheyev, Vadim. OKB Kamov: 1948-1998. Polygon, 1999 (Russian).
2. Gordon, Yefim and Komissarov, Dmitriy. Soviet/Russian Aircraft Weapons Since World War II. Hikoki, 2004.
3. FAI World Record archive, file 1961-11-07.

---

### 1959-11-24 — Hiller X-18

- **id:** `hiller-x-18`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Hiller Aircraft / U.S. Air Force
- **disclosure citation:** Hiller X-18 first conventional flight 1959-11-24; first hover 1960-12-12. Program cancelled 1961 after 20 flights without achieving full transition due to engine and stability problems. USAF / Hiller Aircraft program. Documented in USAF Flight Test Center reports and NASA archives.
- **disclosed subsystems:** `lift-tilt-wing`, `transition-thrust-borne-to-wing-borne`, `lift-coaxial-rotor`, `cert-experimental`

**Prior art notes:**

> Hiller X-18 is the second tilt-wing aircraft to fly (after VZ-2, 1957) and the largest tilt-wing demonstrator before XC-142 (1964). Although the program ended without achieving full transition, the design disclosure is complete in USAF program documentation. Establishes prior art for: (1) twin-engine tilt-wing architecture at scale, (2) contra-rotating coaxial propellers in tilt-wing application. Combined with boeing-vertol-vz-2, ltv-xc-142, canadair-cl-84, and airbus-vahana, comprehensively places tilt-wing architecture in continuous prior-art coverage from 1957 forward.

**Sources:**

1. USAF Flight Test Center X-18 program reports.
2. Markman and Holder. Straight Up. Schiffer, 2000.
3. Hiller Aircraft Company archives, Hiller Aviation Museum.

---

### 1961-04-20 — Bell Rocket Belt

- **id:** `bell-rocket-belt`
- **corpus:** private
- **ip status:** patented
- **creator:** Bell Aerosystems / U.S. Army Transportation Research Command
- **disclosure citation:** Bell Rocket Belt first untethered free flight 1961-04-20 at Niagara Falls, by Harold M. Graham; demonstrated to U.S. Army at Fort Eustis 1961-06-08. Documented in U.S. Army Transportation Research Command test reports and Bell Aerosystems engineering reports.
- **disclosed subsystems:** `cert-experimental`, `lift-vectored-thrust`, `propulsion-tip-jet`

**Prior art notes:**

> The Bell Rocket Belt is the foundational disclosure of personal-scale VTOL flight. Wendell Moore's US Patent 3,243,144 has long expired, placing the basic personal rocket-belt architecture (twin-nozzle peroxide-decomposition, body-lean attitude control, hand-throttle thrust modulation) in the public domain. Establishes prior art for: (1) strap-on personal VTOL with cantilevered thrusters, (2) twist-grip vectoring for yaw, (3) body-lean attitude control. Anticipates: JetPack Aviation, Gravity Industries jet suit, Martin Aircraft Jetpack, Williams X-Jet, and any modern personal-VTOL claims relating to the strap-on form factor.

**Sources:**

1. Moore, Wendell F. US Patent 3,243,144 'Personal Propulsion Unit', 1966.
2. Bell Aerosystems Rocket Belt program reports, NARA.
3. Carlson, Steve. Bell Rocket Belt: A History. The Rocket Belt Convention, multiple editions.

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

### 1976-10-12 — Sikorsky S-72 RSRA

- **id:** `sikorsky-s-72-rsra`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Sikorsky Aircraft / NASA / U.S. Army
- **disclosure citation:** Sikorsky S-72 RSRA first flight 1976-10-12 at Sikorsky Stratford CT; delivered to NASA Ames 1976. Two prototypes built; flew through 1980s as test-bed for rotor system research. Documented in NASA technical reports.
- **disclosed subsystems:** `lift-compound-rotorcraft`, `cert-experimental`

**Prior art notes:**

> The Sikorsky S-72 RSRA is the foundational compound-rotorcraft research aircraft of the modern era — designed specifically as a platform to test alternative rotor systems and compound-rotorcraft configurations. Most significantly, the RSRA included a unique ejection capability for the entire rotor system (allowing the rotor to be jettisoned and the aircraft to land as a fixed-wing aircraft) — establishing prior art for: (1) compound-rotorcraft test platforms, (2) rotor-jettison emergency systems, (3) the research methodology that produced subsequent compound-rotorcraft (Sikorsky X2, S-97 Raider, SB>1 Defiant).

**Sources:**

1. NASA Technical Memoranda on RSRA, multiple 1977–1985.
2. Sikorsky Aircraft S-72 program archive.

---

### 1977-05-03 — Bell XV-15

- **id:** `bell-xv-15`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Bell Helicopter / NASA / U.S. Army
- **disclosure citation:** Bell XV-15 first hover flight 1977-05-03 at Bell Helicopter Arlington; first full transition 1979-07-24. Documented exhaustively in NASA SP-2000-4517, 'The History of the XV-15 Tilt Rotor Research Aircraft' (Maisel, Giulianetti, Dugan).
- **disclosed subsystems:** `cert-experimental`, `control-fly-by-wire-triplex`, `lift-tilt-rotor`, `transition-conversion-corridor`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The XV-15 is the foundational disclosure for the modern tilt-rotor architecture that now dominates the eVTOL air-taxi design space (Joby S4, Archer Midnight, Vertical VX4, Beta Alia tilt-cruise variants all descend from this geometry). Establishes prior art for: (1) wingtip-mounted gimbaled prop-rotor with cyclic and collective blade pitch, (2) the conversion-corridor envelope explicitly mapped and published by Bell/NASA, (3) cross-shafted twin-engine drive of dual prop-rotors with engine-out lift continuation, (4) coordinated nacelle tilt with thrust vector for transition control. Hundreds of NASA reports document the design completely. Filed against any post-1977 tilt-rotor patent claim, this entry is a canonical 102/103 anchor. The XV-15 directly precedes the V-22 Osprey (descended program) and the entire current generation of commercial eVTOL tilt-rotors.

**Sources:**

1. Maisel, Martin D., Giulianetti, Demo J., Dugan, Daniel C. The History of the XV-15 Tilt Rotor Research Aircraft: From Concept to Flight. NASA SP-2000-4517, 2000.
2. NASA TM-86680, NASA TM-86847, and many other XV-15 flight-test reports.
3. Bell Helicopter XV-15 program archives.

---

### 1989-04 — Moller Skycar M400

- **id:** `moller-skycar-m400`
- **corpus:** private
- **ip status:** patented
- **creator:** Moller International / Paul Moller
- **disclosure citation:** Moller Skycar M200X (predecessor) first tethered hover 1989-04; M400 design publicly disclosed 1990 with continuous development through 2010s; first untethered M400 flight 2003-04 (limited tethered hover to 5 m). Moller holds the largest single inventor's portfolio of VTOL flying-car patents (>40 issued patents 1965-2015).
- **disclosed subsystems:** `cert-experimental`, `lift-ducted-fan-array`, `lift-vectored-thrust`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Moller Skycar M400 is the foundational disclosure of the four-nacelle tilting-ducted-fan flying-car architecture. Although the M400 never achieved sustained free flight, Paul Moller's continuously-published patent portfolio (40+ issued US patents 1965-2015) constitutes the deepest single-inventor prior art base for VTOL flying-car designs. Establishes prior art for: (1) four-nacelle tilting-ducted-fan architecture, (2) Wankel rotary engine for VTOL propulsion, (3) clamshell thrust-vectoring deflectors. Most Moller patents have expired or are nearing expiration. Anticipates virtually every modern ducted-fan eVTOL (Lilium, AutoFlight, etc.) on architectural primitives.

**Sources:**

1. Moller, Paul S. Multiple US patents 1965-2015, USPTO archive.
2. Moller, Paul. Skycar: The Air Car of the Future. Davis, 1996 (self-published).
3. Aviation Week and Popular Science coverage 1989-2010.

---

### 2008-07-29 — Martin Aircraft Jetpack

- **id:** `martin-aircraft-jetpack`
- **corpus:** private
- **ip status:** patented
- **creator:** Martin Aircraft Company (Christchurch, New Zealand)
- **disclosure citation:** Martin Jetpack publicly unveiled 2008-07-29 at AirVenture Oshkosh, US; FAA approved as 'experimental category' aircraft 2010-08-22; first untethered piloted free-flight 2011-04-29. Glenn Martin holds NZ and US patents on the ducted-fan dual-rotor jetpack architecture.
- **disclosed subsystems:** `cert-experimental`, `lift-ducted-fan-array`, `lift-vectored-thrust`

**Prior art notes:**

> Martin Jetpack is New Zealand's foundational disclosure of long-endurance personal-VTOL flight. Architecturally distinct from Bell Rocket Belt (rockets, 21 sec) and Gravity Industries (turbojets, 10 min) by using twin large ducted fans for ~30 min endurance. Establishes prior art for: (1) twin-ducted-fan personal-VTOL strap-on, (2) cyclic-pitch fan attitude control distinct from differential thrust, (3) FAA experimental-category personal jetpack certification basis. Glenn Martin's patents (NZ 539537, US 7,484,687) cover the architecture; some now expired.

**Sources:**

1. Martin, Glenn. NZ Patent 539537, 2009.
2. Martin, Glenn. US Patent 7,484,687, 2009.
3. Martin Aircraft Company press releases and SEC filings (NZX, 2015 IPO).

---

### 2009-12-21 — Urban Aeronautics CityHawk

- **id:** `urban-aero-cityhawk`
- **corpus:** private
- **ip status:** patented
- **creator:** Urban Aeronautics Ltd (Yavne, Israel)
- **disclosure citation:** Urban Aeronautics' X-Hawk / AirMule first untethered hover 2009-12-21 at Megiddo airfield, Israel; CityHawk civil variant unveiled 2018-02-08. Urban Aeronautics holds the Fancraft / fuselage-internal-rotor patent family (US 7,789,342 et seq., filed early 2000s).
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-experimental`, `lift-ducted-fan-array`, `lift-vectored-thrust`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Urban Aeronautics CityHawk / Cormorant establishes Israeli prior-art lineage for ducted-fan internal-rotor VTOL ('Fancraft'). The fuselage-internal lift-fan architecture is uncommon and relatively narrowly patented by Urban Aeronautics. Cormorant (military cargo variant) completed Israeli Defense Forces evaluation 2016. Establishes prior art for: (1) fuselage-internal ducted lift fan, (2) cascade-vane deflection for attitude control in lieu of differential rotor thrust, (3) compact urban-VTOL form factor without exposed rotors. Anticipates modern claims around safety-margin-improvement via internal rotors.

**Sources:**

1. Yoeli, Rafi. US Patent 7,789,342, 'VTOL Aircraft Having Deployable Wings,' 2010.
2. Urban Aeronautics technical white papers and press releases 2009–2020.
3. Israel Aerospace Industries / IDF Cormorant evaluation reports (declassified excerpts).

---

### 2011-03-22 — Festo SmartBird

- **id:** `festo-smartbird`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Festo AG & Co. KG / Bionic Learning Network
- **disclosure citation:** Festo SmartBird publicly unveiled 2011-03-22 at TED Conference, Edinburgh; subsequently demonstrated at Hannover Messe 2011. Festo Bionic Learning Network technical white papers and design notes publicly released.
- **disclosed subsystems:** `cert-experimental`

**Prior art notes:**

> Festo SmartBird is the canonical modern engineering disclosure of controlled-flapping-wing flight. Establishes prior art for: (1) single-motor articulated-flapping-wing actuation, (2) active-twist wing control with embedded actuators, (3) lifelike biomimetic flapping-wing VTOL/STOL flight. Combined with laputa-flapter (1986 fictional), provides joint engineering+narrative prior-art base for any flapping-wing or ornithopter claim.

**Sources:**

1. Festo Bionic Learning Network 'SmartBird' technical disclosure, 2011.
2. Send, R. and Festo team. 'SmartBird Aerodynamic Concept.' SAE technical paper, 2012.
3. Festo TED Talk and Hannover Messe demonstration materials.

---

### 2011-06-13 — D-Dalus (IAT-21)

- **id:** `d-dalus`
- **corpus:** academic
- **ip status:** patented
- **creator:** IAT-21 / Innovative Aeronautical Technologies (Linz, Austria)
- **disclosure citation:** D-Dalus prototype publicly unveiled 2011-06-13 at Paris Air Show; co-developed with Sikorsky / United Technologies. Cycloidal rotor patents held by IAT-21 and earlier inventors (cf. Pateras Pescara's 1928 Italian and French cyclogiro patents — the cyclorotor concept originated with Pescara nearly a century earlier).
- **disclosed subsystems:** `cert-experimental`, `lift-cyclorotor`

**Prior art notes:**

> D-Dalus is the modern Austrian disclosure of cycloidal-rotor (cyclogiro) VTOL — a niche but distinct architecture that traces back to Pateras Pescara's 1928 cyclogiro patents. Establishes prior art for: (1) the cyclorotor lift architecture in modern technical literature, (2) omnidirectional thrust vectoring via azimuthal blade-pitch modulation. Pescara's foundational cyclogiro patents are long expired, placing the basic cyclorotor concept in the public domain. Anticipates modern exotic-VTOL claims (occasionally surfacing in cycloidal-fan or barrel-rotor patent filings) asserting novelty over the cyclorotor architecture.

**Sources:**

1. IAT-21 / Innovative Aeronautical Technologies disclosures 2011.
2. Sikorsky / United Technologies cyclorotor research publications.
3. Pescara, Raúl. Italian Patent on cyclogiro, 1928.
4. Hwang, Heng et al. 'Numerical Investigation of Cyclorotor Aerodynamics.' AIAA papers.

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

### 2017-04-20 — Gravity Industries Jet Suit

- **id:** `gravity-industries-jet-suit`
- **corpus:** private
- **ip status:** patented
- **creator:** Gravity Industries Ltd / Richard Browning
- **disclosure citation:** Gravity Industries Daedalus Mark 1 jet suit publicly demonstrated by Richard Browning 2017-04-20 (TED Talk, Vancouver); set Guinness world record fastest body-controlled jet suit 2019-11-12 (85.06 mph). Multiple subsequent public displays 2017–2024.
- **disclosed subsystems:** `cert-experimental`, `lift-vectored-thrust`, `propulsion-tip-jet`

**Prior art notes:**

> Gravity Industries Daedalus jet suit establishes the modern British iteration of Bell Rocket Belt prior art — the multi-turbojet body-mounted personal-flight architecture. Adds 50+ years of incremental disclosure to the personal-VTOL design space, with arm-mounted thrust effectors as primary control distinguishing from Bell's hand-throttle. Filed against any modern personal-flight patent attempt asserting novelty over body-mounted multi-turbojet architecture, this entry combined with bell-rocket-belt is anticipating prior art.

**Sources:**

1. Browning, Richard. TED Talk 'How I built a jet suit,' April 2017.
2. Browning, Richard. Taking on Gravity. Bantam Press, 2019.
3. Gravity Industries press materials and patent filings.
4. Guinness World Records archive 2019-11-12.

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

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `b4393b4`.*
