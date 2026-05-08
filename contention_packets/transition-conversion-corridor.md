---
title: "transition-conversion-corridor"
parent: "Invalidity Contentions"
nav_order: 36
layout: default
---

# Invalidity Contention Packet — `transition-conversion-corridor`

**Generated:** 2026-05-08  
**Cross-cut tag:** `transition-conversion-corridor`  
**Entries:** 5 (5 commons-grade, 0 draft)  
**Earliest disclosure:** 1977-05-03  
**Most recent disclosure:** 2018-12-20

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `transition-conversion-corridor`.

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

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision (unknown).*
