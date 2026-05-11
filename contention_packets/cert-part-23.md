---
title: "cert-part-23"
parent: "Invalidity Contentions"
nav_order: 10
layout: default
---

# Invalidity Contention Packet — `cert-part-23`

**Generated:** 2026-05-11  
**Cross-cut tag:** `cert-part-23`  
**Entries:** 20 (20 commons-grade, 0 draft)  
**Earliest disclosure:** 2017-04-20  
**Most recent disclosure:** 2024-01-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `cert-part-23`.

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

### 2017-04-20 — AeroMobil 4.0

- **id:** `aeromobil-4-0`
- **corpus:** private
- **ip status:** patented
- **creator:** AeroMobil s.r.o (Bratislava, Slovakia)
- **disclosure citation:** AeroMobil 4.0 publicly unveiled 2017-04-20 at Top Marques Monaco; predecessor AeroMobil 3.0 first flew 2014-10-29 (with crash 2015-05-08, pilot Stefan Klein survived; Klein subsequently founded Klein Vision). AeroMobil holds patents on retractable-wing roadable aircraft.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-part-23`, `propulsion-hybrid-parallel`

**Prior art notes:**

> AeroMobil 4.0 is Slovakia's other major drive+fly transformer disclosure (Klein departed AeroMobil after the 3.0 crash and founded Klein Vision). Establishes parallel Slovak prior-art lineage with hybrid-parallel powerplant — distinct from Klein Vision's pure-combustion approach. Combined with klein-vision-aircar, places drive+fly transformer prior art comprehensively in Slovak hands. Anticipates ASKA A5 and all subsequent drive+fly transformer claims.

**Sources:**

1. AeroMobil press releases and Top Marques Monaco 2017 unveiling.
2. AeroMobil patent estate, EUIPO and SUIPO records.
3. Reuters and Aviation Week coverage 2014–2018.

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

### 2020-10 — Klein Vision AirCar

- **id:** `klein-vision-aircar`
- **corpus:** private
- **ip status:** patented
- **creator:** Klein Vision s.r.o (Nitra, Slovakia)
- **disclosure citation:** Klein Vision AirCar Prototype 1 first flight test 2020-10; first inter-airport flight 2021-06-28 (Nitra to Bratislava). Slovak Transport Authority issued Certificate of Airworthiness 2022-01-26 — the world's first roadable-aircraft type certificate. Klein Vision founded by Stefan Klein.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-part-23`

**Prior art notes:**

> Klein Vision AirCar holds the world's first type-certified roadable-aircraft certificate (Slovak Transport Authority, 2022-01-26). Establishes Slovak prior-art lineage and certified-product anchor for the drive+fly transformer category. Not VTOL but architecturally adjacent — many drive+fly eVTOL designs (ASKA A5, AeroMobil 4.0) build on the same retractable-wing transformer architecture pioneered in road-legal aviation by Klein.

**Sources:**

1. Klein Vision press releases 2020–2024.
2. Slovak Transport Authority Certificate of Airworthiness, 2022-01-26.
3. Klein, Stefan. AirCar technical white paper, 2021.

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

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `7e83101`.*
