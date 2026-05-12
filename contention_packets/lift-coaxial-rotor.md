---
title: "lift-coaxial-rotor"
parent: "Invalidity Contentions"
nav_order: 22
layout: default
---

# Invalidity Contention Packet — `lift-coaxial-rotor`

**Generated:** 2026-05-12  
**Cross-cut tag:** `lift-coaxial-rotor`  
**Entries:** 27 (27 commons-grade, 0 draft)  
**Earliest disclosure:** 1922  
**Most recent disclosure:** 2023-08-16

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `lift-coaxial-rotor`.

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

### 1941-10-30 — Flettner Fl 282 Kolibri

- **id:** `flettner-fl-282-kolibri`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Anton Flettner / Flettner Flugzeugbau
- **disclosure citation:** Flettner Fl 282 Kolibri first flight 1941-10-30 (some sources say 1941-08); production order from Kriegsmarine 1942 for 1,000 aircraft; only ~24 completed before Allied strategic bombing of Flettner factory 1944. The first production-ordered intermeshing-rotor helicopter in history. Documented in Allied CIOS reports and Smithsonian collections.
- **disclosed subsystems:** `lift-coaxial-rotor`, `cert-military`

**Prior art notes:**

> Flettner Fl 282 Kolibri establishes the foundational intermeshing-rotor (synchropter) architecture. Anton Flettner's design directly inspired Charles H. Kaman's post-war intermeshing-rotor work; Kaman acknowledged Flettner as a primary technical influence. Establishes prior art for: (1) intermeshing-rotor architecture in production form, (2) torque-cancellation without anti-torque tail rotor via two-rotor synchronization. Combined with kaman-hh-43-huskie (1953) and kaman-k-max (1991), provides 50+ years of intermeshing-rotor prior art continuously in the public domain.

**Sources:**

1. Flettner, Anton. Mein Weg zum Hubschrauber. Verlag der Luftfahrtforschung, 1949.
2. Allied CIOS reports on Flettner Fl 282, post-1945.
3. Smith and Kay. German Aircraft of the Second World War. Putnam, 1972.

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

### 1953-09-13 — Kaman HH-43 Huskie

- **id:** `kaman-hh-43-huskie`
- **corpus:** academic
- **ip status:** patented
- **creator:** Kaman Aircraft Corporation / U.S. Air Force
- **disclosure citation:** Kaman HH-43 Huskie (originally HOK-1 for U.S. Marine Corps) first flight 1953-09-13; entered USAF service 1958 as primary base-rescue helicopter. Kaman holds the founding patents on intermeshing-rotor (synchropter) architecture (US Patent 2,496,857 'Helicopter rotor construction', 1950 — Charles H. Kaman). Documented in U.S. Air Force technical orders and Kaman Aircraft archives.
- **disclosed subsystems:** `cert-military`, `lift-coaxial-rotor`

**Prior art notes:**

> Kaman HH-43 Huskie is the foundational disclosure of intermeshing-rotor (synchropter) architecture in production form. Establishes prior art for: (1) two-rotor intermeshing geometry with blade-collision prevention via phased rotation, (2) torque-cancellation without anti-torque tail rotor (a fundamental architecture decision shared with coaxial counter-rotating designs), (3) full-scale operational intermeshing helicopter (300+ HH-43 produced). Kaman's original patent (US 2,496,857, 1950) has been expired for over 50 years. Anticipates: Kaman K-MAX (descendant), and any modern eVTOL claiming novelty over intermeshing-rotor lift architecture.

**Sources:**

1. Kaman, Charles H. US Patent 2,496,857, 1950.
2. U.S. Air Force HH-43 Huskie technical orders, AFTO archives.
3. Kaman Aircraft Corporation 50th Anniversary History, 1995.

---

### 1954-03-23 — Lockheed XFV-1 Salmon

- **id:** `lockheed-xfv-salmon`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Lockheed Aircraft / U.S. Navy Bureau of Aeronautics
- **disclosure citation:** Lockheed XFV-1 first flight (with conventional landing gear, no vertical takeoff or landing) 1954-03-23; intended VTOL transition trials cancelled before achieving full vertical flight. Sister program to Convair XFY-1 Pogo. Documented in U.S. Navy BuAer test reports and NASA Langley archives.
- **disclosed subsystems:** `cert-military`, `lift-coaxial-rotor`, `transition-tail-sitter-pitch-up`

**Prior art notes:**

> Lockheed XFV-1 Salmon is the parallel-track Convair XFY-1 Pogo competitor — same Tri-Service VTOL fighter program, distinct airframe designs from different contractors. Establishes additional U.S. tail-sitter prior art (with convair-xfy-pogo) and demonstrates the design space was actively explored by multiple manufacturers in 1954. Together with XFY-1, comprehensively places contra-rotating coaxial-prop tail-sitter VTOL architecture in the public domain.

**Sources:**

1. Markman, Steve and Holder, Bill. Straight Up. Schiffer, 2000.
2. U.S. Navy BuAer XFV-1 test reports, NARA RG72.
3. Lockheed Aircraft Skunk Works archives.

---

### 1954-08-01 — Convair XFY-1 Pogo

- **id:** `convair-xfy-pogo`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Convair / U.S. Navy Bureau of Aeronautics
- **disclosure citation:** Convair / U.S. Navy XFY-1 program; first vertical takeoff and landing achieved 1954-08-01 (tethered hover); first complete transition flight 1954-11-02 by James F. 'Skeets' Coleman. Documented in Navy BuAer test reports and NACA literature.
- **disclosed subsystems:** `cert-military`, `lift-coaxial-rotor`, `transition-tail-sitter-pitch-up`

**Prior art notes:**

> The XFY-1 Pogo is the first heavier-than-air aircraft to demonstrate full VTOL transition: vertical takeoff, transition to horizontal flight, sustained cruise, transition back to vertical, and vertical landing — all in one flight, by Coleman on 1954-11-02. Establishes prior art for the entire concept of a hover-cruise VTOL transition envelope, the conversion-corridor concept, and the tail-sitter architecture. Specific subsystems disclosed: contra-rotating coaxial lift propulsion (anticipates Wisk Cora-class coax claims), tail-sitter pitch-up transition, manual aerodynamic transition control. Modern eVTOL programs that abandoned tail-sitting in favor of tilt-rotor or tilt-wing did so because of pilot ergonomics, not because tail-sitting didn't work — XFY-1 demonstrated it does.

**Sources:**

1. Markman, Steve and Holder, Bill. Straight Up: A History of Vertical Flight. Schiffer, 2000.
2. Rogers, Mike. VTOL: Military Research Aircraft. Orion Books, 1989.
3. Coleman, James F. Skeets. 'The XFY-1 Pogo Story.' Naval Aviation News, various.
4. U.S. Navy BuAer test reports on XFY-1, NARA RG72.

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

### 1965-08-13 — Kamov Ka-26 Hoodlum

- **id:** `kamov-ka-26`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Kamov Design Bureau
- **disclosure citation:** Kamov Ka-26 first flight 1965-08-13; flight test program documented in Soviet Aviation Industry / GosNII GA reports; entered service 1968. Subject of multiple Soviet aviation patents on coaxial rotor hub design.
- **disclosed subsystems:** `cert-part-29`, `lift-coaxial-rotor`

**Prior art notes:**

> The Ka-26 is the foundational Soviet civil disclosure of coaxial counter-rotating-rotor architecture in production form. Establishes prior art for: (1) coaxial gearbox transmission with synchronized counter-rotating rotors, (2) the entire Kamov lineage of coaxial rotorcraft now operational worldwide. Combined with Pescara helicopter (1922), comprehensively covers coaxial-rotor lift architecture for invalidity contention purposes from 1922 forward. Modern eVTOL using coaxial lift pairs (Beta Alia, EHang EH216 8-pair coaxial geometry) all sit downstream of this disclosure.

**Sources:**

1. Mikheyev, Vadim. OKB Kamov. Polygon, 1999.
2. Gunston, Bill. The Osprey Encyclopedia of Russian Aircraft. Osprey, 1995.

---

### 1969-12-01 — Take-copter (Doraemon)

- **id:** `doraemon-takecopter`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Fujiko F. Fujio (Hiroshi Fujimoto and Motoo Abiko)
- **disclosure citation:** Take-copter (タケコプター) first appeared in Doraemon manga, December 1969 issue of CoroCoro Comic / serialized in six children's magazines simultaneously. Subsequently a defining recurring gadget across 50+ years of Doraemon manga and anime.
- **disclosed subsystems:** `lift-coaxial-rotor`

**Prior art notes:**

> Take-copter is the canonical Japanese fictional disclosure of head-mounted coaxial-rotor personal flight. With 50+ years of recurring depictions and billions of cumulative impressions across manga, anime, and merchandise, Take-copter is among the most globally-recognized fictional VTOL devices. Establishes prior art for: (1) head-mounted personal-VTOL form factor (distinct from strap-on rocket belt or jetpack), (2) coaxial-counter-rotating small-scale rotor for personal lift. Anticipates: any post-1969 personal-flight patent attempt asserting novelty over head-mounted small-rotor lift devices.

**Sources:**

1. Fujiko F. Fujio. Doraemon, CoroCoro Comic and other Shogakukan magazines, December 1969 onward.
2. Fujiko-F-Fujio Pro corporate Doraemon archive (Kawasaki).
3. Encyclopedia Doraemonica, Shogakukan, multiple editions.

---

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

### 2015-05-22 — Sikorsky S-97 Raider

- **id:** `sikorsky-s-97-raider`
- **corpus:** private
- **ip status:** patented
- **creator:** Sikorsky Aircraft (Lockheed Martin)
- **disclosure citation:** Sikorsky S-97 Raider first flight 2015-05-22 at West Palm Beach FL. Production-track development of the X2 demonstrator (2008-08-27 first flight). Documented in Sikorsky technical papers and AHS / VFS Forum publications.
- **disclosed subsystems:** `lift-coaxial-rotor`, `lift-compound-rotorcraft`, `cert-military`

**Prior art notes:**

> Sikorsky S-97 Raider is the production-track sibling to the SB>1 Defiant — same X2 rigid-coaxial-rotor + rear-pusher architecture, smaller scale for armed-reconnaissance role. Together with sikorsky-boeing-defiant, comprehensively documents Sikorsky's modern coaxial rigid-rotor compound rotorcraft architecture in production-track form.

**Sources:**

1. Sikorsky Aircraft press releases and technical papers 2015–2024.
2. AHS / VFS Forum papers from Sikorsky engineering 2008–2024.

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

### 2019-03-21 — Sikorsky-Boeing SB>1 Defiant

- **id:** `sikorsky-boeing-defiant`
- **corpus:** private
- **ip status:** patented
- **creator:** Sikorsky Aircraft (Lockheed Martin) / Boeing
- **disclosure citation:** Sikorsky-Boeing SB>1 Defiant first flight 2019-03-21 at West Palm Beach FL (U.S. Army Future Vertical Lift / Joint Multi-Role Technology Demonstrator program). Predecessor Sikorsky X2 first flight 2008-08-27. Sikorsky holds extensive coaxial-rigid-rotor patent estate.
- **disclosed subsystems:** `cert-military`, `lift-coaxial-rotor`, `lift-compound-rotorcraft`

**Prior art notes:**

> Sikorsky-Boeing Defiant establishes prior art for: (1) modern rigid coaxial counter-rotating rotor design overcoming retreating-blade-stall speed limits, (2) compound rotorcraft architecture (lift rotor + auxiliary cruise propulsion). Although not eVTOL, the architectural patterns directly anticipate any modern compound-rotorcraft eVTOL (Jaunt Journey, Karem AR40) claiming coaxial-plus-pusher novelty.

**Sources:**

1. Sikorsky / Boeing JMR-TD program disclosures.
2. Sikorsky X2 technology white papers, AHS / VFS Forums 2008–2024.
3. U.S. Army Future Vertical Lift program reports.

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

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `d899fde`.*
