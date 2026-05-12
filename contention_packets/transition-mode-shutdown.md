---
title: "transition-mode-shutdown"
parent: "Invalidity Contentions"
nav_order: 49
layout: default
---

# Invalidity Contention Packet — `transition-mode-shutdown`

**Generated:** 2026-05-12  
**Cross-cut tag:** `transition-mode-shutdown`  
**Entries:** 26 (26 commons-grade, 0 draft)  
**Earliest disclosure:** 1959  
**Most recent disclosure:** 2022-08

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `transition-mode-shutdown`.

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

### 1964-05-25 — Ryan XV-5 Vertifan

- **id:** `ryan-xv-5-vertifan`
- **corpus:** academic
- **ip status:** patented
- **creator:** Ryan Aeronautical Company / U.S. Army / NASA
- **disclosure citation:** Ryan XV-5A Vertifan first flight 1964-05-25; first transition 1964-11-05. A 'lift-fan' VTOL using gas-driven lift fans embedded in the wings and nose. U.S. Army / NASA program; flew through the late 1960s. Documented in NASA and U.S. Army test reports.
- **disclosed subsystems:** `lift-ducted-fan-array`, `transition-lift-fan-clutched`, `transition-mode-shutdown`, `cert-military`

**Prior art notes:**

> The Ryan XV-5 Vertifan (1964) is the foundational disclosure of the gas-driven tip-turbine lift fan — large lift fans embedded in the wings/nose, driven by turbojet exhaust gas routed to turbines on the fan rims (rather than mechanical shafts), with the fans covered by louvres for cruise. Establishes prior art for: (1) tip-turbine gas-coupled lift fans, (2) fan-in-wing embedded lift, (3) divert-exhaust mode transition. General Electric's 1960s tip-turbine lift-fan patents are expired. Together with vanguard-omniplane (1959, mechanically-driven fan-in-wing) and lockheed-xv-4-hummingbird (1962, ejector-augmenter), places fan-in-wing / embedded-lift-fan VTOL architecture comprehensively in 1959-1964 public-domain prior art — directly relevant to Lilium's ducted-fan-array eVTOL and modern fan-in-wing eVTOL concepts.

**Sources:**

1. NASA / U.S. Army Ryan XV-5 Vertifan test reports.
2. General Electric tip-turbine lift-fan patents, USPTO, 1960s.
3. Markman and Holder. Straight Up. Schiffer, 2000.

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

### 2018-11-08 — Pegasus Vertical Business Jet

- **id:** `pegasus-universal-aerospace`
- **corpus:** private
- **ip status:** patented
- **creator:** Pegasus Universal Aerospace (Johannesburg, South Africa)
- **disclosure citation:** Pegasus Vertical Business Jet design publicly unveiled 2018-11-08 at Aero South Africa; subsequent design refinements 2020–2024. Pegasus Universal Aerospace founded 2017 by Reza Mia. South African Civil Aviation Authority engagement on certification framework 2021 onward.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-part-23`, `lift-ducted-fan-array`, `lift-vectored-thrust`, `propulsion-hybrid-series`, `transition-mode-shutdown`

**Prior art notes:**

> Pegasus Vertical Business Jet is South Africa's lead commercial VTOL design — distinct architectural commitment to executive-jet operations (2,200 km range, 400 kt cruise) with VTOL hover capability. Establishes African continental prior-art lineage for commercial VTOL business aviation distinct from urban air taxi. Architecturally similar to Lockheed Martin / Aurora LightningStrike (XV-24A, US military 2016) in fuselage-internal lift fan + cruise jet topology.

**Sources:**

1. Pegasus Universal Aerospace press releases 2018–2024.
2. South African Civil Aviation Authority engagement records.
3. Aero South Africa exhibition materials 2018-11-08.

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

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `3a3786e`.*
