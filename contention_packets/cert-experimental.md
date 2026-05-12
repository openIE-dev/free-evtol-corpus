---
title: "cert-experimental"
parent: "Invalidity Contentions"
nav_order: 8
layout: default
---

# Invalidity Contention Packet — `cert-experimental`

**Generated:** 2026-05-12  
**Cross-cut tag:** `cert-experimental`  
**Entries:** 70 (70 commons-grade, 0 draft)  
**Earliest disclosure:** 1907-11-13  
**Most recent disclosure:** 2024-04-25

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

### 1917-02 — Curtiss Autoplane

- **id:** `curtiss-autoplane`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Glenn Curtiss / Curtiss Aeroplane and Motor Company
- **disclosure citation:** Glenn Curtiss exhibited the Autoplane at the Pan-American Aeronautical Exposition, New York, February 1917. A three-seat aluminium car body with detachable triplane wings and a four-blade pusher propeller; it made short hops but never sustained flight before the U.S. entry into WWI ended the project. The first serious attempt at a roadable aircraft. Documented in Curtiss company records and Smithsonian collections.
- **disclosed subsystems:** `cert-experimental`

**Prior art notes:**

> The Curtiss Autoplane (1917) is the foundational disclosure of the roadable-aircraft / drive+fly transformer concept — a road automobile with detachable wings and a pusher propeller. Although it only made short hops, the engineering disclosure (detachable wing assembly, belt-driven pusher, dual-use chassis) is documented in Curtiss company records. Glenn Curtiss's 1917 patents are long expired. Combined with waterman-aerobile (1937), fulton-airphibian (1946), taylor-aerocar (1949), terrafugia-transition (2009), and the modern drive+fly cluster (Klein Vision, AeroMobil, ASKA, PAL-V, Alef), comprehensively places drive+fly transformer architecture in a century-spanning public-domain prior-art base from 1917 forward.

**Sources:**

1. Curtiss Aeroplane and Motor Company records, Smithsonian National Air and Space Museum.
2. Roseberry, C.R. Glenn Curtiss: Pioneer of Flight. Doubleday, 1972.
3. Pan-American Aeronautical Exposition catalogue, New York, 1917.

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

### 1922 — Kirsten-Boeing cyclogiro

- **id:** `kirsten-boeing-cyclogiro`
- **corpus:** academic
- **ip status:** patented
- **creator:** Frederick Kirsten / University of Washington / Boeing Airplane Company
- **disclosure citation:** Frederick Kirsten (University of Washington, later consulting for Boeing) developed the cyclogiro — a cycloidal-rotor propulsion/lift device — from the early 1920s; a 1922-1933 program produced wind-tunnel models and design studies for a cyclogiro aircraft, with Boeing involvement. Kirsten holds foundational US cyclogiro patents. Documented in NACA technical reports and University of Washington / Boeing archives.
- **disclosed subsystems:** `lift-cyclorotor`, `cert-experimental`

**Prior art notes:**

> The Kirsten-Boeing cyclogiro program (Frederick Kirsten, University of Washington / Boeing, 1922-1933) is the foundational US disclosure of the cyclogiro / cyclorotor lift architecture — barrel rotors with cyclically-pitched airfoil blades giving omnidirectional in-plane thrust. Kirsten's 1920s-1930s patents are long expired. Together with the Pescara cyclogiro patents (1928), d-dalus (2011), and cyclotech-cruiseup (2022), comprehensively places cyclorotor architecture in a century-spanning public-domain prior-art base from 1922 forward. Notably, Kirsten's work is contemporaneous with the de Bothezat quadrotor and Pescara helicopter — 1922 is a remarkably productive year for the foundational rotorcraft prior-art base.

**Sources:**

1. Kirsten, F.K. NACA Technical Notes on the cyclogiro, 1920s-1930s.
2. Kirsten, Frederick. Cyclogiro patents, USPTO, 1920s-1930s.
3. Wheatley, J.B. 'Simplified Aerodynamic Analysis of the Cyclogiro Rotating-Wing System.' NACA TN 467, 1933.
4. University of Washington / Boeing Airplane Company archives.

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

### 1937-02-21 — Waterman Arrowbile / Aerobile

- **id:** `waterman-aerobile`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Waldo Waterman
- **disclosure citation:** Waldo Waterman's Arrowbile first flight 1937-02-21 at Santa Monica CA; developed from his tailless 'Whatsit' (1932), it was a tailless flying wing with a detachable wing and a Studebaker engine, able to drive on roads. Five built; one survives at the Smithsonian as the 'Aerobile'. The first roadable aircraft to repeatedly fly and drive. Documented in Smithsonian collections and Waterman's autobiography.
- **disclosed subsystems:** `cert-experimental`

**Prior art notes:**

> Waldo Waterman's Arrowbile/Aerobile (1937) is the foundational disclosure of the practical roadable aircraft — a tailless flying wing with detachable wing and dual-use automobile engine that demonstrated repeated flight and road operation. Establishes prior art for: (1) tailless-flying-wing roadable aircraft, (2) shared automobile engine for flight and road drive. Waterman's 1930s patents are long expired. Together with curtiss-autoplane (1917), fulton-airphibian (1946), and taylor-aerocar (1949), places early roadable-aircraft architecture comprehensively in the public domain.

**Sources:**

1. Waterman, Waldo. Waldo: Pioneer Aviator. Arsdalen Bosch, 1988.
2. Smithsonian National Air and Space Museum, Waterman Aerobile collection.

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

### 1947-12-07 — Fairey Gyrodyne / Jet Gyrodyne

- **id:** `fairey-gyrodyne`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Fairey Aviation Company
- **disclosure citation:** Fairey FB-1 Gyrodyne first flight 1947-12-07; set an FAI helicopter speed record 1948-06-28 (124 mph). The Jet Gyrodyne (a modified Gyrodyne with tip-jet rotor drive, 1954) was the direct technology demonstrator for the Fairey Rotodyne. Documented in Fairey company archives and UK Ministry of Supply reports.
- **disclosed subsystems:** `lift-compound-rotorcraft`, `lift-tip-jet-rotor`, `cert-experimental`

**Prior art notes:**

> The Fairey Gyrodyne (1947) and Jet Gyrodyne (1954) are the foundational UK compound-autogyro disclosures that led to the Fairey Rotodyne (1957). Establishes prior art for: (1) compound autogyro/helicopter with stub-wing tractor propeller providing both forward thrust and anti-torque (no tail rotor), (2) tip-jet rotor drive in a compound rotorcraft (the Jet Gyrodyne, 1954). UK Ministry of Supply public-domain disclosure. Together with cierva-autogyro (1923), fairey-rotodyne (1957), eurocopter-x3 (2010), and the modern compound-rotorcraft cluster, places compound-rotorcraft architecture in continuous prior art.

**Sources:**

1. Fairey Aviation Company Gyrodyne / Jet Gyrodyne archives.
2. UK Ministry of Supply Gyrodyne test reports.
3. Wood, Derek. Project Cancelled. Macdonald & Jane's, 1975.

---

### 1954-11 — Bell ATV (Air Test Vehicle)

- **id:** `bell-atv`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Bell Aircraft Corporation / U.S. Air Force
- **disclosure citation:** Bell ATV (Air Test Vehicle, Model 65) first tethered hover November 1954; first transition to horizontal flight 1955. A small demonstrator with two tilting turbojets on the wings plus a fixed vertical lift jet — Bell's first VTOL transition aircraft, the stepping stone toward the XV-3 tilt-rotor. Documented in USAF Flight Test Center reports and Bell Aircraft archives.
- **disclosed subsystems:** `lift-tilt-rotor`, `lift-vectored-thrust`, `transition-thrust-borne-to-wing-borne`, `cert-experimental`

**Prior art notes:**

> The Bell ATV (Air Test Vehicle, 1954) is Bell Aircraft's first VTOL transition aircraft — wingtip-mounted tilting turbojets plus a fixed lift jet — and the experimental basis for the Bell XV-3 tilt-rotor (1955). Establishes prior art for: (1) wingtip-mounted tilting propulsors for VTOL transition (the tilt-rotor architectural concept in tilt-jet form), (2) combined wingtip-tilt + fixed-lift-jet hover augmentation. Together with bell-xv-3 (1955), bell-xv-15 (1977), v-22-osprey (1989), and the modern tilt-rotor cluster, places the wingtip-tilting-propulsor architecture in continuous public-domain prior art from 1954 forward.

**Sources:**

1. USAF Flight Test Center Bell ATV reports.
2. Bell Aircraft Corporation Model 65 program archives.
3. Markman and Holder. Straight Up. Schiffer, 2000.

---

### 1955-01 — de Lackner HZ-1 Aerocycle

- **id:** `de-lackner-hz-1-aerocycle`
- **corpus:** academic
- **ip status:** patented
- **creator:** de Lackner Helicopters Inc / U.S. Army
- **disclosure citation:** de Lackner HZ-1 Aerocycle first tethered flights January 1955; first free flight 1955-11. U.S. Army Transportation Research Command program; cancelled 1956 after instability and rotor-strike concerns. Documented in TRC test reports and Smithsonian collections.
- **disclosed subsystems:** `lift-coaxial-rotor`, `lift-distributed-electric-propulsion`, `cert-experimental`

**Prior art notes:**

> The de Lackner HZ-1 Aerocycle is the open-rotor counterpart to the Hiller VZ-1 Pawnee — a standing personal-platform with coaxial counter-rotating open rotors below the pilot, controlled by leaning. Establishes prior art for: (1) the open-rotor personal flying-platform / 'flying motorcycle' architecture, (2) handlebar-and-lean control of a personal VTOL. Combined with hiller-vz-1-pawnee (1955, ducted-fan variant) and aerofex-aero-x (2008, modern hover bike), places personal-platform VTOL in continuous public-domain prior art.

**Sources:**

1. U.S. Army Transportation Research Command HZ-1 Aerocycle reports.
2. Markman and Holder. Straight Up. Schiffer, 2000.
3. Smithsonian / U.S. Army Transportation Museum HZ-1 collection.

---

### 1955-02 — Hiller VZ-1 Pawnee

- **id:** `hiller-vz-1-pawnee`
- **corpus:** academic
- **ip status:** patented
- **creator:** Hiller Aircraft / U.S. Army / Office of Naval Research
- **disclosure citation:** Hiller VZ-1 Pawnee (originally ONR-funded 'Flying Platform') first tethered hover early 1955; first free flight 1955-04. Office of Naval Research / U.S. Army Transportation Research Command program. Documented in ONR / TRC test reports and Hiller Aviation Museum collections.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `cert-experimental`

**Prior art notes:**

> Hiller VZ-1 Pawnee is the foundational disclosure of the standing ducted-fan personal flying-platform architecture with kinesthetic (body-weight-shift) control. Establishes prior art for: (1) counter-rotating ducted lift fans in a personal-scale platform, (2) kinesthetic attitude control (the lean-to-steer paradigm later used by hover bikes and the Pivotal/Opener tail-sitter), (3) the duct-as-structure design. Hiller's 1950s ducted-fan patents are long expired. Combined with de-lackner-hz-1-aerocycle (1955), williams-x-jet (1982), and solotrek-xfv (2001), comprehensively places ducted-fan personal-platform VTOL in continuous public-domain prior art from 1955 forward.

**Sources:**

1. Office of Naval Research / U.S. Army Transportation Research Command VZ-1 reports.
2. Markman and Holder. Straight Up. Schiffer, 2000.
3. Hiller Aviation Museum VZ-1 collection.

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

### 1959 — Vanguard Omniplane

- **id:** `vanguard-omniplane`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Vanguard Air and Marine Corporation / U.S. Army
- **disclosure citation:** Vanguard Omniplane first tethered hover 1959; never achieved free flight or transition (gearbox failure during testing, program ended ~1962). A small VTOL with two ducted lift fans buried in the wings plus a pusher propeller. Documented in U.S. Army TRC reports and Smithsonian collections.
- **disclosed subsystems:** `lift-ducted-fan-array`, `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `cert-experimental`

**Prior art notes:**

> The Vanguard Omniplane (1959) is an early disclosure of the 'fan-in-wing' VTOL architecture — ducted lift fans embedded inside the wing structure, covered by louvres in cruise, with a separate pusher propeller for forward flight. Establishes prior art for: (1) fan-in-wing embedded lift fans, (2) louvre-covered lift fans for cruise drag reduction, (3) the mode-shutdown transition (lift fans off in cruise, pusher provides thrust). Although the program failed mechanically, the design disclosure is complete in U.S. Army documentation. Anticipates the Ryan XV-5 Vertifan (1964) and modern fan-in-wing eVTOL (Horizon Aircraft Cavorite X5). Together with the lift+cruise cluster, places mode-shutdown / fan-in-wing architecture in public-domain prior art.

**Sources:**

1. U.S. Army Transportation Research Command Vanguard Omniplane reports.
2. Markman and Holder. Straight Up. Schiffer, 2000.
3. Smithsonian National Air and Space Museum, Vanguard Omniplane collection.

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

### 1963-11-20 — Curtiss-Wright X-19

- **id:** `curtiss-wright-x-19`
- **corpus:** academic
- **ip status:** patented
- **creator:** Curtiss-Wright Corporation / U.S. Army / U.S. Air Force / U.S. Navy
- **disclosure citation:** Curtiss-Wright X-19 first flight 1963-11-20 (the predecessor X-100 demonstrator first flew 1959); program ended 1965 after a crash. A four-propeller 'radial-lift-force' tilt-prop VTOL using Curtiss-Wright's patented radial-force propeller. Tri-Service program. Documented in NASA and U.S. military test reports.
- **disclosed subsystems:** `lift-tilt-rotor`, `transition-thrust-borne-to-wing-borne`, `cert-experimental`

**Prior art notes:**

> The Curtiss-Wright X-19 (1963; predecessor X-100, 1959) is the foundational disclosure of the four-propeller tandem-wing tilt-prop VTOL — four propellers at the tips of fore-and-aft wings, each tilting between vertical and horizontal, cross-shafted to two engines. Establishes prior art for: (1) the four-rotor tandem-wing tilt-prop configuration (distinct from the two-rotor tilt-rotor and the tilt-wing), (2) the 'radial lift force' propeller concept, (3) cross-shafted four-rotor tilt VTOL. Curtiss-Wright's 1950s-60s patents are expired. Together with bell-xv-3, ltv-xc-142, bell-x-22, and the modern multi-rotor tilt eVTOL cluster (Joby S4, Archer Midnight, TCab E20, Geely Aerofugia, Vertical VX4, Hyundai Supernal), comprehensively places multi-rotor tilt VTOL architecture in public-domain prior art from 1959 forward.

**Sources:**

1. NASA / U.S. military X-19 / X-100 test reports.
2. Curtiss-Wright radial-lift-force propeller patents, USPTO.
3. Markman and Holder. Straight Up. Schiffer, 2000.

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

### 1986-12-02 — Sikorsky/DARPA X-Wing

- **id:** `sikorsky-x-wing`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Sikorsky Aircraft / NASA / DARPA / U.S. Army
- **disclosure citation:** RSRA/X-Wing technology demonstrator first flight (fixed-wing mode, rotor stopped) 1986-12-02 at NASA Ames; program cancelled 1988 before in-flight rotor stop/start was demonstrated. Built on the Sikorsky S-72 RSRA airframe with a four-bladed rigid rotor that could be stopped in flight to act as an X-shaped fixed wing. Documented in NASA / DARPA technical reports.
- **disclosed subsystems:** `lift-compound-rotorcraft`, `transition-mode-shutdown`, `cert-experimental`

**Prior art notes:**

> The Sikorsky/DARPA X-Wing (RSRA-based, 1986) is the foundational disclosure of the stopped-rotor / rotor-wing architecture: a rigid rotor with circulation control that spins for hover, then stops to act as a fixed X-shaped wing for high-speed cruise. Establishes prior art for: (1) stoppable-in-flight rigid rotor that doubles as a fixed wing, (2) circulation-control (blown) rotor blades enabling lift across the full azimuth, (3) the rotor-stop-and-restart transition concept. Although in-flight rotor stop was never demonstrated before cancellation, the design disclosure is complete in NASA/DARPA documentation. Anticipates: any modern eVTOL claim involving stoppable lift rotors that become fixed lifting surfaces (a recurring concept in high-speed-cruise VTOL proposals).

**Sources:**

1. NASA Technical Memoranda on RSRA/X-Wing, multiple 1984-1988.
2. Sikorsky Aircraft X-Wing program archive.
3. DARPA X-Wing program reports, DTIC.

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

### 1998-09 — CarterCopter / Carter PAV

- **id:** `cartercopter`
- **corpus:** private
- **ip status:** patented
- **creator:** Carter Aviation Technologies (Wichita Falls, Texas) / Jay Carter Jr
- **disclosure citation:** Carter Aviation Technologies' CarterCopter Technology Demonstrator first flight September 1998; achieved 'Mu-1' (rotor advance ratio of 1.0 — flying as fast as the rotor tips advance, the holy grail of slowed-rotor compounds) on 2005-06-17, a documented first. The Carter PAV (Personal Air Vehicle) followed (2011). Carter's slowed-rotor technology was later licensed to Jaunt Air Mobility for an eVTOL. Documented in Carter Aviation technical papers and patents.
- **disclosed subsystems:** `lift-compound-rotorcraft`, `cert-experimental`

**Prior art notes:**

> The CarterCopter / Carter PAV (Carter Aviation, 1998-2011) is the foundational modern disclosure of 'Slowed Rotor/Compound' (SR/C) technology — a high-inertia rotor that spins fast for jump-takeoff (stored kinetic energy), then is dramatically slowed in cruise while a wing carries lift and a pusher provides thrust, reaching rotor advance ratios > 1.0 (the 'Mu-1' milestone, documented 2005). Establishes prior art for: (1) high-inertia jump-takeoff rotor, (2) dramatic rotor-RPM reduction in cruise (slowed-rotor compound), (3) the wing-offloads-rotor-in-cruise compound architecture. Carter's SR/C patents were licensed to Jaunt Air Mobility for an eVTOL. Together with autogyro/compound anchors (Cierva 1923, Fairey Gyrodyne 1947, Fairey Rotodyne 1957), karem-ar40 (2008, optimum-speed rotor), jaunt-air-mobility (2019), and overair-butterfly (2020), comprehensively places slowed-rotor / variable-RPM-rotor compound architecture in public-domain and licensed prior art.

**Sources:**

1. Carter Aviation Technologies SR/C technical papers, AHS/VFS Forums 1998-2020.
2. Carter, Jay Jr. Slowed Rotor/Compound patents, USPTO.
3. FAI / AHS documentation of the CarterCopter Mu-1 milestone, 2005-06-17.

---

### 2001-12-17 — SoloTrek XFV / Trek Aerospace Springtail

- **id:** `solotrek-xfv`
- **corpus:** private
- **ip status:** patented
- **creator:** Millennium Jet / Trek Aerospace / NASA / DARPA
- **disclosure citation:** Millennium Jet SoloTrek XFV first tethered hover 2001-12-17; developed under NASA and DARPA contracts. Renamed Springtail Exoskeleton Flying Vehicle by successor Trek Aerospace ~2003. Documented in NASA / DARPA technical reports and Trek Aerospace patent filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `cert-experimental`

**Prior art notes:**

> SoloTrek XFV / Springtail establishes prior art for the back-worn ducted-fan exoskeleton flying vehicle — twin shoulder-mounted ducted lift fans on a wearable frame. Establishes prior art for: (1) exoskeleton-mounted ducted-fan personal VTOL, (2) the upright-pilot-in-wearable-frame architecture, (3) single-engine belt-driven dual-fan personal VTOL. Combined with hiller-vz-1-pawnee, williams-x-jet, gravity-industries-jet-suit, martin-aircraft-jetpack, and iron-man-suit (fictional), comprehensively places personal-VTOL exoskeleton/platform architecture in 1955-2017 prior art.

**Sources:**

1. NASA / DARPA SoloTrek XFV technical reports.
2. Trek Aerospace Springtail patent filings, USPTO.
3. Popular Science and Aviation Week coverage 2001-2003.

---

### 2005-07 — TU Delft DelFly

- **id:** `tu-delft-delfly`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Delft University of Technology Micro Air Vehicle Lab (Guido de Croon / GertJan van der Wijngaart)
- **disclosure citation:** TU Delft DelFly first flight July 2005 (a student project that became the long-running DelFly programme); DelFly Micro (2008) set a Guinness record as the smallest camera-equipped flapping-wing MAV (3 g); DelFly Nimble (2018, published in Science) demonstrated insect-like agile manoeuvres. Documented in TU Delft MAV Lab publications, including Karásek, M. et al. 'A tailless aerial robotic flapper reveals that flies use torque coupling in rapid banked turns,' Science 361(6407), 2018.
- **disclosed subsystems:** `cert-experimental`

**Prior art notes:**

> The TU Delft DelFly programme (2005-present) is the longest-running academic disclosure of flapping-wing micro air vehicles — including the clap-and-fling X-wing flapping mechanism, the camera-equipped 3-gram DelFly Micro (2008), and the tailless flight-kinematics-only controlled DelFly Nimble (2018, published in Science). Establishes Dutch prior art for: (1) clap-and-fling flapping-wing lift, (2) tailless flapping-wing attitude control via kinematics modulation, (3) camera-carrying insect-scale flapping MAVs. Together with festo-smartbird (2011), aerovironment-nano-hummingbird (2011), harvard-robobee (2013), da-vinci-ornithopter (1485 sketches), laputa-flapter (1986 fictional), and dune-ornithopter (1965 fictional), comprehensively places flapping-wing flight architecture in deep cross-disciplinary prior art. Adds Netherlands depth alongside PAL-V (Dutch flying car).

**Sources:**

1. Karásek, M., Muijres, F.T., De Wagter, C., Remes, B.D.W., de Croon, G.C.H.E. 'A tailless aerial robotic flapper reveals that flies use torque coupling in rapid banked turns.' Science 361(6407), 2018.
2. De Croon, G.C.H.E. et al. 'Design, aerodynamics, and vision-based control of the DelFly.' International Journal of Micro Air Vehicles 1(2), 2009.
3. TU Delft Micro Air Vehicle Lab publications archive.

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

### 2010-09-06 — Eurocopter X3

- **id:** `eurocopter-x3`
- **corpus:** private
- **ip status:** patented
- **creator:** Eurocopter (later Airbus Helicopters)
- **disclosure citation:** Eurocopter X3 first flight 2010-09-06 at Istres, France; set an unofficial rotorcraft speed record of 472 km/h (255 kt) in level flight 2013-06-07. The X3 demonstrated the compound-helicopter architecture (main rotor + wing-mounted forward-thrust propellers) as a practical high-speed configuration. Documented in Eurocopter / Airbus Helicopters technical papers and AHS/VFS Forum publications.
- **disclosed subsystems:** `lift-compound-rotorcraft`, `cert-experimental`

**Prior art notes:**

> The Eurocopter X3 establishes French/European prior art for the modern compound-helicopter architecture: a single main rotor for lift plus wing-mounted forward-thrust propellers that also provide anti-torque via differential thrust (no tail rotor). The 472 km/h speed record (2013) demonstrated the configuration's high-speed capability. Establishes prior art for: (1) main-rotor + wing-mounted lateral-propeller compound architecture, (2) differential-lateral-propeller-thrust anti-torque (replacing the tail rotor), (3) wing-offloading of the main rotor in cruise. Direct ancestor of the Airbus RACER (2022). Together with fairey-rotodyne (1957), sikorsky-boeing-defiant (2019), sikorsky-s-97-raider (2015), and airbus-racer (2022), comprehensively places compound-rotorcraft architecture in prior art.

**Sources:**

1. Eurocopter / Airbus Helicopters X3 technical papers, AHS/VFS Forums 2011-2015.
2. Fédération Aéronautique Internationale records / Airbus speed-record documentation 2013.

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

### 2013-05-02 — Harvard RoboBee

- **id:** `harvard-robobee`
- **corpus:** academic
- **ip status:** patented
- **creator:** Harvard Microrobotics Laboratory / Wyss Institute (Robert Wood)
- **disclosure citation:** Harvard RoboBee first controlled flight reported in Ma, Kevin Y.; Chirarattananon, Pakpong; Fuller, Sawyer B.; Wood, Robert J. 'Controlled Flight of a Biologically Inspired, Insect-Scale Robot.' Science 340(6132), 2013-05-02. Subsequent milestones: RoboBee that perches via electrostatic adhesion (2016), RoboBee that swims and flies (2017), and the solar-powered tetherless RoboBee X-Wing (2019, Nature). Harvard Microrobotics Lab / Wyss Institute.
- **disclosed subsystems:** `cert-experimental`

**Prior art notes:**

> The Harvard RoboBee (Wood lab / Wyss Institute, Science 2013) is the foundational disclosure of insect-scale flapping-wing flight — wings driven by piezoelectric bending actuators at ~120 Hz, attitude controlled by wing-kinematics modulation, structure built by pop-up MEMS lamination. Establishes prior art for: (1) piezoelectric-actuated insect-scale flapping flight, (2) pop-up MEMS aerial-robot fabrication, (3) the smallest controlled flying robot. Subsequent RoboBee variants added perching, swimming, and solar-powered tetherless flight. Together with tu-delft-delfly, festo-smartbird, aerovironment-nano-hummingbird, and the historical/fictional flapping-wing anchors, comprehensively places flapping-wing flight architecture across scales from insect (RoboBee) to bird (SmartBird, Nano Hummingbird) to human (da Vinci sketches, Dune/Laputa fictional) in deep prior art.

**Sources:**

1. Ma, K.Y., Chirarattananon, P., Fuller, S.B., Wood, R.J. 'Controlled Flight of a Biologically Inspired, Insect-Scale Robot.' Science 340(6132), 2013.
2. Jafferis, N.T., Helbling, E.F., Karpelson, M., Wood, R.J. 'Untethered flight of an insect-sized flapping-wing microscale aerial vehicle.' Nature 570, 2019.
3. Harvard Microrobotics Laboratory / Wyss Institute publications archive.

---

### 2013-09-05 — Aeros Aeroscraft / Dragon Dream

- **id:** `aeros-aeroscraft-dragon-dream`
- **corpus:** private
- **ip status:** patented
- **creator:** Aeros (Aeros Corporation / Worldwide Aeros Corp) / Igor Pasternak
- **disclosure citation:** Aeros 'Dragon Dream' (a ~79 m sub-scale demonstrator of the planned Aeroscraft ML866) first untethered flight 2013-09-05 at Tustin CA (inside a former blimp hangar). Aeros (Igor Pasternak) develops rigid variable-buoyancy airships using 'Control Of Static Heaviness' (COSH) to take off and land vertically without ballast exchange. Documented in Aeros materials, U.S. DARPA/Defense Department reports, and FAA filings.
- **disclosed subsystems:** `lift-buoyant-hybrid`, `lift-distributed-electric-propulsion`, `propulsion-hybrid-series`, `cert-experimental`

**Prior art notes:**

> The Aeros Aeroscraft / Dragon Dream (2013) establishes prior art for the variable-buoyancy VTOL airship — a rigid airship with 'Control Of Static Heaviness' (COSH): helium is compressed/released to shift between heavier-than-air (landing) and lighter-than-air (takeoff), enabling controlled vertical takeoff/landing without ballast exchange. Establishes prior art for: (1) variable-buoyancy / COSH airship control, (2) ballast-free vertical-takeoff airship operation, (3) rigid-frame heavy-lift airship with vectored hybrid propulsion. Together with lta-research-pathfinder-1 (2023), hybrid-air-vehicles-airlander-10 (2012), and flying-whales-lca60t (2012), comprehensively places the modern buoyant-hybrid / VTOL-airship architecture in public-domain prior art.

**Sources:**

1. Aeros / Worldwide Aeros Corp technical materials and press releases 2010-2024.
2. U.S. DARPA / Defense Department Aeroscraft (Walrus / Pelican) program reports.
3. Aeros / Igor Pasternak COSH patents, USPTO.
4. Dragon Dream first flight, Tustin CA, 2013-09-05.

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

### 2014-09 — EPFL GimBall

- **id:** `epfl-gimball`
- **corpus:** academic
- **ip status:** patented
- **creator:** EPFL Laboratory of Intelligent Systems (Dario Floreano) / Adrien Briod (later Flyability SA)
- **disclosure citation:** Briod, Adrien; Kornatowski, Przemyslaw; Zufferey, Jean-Christophe; Floreano, Dario. 'A Collision-resilient Flying Robot.' Journal of Field Robotics 31(4), 2014. EPFL Laboratory of Intelligent Systems; won the UAE Drones for Good Award 2015; commercialized as Flyability Elios via the Flyability SA spinout.
- **disclosed subsystems:** `airframe-collision-resilient-cage`, `lift-coaxial-rotor`, `lift-distributed-electric-propulsion`, `cert-experimental`

**Prior art notes:**

> EPFL's GimBall (Briod, Kornatowski, Zufferey, Floreano, JFR 2014) is the foundational disclosure of the gimbaled protective-cage flying-robot architecture — a freely-rotating outer cage that decouples collision impacts from the inner flight system, enabling collision-tolerant flight. Establishes prior art for: (1) rotating protective-cage airframe geometry, (2) collision-tolerant operation enabling contact-based maneuvers (including docking). The protective-cage concept is directly antecedent to ModQuad's cuboid-frame docking architecture. Commercialized as Flyability Elios for industrial confined-space inspection.

**Sources:**

1. Briod, A., Kornatowski, P., Zufferey, J.-C., Floreano, D. 'A Collision-resilient Flying Robot.' Journal of Field Robotics 31(4), 2014.
2. EPFL Laboratory of Intelligent Systems publications archive.
3. Flyability SA technical materials.

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

### 2016-05 — ETH Omnicopter

- **id:** `eth-omnicopter`
- **corpus:** academic
- **ip status:** patented
- **creator:** ETH Zurich Institute for Dynamic Systems and Control (Raffaello D'Andrea) / Dario Brescianini
- **disclosure citation:** Brescianini, Dario; D'Andrea, Raffaello. 'Design, modeling and control of an omni-directional aerial vehicle.' IEEE International Conference on Robotics and Automation (ICRA), Stockholm, May 2016; subsequent IEEE Transactions on Control Systems Technology and demonstration videos (catching and throwing a ball mid-air). ETH Zurich IDSC.
- **disclosed subsystems:** `control-fully-actuated-omnidirectional`, `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `cert-experimental`

**Prior art notes:**

> The ETH Omnicopter (Brescianini & D'Andrea, ICRA 2016) is the foundational disclosure of the fully-actuated omnidirectional multirotor — eight bidirectional propellers on a cubic frame giving independent control of force and torque in all six degrees of freedom, able to hover at arbitrary attitudes and recover from any orientation. Establishes prior art for: (1) fully-actuated (6-DOF) multirotor architecture, (2) bidirectional-propeller thrust vectoring, (3) arbitrary-attitude hover and orientation recovery. Anticipates: Voliro (omnidirectional tilt-rotor hexrotor), CycloTech (omnidirectional cyclorotor), and any commercial eVTOL claim asserting novelty over fully-actuated or arbitrary-attitude multirotor control.

**Sources:**

1. Brescianini, D., D'Andrea, R. 'Design, modeling and control of an omni-directional aerial vehicle.' ICRA 2016.
2. Brescianini, D., D'Andrea, R. 'An omni-directional multirotor vehicle.' Mechatronics, 2018.
3. ETH Zurich IDSC publications archive.

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

### 2017 — Alauda Aeronautics Airspeeder (Mk3 / Mk4)

- **id:** `alauda-airspeeder`
- **corpus:** private
- **ip status:** patented
- **creator:** Alauda Aeronautics / Airspeeder (Adelaide, Australia) / Matthew Pearson
- **disclosure citation:** Alauda Aeronautics (founded 2016 in Adelaide by Matthew Pearson) developed the Airspeeder racing eVTOL — the Mk3 (uncrewed remote-piloted racer, first flew 2021, raced in the 'EXA Series' 2022) and the Mk4 (crewed racer, unveiled 2022, designed for the manned Airspeeder Grand Prix). The world's first eVTOL racing series. Documented in Alauda/Airspeeder materials and Australian CASA filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> Alauda Aeronautics' Airspeeder (Mk3 uncrewed 2021, Mk4 crewed 2022) establishes Australian prior art for the racing eVTOL — a high-power-to-weight single-seat (or uncrewed) octocopter designed for close-formation pylon racing, the world's first eVTOL racing series. Establishes prior art for: (1) racing-tuned eVTOL flight envelope and aggressive-maneuvering control, (2) the racing-eVTOL operational concept, (3) crewed/uncrewed variants on a racing airframe. Together with amsl-vertiia (AU, hydrogen passenger eVTOL), deepens Australia's eVTOL footprint. The racing-eVTOL niche is a distinct application alongside passenger air taxi, cargo, personal, and military eVTOL — and Airspeeder is its foundational disclosure.

**Sources:**

1. Alauda Aeronautics / Airspeeder Mk3 / Mk4 technical materials 2017-2024.
2. Airspeeder EXA Series race records 2022.
3. Australian CASA (Civil Aviation Safety Authority) Airspeeder filings.

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

### 2018-05 — Voliro omnidirectional flying robot

- **id:** `voliro`
- **corpus:** private
- **ip status:** patented
- **creator:** Voliro Airborne Robotics (ETH Zurich spinout) / Marco Tognon / Mina Kamel / Roland Siegwart (ASL)
- **disclosure citation:** Voliro hexacopter with tiltable rotor arms first publicly disclosed 2018 (ETH Zurich Autonomous Systems Lab student project, then ETH spinout Voliro Airborne Robotics, founded 2019); academic paper Bodie, Karen et al. 'Towards Efficient Full Pose Omnidirectionality with Overactuated MAVs,' ISER 2018 / and related ASL publications. Commercialized for contact-based industrial inspection (Voliro X, 2022).
- **disclosed subsystems:** `control-fully-actuated-omnidirectional`, `lift-tilt-rotor`, `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `cert-experimental`

**Prior art notes:**

> Voliro establishes prior art for the tilting-arm omnidirectional multirotor — a hexacopter with six independently-tilting rotor arms giving full-pose (6-DOF) control via tilt geometry rather than bidirectional propellers. Distinct from the ETH Omnicopter approach. Establishes prior art for: (1) independently-tilting-arm omnidirectional multirotor, (2) contact-based aerial interaction (pressing sensors against surfaces). Commercialized for industrial inspection. Together with eth-omnicopter (2016) and cyclotech-cruiseup (2022), comprehensively places omnidirectional / fully-actuated multirotor architecture in academic and commercial prior art.

**Sources:**

1. Bodie, K. et al. 'Towards Efficient Full Pose Omnidirectionality with Overactuated MAVs.' ISER 2018.
2. Bodie, K. et al. 'An Omnidirectional Aerial Manipulation Platform for Contact-Based Inspection.' RSS 2019.
3. Voliro Airborne Robotics technical materials, voliro.com.

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

### 2019-09 — Lazareth LMV 496

- **id:** `lazareth-lmv-496`
- **corpus:** private
- **ip status:** patented
- **creator:** Lazareth Auto-Moto (Annecy, France) / Ludovic Lazareth
- **disclosure citation:** Lazareth Auto-Moto (a French custom-vehicle maker) unveiled the LMV 496 'La Moto Volante' — a motorcycle whose four wheels each contain a JetCat micro-turbojet that swivels downward for VTOL flight — in September 2019; tethered hover demonstrations 2021. A French jet-turbine flying motorcycle / hover-bike. Documented in Lazareth materials and motoring/aviation press.
- **disclosed subsystems:** `lift-vectored-thrust`, `cert-experimental`

**Prior art notes:**

> The Lazareth LMV 496 establishes French prior art for the four-micro-turbojet flying motorcycle — a road motorcycle whose four wheels each house a tilting micro-turbojet, swiveling downward for VTOL flight. Establishes prior art for: (1) wheel-integrated tilting-turbojet VTOL drive, (2) the jet-turbine flying-motorcycle / drive+fly hover-bike hybrid. Together with jetpack-aviation-speeder (2021, jet-turbine hover-bike), hoversurf-s3 (2017, open-rotor hover-bike), aerofex-aero-x (2008), and malloy-aeronautics-hoverbike (2014, ducted-rotor), comprehensively places hover-bike / flying-motorcycle architecture in cross-national prior art. Adds another French entry alongside the Eurocopter X3 / Airbus RACER / Flying Whales / SNECMA / Cyrano / Verne French VTOL heritage.

**Sources:**

1. Lazareth Auto-Moto LMV 496 technical materials and press releases 2019-2024.
2. Motoring and aviation press coverage of the Lazareth flying motorcycle 2019-2021.

---

### 2022-06 — Doroni H1 / H1-X

- **id:** `doroni-h1`
- **corpus:** private
- **ip status:** patented
- **creator:** Doroni Aerospace (Fort Lauderdale, Florida) / Doron Merdinger
- **disclosure citation:** Doroni Aerospace (founded 2016 by Doron Merdinger) unveiled the H1 two-seat personal eVTOL in 2022; first crewed test flight 2023-05; received an FAA Special Airworthiness Certificate (Experimental) 2023; developing the H1-X for FAA Part 23 certification. Designed to fit in a two-car garage and operate from driveways under (intended) Part 103 ultralight or LSA rules. Documented in Doroni materials and FAA filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `control-simplified-vehicle-operations`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> Doroni H1 establishes US prior art for the garage-storable enclosed-rotor two-seat personal eVTOL — eight ducted lift rotors housed within the airframe body (not on exposed booms), small fixed wings, car-like footprint, driveway operation. Establishes prior art for: (1) fully-enclosed-within-body lift rotors on a personal eVTOL, (2) garage-storable / driveway-operable two-seat personal eVTOL form factor. Together with pivotal-blackfly, jetson-one, lift-aircraft-hexa, alef-model-a, and the historical personal-platform anchors, comprehensively places small-personal eVTOL architecture in prior art.

**Sources:**

1. Doroni Aerospace H1 / H1-X technical materials 2022-2024.
2. FAA Special Airworthiness Certificate dossier (Doroni H1).

---

### 2022-10-19 — Alef Aeronautics Model A

- **id:** `alef-model-a`
- **corpus:** private
- **ip status:** patented
- **creator:** Alef Aeronautics Inc (San Mateo, California)
- **disclosure citation:** Alef Aeronautics Model A publicly unveiled 2022-10-19; received FAA Special Airworthiness Certificate (Experimental) 2023-06-12 — the first 'flying car' to receive an FAA airworthiness certificate. Alef (founded 2015) demonstrated a full-scale prototype driving and (briefly) lifting 2022-2023. Documented in Alef press materials, FAA filings, and Alef patent filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-tail-sitter-pitch-up`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> Alef Aeronautics Model A establishes US prior art for the rotors-under-mesh-skin drive+fly transformer — a road-legal car with eight electric lift rotors hidden under a perforated upper skin, taking off vertically through the mesh and then rotating the whole body (cabin gimballed level) to fly as a biplane-wing. The first 'flying car' to receive an FAA airworthiness certificate (2023). Establishes prior art for: (1) mesh-skin / perforated-surface lift-rotor concealment architecture, (2) whole-body-rotation drive+fly transition with gimballed cabin, (3) the car-body-as-biplane-wing configuration. Distinct from the folding-wing transformers (Klein Vision, AeroMobil, ASKA) and modular-capsule transformers (Airbus Pop.Up, XPENG AeroHT). Together with these and pal-v-liberty (autogyro transformer), comprehensively places drive+fly transformer architecture in prior art across folding-wing / modular-capsule / whole-body-rotation / autogyro variants.

**Sources:**

1. Alef Aeronautics press releases 2022-2024.
2. FAA Special Airworthiness Certificate dossier (Alef Model A), 2023-06-12.
3. Alef Aeronautics patent filings, USPTO (incl. US 11,167,839).

---

### 2023-11-08 — LTA Research Pathfinder 1

- **id:** `lta-research-pathfinder-1`
- **corpus:** private
- **ip status:** patented
- **creator:** LTA Research and Exploration (Mountain View, CA) — funded by Sergey Brin
- **disclosure citation:** LTA Research Pathfinder 1 received FAA Special Airworthiness Certificate (Experimental) 2023-09; first untethered flight 2023-11-08 at Moffett Field, CA. LTA Research (funded by Google co-founder Sergey Brin since ~2016) builds rigid electric airships for humanitarian cargo and disaster relief. Documented in FAA filings and LTA Research materials.
- **disclosed subsystems:** `lift-buoyant-hybrid`, `lift-distributed-electric-propulsion`, `propulsion-bldc-direct-drive`, `cert-experimental`

**Prior art notes:**

> LTA Research Pathfinder 1 establishes modern prior art for the electric rigid airship with vectored-thrust VTOL augmentation — buoyant helium lift augmented by distributed electric propellers for controlled vertical takeoff/landing without ground infrastructure. Establishes prior art for: (1) modern rigid electric airship architecture, (2) lidar-based ballast/lift management, (3) the buoyant-hybrid VTOL concept (static lift + vectored thrust). The corpus scope includes buoyant-hybrid craft with VTOL-like operations. Together with hybrid-air-vehicles-airlander (2012) and flying-whales-lca60t (2012), establishes the modern hybrid-airship / buoyant-VTOL prior-art base.

**Sources:**

1. LTA Research and Exploration technical materials and press releases 2023-2025.
2. FAA Special Airworthiness Certificate dossier (Pathfinder 1).
3. Pathfinder 1 first flight, Moffett Field CA, 2023-11-08.

---

### 2024-04-25 — Airbus RACER

- **id:** `airbus-racer`
- **corpus:** private
- **ip status:** patented
- **creator:** Airbus Helicopters / Clean Sky 2 (EU Horizon programme)
- **disclosure citation:** Airbus RACER first flight 2024-04-25 at Marignane, France; developed under the EU Clean Sky 2 / Clean Aviation programme (announced 2017, rolled out 2023, first flight 2024). Production-track successor to the Eurocopter X3 demonstrator. Documented in Airbus Helicopters / Clean Sky technical materials.
- **disclosed subsystems:** `lift-compound-rotorcraft`, `cert-experimental`

**Prior art notes:**

> The Airbus RACER is the production-track European compound-helicopter demonstrator (first flight 2024). Refines the Eurocopter X3 architecture with a box-wing carrying lateral cruise/anti-torque propellers and an engine eco-mode (one engine shut down in cruise). Establishes prior art for: (1) box-wing compound-helicopter configuration, (2) eco-mode engine shutdown in compound rotorcraft cruise. Together with eurocopter-x3 (2010) and the Sikorsky compound-rotorcraft lineage, comprehensively places compound-rotorcraft architecture in 1957-2024 prior art.

**Sources:**

1. Airbus Helicopters / Clean Sky 2 RACER technical materials 2017-2024.
2. Airbus press release, RACER first flight, 2024-04-25.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `3a3786e`.*
