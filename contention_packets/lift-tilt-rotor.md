---
title: "lift-tilt-rotor"
parent: "Invalidity Contentions"
nav_order: 25
layout: default
---

# Invalidity Contention Packet — `lift-tilt-rotor`

**Generated:** 2026-05-11  
**Cross-cut tag:** `lift-tilt-rotor`  
**Entries:** 23 (23 commons-grade, 0 draft)  
**Earliest disclosure:** 1955-08-11  
**Most recent disclosure:** 2024-01-09

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `lift-tilt-rotor`.

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

### 1985-03 — Mil Mi-30

- **id:** `mil-mi-30`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Mil Moscow Helicopter Plant
- **disclosure citation:** Mil Mi-30 design specification approved by Soviet Ministry of Aviation Industry March 1985; multiple wind-tunnel and design studies completed; cancelled after Soviet collapse 1991 before any prototype built. Design materials in Mil OKB declassified archives.
- **disclosed subsystems:** `cert-military`, `lift-tilt-rotor`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The Mi-30 is the Soviet/Russian tilt-rotor program — designed but not built before USSR dissolution. Establishes Soviet prior-art lineage for tilt-rotor architecture in heavy military configuration (parallel to V-22 development). Combined with kamov-ka-22-vintokryl (1959) and Mi-30 (1985), Soviet/Russian tilt-rotor / convertiplane design materials cover three decades and are comprehensively in the public domain.

**Sources:**

1. Mikheyev, Vadim. OKB Mil. Polygon, 1999.
2. Gunston, Bill. The Osprey Encyclopedia of Russian Aircraft. Osprey, 1995.
3. Mil OKB declassified design materials, RGAE archives.

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

### 1989-04-13 — Helldiver carrier (Patlabor)

- **id:** `patlabor-helldiver`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Headgear / Yutaka Izubuchi (mecha design) / Sunrise / Bandai Visual
- **disclosure citation:** Patlabor: The Mobile Police (機動警察パトレイバー), original video animation first release 1988-04-25; theatrical film Patlabor: The Movie released 1989-04-13. The Helldiver mecha-carrier and other Patlabor flight machines documented in the Patlabor Mechanical Files (Bandai, multiple volumes) and Headgear design archives.
- **disclosed subsystems:** `lift-tilt-rotor`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The Patlabor Helldiver establishes 1989 Japanese fictional prior art for tilt-rotor cargo carrier architecture in cinematic depiction contemporaneous with V-22 Osprey first flight (1989). Yutaka Izubuchi's mecha design notes explicitly reference V-22 lineage. Combined with macross-vf-1-veritech (1982), gundam-gaw (1979), ghost-in-the-shell-tiltrotor (1989), and laputa-flapter (1986), provides comprehensive Japanese fictional prior-art base for tilt-rotor and rotor-craft architectures.

**Sources:**

1. Patlabor: The Movie (機動警察パトレイバー the Movie). Bandai Visual / Sunrise, 1989.
2. Patlabor Mechanical Files. Bandai, multiple volumes 1989-2010.
3. Headgear (Mamoru Oshii / Yutaka Izubuchi / Kazunori Itō / Akemi Takada / Masami Yūki) design archives.

---

### 1989-05 — Section 9 Tilt-Rotor (Ghost in the Shell)

- **id:** `ghost-in-the-shell-tiltrotor`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Masamune Shirow / Mamoru Oshii / Production I.G
- **disclosure citation:** Ghost in the Shell (攻殻機動隊 Kōkaku Kidōtai) manga first appearance Young Magazine, May 1989; Mamoru Oshii anime film 1995-11-18 with highly-detailed tilt-rotor police craft. Subsequent disclosures in Stand Alone Complex (2002) and Innocence (2004) animations and associated visual-design books.
- **disclosed subsystems:** `lift-tilt-rotor`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Ghost in the Shell's Section 9 tilt-rotor is among the most engineering-detailed fictional tilt-rotor depictions. Production I.G design books (multiple editions) include schematic-grade illustrations. Establishes additional Japanese fictional prior art for civilian/police tilt-rotor passenger transport, complementing macross-vf-1-veritech (1982).

**Sources:**

1. Shirow, Masamune. Ghost in the Shell manga, Young Magazine / Kodansha, 1989-1991.
2. Oshii, Mamoru (dir.). Ghost in the Shell. Production I.G, 1995.
3. Ghost in the Shell: Stand Alone Complex Visual Book. Kodansha, 2003.

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

### 2003-03-06 — Bell Eagle Eye TR918

- **id:** `bell-eagle-eye`
- **corpus:** private
- **ip status:** patented
- **creator:** Bell Helicopter Textron / U.S. Coast Guard / U.S. Army
- **disclosure citation:** Bell Eagle Eye first hover 2003-03-06; first transition flight 2003-08-22; full-scale TR918 unveiled at HAI Heli-Expo 2005. U.S. Coast Guard Deepwater program cancellation 2007 ended production but Bell continues design work. Documented in Bell technical papers and Coast Guard procurement records.
- **disclosed subsystems:** `lift-tilt-rotor`, `transition-thrust-borne-to-wing-borne`, `autonomy-pilot-removed`, `cert-military`

**Prior art notes:**

> Bell Eagle Eye is the unmanned-scale tilt-rotor descended from the V-22 program — establishes prior art for: (1) tilt-rotor architecture in unmanned tactical UAV scale, (2) autonomous tilt-rotor mission operation. Together with bell-xv-15, v-22-osprey, bell-v-280-valor, and aerovironment-skytote, places tilt-rotor architecture across the full scale spectrum from small unmanned to large troop transport in comprehensive prior-art coverage.

**Sources:**

1. Bell Helicopter Eagle Eye technical papers, AHS Forum 2003–2008.
2. U.S. Coast Guard Deepwater program records, declassified portions.

---

### 2008 — Karem AR40 / Optimum Speed Tilt-Rotor

- **id:** `karem-ar40`
- **corpus:** private
- **ip status:** patented
- **creator:** Karem Aircraft Inc (Lake Forest, California)
- **disclosure citation:** Karem Aircraft AR40 / Optimum Speed Tilt-Rotor concept publicly disclosed in U.S. Army FVL program documentation 2008-2010; AR40 design materials in DARPA / Army Heavy Lift program filings. Karem holds Optimum Speed Rotor patents covering variable-RPM rotor operation.
- **disclosed subsystems:** `cert-military`, `lift-tilt-rotor`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Karem AR40 establishes prior art for: (1) variable-RPM Optimum Speed Rotor technology (continuously varying rotor RPM with forward speed and altitude for fuel-burn optimization), (2) very-large-payload tilt-rotor architecture. Karem's slowed-rotor patents are cited as prior art in Joby and Archer patent filings around variable-RPM rotor operation. Anticipates modern eVTOL claims around variable-RPM operation for efficiency optimization.

**Sources:**

1. Karem Aircraft technical white papers and patent estate.
2. DARPA / Army Heavy Lift Tilt-Rotor program reports.
3. Karem, Abraham, et al. Karem Aircraft U.S. patent filings.

---

### 2009-12-18 — Samson and Scorpion (Avatar)

- **id:** `avatar-samson-scorpion`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** James Cameron / Lightstorm Entertainment / 20th Century Fox
- **disclosure citation:** Avatar (Avatar: The Way of Water and sequels), directed by James Cameron, theatrical release 2009-12-18. Production designer Robert Stromberg and concept artists at Lightstorm developed detailed engineering depictions of the AT-99 Scorpion and SA-2 Samson, documented in The Art of Avatar (Abrams, 2009).
- **disclosed subsystems:** `lift-tilt-rotor`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Avatar's Scorpion and Samson tilt-rotor gunships establish 2009 fictional cinematic prior art for military tilt-rotor architecture. Production-designed depictions in The Art of Avatar include detailed cutaway schematics. Combined with macross-vf-1-veritech (1982), ghost-in-the-shell-tiltrotor (1989), and bell-xv-15 (1977), provides multi-decade tilt-rotor prior art across both academic / military / commercial real-world programs and fictional cinematic depictions.

**Sources:**

1. Cameron, James (dir.). Avatar. 20th Century Fox, 2009.
2. Fitzpatrick, Lisa. The Art of Avatar. Abrams, 2009.
3. Wilhelm, Maria and Mathison, Dirk. Avatar: A Confidential Report on the Biological and Social History of Pandora. It Books, 2009.

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

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `bff4888`.*
