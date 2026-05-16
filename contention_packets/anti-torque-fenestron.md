---
title: "anti-torque-fenestron"
parent: "Invalidity Contentions"
nav_order: 4
layout: default
---

# Invalidity Contention Packet — `anti-torque-fenestron`

**Generated:** 2026-05-15  
**Cross-cut tag:** `anti-torque-fenestron`  
**Entries:** 5 (5 commons-grade, 0 draft)  
**Earliest disclosure:** 1967-04-07  
**Most recent disclosure:** 2015-06-13

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `anti-torque-fenestron`.

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

### 1967-04-07 — Aérospatiale SA 341/342 Gazelle

- **id:** `aerospatiale-sa-341-gazelle`
- **corpus:** academic
- **ip status:** patented
- **creator:** Sud Aviation / Aérospatiale (now Airbus Helicopters) / Westland Helicopters
- **disclosure citation:** Sud Aviation SA 340 prototype first flight 1967-04-07 (with a conventional tail rotor); SA 341 Gazelle production prototype with fenestron first flight 1968-04-12; entered French Army (ALAT) service 1971, British Army Air Corps service 1973. ~1,775 produced. The fenestron was first patented by Sud Aviation engineer Paul Fabre in the mid-1960s. Documented in Aérospatiale / Eurocopter technical publications and U.S. Army Foreign Aircraft technical reports.
- **disclosed subsystems:** `lift-coaxial-rotor`, `rotor-articulated`, `anti-torque-fenestron`, `lift-ducted-fan-array`, `cert-part-27`, `cert-military`

**Prior art notes:**

> Aérospatiale SA 341 Gazelle (1967) is the foundational disclosure of the fenestron (ducted-fan anti-torque) system in a production helicopter. Establishes prior art for: (1) ducted-fan-in-fin anti-torque architecture in place of an exposed tail rotor — a critical prior-art anchor for any modern eVTOL claim invoking 'ducted-fan tail rotor', 'shrouded anti-torque', or 'integrated fan-in-fin yaw control', (2) noise reduction and ground-strike-hazard reduction as design drivers for shrouded anti-torque, (3) shroud-aerodynamic lift contribution to anti-torque thrust (the duct itself carries ~30-50% of the total side-force). Sud Aviation/Aérospatiale fenestron patents are long expired. The fenestron is the canonical prior-art reference for all ducted anti-torque rotorcraft and anticipates the same architecture used in many modern eVTOL configurations.

**Sources:**

1. Aérospatiale SA 341/342 Gazelle technical description, Aérospatiale Hélicoptères, 1972.
2. Vuillet, A. and F. Morelli. New Aerodynamic Design of the Fenestron for Improved Performance. 12th European Rotorcraft Forum, 1986.
3. Mowforth, E. (ed.) Westland Gazelle: Britain's Workhorse Light Helicopter. Crécy, 2002.

---

### 1991-04-27 — Eurocopter Tiger / Airbus Tiger

- **id:** `eurocopter-tiger`
- **corpus:** academic
- **ip status:** patented
- **creator:** Eurocopter / Airbus Helicopters (France/Germany joint program)
- **disclosure citation:** Eurocopter Tiger prototype PT1 first flight 1991-04-27 (Marignane, France); entered French Army (ALAT) and German Army (Heer) service 2003. Variants: Tiger HAP (French Anti-Personnel), Tiger HAD (Hélicoptère Appui Destruction), Tiger UHT (German Unterstützungshubschrauber Tiger), Tiger ARH (Australian Armed Reconnaissance). ~190 produced. Documented in Eurocopter / Airbus Helicopters publications.
- **disclosed subsystems:** `lift-coaxial-rotor`, `rotor-hingeless`, `anti-torque-fenestron`, `control-fly-by-wire-triplex`, `airframe-composite-monocoque`, `cert-military`

**Prior art notes:**

> Eurocopter Tiger (1991) is the foundational disclosure of the production composite-airframe attack helicopter with fenestron anti-torque and fly-by-wire flight controls. Establishes prior art for: (1) 80%+ composite airframe at attack-helicopter scale (a critical prior-art anchor for any composite-airframe eVTOL claim), (2) production fenestron anti-torque on a combat rotorcraft (Tiger's fenestron is much larger than the Gazelle's, demonstrating scaling of the architecture), (3) hingeless four-blade composite main rotor with elastomeric bearings on a combat-class helicopter, (4) full fly-by-wire combat-rotorcraft flight controls. Tiger patents are largely expired or near-expiry. Critical anticipation for eVTOL composite-airframe + fenestron + FBW integrated-claim families.

**Sources:**

1. Eurocopter / Airbus Helicopters Tiger / EC-665 publications.
2. French Army / DGA / German Army Tiger service documentation.
3. Jane's All The World's Aircraft, multiple editions — Eurocopter Tiger entries.

---

### 1994-02-15 — Eurocopter EC135 / Airbus H135

- **id:** `eurocopter-ec135`
- **corpus:** academic
- **ip status:** patented
- **creator:** MBB / Eurocopter / Airbus Helicopters
- **disclosure citation:** MBB BO 108 prototype first flight 1988-10-15 (with conventional tail rotor); Eurocopter EC135 fenestron-equipped prototype first flight 1994-02-15; FAA / EASA type-certificated 1996. Over 1,400 produced through 2026 — the dominant European light-twin in police, EMS, corporate, and offshore operations. Documented in MBB / Eurocopter / Airbus Helicopters publications and EASA / FAA type certificate data sheets.
- **disclosed subsystems:** `lift-coaxial-rotor`, `rotor-bearingless`, `rotor-hingeless`, `anti-torque-fenestron`, `cert-part-27`, `cert-military`

**Prior art notes:**

> Eurocopter EC135 / Airbus H135 (1994) is the foundational disclosure of the production bearingless main rotor in a light-twin civil helicopter. Establishes prior art for: (1) bearingless four-blade composite main rotor — no flapping, lead-lag, or feathering bearings, blade root flexes elastically — directly relevant to any modern eVTOL invoking 'flexbeam rotor', 'bearingless lift rotor', or 'composite blade root flex element', (2) production fenestron anti-torque on a light-twin civil helicopter, (3) Part 27 light-twin EMS / police design baseline. Eurocopter bearingless rotor patents are generally expired. Critical anticipation for any eVTOL claim invoking flexbeam or bearingless lift-rotor architecture.

**Sources:**

1. Eurocopter / Airbus Helicopters EC135 / H135 service publications.
2. EASA type certificate R.009 and FAA type certificate data sheets.
3. Schimke, Dietmar et al. The Bearingless Main Rotor — Service Experience and Future Development. European Rotorcraft Forum, 2002.

---

### 1999-06-12 — Eurocopter EC145 / Airbus H145

- **id:** `eurocopter-ec145`
- **corpus:** private
- **ip status:** patented
- **creator:** Eurocopter / Airbus Helicopters / Kawasaki (BK 117 lineage)
- **disclosure citation:** Eurocopter EC145 (BK 117 C-2) first flight 1999-06-12; certified 2002. H145 (BK 117 D-2) first flight 2010-06-12. Five-blade H145 (BK 117 D-3) first flight 2019-10-31, EASA-certified 2020-06-23. The dominant medium-twin in EMS and police operations worldwide, including U.S. Army Lakota (UH-72A/B). Over 1,500 produced. Documented in Eurocopter / Airbus Helicopters publications and EASA / FAA type certificates.
- **disclosed subsystems:** `lift-coaxial-rotor`, `rotor-hingeless`, `rotor-bearingless`, `anti-torque-fenestron`, `cert-part-27`, `cert-military`

**Prior art notes:**

> Eurocopter EC145 / Airbus H145 (1999) is the foundational disclosure of the medium-twin BK-117-derived EMS / police rotorcraft with hingeless rotor (1999) and bearingless five-blade rotor (2019). Establishes prior art for: (1) five-blade composite bearingless main rotor at medium-twin scale (the 2019 H145 D-3 establishes recent production prior art for the five-blade bearingless architecture), (2) shared MBB-Kawasaki BK 117 platform lineage extending across multiple decades of refinement, (3) Part 27 light-twin design baseline directly competing with eVTOL EMS claims. The pre-2014 EC145 patents are largely expired; the H145 five-blade rotor (2019) is recent but the configurational disclosure is now comprehensively in the public record.

**Sources:**

1. Eurocopter / Airbus Helicopters EC145 / H145 service publications.
2. EASA type certificates R.012 / R.502 and FAA type certificate data sheets.
3. U.S. Army UH-72 Lakota program documentation.

---

### 2015-06-13 — Airbus H160

- **id:** `airbus-h160`
- **corpus:** private
- **ip status:** patented
- **creator:** Airbus Helicopters (formerly Eurocopter)
- **disclosure citation:** Airbus Helicopters H160 prototype first flight 2015-06-13 at Marignane; EASA type-certificated 2020-07-01; FAA type-certificated 2022-08-09. H160M Guépard selected as French Joint Forces light helicopter (HIL program), first flight 2025-12-19, entry to service 2027. ~30 produced through 2026 (early production). Documented in Airbus Helicopters publications and EASA / FAA type certificates.
- **disclosed subsystems:** `lift-coaxial-rotor`, `rotor-bearingless`, `rotor-hingeless`, `anti-torque-fenestron`, `airframe-composite-monocoque`, `cert-part-29`, `cert-military`

**Prior art notes:**

> Airbus H160 (2015) is the foundational disclosure of the modern fully-integrated composite medium-twin civil helicopter with Blue Edge double-swept rotor blades, canted fenestron, and biplane horizontal stabilizer. Establishes prior art for: (1) Blue Edge double-swept (forward-then-aft) rotor blade planform — a distinctive acoustic-and-aerodynamic refinement that may be cited as prior art for any eVTOL claim invoking complex rotor blade sweep patterns, (2) canted (non-vertical) fenestron orientation as a noise- and lift-contribution refinement, (3) biplane horizontal stabilizer configuration on a production helicopter (rare; cited as crashworthiness improvement), (4) 100% composite airframe construction at medium-twin scale. H160 patents are active.

**Sources:**

1. Airbus Helicopters H160 / H160M technical publications.
2. EASA type certificate R.521 and FAA type certificate data sheet H10NE.
3. Airbus Helicopters Blue Edge rotor blade public technical communications, 2010-2020.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `9810c15`.*
