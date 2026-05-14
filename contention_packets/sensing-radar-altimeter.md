---
title: "sensing-radar-altimeter"
parent: "Invalidity Contentions"
nav_order: 45
layout: default
---

# Invalidity Contention Packet — `sensing-radar-altimeter`

**Generated:** 2026-05-14  
**Cross-cut tag:** `sensing-radar-altimeter`  
**Entries:** 12 (12 commons-grade, 0 draft)  
**Earliest disclosure:** 2003-03-06  
**Most recent disclosure:** 2024-01-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `sensing-radar-altimeter`.

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

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `7ec5755`.*
