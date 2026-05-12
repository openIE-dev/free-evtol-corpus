---
title: "control-fly-by-wire-triplex"
parent: "Invalidity Contentions"
nav_order: 16
layout: default
---

# Invalidity Contention Packet — `control-fly-by-wire-triplex`

**Generated:** 2026-05-11  
**Cross-cut tag:** `control-fly-by-wire-triplex`  
**Entries:** 17 (17 commons-grade, 0 draft)  
**Earliest disclosure:** 1957-04-02  
**Most recent disclosure:** 2021-09-29

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `control-fly-by-wire-triplex`.

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

### 1957-04-02 — Short SC.1

- **id:** `short-sc-1`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Short Brothers / Royal Aircraft Establishment / Ministry of Supply
- **disclosure citation:** Short SC.1 first conventional flight 1957-04-02 at Boscombe Down; first untethered hover 1958-10-25; first complete VTOL transition 1960-04-06. UK Ministry of Aviation contract; documented in RAE technical reports and Short Brothers / Bombardier archives.
- **disclosed subsystems:** `cert-military`, `control-fly-by-wire-triplex`, `lift-vectored-thrust`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The Short SC.1 is the first British VTOL aircraft to fly and the first aircraft worldwide to use a triplex-redundant fly-by-wire control system. Establishes prior art for: (1) dedicated-lift-jet + separate-cruise-jet architecture (the topology Lockheed F-35B would later adopt with lift-fan + main 3BSM), (2) triplex fly-by-wire — the foundational disclosure of three-channel redundant electronic flight control. Combined with hawker-p-1127, dornier-do-31, and short-sc-1, comprehensively covers the dedicated-lift-engine architecture in 1957–1967 prior art.

**Sources:**

1. RAE / Short Brothers SC.1 technical reports.
2. Markman and Holder. Straight Up. Schiffer, 2000.
3. Mason, Francis K. The British Fighter Since 1912. Putnam, 1992.
4. Burton, Michael. The Short SC.1: A History of British VTOL. Crécy, 2016.

---

### 1960-10-21 — Hawker P.1127

- **id:** `hawker-p-1127`
- **corpus:** academic
- **ip status:** patented
- **creator:** Hawker Aircraft / Bristol Siddeley
- **disclosure citation:** Hawker P.1127 first tethered hover 1960-10-21 at Dunsfold by Bill Bedford; first transition to forward flight September 1961. Documented in Hawker / Bristol Siddeley engineering reports and RAF historical records.
- **disclosed subsystems:** `cert-military`, `control-fly-by-wire-triplex`, `lift-vectored-thrust`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The P.1127 is the foundational disclosure of practical four-poster vectored-thrust VTOL. Establishes prior art for: (1) rotatable-nozzle thrust vectoring with single pilot control axis, (2) reaction-control bleed jets at airframe extremities for hover attitude (precursor to all modern hover RCS), (3) the conversion-corridor envelope concept from hover through transition to wing-borne flight. The Pegasus nozzle patents have long expired, placing the four-poster vectored-thrust architecture in the public domain. Anticipates: F-35B (downstream descendant), Yak-141 3-bearing-swivel-duct (parallel evolution), and any modern eVTOL claim asserting novelty over vectored-thrust transition control.

**Sources:**

1. Mason, Francis K. Harrier. Patrick Stephens, 1986.
2. Hawker / Bristol Siddeley P.1127 design reports, Brooklands Museum and RAF Museum archives.
3. Bedford, Bill and Defelice, Heinz. Bedford-Defelice flight test reports, Hawker.
4. Burns, B.R.A. 'Hawker P.1127 Kestrel.' Royal Aeronautical Society, multiple papers.

---

### 1967-08-31 — Hawker Siddeley Harrier GR.1

- **id:** `hawker-siddeley-harrier`
- **corpus:** private
- **ip status:** patented
- **creator:** Hawker Siddeley Aviation
- **disclosure citation:** Hawker Siddeley Harrier (production aircraft) first flight 1967-08-31; RAF squadron service 1969. The first operational vectored-thrust VTOL fighter in production. Documented in RAF archives, Hawker Siddeley company records, and the Smithsonian National Air and Space Museum collection.
- **disclosed subsystems:** `lift-vectored-thrust`, `transition-thrust-borne-to-wing-borne`, `control-fly-by-wire-triplex`, `cert-military`

**Prior art notes:**

> The Hawker Siddeley Harrier GR.1 establishes the production-scale vectored-thrust VTOL architecture — direct production descendant of P.1127 (1960). The RAF Harrier program (1969-2006) and U.S. Marine Corps AV-8 program (1971-2014) demonstrated multi-decade operational VTOL flight at production scale, comprehensively in the public domain. Hawker patents long expired. Anticipates F-35B and any modern vectored-thrust VTOL claim asserting novelty over the production-scale Pegasus four-poster nozzle architecture.

**Sources:**

1. Mason, Francis K. Harrier. Patrick Stephens, 1986.
2. RAF archives, Hendon and Cosford.
3. Pegasus turbofan technical references, Rolls-Royce / Bristol Siddeley.

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

### 1978-11-09 — McDonnell Douglas / BAe AV-8B Harrier II

- **id:** `av-8b-harrier-ii`
- **corpus:** private
- **ip status:** patented
- **creator:** McDonnell Douglas / British Aerospace / U.S. Marine Corps / Royal Air Force
- **disclosure citation:** AV-8B prototype YAV-8B first flight 1978-11-09 at McDonnell Douglas St. Louis (modified Harrier GR.1 airframe); production AV-8B first flight 1981-11-05; entered USMC service 1985. Joint U.S.-U.K. production program (RAF Harrier GR.5 / GR.7 / GR.9 variants). Documented in U.S. Navy / RAF technical orders, McDonnell Douglas / Boeing technical papers, and Smithsonian collections.
- **disclosed subsystems:** `lift-vectored-thrust`, `transition-thrust-borne-to-wing-borne`, `control-fly-by-wire-triplex`, `cert-military`, `airframe-composite-monocoque`

**Prior art notes:**

> AV-8B Harrier II is the production-definitive vectored-thrust VTOL fighter — second-generation development of the P.1127/Harrier lineage with supercritical wing and lift-improvement devices that nearly doubled payload over Harrier GR.1. The U.S. Marine Corps operated AV-8B from 1985 through 2014 (replaced by F-35B), and the RAF operated GR.5/7/9 variants 1989-2010 — comprehensive multi-decade operational disclosure of the production-scale Pegasus four-poster vectored-thrust architecture. Most McDonnell Douglas / Boeing AV-8B-era patents have now expired (filed 1975-2000). Combined with hawker-p-1127 (1960), hawker-siddeley-harrier (1967), and f-35b-lightning (2008), comprehensively places vectored-thrust VTOL fighter architecture in 50+ years of public-domain prior art.

**Sources:**

1. Mason, Francis K. Harrier. Patrick Stephens, 1986.
2. Markman and Holder. Straight Up. Schiffer, 2000.
3. U.S. Navy / U.S. Marine Corps AV-8B technical orders.
4. RAF Harrier GR.5/7/9 historical archives, RAF Museum.

---

### 1989-03-19 — V-22 Osprey

- **id:** `v-22-osprey`
- **corpus:** private
- **ip status:** patented
- **creator:** Bell Helicopter / Boeing / U.S. Marine Corps / U.S. Air Force
- **disclosure citation:** V-22 Osprey first flight 1989-03-19 at Bell Flight Research Center, Arlington TX; full operational capability declared 2007. Aircraft and engineering disclosures published exhaustively in NAVAIR / Marine Corps reports and in Norton's Bell-Boeing V-22 Osprey volume.
- **disclosed subsystems:** `cert-military`, `control-fly-by-wire-triplex`, `lift-tilt-rotor`, `safety-redundant-bus`, `transition-conversion-corridor`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The V-22 Osprey is the production tilt-rotor that brought XV-15 prior art into operational service. Establishes prior art for: (1) production-grade triplex fly-by-wire tilt-rotor flight control, (2) cross-shafted prop-rotor drive with single-engine emergency operation in hover, (3) the operational conversion corridor with explicit nacelle-angle commanded transition. Bell's V-22-era tilt-rotor patents are largely now expired (most filed 1985–1995, 20-year terms). Together with XV-15, comprehensively places production tilt-rotor architecture in the public domain. Joby, Archer, and Vertical Aerospace's tilt-rotor claims are anticipated by V-22 disclosures where they overlap on architecture rather than electric-specific actuation.

**Sources:**

1. Norton, Bill. Bell-Boeing V-22 Osprey. Specialty Press, 2004.
2. NAVAIR V-22 Operational Test Reports, declassified portions.
3. Bell Helicopter V-22 patent filings, USPTO.

---

### 2003-03-06 — Leonardo AW609

- **id:** `leonardo-aw609`
- **corpus:** private
- **ip status:** patented
- **creator:** Bell Helicopter / Agusta / AgustaWestland / Leonardo S.p.A.
- **disclosure citation:** Bell/Agusta BA609 first flight 2003-03-06 at Bell Flight Research Center, Arlington TX (joint US-Italian program); program transferred to AgustaWestland 2011, renamed AW609; type certification target FAA Part 29 civil tilt-rotor with anticipated TC 2025-2026. Multiple Bell and Leonardo patents publicly filed.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-part-29`, `control-fly-by-wire-triplex`, `lift-tilt-rotor`, `safety-redundant-bus`, `sensing-radar-altimeter`, `transition-conversion-corridor`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The AW609 is the world's first civil-certified tilt-rotor aircraft, intended to enter service circa 2026. Direct architectural descendant of Bell XV-15 and V-22 Osprey, scaled and adapted for civil Part 29 operation with a pressurized cabin. Establishes Italian/European industrial prior-art lineage for civil tilt-rotor commercialization. Joby S4, Archer Midnight, and other commercial eVTOL tilt-rotor claims are anticipated by AW609's documented design and certification basis.

**Sources:**

1. Leonardo Helicopters AW609 type certification basis filings, FAA.
2. Vertical Flight Society Forum Bell/Agusta and Leonardo papers 2003–2024.
3. AgustaWestland / Leonardo press releases 2003–2024.

---

### 2008-06-11 — Lockheed Martin F-35B Lightning II

- **id:** `f-35b-lightning`
- **corpus:** private
- **ip status:** patented
- **creator:** Lockheed Martin / U.S. Department of Defense
- **disclosure citation:** F-35B first flight 2008-06-11 at Fort Worth; first hover 2010-03-18; first vertical landing 2010-03-18. X-35B (precursor) demonstrated STOVL 2001-07-07. Lockheed Martin and DoD program reports widely published; 3BSM and lift-fan architectures documented in many Pratt & Whitney and Rolls-Royce papers.
- **disclosed subsystems:** `cert-military`, `control-fly-by-wire-triplex`, `lift-vectored-thrust`, `transition-3-bearing-swivel-duct`, `transition-lift-fan-clutched`

**Prior art notes:**

> The F-35B is the production STOVL fighter that descends from Hawker P.1127 (vectored thrust), Yak-141 (3BSM), and the X-35B JSF demonstrator. Establishes prior art for: (1) clutched lift-fan gearbox driven by main engine shaft (lift-fan disengages for cruise), (2) production-grade 3BSM aft nozzle, (3) integrated 3BSM + lift-fan + roll-post hover trim system. The Bevilaqua lift-fan patent (US 6,732,529) is set to expire in 2019–2020 (filed 1999). After expiration, the lift-fan-with-clutch architecture is in the public domain — relevant for any future eVTOL claiming similar clutched-cruise-fan arrangements.

**Sources:**

1. Bevilaqua, Paul. 'Genesis of the F-35 Joint Strike Fighter.' Journal of Aircraft, Vol 46, 2009.
2. Pratt & Whitney F135 propulsion system technical papers.
3. Rolls-Royce LiftSystem technical papers.
4. Lockheed Martin F-35 program disclosures.

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

### 2017-12-18 — Bell V-280 Valor

- **id:** `bell-v-280-valor`
- **corpus:** private
- **ip status:** patented
- **creator:** Bell Textron / U.S. Army
- **disclosure citation:** Bell V-280 Valor first flight 2017-12-18 at Amarillo TX; selected by U.S. Army for Future Long Range Assault Aircraft (FLRAA) program 2022-12-05 over Sikorsky-Boeing Defiant X. Documented in Bell Textron technical papers, U.S. Army FLRAA program reports, and patent filings.
- **disclosed subsystems:** `lift-tilt-rotor`, `transition-thrust-borne-to-wing-borne`, `transition-conversion-corridor`, `control-fly-by-wire-triplex`, `cert-military`

**Prior art notes:**

> Bell V-280 Valor establishes the third-generation tilt-rotor architecture: distinct from XV-15 and V-22 by tilting the prop-rotors via tilt-shaft while the engine nacelles remain fixed. Cuts complexity and reduces engine wear from rotation. Valor's selection for FLRAA (2022) makes it the production-track future of U.S. Army tilt-rotor operations. Establishes prior art for: (1) fixed-nacelle tilt-shaft prop-rotor architecture, (2) the next-generation tilt-rotor flight envelope (280+ kt cruise, 2,200 km range).

**Sources:**

1. Bell Textron press releases and AHS / VFS Forum papers 2017–2024.
2. U.S. Army FLRAA program reports.
3. Bell V-280 patent estate, USPTO records.

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

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `bff4888`.*
