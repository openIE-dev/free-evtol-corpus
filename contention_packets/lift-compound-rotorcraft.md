---
title: "lift-compound-rotorcraft"
parent: "Invalidity Contentions"
nav_order: 23
layout: default
---

# Invalidity Contention Packet — `lift-compound-rotorcraft`

**Generated:** 2026-05-12  
**Cross-cut tag:** `lift-compound-rotorcraft`  
**Entries:** 12 (12 commons-grade, 0 draft)  
**Earliest disclosure:** 1923-01-09  
**Most recent disclosure:** 2024-04-25

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `lift-compound-rotorcraft`.

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

### 1923-01-09 — Cierva C.4 autogyro

- **id:** `cierva-autogyro`
- **corpus:** academic
- **ip status:** patented
- **creator:** Juan de la Cierva y Codorníu
- **disclosure citation:** Cierva C.4 first sustained autorotation flight 1923-01-09 at Getafe airfield, Madrid, by Lieutenant Alejandro Gómez Spencer. Cierva published design in Spanish Royal Academy of Sciences proceedings (1923) and held Spanish and British patents covering articulated rotor blade architecture.
- **disclosed subsystems:** `cert-experimental`, `lift-compound-rotorcraft`

**Prior art notes:**

> Cierva's C.4 is the foundational disclosure of articulated rotor blades with flapping hinges — the fundamental enabling invention without which modern rotorcraft (and any eVTOL with articulated blade roots) would not function. Establishes prior art for: (1) flapping-hinge articulated rotor blade design (the patent that made all subsequent rotorcraft possible), (2) compound rotorcraft architecture (forward thrust separate from rotor lift, anticipating modern compound rotorcraft like Fairey Rotodyne, Jaunt Journey, and Sikorsky Raider/Defiant). Cierva patents are long expired; the architectural disclosure is in the public domain.

**Sources:**

1. Cierva, Juan de la. Wings of Tomorrow. McBride, 1931.
2. Brooks, Peter W. Cierva Autogiros: The Development of Rotary-Wing Flight. Smithsonian, 1988.
3. Charnov, Bruce H. From Autogiro to Gyroplane. Praeger, 2003.

---

### 1943-05 — Doblhoff WNF 342

- **id:** `doblhoff-wnf-342`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Friedrich Doblhoff / Wiener Neustädter Flugzeugwerke
- **disclosure citation:** Doblhoff WNF 342 first hover 1943-05; first transition flight 1944-09. Captured by Allied forces 1945; Doblhoff subsequently emigrated to USA and worked at McDonnell on tip-jet helicopters (1947-1956). Documented in Allied technical intelligence reports and McDonnell tip-jet program archives.
- **disclosed subsystems:** `cert-military`, `lift-compound-rotorcraft`, `lift-tip-jet-rotor`, `propulsion-tip-jet`

**Prior art notes:**

> Doblhoff WNF 342 is the first tip-jet rotor helicopter to fly. Establishes prior art for: (1) tip-jet rotor propulsion in working form (predates Focke-Wulf Triebflügel's tip-ramjet by months but with simpler combustion-burner-at-tip architecture), (2) compound rotorcraft architecture switching between hover (rotor powered by tip-burners) and cruise (rotor autorotates, forward thrust via tractor propeller), (3) the no-anti-torque-tail-rotor architecture via tip-driven rotor. Doblhoff's emigration to McDonnell carried the technology directly into the U.S. tip-jet helicopter lineage.

**Sources:**

1. Allied technical intelligence reports on WNF 342, 1945.
2. Smith and Kay. German Aircraft of the Second World War. Putnam, 1972.
3. McDonnell tip-jet helicopter program archives, post-1947.

---

### 1957-11-06 — Fairey Rotodyne

- **id:** `fairey-rotodyne`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Fairey Aviation Company / British European Airways
- **disclosure citation:** Fairey Rotodyne first flight 1957-11-06 at Boscombe Down; first transition (helicopter mode to autorotation cruise) 1958-04-10. Set FAI compound-rotorcraft world speed record 307 km/h on 1959-01-05. Program cancelled 1962. Documented in BEA / Fairey company archives and U.K. Ministry of Aviation reports.
- **disclosed subsystems:** `lift-compound-rotorcraft`, `lift-tip-jet-rotor`, `propulsion-tip-jet`, `cert-experimental`

**Prior art notes:**

> The Fairey Rotodyne is the UK's foundational compound-rotorcraft + tip-jet disclosure — production-scale (48-passenger) tip-burner rotor with autorotation cruise mode, holding the world compound-rotorcraft speed record. Establishes prior art for: (1) production-scale compound-rotorcraft architecture, (2) tip-burner rotor with auxiliary turboprop cruise, (3) the conversion-mode-shutdown (rotor powered in hover, autorotates in cruise) pattern that modern lift+cruise eVTOL adopt in electric form. Combined with doblhoff-wnf-342 and mil-v-7-tarakan, comprehensively places tip-jet rotor compound-rotorcraft in 1943-1957 prior art.

**Sources:**

1. Wood, Derek. The Project Cancelled: The Disaster of Britain's Abandoned Aircraft Projects. Macdonald & Jane's, 1975.
2. BEA / Fairey Aviation archives.
3. Markman and Holder. Straight Up. Schiffer, 2000.

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

### 1976-10-12 — Sikorsky S-72 RSRA

- **id:** `sikorsky-s-72-rsra`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Sikorsky Aircraft / NASA / U.S. Army
- **disclosure citation:** Sikorsky S-72 RSRA first flight 1976-10-12 at Sikorsky Stratford CT; delivered to NASA Ames 1976. Two prototypes built; flew through 1980s as test-bed for rotor system research. Documented in NASA technical reports.
- **disclosed subsystems:** `lift-compound-rotorcraft`, `cert-experimental`

**Prior art notes:**

> The Sikorsky S-72 RSRA is the foundational compound-rotorcraft research aircraft of the modern era — designed specifically as a platform to test alternative rotor systems and compound-rotorcraft configurations. Most significantly, the RSRA included a unique ejection capability for the entire rotor system (allowing the rotor to be jettisoned and the aircraft to land as a fixed-wing aircraft) — establishing prior art for: (1) compound-rotorcraft test platforms, (2) rotor-jettison emergency systems, (3) the research methodology that produced subsequent compound-rotorcraft (Sikorsky X2, S-97 Raider, SB>1 Defiant).

**Sources:**

1. NASA Technical Memoranda on RSRA, multiple 1977–1985.
2. Sikorsky Aircraft S-72 program archive.

---

### 1979-12-15 — Cagliostro autogyro (Lupin III)

- **id:** `cagliostro-autogyro`
- **corpus:** fictional
- **ip status:** fictional
- **creator:** Hayao Miyazaki / TMS Entertainment / Tokyo Movie Shinsha
- **disclosure citation:** Lupin III: Castle of Cagliostro (ルパン三世 カリオストロの城), directed by Hayao Miyazaki, theatrical release 1979-12-15 in Japan. The autogyro chase and rescue sequence is one of the most-celebrated depictions of fictional rotorcraft. Production materials in the Castle of Cagliostro design archive (TMS Entertainment).
- **disclosed subsystems:** `lift-compound-rotorcraft`

**Prior art notes:**

> Miyazaki's Castle of Cagliostro autogyro establishes Japanese fictional prior art for autogyro architecture in cinematic depiction (the autogyro chase sequence is one of the most-detailed fictional rotorcraft action depictions). Combined with cierva-autogyro (1923 real) and pal-v-liberty (2024 commercial), provides century-spanning autogyro prior-art base.

**Sources:**

1. Miyazaki, Hayao (dir.). Lupin III: Castle of Cagliostro / ルパン三世 カリオストロの城. TMS Entertainment, 1979.
2. Yamamoto, Kotori. The Castle of Cagliostro: Reference Design Materials. Tokuma Shoten, multiple editions.
3. Miyazaki, Hayao. Starting Point: 1979-1996. VIZ Media, 2009.

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

### 2010-09-06 — Eurocopter X3

- **id:** `eurocopter-x3`
- **corpus:** private
- **ip status:** patented
- **creator:** Eurocopter (later Airbus Helicopters)
- **disclosure citation:** Eurocopter X3 first flight 2010-09-06 at Istres, France; set an unofficial rotorcraft speed record of 472 km/h (255 kt) in level flight 2013-06-07. The X3 demonstrated the compound-helicopter architecture (main rotor + wing-mounted forward-thrust propellers) as a practical high-speed configuration. Documented in Eurocopter / Airbus Helicopters technical papers and AHS/VFS Forum publications.
- **disclosed subsystems:** `lift-compound-rotorcraft`, `cert-experimental`

**Prior art notes:**

> The Eurocopter X3 establishes French/European prior art for the modern compound-helicopter architecture: a single main rotor for lift plus wing-mounted forward-thrust propellers that also provide anti-torque via differential thrust (no tail rotor). The 472 km/h speed record (2013) demonstrated the configuration's high-speed capability. Establishes prior art for: (1) main-rotor + wing-mounted lateral-propeller compound architecture, (2) differential-lateral-propeller-thrust anti-torque (replacing the tail rotor), (3) wing-offloading of the main rotor in cruise. Direct ancestor of the Airbus RACER (2022). Together with fairey-rotodyne (1957), sikorsky-boeing-defiant (2019), sikorsky-s-97-raider (2015), and airbus-racer (2022), comprehensively places compound-rotorcraft architecture in prior art.

**Sources:**

1. Eurocopter / Airbus Helicopters X3 technical papers, AHS/VFS Forums 2011-2015.
2. Fédération Aéronautique Internationale records / Airbus speed-record documentation 2013.

---

### 2012-04-01 — PAL-V Liberty

- **id:** `pal-v-liberty`
- **corpus:** private
- **ip status:** patented
- **creator:** PAL-V International B.V. (Raamsdonksveer, Netherlands)
- **disclosure citation:** PAL-V One prototype first flight 2012-04-01; PAL-V Liberty production design unveiled 2017-03-07 at Geneva Motor Show; received EASA Type Certificate Part 27 (CS-27) for autogyro mode 2024-04-29. PAL-V founded 2008 by John Bakker.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-part-27`, `lift-compound-rotorcraft`

**Prior art notes:**

> PAL-V Liberty is the Netherlands' lead drive+fly transformer — architecturally distinct from Slovak peers (Klein/AeroMobil) by using autogyro lift rather than fixed-wing flight. Holds EASA Type Certificate Part 27 (autogyro mode), 2024-04-29 — the world's first type-certified flying car under autogyro classification. Direct architectural descendant of Cierva autogyro (1923) in road-legal passenger form factor.

**Sources:**

1. PAL-V press releases 2008–2024.
2. EASA Type Certificate Part 27, 2024-04-29 (PAL-V Liberty).
3. PAL-V technical white papers and patent filings.

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

### 2024-04-25 — Airbus RACER

- **id:** `airbus-racer`
- **corpus:** private
- **ip status:** patented
- **creator:** Airbus Helicopters / Clean Sky 2 (EU Horizon programme)
- **disclosure citation:** Airbus RACER first flight 2024-04-25 at Marignane, France; developed under the EU Clean Sky 2 / Clean Aviation programme (announced 2017, rolled out 2023, first flight 2024). Production-track successor to the Eurocopter X3 demonstrator. Documented in Airbus Helicopters / Clean Sky technical materials.
- **disclosed subsystems:** `lift-compound-rotorcraft`, `cert-experimental`

**Prior art notes:**

> The Airbus RACER is the production-track European compound-helicopter demonstrator (first flight 2024). Refines the Eurocopter X3 architecture with a box-wing carrying lateral cruise/anti-torque propellers and an engine eco-mode (one engine shut down in cruise). Establishes prior art for: (1) box-wing compound-helicopter configuration, (2) eco-mode engine shutdown in compound rotorcraft cruise. Together with eurocopter-x3 (2010) and the Sikorsky compound-rotorcraft lineage, comprehensively places compound-rotorcraft architecture in 1957-2024 prior art.

**Sources:**

1. Airbus Helicopters / Clean Sky 2 RACER technical materials 2017-2024.
2. Airbus press release, RACER first flight, 2024-04-25.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `d899fde`.*
