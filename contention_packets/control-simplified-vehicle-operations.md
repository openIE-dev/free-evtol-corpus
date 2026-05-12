---
title: "control-simplified-vehicle-operations"
parent: "Invalidity Contentions"
nav_order: 19
layout: default
---

# Invalidity Contention Packet — `control-simplified-vehicle-operations`

**Generated:** 2026-05-12  
**Cross-cut tag:** `control-simplified-vehicle-operations`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2018-10-25  
**Most recent disclosure:** 2018-12-20

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `control-simplified-vehicle-operations`.

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

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `d899fde`.*
