---
title: "lift-distributed-electric-propulsion"
parent: "Invalidity Contentions"
nav_order: 26
layout: default
---

# Invalidity Contention Packet — `lift-distributed-electric-propulsion`

**Generated:** 2026-05-14  
**Cross-cut tag:** `lift-distributed-electric-propulsion`  
**Entries:** 117 (117 commons-grade, 0 draft)  
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

### 1907-09-29 — Breguet-Richet Gyroplane No.1

- **id:** `breguet-richet-gyroplane`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Louis Breguet / Jacques Bichon / Professor Charles Richet
- **disclosure citation:** Louis Breguet, his brother Jacques, and Professor Charles Richet lifted the Breguet-Richet Gyroplane No.1 off the ground at Douai, France, 1907-09-29 — a tethered hop with the pilot 1.5 m off the ground for ~1 minute, by some accounts the first time a manned heavier-than-air rotorcraft lifted free of the ground (predating Cornu's free flight by ~5 weeks, though tethered). Documented in the Aero Club de France 1907 records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `cert-experimental`

**Prior art notes:**

> The Breguet-Richet Gyroplane No.1 (1907-09-29) is by some accounts the first manned heavier-than-air rotorcraft to lift free of the ground in any form (tethered hop, predating Cornu's free flight by ~5 weeks). Establishes the foundational French / European manned-multi-rotor prior art — four-rotor cross-frame with cross-belt single-engine drive, 15 years before de Bothezat (1922). Louis Breguet would later found Breguet Aviation and remain a major figure in French aerospace. Comprehensively in the public domain (Breguet died 1955). Together with cornu-helicopter (FR 1907-11-13, first free flight), ellehammer-helicopter (DK 1912), and the 1922 cluster (de Bothezat, Pescara, Kirsten-Boeing, Berliner), establishes the deep early-rotorcraft prior-art base from 1907 forward.

**Sources:**

1. Aero Club de France 1907 archives, Paris.
2. Liberatore, E.K. Helicopters Before Helicopters. Krieger, 1998.
3. Boulet, Jean. History of the Helicopter as Told by its Pioneers 1907-1956. France-Empire, 1991.

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

### 1922-06-16 — Berliner helicopter

- **id:** `berliner-helicopter`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Henry Berliner / Emile Berliner / Berliner Aircraft Company
- **disclosure citation:** Henry Berliner (son of Emile Berliner, inventor of the gramophone) demonstrated his first practical helicopter to the U.S. Army at College Park MD on 1922-06-16 — the same year as the de Bothezat quadrotor and the Pescara coaxial helicopter. The Berliner machine made tethered hops and short free flights through 1925. Documented in U.S. Army Air Service reports, Smithsonian National Air and Space Museum collections (a Berliner is preserved at College Park), and Berliner family papers.
- **disclosed subsystems:** `lift-coaxial-rotor`, `lift-distributed-electric-propulsion`, `cert-experimental`

**Prior art notes:**

> Henry Berliner's 1922 helicopter is the parallel American disclosure to the de Bothezat quadrotor and Pescara coaxial — three independent 1922 manned-multirotor disclosures across the U.S., Argentina/France, and France. Establishes prior art for: (1) lateral side-by-side twin-rotor architecture in 1922 (predating Focke-Wulf Fa 61 by 14 years), (2) the parallel-track development of practical rotorcraft across multiple national prior-art bases. The U.S. Army Air Service evaluated the Berliner alongside the de Bothezat. Berliner's patents are long expired.

**Sources:**

1. U.S. Army Air Service Berliner helicopter test reports, College Park MD, 1922-1925.
2. Smithsonian National Air and Space Museum, Berliner helicopter collection (Paul E. Garber facility, College Park).
3. Berliner, Henry / Emile Berliner family papers, Library of Congress.

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

### 1945-03-07 — Piasecki H-21 / HRP Rescuer

- **id:** `piasecki-h-21`
- **corpus:** academic
- **ip status:** patented
- **creator:** Piasecki Helicopter Corporation / U.S. Navy / U.S. Army / U.S. Air Force
- **disclosure citation:** Piasecki PV-3 / XHRP-1 Rescuer first flight 1945-03-07; the production H-21 Workhorse/Shawnee entered service 1949. Frank Piasecki's tandem-rotor (overlapping fore-and-aft rotors) architecture became one of the two dominant heavy-helicopter configurations (the other being Sikorsky's single-main-rotor). Documented in U.S. Navy/Army technical orders and Smithsonian collections.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `cert-military`

**Prior art notes:**

> The Piasecki H-21 / HRP Rescuer (Frank Piasecki, 1945) is the foundational disclosure of the tandem-rotor helicopter architecture — two large counter-rotating rotors fore and aft, synchronized to cancel torque without a tail rotor. Establishes prior art for: (1) tandem-rotor lift architecture (ancestor of the Boeing CH-47 Chinook), (2) overlapping-rotor synchronization, (3) torque cancellation between two main lift rotors. Piasecki's 1940s patents are long expired. The tandem-rotor configuration is relevant prior art for any eVTOL using fore-and-aft lift-rotor pairs (a recurring lift+cruise and multirotor geometry). Combined with de-bothezat-quadrotor (1922) and convertawings-model-a (1956), places multi-rotor lift architectures comprehensively in mid-20th-century prior art.

**Sources:**

1. Piasecki, Frank. Tandem-rotor helicopter patents, USPTO, 1940s-1950s.
2. U.S. Navy / U.S. Army H-21 technical orders.
3. Spenser, Jay P. Whirlybirds: A History of the U.S. Helicopter Pioneers. University of Washington Press, 1998.

---

### 1948-12-08 — Cierva W.11 Air Horse

- **id:** `cierva-air-horse`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Cierva Autogiro Company / Cunliffe-Owen Aircraft (UK)
- **disclosure citation:** Cierva W.11 Air Horse first flight 1948-12-08 at Eastleigh, Hampshire. The largest helicopter in the world at the time — three large rotors arranged in tandem (forward, port-aft, starboard-aft) driven by a single Rolls-Royce Merlin engine via cross-shafting. Cancelled after a fatal crash 1950. Documented in Cierva / Cunliffe-Owen archives and UK Ministry of Supply reports.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `cert-experimental`

**Prior art notes:**

> The Cierva W.11 Air Horse (1948) is the foundational disclosure of the three-rotor heavy-lift helicopter architecture — three large rotors arranged at the corners of a triangle, cross-shafted to a single engine. The largest helicopter in the world at the time, predating the Soviet Mil V-12 (1968, two-rotor lateral) and the Sikorsky CH-53E (1974). Establishes UK prior art for triangular-three-rotor lift architecture — a distinct multirotor configuration from the X-frame quadrotor (de Bothezat 1922), tandem (Piasecki 1945), lateral (Focke-Wulf Fa 61 1936, Berliner 1922), and coaxial (Pescara 1922) lineages. Cierva's post-Juan-de-la-Cierva company carried the Cierva-name autogyro/rotorcraft tradition into the post-war heavy-lift era.

**Sources:**

1. Cierva Autogiro Company / Cunliffe-Owen W.11 Air Horse program archives.
2. UK Ministry of Supply Air Horse test reports.
3. Brooks, Peter W. Cierva Autogiros. Smithsonian, 1988.

---

### 1952-07-03 — Yakovlev Yak-24

- **id:** `yak-24`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Yakovlev Design Bureau
- **disclosure citation:** Yakovlev Yak-24 first flight 1952-07-03; entered limited Soviet service 1955. A tandem-rotor heavy transport helicopter — the Soviet answer to the Piasecki tandem-rotor configuration. Set FAI payload records 1956. Documented in Yakovlev OKB archives (post-1991 declassified) and Gunston's Soviet aircraft references.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `cert-military`

**Prior art notes:**

> The Yakovlev Yak-24 (1952) is the Soviet tandem-rotor heavy helicopter — the Soviet counterpart to the Piasecki H-21, demonstrating the tandem-rotor architecture in an independently-developed lineage. Soviet government work, fully in the public domain post-1991. Together with piasecki-h-21 (1945), places tandem-rotor lift architecture in cross-national prior art. Adds another Russian/Soviet entry to the deep Soviet rotorcraft heritage (TsAGI 1-EA, de Bothezat, Mil V-12, Kamov lineage, Yak VTOL fighters, Mil tip-jet, Mil Mi-30 tilt-rotor).

**Sources:**

1. Yakovlev OKB Yak-24 archives, post-1991 declassified, RGAE.
2. Gunston, Bill. The Osprey Encyclopedia of Russian Aircraft. Osprey, 1995.
3. Gunston and Gordon. Yakovlev Aircraft Since 1924. Putnam, 1997.

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

### 1958 — Chrysler VZ-6

- **id:** `chrysler-vz-6`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Chrysler Corporation / U.S. Army Transportation Research Command
- **disclosure citation:** Chrysler VZ-6 'flying jeep' first (and essentially only) flight tests 1959 at Chrysler's facility — it proved unstable and overweight and the program ended quickly. The third of the three U.S. Army 'flying jeep' programs (with Curtiss-Wright VZ-7 and Piasecki VZ-8). Documented in U.S. Army TRC reports.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `cert-military`

**Prior art notes:**

> The Chrysler VZ-6 (1958-1959) is the third of the three U.S. Army 'flying jeep' programs, completing the trio with the Curtiss-Wright VZ-7 (open quadrotor) and the Piasecki VZ-8 Airgeep (tandem open rotors). The VZ-6 used twin ducted lift fans fore and aft of the pilot with exhaust-vane attitude control. Establishes additional U.S. public-domain prior art for: (1) twin-ducted-fan personal/light flying-platform architecture, (2) exhaust-vane attitude control. Together with curtiss-wright-vz-7, piasecki-vz-8-airgeep, hiller-vz-1-pawnee, and de-lackner-hz-1-aerocycle, comprehensively places the 1955-1958 'flying jeep' / personal-platform design space in public-domain prior art.

**Sources:**

1. U.S. Army Transportation Research Command VZ-6 reports.
2. Markman and Holder. Straight Up. Schiffer, 2000.

---

### 1958-07-05 — Bristol Type 192 Belvedere

- **id:** `bristol-belvedere`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Bristol Aeroplane Company / Westland Helicopters (production) / Royal Air Force
- **disclosure citation:** Bristol Type 192 Belvedere first flight 1958-07-05; entered Royal Air Force service 1961 as the Belvedere HC.1 — the RAF's first twin-engine, twin-rotor helicopter and the first British tandem-rotor production helicopter. Documented in Bristol Aeroplane Company / Westland archives and RAF historical records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `cert-military`

**Prior art notes:**

> The Bristol Belvedere (1958) is the British tandem-rotor production helicopter — completing the cross-national tandem-rotor prior-art set alongside the US (Piasecki H-21 1945, CH-47 Chinook 1961) and Soviet (Yakovlev Yak-24 1952) lineages. Establishes UK prior art for tandem-rotor heavy-lift architecture with cross-shafted twin-turboshaft drive.

**Sources:**

1. Bristol Aeroplane Company / Westland Belvedere program archives.
2. RAF Belvedere HC.1 historical materials.

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

### 1972 — Hawker Siddeley HS.141

- **id:** `hawker-siddeley-hs-141`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Hawker Siddeley Aviation
- **disclosure citation:** Hawker Siddeley HS.141 VTOL short-haul airliner design study, developed 1971-1973 in response to a perceived 1980s market for city-centre vertiport airline service; never built. A ~100-seat jet airliner with a bank of dedicated lift engines plus cruise turbofans. Documented in Hawker Siddeley company materials, the UK aerospace press of the early 1970s, and Wood's Project Cancelled.
- **disclosed subsystems:** `lift-vectored-thrust`, `lift-distributed-electric-propulsion`, `transition-thrust-borne-to-wing-borne`, `cert-part-25`

**Prior art notes:**

> The Hawker Siddeley HS.141 (1972) is the foundational disclosure of the civil-airliner-scale VTOL passenger transport with distributed dedicated lift engines plus cruise engines, designed for city-centre vertiport operation. Establishes prior art for: (1) airliner-scale VTOL passenger transport, (2) the vertiport-city-centre airline-service operational concept, (3) sixteen-lift-engine distributed-lift architecture at airliner scale. Although never built, the design disclosure is documented in Hawker Siddeley materials and the UK aerospace press. Anticipates: the entire modern eVTOL urban-air-mobility / vertiport business thesis (Joby, Archer, Lilium, Eve, Volocopter all pitch city-centre vertiport service), demonstrating that the operational concept was specifically disclosed in 1972.

**Sources:**

1. Hawker Siddeley Aviation HS.141 study materials.
2. Wood, Derek. Project Cancelled. Macdonald & Jane's, 1975.
3. Flight International coverage of the HS.141, early 1970s.

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

### 2009 — MIT ACL aggressive quadrotor maneuvers

- **id:** `mit-acl-aggressive-quadrotor`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** MIT Aerospace Controls Laboratory (Jonathan How) / RAVEN testbed
- **disclosure citation:** MIT Aerospace Controls Laboratory (Jonathan How) developed the RAVEN (Real-time indoor Autonomous Vehicle test ENvironment) testbed and a long series of aggressive-quadrotor-maneuver publications from 2009 onward. Foundational paper: Cutler, M. and How, J.P. 'Analysis and Control of a Variable-Pitch Quadrotor for Agile Flight.' ASME Journal of Dynamic Systems, Measurement, and Control 137(10), 2015. Subsequent papers through 2020 cover aerobatic maneuvers, variable-pitch propellers, and learning-based control.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `cert-experimental`

**Prior art notes:**

> MIT Aerospace Controls Lab (Jonathan How) RAVEN-platform aggressive-quadrotor maneuver work (2009-2020) establishes US academic prior art for variable-pitch quadrotor architecture and aerobatic-envelope control. Distinct from fixed-pitch BLDC commodity multirotor designs by adding per-rotor collective-pitch control — relevant prior art for any eVTOL claim involving variable-pitch lift rotors (Joby S4, Archer Midnight, Vahana, and other modern eVTOL all use variable-pitch on at least some rotors). Adds MIT to the US academic aerial-robotics anchor set alongside UPenn GRASP, Harvard Microrobotics, and the various NASA / DARPA programs.

**Sources:**

1. Cutler, M., How, J.P. 'Analysis and Control of a Variable-Pitch Quadrotor for Agile Flight.' ASME JDSMC 137(10), 2015.
2. MIT Aerospace Controls Lab publications archive (RAVEN testbed).
3. How, J.P. et al. 'RAVEN: Indoor multi-vehicle UAV test environment.' AIAA GNC 2008.

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

### 2012 — Flying Whales LCA60T

- **id:** `flying-whales-lca60t`
- **corpus:** private
- **ip status:** patented
- **creator:** Flying Whales (Bordeaux, France) — backed by the French state and Quebec
- **disclosure citation:** Flying Whales (founded 2012 in Bordeaux, originally to support French national forestry log extraction) developing the LCA60T — a rigid airship designed to carry 60 tonnes of cargo with load/unload while hovering (no landing required). Backed by Bpifrance, the Nouvelle-Aquitaine region, the government of Quebec, and ADP (Aéroports de Paris). First flight targeted ~2027. Documented in Flying Whales technical materials and French government investment disclosures.
- **disclosed subsystems:** `lift-buoyant-hybrid`, `lift-distributed-electric-propulsion`, `propulsion-hybrid-series`, `propulsion-bldc-direct-drive`, `cert-part-23`

**Prior art notes:**

> Flying Whales LCA60T establishes French prior art for the heavy-lift cargo airship with hover-mode load/unload — a 60-tonne-capacity rigid airship with 32 distributed electric propellers, designed to deliver cargo from a stationary hover without landing or ground infrastructure. Establishes prior art for: (1) heavy-lift buoyant-hybrid cargo architecture, (2) distributed-electric-propeller precision hover on a large airship, (3) crane-mode hovering cargo delivery. Together with lta-research-pathfinder-1 and hybrid-air-vehicles-airlander-10, establishes the modern hybrid-airship / buoyant-VTOL prior-art base. Adds another French entry alongside the Eurocopter X3 / Airbus RACER compound-helicopter lineage and the SNECMA / Cyrano / Verne French VTOL heritage.

**Sources:**

1. Flying Whales technical materials and press releases 2012-2025.
2. Bpifrance / Nouvelle-Aquitaine / government of Quebec investment disclosures.
3. Flying Whales patent filings, INPI / EPO records.

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

### 2012-08-07 — Hybrid Air Vehicles Airlander 10

- **id:** `hybrid-air-vehicles-airlander-10`
- **corpus:** private
- **ip status:** patented
- **creator:** Hybrid Air Vehicles Ltd (Bedford, United Kingdom)
- **disclosure citation:** Hybrid Air Vehicles HAV-304 (built for the cancelled U.S. Army LEMV programme) first flight 2012-08-07 at Lakehurst NJ; rebuilt as the Airlander 10 by HAV in the UK, first flight 2016-08-17 at Cardington. Hybrid Air Vehicles is developing the production Airlander 10 for passenger and cargo service (~2026-2028). Documented in HAV technical materials, U.S. Army LEMV reports, and UK CAA certification filings.
- **disclosed subsystems:** `lift-buoyant-hybrid`, `lift-vectored-thrust`, `lift-distributed-electric-propulsion`, `propulsion-hybrid-series`, `cert-part-23`

**Prior art notes:**

> Hybrid Air Vehicles Airlander 10 establishes UK prior art for the hybrid airship — a hull shaped to generate ~40% aerodynamic lift alongside ~60% buoyant helium lift, with vectored ducted propulsors for VTOL control, able to operate from unprepared sites (water, ice, sand, rough ground). Establishes prior art for: (1) hybrid aerodynamic-plus-buoyant lift architecture, (2) vectored-propulsor VTOL control on an airship, (3) infrastructure-free VTOL operation at large scale. Together with lta-research-pathfinder-1 (2023) and flying-whales-lca60t (2012), establishes the modern hybrid-airship / buoyant-VTOL prior-art base. Also relevant to the Orb Aerospace / Skyways 'unprepared site operations' thesis at a much larger scale.

**Sources:**

1. Hybrid Air Vehicles technical materials and press releases 2012-2025.
2. U.S. Army LEMV (Long Endurance Multi-intelligence Vehicle) programme reports.
3. UK CAA Airlander 10 certification filings.

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

### 2015-08 — Joby S2

- **id:** `joby-s2`
- **corpus:** private
- **ip status:** patented
- **creator:** Joby Aviation (Santa Cruz, California)
- **disclosure citation:** Joby S2 design publicly disclosed by JoeBen Bevirt and Joby Aviation August 2015 (technical white paper and Vertical Flight Society Forum presentation); first untethered transition flight 2017-08. The single-pilot predecessor that established Joby Aviation's six-rotor tilt-rotor architecture later scaled up for the S4 production design. Documented in Joby technical white papers and AHS/VFS Forum presentations 2015-2018.
- **disclosed subsystems:** `lift-tilt-rotor`, `lift-distributed-electric-propulsion`, `transition-thrust-borne-to-wing-borne`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> Joby Aviation's S2 (2015) is the architectural prototype for Joby's six-tilt-rotor distributed-electric-propulsion eVTOL — establishing the 4-wing + 2-stabilator tilt-rotor configuration two years before the public S4 unveil (joby-s4, 2018) and anchoring the Joby Aviation patent estate priority chain. The 2015 disclosure makes Joby's architectural choices public prior art before any patent dates that depend on the S4 disclosure date. Important for invalidity-contention purposes: any Joby patent claiming priority later than 2015 against S2-disclosed elements has prior art from Joby's own earlier disclosure.

**Sources:**

1. Bevirt, JoeBen et al. Joby S2 technical white paper, 2015.
2. Joby Aviation S-1 SEC filing 2020 (history section).
3. Vertical Flight Society Forum technical papers from Joby engineering 2015-2018.

---

### 2016 — Caltech CAST drone autonomy / Neural-Fly

- **id:** `caltech-cast-neural-fly`
- **corpus:** academic
- **ip status:** open-permissive
- **creator:** Caltech Center for Autonomous Systems and Technologies / Soon-Jo Chung / Aaron Ames
- **disclosure citation:** Caltech CAST (Center for Autonomous Systems and Technologies) established 2016 at Caltech. Key publications: O'Connell, M. et al. 'Neural-Fly enables rapid learning for agile flight in strong winds.' Science Robotics 7(66), 2022 (a paper demonstrating deep-learning-augmented quadrotor control in high-wind environments); plus a long series of multi-modal flying-robot papers from Soon-Jo Chung's group (LEONARDO, the bipedal-robot-with-multirotor hybrid, 2021).
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `cert-experimental`

**Prior art notes:**

> Caltech CAST (Center for Autonomous Systems and Technologies, Soon-Jo Chung / Aaron Ames groups, 2016-) establishes US academic prior art for deep-learning-augmented quadrotor control (Neural-Fly, Science Robotics 2022) and for multi-modal walking/flying hybrid robots (LEONARDO, 2021). Relevant prior art for any eVTOL claim involving ML-augmented adaptive control or hybrid bipedal-flying robotic platforms. Adds Caltech to the US academic aerial-robotics anchor set alongside UPenn GRASP, MIT ACL, Harvard, Stanford, and the various NASA / DARPA programs.

**Sources:**

1. O'Connell, M., Shi, G., Shi, X., Azizzadenesheli, K., Anandkumar, A., Yue, Y., Chung, S.-J. 'Neural-Fly enables rapid learning for agile flight in strong winds.' Science Robotics 7(66), 2022.
2. Kim, K., Spieler, P., Lupu, E.-S., Ramezani, A., Chung, S.-J. 'A bipedal walking robot that can fly, slackline, and skateboard (LEONARDO).' Science Robotics 6(59), 2021.
3. Caltech CAST publications archive.

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

### 2017-04-20 — Lilium Phoenix 2

- **id:** `lilium-phoenix-2`
- **corpus:** private
- **ip status:** patented
- **creator:** Lilium GmbH
- **disclosure citation:** Lilium GmbH (founded 2015 at TU Munich) unveiled the Phoenix 2 (a two-seat prototype eVTOL with 36 ducted electric fans) on 2017-04-20; first unmanned hover test 2017-04. The Phoenix 2 was the predecessor to the production Lilium Jet (5-seat, unveiled 2019); both used the embedded-tilting-ducted-fan-array architecture. Documented in Lilium materials and DLR / Bavarian aerospace press.
- **disclosed subsystems:** `lift-ducted-fan-array`, `lift-distributed-electric-propulsion`, `transition-thrust-borne-to-wing-borne`, `transition-tilt-wing`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> The Lilium Phoenix 2 (2017) is the predecessor disclosure of the Lilium ducted-fan-array eVTOL architecture — 36 embedded tilting electric ducted fans in a two-seat configuration. Establishes Lilium's own prior art for: (1) the foundational embedded-tilting-ducted-fan-array eVTOL configuration, (2) the architectural concept that the production 5-seat Lilium Jet (2019) refined. Lilium GmbH filed for insolvency 2024-10; its patent estate was auctioned and acquired by various successor entities; this commons-grade entry preserves the Phoenix 2 prior-art date independent of any post-bankruptcy successor claims. Useful for invalidity contention against any successor entity attempting to assert post-2017 patents on Lilium-architecture eVTOL.

**Sources:**

1. Lilium GmbH press releases and technical materials 2015-2024.
2. Phoenix 2 unveiling materials, Munich 2017-04-20.
3. TU Munich / DLR Bavarian aerospace press 2015-2024.

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

### 2018 — Skygauge Robotics inspection drone

- **id:** `skygauge-robotics`
- **corpus:** private
- **ip status:** patented
- **creator:** Skygauge Robotics (Toronto, Canada)
- **disclosure citation:** Skygauge Robotics (founded 2018 in Toronto by Maks Zubko and Linar Ismagilov) developed a tilting-rotor industrial-inspection drone capable of stable contact with vertical surfaces; first commercial deployment 2021. Designed for ultrasonic-thickness inspection of tall industrial structures (oil storage tanks, refineries, pressure vessels). Documented in Skygauge materials and Canadian industrial-inspection records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-fully-actuated-omnidirectional`, `lift-tilt-rotor`, `propulsion-bldc-direct-drive`, `cert-easa-special-condition-vtol`

**Prior art notes:**

> Skygauge Robotics (CA 2018-) establishes Canadian prior art for the tilting-arm quadrotor industrial-inspection drone — independently-tilting rotor arms enabling controlled horizontal thrust during hover for contact-based surface inspection (ultrasonic thickness measurement on industrial structures). Smaller-scale industrial counterpart to Voliro (CH, omnidirectional hexrotor inspection). Adds Canadian depth alongside Jaunt Air Mobility (slowed-rotor compound eVTOL), Horizon Aircraft Cavorite X5 (fan-in-wing eVTOL), and the Avro Canada Avrocar heritage.

**Sources:**

1. Skygauge Robotics technical materials 2018-2024.
2. Skygauge Robotics patent filings, Canadian Intellectual Property Office and USPTO.

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

### 2018-10-25 — LIFT Aircraft Hexa

- **id:** `lift-aircraft-hexa`
- **corpus:** private
- **ip status:** patented
- **creator:** LIFT Aircraft Inc (Austin, Texas)
- **disclosure citation:** LIFT Aircraft Hexa publicly unveiled 2018-10-25; first crewed flights 2019; FAA Part 103 ultralight category (no pilot license required); public 'flight experiences' / training-flight programme launched 2021-2024. Documented in LIFT Aircraft press materials, FAA Part 103 registrations, and U.S. Air Force AFWERX Agility Prime contracts.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `control-simplified-vehicle-operations`, `cert-part-103-ultralight`, `airframe-composite-monocoque`

**Prior art notes:**

> LIFT Aircraft Hexa establishes US prior art for the maximally-redundant single-seat multirotor eVTOL — eighteen independent rotors each with its own battery and motor (full distributed redundancy, tolerates loss of six rotors), single-joystick fly-by-wire simplified vehicle operations, FAA Part 103 ultralight operation. Establishes prior art for: (1) per-rotor-independent battery/motor architecture with deep failure tolerance, (2) consumer-grade single-joystick SVO for an 18-rotor eVTOL, (3) Part 103 ultralight commercial flight-experience deployment. Together with pivotal-blackfly, jetson-one, ehang-eh216, and volocopter-volocity, comprehensively places single-seat / small-pax multirotor eVTOL in commercial prior art.

**Sources:**

1. LIFT Aircraft press releases and FAA Part 103 registrations 2018-2024.
2. U.S. Air Force AFWERX Agility Prime contract records (LIFT Hexa).

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

### 2019 — teTra Mk-5

- **id:** `tetra-mk-5`
- **corpus:** private
- **ip status:** patented
- **creator:** teTra Aviation Corporation (Tokyo, Japan) / Tasuku Nakai
- **disclosure citation:** teTra Aviation Corporation (founded 2018 in Tokyo, an outgrowth of GoFly Prize-competing students) revealed the Mk-3 personal eVTOL (2020, GoFly Prize 'Pratt & Whitney Disruptor Award' winner) and subsequently the production Mk-5 single-seat personal eVTOL (2021); first crewed flights and FAA Special Airworthiness Certificate process underway. Documented in teTra materials and GoFly Prize records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `transition-mode-shutdown`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-103-ultralight`

**Prior art notes:**

> teTra Mk-5 establishes Japanese prior art for the high-rotor-count single-seat personal eVTOL — a fixed-wing airframe with 32 small distributed lift rotors for hover redundancy plus wing lift for cruise efficiency. A GoFly Prize-derived design. Establishes prior art for: (1) very-high-rotor-count (~32) personal eVTOL with fixed wings, (2) the GoFly Prize lineage of personal-flight designs. Together with skydrive-sd-05 (JP, multirotor air taxi), aska-a5 (JP/US, drive+fly), honda-evtol (JP, hybrid), and the Japanese fictional VTOL anchors, deepens Japan's eVTOL footprint. Together with lift-aircraft-hexa (US, 18-rotor) and ehang-eh216 (CN, 16-rotor), places high-rotor-count personal/small eVTOL architecture in prior art.

**Sources:**

1. teTra Aviation Mk-3 / Mk-5 technical materials 2019-2024.
2. GoFly Prize competition records (teTra Mk-3, Pratt & Whitney Disruptor Award).

---

### 2019 — Bellwether Industries Volar

- **id:** `bellwether-volar`
- **corpus:** private
- **ip status:** patented
- **creator:** Bellwether Industries (London, United Kingdom)
- **disclosure citation:** Bellwether Industries (founded 2019 in London by Kai-Hsiang Lin) publicly disclosed the Volar — a four-seat ducted-fan flying-car concept designed to look like a luxury car — through 2021-2024 design and sub-scale-prototype releases. The 'Antelope' 1/6-scale demonstrator made tethered flights 2021. Documented in Bellwether materials.
- **disclosed subsystems:** `lift-ducted-fan-array`, `lift-distributed-electric-propulsion`, `lift-vectored-thrust`, `propulsion-hybrid-series`, `propulsion-bldc-direct-drive`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`

**Prior art notes:**

> Bellwether Industries' Volar concept (UK, 2019-) establishes prior art for the 'luxury-car-aesthetic flying car with internal ducted fans' — eight electric ducted lift fans buried inside a sleek closed-body vehicle with no exposed rotors, smooth aerodynamic surface in cruise. Distinct from Alef Model A (rotors under mesh skin, whole-body rotation) and from open-rotor multirotor eVTOLs. Adds UK depth to the flying-car / ducted-fan-array prior-art base alongside Lilium (DE), Aurora LightningStrike (US), Bell X-22 (US), Bell Nexus (US), Doak VZ-4 (US), Pegasus VBJ (ZA), Boeing Phantom Swift (US), and Horizon Aircraft Cavorite X5 (CA).

**Sources:**

1. Bellwether Industries Volar / Antelope technical materials 2019-2024.

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

### 2019-06 — Jaunt Air Mobility Journey

- **id:** `jaunt-air-mobility`
- **corpus:** private
- **ip status:** patented
- **creator:** Jaunt Air Mobility LLC (Montreal, Canada / Texas, USA) — subsidiary of AIRO Group; licensed Carter Aviation SR/C technology
- **disclosure citation:** Jaunt Air Mobility (founded 2019, headquartered in Montreal with Texas operations, a subsidiary of the AIRO Group) unveiled the Journey eVTOL — a slowed-rotor compound electric VTOL using 'ROSA' (Reduced rOtor Speed Aircraft) technology licensed from Carter Aviation — in 2019; selected for the U.S. Air Force AFWERX Agility Prime programme 2020. Documented in Jaunt Air Mobility materials, AFWERX records, and AIRO Group SEC filings (NASDAQ: AIRO).
- **disclosed subsystems:** `lift-compound-rotorcraft`, `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-23`, `airframe-composite-monocoque`

**Prior art notes:**

> Jaunt Air Mobility's Journey eVTOL establishes Canadian/US prior art for the slowed-rotor-compound electric VTOL — a single large rotor that spins fast for jump-takeoff then slows dramatically in cruise while a wing carries lift and electric pushers provide thrust ('ROSA', licensed from Carter Aviation). A distinct eVTOL architecture from the multirotor and tilt-rotor approaches. Establishes prior art for: (1) slowed-rotor-compound electric VTOL, (2) jump-takeoff stored-inertia rotor in an electric eVTOL, (3) the wing-offloads-slowed-rotor-in-cruise eVTOL configuration. Together with cartercopter (1998, the SR/C origin), karem-ar40 (2008, optimum-speed rotor), and overair-butterfly (2020, OSR eVTOL), comprehensively places slowed/variable-RPM-rotor compound eVTOL architecture in prior art. Adds another Canadian entry alongside Horizon Aircraft and the Avro Canada Avrocar heritage.

**Sources:**

1. Jaunt Air Mobility Journey technical materials 2019-2024.
2. U.S. Air Force AFWERX Agility Prime contract records (Jaunt).
3. AIRO Group SEC filings (NASDAQ: AIRO).

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

### 2019-10-15 — Pipistrel Nuuva V300

- **id:** `pipistrel-nuuva-v300`
- **corpus:** private
- **ip status:** patented
- **creator:** Pipistrel (Slovenia; acquired by Textron 2022)
- **disclosure citation:** Pipistrel (a Slovenian light-aircraft maker, the manufacturer of the Velis Electro — the first type-certified electric aeroplane) unveiled the Nuuva V300 hybrid VTOL cargo aircraft 2019-10-15; Pipistrel acquired by Textron 2022-04. The Nuuva V300 is intended as a heavy-cargo lift+cruise hybrid-electric eVTOL. Documented in Pipistrel/Textron materials and EASA filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-hybrid-series`, `power-hybrid-genset`, `propulsion-bldc-direct-drive`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`

**Prior art notes:**

> Pipistrel Nuuva V300 establishes Slovenian prior art for the hybrid-electric heavy-cargo eVTOL — eight electric lift rotors plus a single combustion-driven cruise pusher, designed for ~460 kg cargo over ~2,500 km range. Adds Slovenia (SI) to the global eVTOL OEM map. Pipistrel's parent company is Textron (also owner of Bell Textron) — the Pipistrel-Textron-Bell axis creates an integrated tilt-rotor + hybrid-cargo + electric-fixed-wing eVTOL family. Together with elroy-air-chaparral, sabrewing-rhaegal-a, wingcopter-198, pyka-pelican, amsl-vertiia, autoflight-prosperity-i, dji-flycart-30, and orb-aerospace-nomad, comprehensively places hybrid-electric cargo eVTOL architecture in commercial prior art across nine national/regional lineages.

**Sources:**

1. Pipistrel Nuuva V300 technical materials 2019-2024.
2. Textron acquisition of Pipistrel, 2022-04 disclosures.
3. EASA SC-VTOL public docket (Pipistrel).

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

### 2020-10-15 — Overair Butterfly

- **id:** `overair-butterfly`
- **corpus:** private
- **ip status:** patented
- **creator:** Overair Inc (Santa Ana, California) — Karem Aircraft spinoff; partnered with Hanwha Systems (Korea)
- **disclosure citation:** Overair (spun out of Karem Aircraft in 2020, with investment from Hanwha Systems of South Korea) unveiled the Butterfly eVTOL — a tilt-rotor eVTOL using Karem's 'Optimum Speed Tilt-Rotor' (OSTR) technology (large slow-turning prop-rotors with continuously-variable RPM) — in October 2020. Documented in Overair materials, Hanwha Systems disclosures, and U.S. Air Force AFWERX Agility Prime records.
- **disclosed subsystems:** `lift-tilt-rotor`, `lift-distributed-electric-propulsion`, `transition-thrust-borne-to-wing-borne`, `transition-conversion-corridor`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-23`, `airframe-composite-monocoque`

**Prior art notes:**

> Overair's Butterfly establishes prior art for the optimum-speed tilt-rotor eVTOL — a tilt-rotor eVTOL with four very large, slow-turning prop-rotors whose RPM is continuously varied with flight regime ('OSTR', from Karem Aircraft's OSR technology), giving low disk loading for quiet, efficient hover. Distinct from the small-fast-prop tilt-rotor eVTOLs (Joby S4, TCab E20) by the large-slow-prop approach. Establishes prior art for: (1) continuously-variable-RPM tilt-rotor in an eVTOL, (2) very-low-disk-loading large slow prop-rotors for quiet hover, (3) the OSR-applied-to-eVTOL configuration. Hanwha Systems (Korea) partnership ties this to the Korean eVTOL ecosystem (Hyundai Supernal, Plana). Together with karem-ar40 (2008, OSTR origin), cartercopter (1998), and jaunt-air-mobility (2019), comprehensively places variable-RPM / slowed-rotor / optimum-speed-rotor eVTOL architecture in prior art.

**Sources:**

1. Overair Butterfly technical materials 2020-2024.
2. Hanwha Systems (Korea) Overair investment disclosures.
3. U.S. Air Force AFWERX Agility Prime contract records (Overair).
4. Karem Aircraft / Overair OSR / OSTR patents, USPTO.

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

### 2021-05-17 — Volocopter VoloRegion / VoloConnect

- **id:** `volocopter-voloregion`
- **corpus:** private
- **ip status:** patented
- **creator:** Volocopter GmbH
- **disclosure citation:** Volocopter VoloConnect (later renamed VoloRegion) publicly unveiled 2021-05-17; first full-scale flight 2022-05. Lift+cruise variant of the Volocopter family — distinct from the multirotor VoloCity and the cargo VoloDrone. Documented in Volocopter materials and EASA SC-VTOL filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `safety-redundant-bus`, `safety-ballistic-parachute`, `control-fly-by-wire-triplex`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`, `autonomy-utm-integration`

**Prior art notes:**

> Volocopter VoloRegion / VoloConnect is the lift+cruise variant of the Volocopter family — Volocopter's pivot from pure-multirotor (VoloCity) to lift+cruise topology for regional range and higher cruise speed. Establishes prior art for: (1) lift+cruise variant shared across a multirotor platform's family, (2) Volocopter's platform extension into longer-range mission profiles. Together with volocopter-volocity (passenger multirotor), volocopter-volodrone (cargo multirotor), and volocopter-vc1 (foundational), comprehensively places the Volocopter platform family in prior art.

**Sources:**

1. Volocopter GmbH VoloRegion / VoloConnect technical materials and press releases 2021-2024.
2. EASA SC-VTOL filings (Volocopter VoloRegion).

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

### 2021-07 — CycloTech CruiseUp / CCY-5

- **id:** `cyclotech-cruiseup`
- **corpus:** private
- **ip status:** patented
- **creator:** CycloTech GmbH (Linz, Austria)
- **disclosure citation:** CycloTech GmbH (founded 2004 as D-Dalus successor, rebranded CycloTech 2020) unveiled the CruiseUp passenger eVTOL concept 2022-09; the CCY-5 technology demonstrator (a sub-scale flying testbed using six CycloRotors) achieved first untethered flight 2024-04-17 at Wels, Austria. CycloTech holds an extensive cycloidal-rotor patent estate.
- **disclosed subsystems:** `lift-cyclorotor`, `control-fully-actuated-omnidirectional`, `lift-distributed-electric-propulsion`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`

**Prior art notes:**

> CycloTech CruiseUp / CCY-5 is the modern production-oriented disclosure of cyclorotor (cyclogiro) eVTOL — six electric CycloRotors giving omnidirectional fully-actuated thrust via azimuthal blade-pitch modulation. Establishes Austrian prior art for: (1) passenger-scale cyclorotor eVTOL architecture, (2) electric CycloRotor propulsion with 360° in-plane thrust vectoring, (3) the omnidirectional fully-actuated cyclorotor control. Builds on the D-Dalus research demonstrator (2011) and the foundational Pescara cyclogiro patents (1928, long expired). Together with d-dalus and eth-omnicopter, comprehensively places cyclorotor and omnidirectional VTOL architecture in prior art.

**Sources:**

1. CycloTech GmbH technical white papers and press releases 2020-2024.
2. CycloTech CCY-5 first flight, Wels Austria, 2024-04-17.
3. Pescara cyclogiro patents (1928, foundational, expired).

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

### 2021-09 — Horizon Aircraft Cavorite X5

- **id:** `horizon-aircraft-cavorite-x5`
- **corpus:** private
- **ip status:** patented
- **creator:** New Horizon Aircraft Ltd (Lindsay, Ontario, Canada)
- **disclosure citation:** New Horizon Aircraft (Canadian, founded 2013, public on NASDAQ as HOVR via SPAC merger 2024) unveiled the Cavorite X5 hybrid eVTOL in 2021; 50%-scale prototype first conventional flight 2023-11 and first full transition 2024-11. The Cavorite uses a 'fan-in-wing' design — fourteen lift fans embedded in the wings, covered by sliding panels in cruise so the aircraft flies as a conventional fixed-wing. Documented in Horizon Aircraft materials and SEC filings (named for H.G. Wells's anti-gravity material 'Cavorite').
- **disclosed subsystems:** `lift-ducted-fan-array`, `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-hybrid-series`, `power-hybrid-genset`, `propulsion-bldc-direct-drive`, `cert-part-23`, `airframe-composite-monocoque`

**Prior art notes:**

> Horizon Aircraft Cavorite X5 establishes Canadian prior art for the modern 'fan-in-wing' hybrid eVTOL — fourteen electric lift fans embedded in the wing structure, covered by sliding panels in cruise so the wing becomes a clean conventional wing with a single pusher. Establishes prior art for: (1) modern panel-covered fan-in-wing eVTOL, (2) hybrid-electric fan-in-wing architecture, (3) the wing-as-clean-wing-in-cruise design. Directly descended in concept from vanguard-omniplane (1959) and ryan-xv-5-vertifan (1964). Together with these and lilium-jet (ducted-fan-array), aurora-lightningstrike-xv-24a (tilt-wing ducted-fan), and bell-nexus-4ex (tilt-duct), comprehensively places ducted-fan / fan-in-wing eVTOL architecture in prior art. Adds Canadian depth alongside Jaunt Air Mobility and the Avro Canada Avrocar heritage.

**Sources:**

1. New Horizon Aircraft Cavorite X5 technical materials 2021-2024.
2. New Horizon Aircraft SEC filings (NASDAQ: HOVR).

---

### 2021-09 — Maca Carcopter S11

- **id:** `maca-carcopter`
- **corpus:** private
- **ip status:** patented
- **creator:** MACA Industries (Toulouse, France) / Michaël Carchidi
- **disclosure citation:** MACA Industries (founded 2019 in Toulouse, France) unveiled the S11 Carcopter — a hydrogen-fuel-cell racing eVTOL — at the September 2021 Munich IAA Mobility show. Designed for an envisioned hydrogen racing league. Documented in MACA materials and aerospace press.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `propulsion-hydrogen-fuel-cell`, `propulsion-bldc-direct-drive`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> MACA Carcopter establishes French prior art for the hydrogen-fuel-cell racing eVTOL — distinct from Alauda Airspeeder (AU, battery-electric racing) by the hydrogen powertrain. Together with airspeeder (AU) and amsl-vertiia (AU, hydrogen passenger), places hydrogen and racing eVTOL architecture in cross-national prior art. Adds another French entry to the deep French VTOL heritage (SNECMA Coléoptère, Eurocopter X3, Airbus RACER, Flying Whales, Cornu, Oehmichen, d'Amécourt, Lazareth, Airbus Vahana, Airbus Pop.Up, Verne).

**Sources:**

1. MACA Industries S11 Carcopter technical materials and IAA Mobility 2021 unveiling.
2. MACA Industries press materials 2021-2024.

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

### 2021-10 — REGENT Viceroy seaglider

- **id:** `regent-viceroy-seaglider`
- **corpus:** private
- **ip status:** patented
- **creator:** REGENT Craft Inc (Rhode Island, USA) — founded by Boeing / Aurora Flight Sciences alumni
- **disclosure citation:** REGENT Craft (founded 2020 by Billy Thalheimer and Mike Klinker, ex-Aurora Flight Sciences / Boeing) unveiled the Viceroy seaglider 2021-10; quarter-scale prototype first flight 2022-08; full-scale Viceroy prototype rollout / first sea trials 2024-2025. The seaglider operates in three modes — floating (hull), foiling (hydrofoils), and flying (wing-in-ground-effect, ~9 m altitude). Documented in REGENT technical materials, U.S. Marine Corps / Navy contracts, and patent filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-23`, `airframe-composite-monocoque`

**Prior art notes:**

> REGENT Viceroy is the foundational modern disclosure of the electric wing-in-ground-effect (WIG) 'seaglider' — a distributed-electric-propulsion craft that transitions floating → hydrofoiling → ground-effect flight, operating a few meters above water. Establishes prior art for: (1) electric WIG / ekranoplan-class craft with distributed blown-wing propulsion, (2) the hull/foil/flight three-mode transition, (3) retractable-hydrofoil takeoff for a winged aircraft. While not vertical-takeoff in the classical sense, it is eVTOL-adjacent (the corpus scope covers ground-effect hybrids with VTOL-like operations) and shares DEP blown-wing architecture with eVTOL. Anticipates other electric-WIG and seaglider claims (a growing segment — also pursued by Wigetworks AirFish and others).

**Sources:**

1. REGENT Craft technical white papers and press releases 2021-2025.
2. U.S. Marine Corps / Navy seaglider contract records.
3. REGENT Craft patent filings, USPTO.

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

### 2022-05 — Skyfly Axe

- **id:** `skyfly-axe`
- **corpus:** private
- **ip status:** patented
- **creator:** Skyfly Technologies Ltd (Oxfordshire, United Kingdom)
- **disclosure citation:** Skyfly Technologies (UK, founded 2018 by Michael Thompson, William Bryceson, and Rachel Pearson) unveiled the Axe kit-built tilting eVTOL in May 2022; first untethered hover 2023-04-28. A two-seat tilting eVTOL designed for the kit-built / homebuilt (Light UAV / Sub-115 kg) market under UK CAA Permit to Fly. Documented in Skyfly materials and UK CAA filings.
- **disclosed subsystems:** `lift-tilt-wing`, `lift-distributed-electric-propulsion`, `transition-thrust-borne-to-wing-borne`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> Skyfly Axe establishes UK prior art for the kit-built / homebuilt tilt-wing eVTOL — a four-rotor tandem-tilting-wing two-seat eVTOL targeting the UK light-aircraft market under kit-built rules. Establishes prior art for: (1) kit-built / homebuilt eVTOL business model, (2) the tandem-tilting-wing four-rotor light-aircraft configuration. Together with vertical-vx4, bellwether-volar, malloy-aeronautics-hoverbike, gravity-industries-jet-suit, hawker-siddeley-hs-141, and the deep UK rotorcraft heritage, deepens the UK eVTOL footprint.

**Sources:**

1. Skyfly Technologies Axe technical materials 2022-2024.
2. UK CAA Permit to Fly filings (Skyfly Axe).

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

### 2022-08 — Plana Aero CP-01

- **id:** `plana-cp-01`
- **corpus:** private
- **ip status:** patented
- **creator:** Plana Aerospace Inc (Seongnam, South Korea)
- **disclosure citation:** Plana Aerospace (founded 2021 in South Korea by Braden Kim) unveiled the CP-01 hybrid-electric eVTOL in 2022; sub-scale prototype flight tests 2023-2024; targeting Korean (MOLIT) and FAA certification for regional air mobility. Documented in Plana materials and Korean Ministry of Land, Infrastructure and Transport (MOLIT) records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-hybrid-series`, `power-hybrid-genset`, `propulsion-bldc-direct-drive`, `cert-part-23`, `airframe-composite-monocoque`

**Prior art notes:**

> Plana Aero CP-01 establishes Korean prior art for the hybrid-electric regional eVTOL — a lift+cruise eVTOL with a turbine-genset-electric hybrid powertrain for ~500 km range, targeting intercity routes. Distinct from the urban-air-taxi-focused Korean peer Hyundai Supernal (battery-electric, 100 km). Establishes Korean depth in the hybrid-electric eVTOL space alongside Honda (JP), Zuri (CZ), Elroy Air (US), and AMSL Vertiia (AU). Together with hyundai-supernal-sa2, the Hanwha-Systems-backed overair-butterfly, and (fictionally) space-sweepers-victory, deepens Korea's eVTOL footprint.

**Sources:**

1. Plana Aerospace CP-01 technical materials 2022-2024.
2. Korean MOLIT (Ministry of Land, Infrastructure and Transport) UAM programme records.

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

### 2023-11 — Sarla Aviation Shunya

- **id:** `sarla-aviation-shunya`
- **corpus:** private
- **ip status:** patented
- **creator:** Sarla Aviation (Bangalore, India)
- **disclosure citation:** Sarla Aviation (founded 2023 in Bangalore by Adrian Schmidt, Rakesh Gaonkar, and Shivam Chauhan; named after Sarla Thakral, India's first woman pilot) unveiled the Shunya eVTOL air taxi in November 2023, with production targeted for ~2028 in Indian cities (Bangalore, Mumbai, Delhi, Pune); sub-scale prototype work 2024. Documented in Sarla materials and Indian DGCA engagement records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-23`, `airframe-composite-monocoque`

**Prior art notes:**

> Sarla Aviation Shunya establishes additional Indian prior art for the urban-air-taxi multirotor eVTOL — a five-seat eVTOL designed for short hops in dense Indian cities, the second major Indian eVTOL OEM after ePlane. Establishes Indian depth alongside eplane-company-e200 (IN, lift+cruise) and the Indian fictional flight anchor (Krrish). Together with ehang-eh216 (CN), volocopter-volocity (DE), and the global multirotor air-taxi cluster, places urban-air-taxi multirotor eVTOL architecture in prior art across US, EU, China, India, Japan, Korea, and Brazil lineages.

**Sources:**

1. Sarla Aviation Shunya technical materials 2023-2024.
2. Indian DGCA (Directorate General of Civil Aviation) UAM engagement records.

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

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `674103d`.*
