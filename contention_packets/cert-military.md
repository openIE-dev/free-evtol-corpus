---
title: "cert-military"
parent: "Invalidity Contentions"
nav_order: 10
layout: default
---

# Invalidity Contention Packet — `cert-military`

**Generated:** 2026-05-12  
**Cross-cut tag:** `cert-military`  
**Entries:** 38 (38 commons-grade, 0 draft)  
**Earliest disclosure:** 1941-10-30  
**Most recent disclosure:** 2019-03-21

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `cert-military`.

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

### 1944-09 — Focke-Wulf Triebflügel

- **id:** `focke-wulf-triebflugel`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Focke-Wulf Flugzeugbau / Heinz von Halem (Germany, Luftwaffe contract)
- **disclosure citation:** Focke-Wulf Triebflügel design specification submitted to Reichsluftfahrtministerium 1944-09; never built before WWII end. Design materials captured by Allied technical intelligence (CIOS / BIOS reports) post-war and declassified; documented in Smith and Kay's German Aircraft of the Second World War (1972) and Greenhill Books' Luftwaffe Secret Projects series.
- **disclosed subsystems:** `cert-military`, `lift-tip-jet-rotor`, `propulsion-tip-jet`, `transition-tail-sitter-pitch-up`

**Prior art notes:**

> Focke-Wulf Triebflügel is the foundational German wartime disclosure of tip-jet rotor architecture combined with tail-sitter VTOL. Establishes prior art for: (1) tip-driven rotor (ramjet at blade tip eliminates need for central torque-cancellation gearbox/anti-torque tail rotor — torque-free lift), (2) the tail-sitter / coleopter VTOL lineage in jet/ramjet form. Allied technical intelligence reports post-1945 placed the design comprehensively in the public domain. Anticipates: tip-jet helicopter programs (Mil V-7, Doblhoff WNF 342, Fairey Rotodyne, Hughes XH-17), and any modern attempt to claim novelty over tip-driven rotor architecture.

**Sources:**

1. Smith, J.R. and Kay, Antony. German Aircraft of the Second World War. Putnam, 1972.
2. Allied CIOS (Combined Intelligence Objectives Subcommittee) reports on Luftwaffe projects, post-1945.
3. Schick and Meyer. Luftwaffe Secret Projects: Fighters 1939-1945. Midland, 1997.

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

### 1955-12-10 — Ryan X-13 Vertijet

- **id:** `ryan-x-13-vertijet`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Ryan Aeronautical Company / U.S. Air Force
- **disclosure citation:** Ryan X-13 first conventional flight 1955-12-10 at Edwards AFB; first complete tail-sitting VTOL transition 1957-04-11 (Peter Girard / Ryan, the first complete jet VTOL transition: vertical takeoff from trailer, transition to horizontal flight, transition back, vertical landing). Documented in USAF Flight Test Center reports.
- **disclosed subsystems:** `cert-military`, `lift-vectored-thrust`, `transition-tail-sitter-pitch-up`

**Prior art notes:**

> The Ryan X-13 Vertijet is the first jet aircraft to demonstrate complete tail-sitting VTOL transition. Establishes prior art for: (1) jet-powered tail-sitter VTOL (XFY-1 was turboprop, X-13 is pure jet), (2) reaction-control bleed-jet hover attitude (later essentially identical to Hawker P.1127's reaction-control system), (3) the 'hovering hook' takeoff/landing concept on a vertical trailer. Combined with convair-xfy-pogo and lockheed-xfv-salmon, places jet/turboprop tail-sitter VTOL comprehensively in the public domain by 1957.

**Sources:**

1. USAF Flight Test Center X-13 Vertijet reports.
2. Markman and Holder. Straight Up. Schiffer, 2000.
3. Ryan Aeronautical Company X-13 program archives.

---

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

### 1958 — Curtiss-Wright VZ-7

- **id:** `curtiss-wright-vz-7`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Curtiss-Wright / U.S. Army Transportation Research Command
- **disclosure citation:** U.S. Army Transportation Research Command 'Flying Jeep' program; VZ-7 first flight 1958. Documented in TRC test reports and Markman & Holder, Straight Up (Schiffer 2000).
- **disclosed subsystems:** `cert-military`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`

**Prior art notes:**

> The VZ-7 is one of three contemporaneous U.S. Army 'flying jeep' programs (with the Chrysler VZ-6 and Piasecki VZ-8) that disclosed the modern open-rotor quadrotor architecture in 1958, controlled by differential rotor thrust at the four corners of an X-frame. Establishes a 1958 anchor for: (1) corner-mounted open-rotor quad configuration, (2) cross-shafted single-engine drive of four lift rotors (mechanical analogue of modern electric quadrotors with DC-link power sharing), (3) differential-thrust attitude allocation. Combined with de-bothezat-quadrotor (1922), this places the basic open-rotor quadrotor lift architecture in the public domain a full half-century before any modern multirotor patent attempt. The Hoversurf S3 and Aerofex hover bike as well as Jetson ONE all sit downstream of this disclosure.

**Sources:**

1. Markman, Steve and Holder, Bill. Straight Up. Schiffer, 2000.
2. U.S. Army Transportation Research Command VZ-7 test reports, available DTIC.
3. Lambert, Mark (ed.). Jane's All The World's Aircraft 1959–60.

---

### 1958-02-25 — Doak VZ-4

- **id:** `doak-vz-4`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Doak Aircraft Company / U.S. Army Transportation Research Command
- **disclosure citation:** Doak VZ-4 first VTOL flight 1958-02-25 at Edwards AFB. Documented in U.S. Army Transportation Research Command test reports.
- **disclosed subsystems:** `cert-military`, `lift-tilt-duct`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> First successful tilt-duct VTOL aircraft. Establishes prior art for: (1) wingtip-mounted tilting ducted fans for VTOL, (2) cross-shafted single-engine drive of dual lift fans (critical for engine-out continued lift), (3) the tilt-duct transition methodology with reaction-control supplementation in hover. Anticipates Bell X-22 (1966) tilt-duct claims, and provides foundational prior art for any modern ducted-fan VTOL claiming wingtip tilt-duct architecture (Lilium's ducted-fan-array architecture is a multiplicity extension of this). Combined with Bell X-22, this entry covers the tilt-duct design space for invalidity contention purposes from 1958 forward.

**Sources:**

1. Maisel, Martin D. and Giulianetti, Demo J. The History of the XV-15 Tilt Rotor Research Aircraft. NASA SP-2000-4517, 2000, chapter on VTOL precursors.
2. Markman and Holder. Straight Up. Schiffer, 2000.
3. U.S. Army Transportation Research Command VZ-4 test reports.

---

### 1958-10-12 — Piasecki VZ-8 Airgeep

- **id:** `piasecki-vz-8-airgeep`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Piasecki Aircraft Corporation / U.S. Army Transportation Research Command
- **disclosure citation:** Piasecki VZ-8 Airgeep first flight 1958-10-12 at Piasecki Pennsylvania facility. Sister U.S. Army 'flying jeep' program to Curtiss-Wright VZ-7 and Chrysler VZ-6. Documented in TRC test reports.
- **disclosed subsystems:** `cert-military`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`

**Prior art notes:**

> Piasecki VZ-8 Airgeep is the third major U.S. Army 'flying jeep' program of 1958 (with Curtiss-Wright VZ-7 and Chrysler VZ-6), establishing prior art for: (1) tandem fore-and-aft open-rotor architecture (precursor to Aerofex Aero-X hover-bike geometry by 50 years), (2) cross-coupled twin-piston-engine drive with engine-out continued lift. The hover-bike architecture descends directly from this 1958 disclosure.

**Sources:**

1. U.S. Army Transportation Research Command VZ-8 reports.
2. Piasecki Aircraft Corporation archives.
3. Markman and Holder. Straight Up. Schiffer, 2000.

---

### 1958-12-05 — Avrocar VZ-9

- **id:** `avrocar-vz-9`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Avro Canada / U.S. Army / U.S. Air Force
- **disclosure citation:** Avrocar VZ-9 first untethered hover 1958-12-05 at Avro Canada Malton facility. Declassified by USAF / U.S. Army; reports available through DTIC and the Smithsonian.
- **disclosed subsystems:** `cert-military`, `lift-coanda-effect`

**Prior art notes:**

> The Avrocar is the canonical disclosure of Coandă-effect lift in a heavier-than-air VTOL platform. Establishes prior art for: (1) annular-wing Coandă lift, (2) peripheral-jet thrust vectoring for VTOL attitude and translation, (3) saucer/disc planform with central turbomachinery. Although the program failed to scale due to ground-effect-only stability limits, the disclosure is complete: Avro published full design and test reports declassified between 1990–2010. Filed against any modern Coandă-lift VTOL patent attempt (occasional novelty claims surface in exotic VTOL filings) this is anticipating prior art.

**Sources:**

1. Whitcomb, Randall. Avro Aircraft and Cold War Aviation. Vanwell Publishing, 2002.
2. Murray, Russ. Project Silver Bug: The Top Secret Story of the World's First Flying Saucer. Greenleaf, 2010.
3. Avro Canada VZ-9 final test reports, declassified, available via DTIC.
4. Smithsonian Air & Space Museum, Avrocar VZ-9 collection notes.

---

### 1959-05-06 — SNECMA C.450 Coléoptère

- **id:** `snecma-coleoptere`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** SNECMA
- **disclosure citation:** SNECMA C.450 Coléoptère first free vertical flight 1959-05-06 at Melun-Villaroche; program terminated after fatal crash 1959-07-25. Documented in Aviation Magazine International, French Air Ministry reports, and Markman & Holder.
- **disclosed subsystems:** `cert-military`, `lift-vectored-thrust`, `transition-tail-sitter-pitch-up`

**Prior art notes:**

> The Coléoptère is the canonical disclosure of the annular-wing coleopter VTOL configuration: a tail-sitting fuselage surrounded by a circular wing that doubles as a thrust-augmenting duct. Establishes prior art for: (1) annular-wing tail-sitter architecture, (2) exhaust-vane jet vectoring for hover attitude control, (3) single-engine VTOL with full envelope from hover to cruise. Although the program ended after one fatal accident, the engineering disclosure is complete in published SNECMA documentation. Modern attempts at exotic annular-wing or duct-as-wing VTOL configurations are anticipated by this 1959 disclosure.

**Sources:**

1. Markman and Holder. Straight Up. Schiffer, 2000.
2. SNECMA technical reports on C.450 Coléoptère, French Ministry of Aviation archives.
3. Aviation Magazine International coverage 1958–59.

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

### 1962-07-07 — Lockheed XV-4 Hummingbird

- **id:** `lockheed-xv-4-hummingbird`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Lockheed-Georgia Company / U.S. Army
- **disclosure citation:** Lockheed XV-4A Hummingbird first conventional flight 1962-07-07; first hover 1963-05-24; first transition 1963-11-20. Documented in U.S. Army Aviation Laboratory and NASA Langley reports.
- **disclosed subsystems:** `cert-military`, `lift-vectored-thrust`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Lockheed XV-4 Hummingbird establishes prior art for the ejector-augmenter VTOL architecture: dedicated lift through an air-entrainment ejector that multiplies engine thrust during hover. Although the augmenter approach proved less efficient than direct-lift jets and was not adopted in subsequent VTOL designs, the disclosure is complete in U.S. government documentation. Filed against any modern attempt to claim novelty over thrust-augmenting ejector VTOL configurations, this is anticipating prior art.

**Sources:**

1. U.S. Army Aviation Laboratory XV-4 reports.
2. NASA Langley Research Center XV-4 technical memoranda.
3. Markman and Holder. Straight Up. Schiffer, 2000.

---

### 1964-07 — Yakovlev Yak-36

- **id:** `yak-36-freehand`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Yakovlev Design Bureau
- **disclosure citation:** Yak-36 first untethered hover 1964-07; first complete VTOL transition 1966-09-24; public demonstration at Domodedovo Air Show 1967-07-09. Documented in Yakovlev OKB technical bulletins (post-1991 declassified) and in Gordon's Soviet/Russian VTOL aircraft history.
- **disclosed subsystems:** `cert-military`, `lift-vectored-thrust`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Yak-36 is the Soviet contemporary of Hawker P.1127 — first Soviet VTOL fighter to achieve full transition. Establishes parallel-track Soviet prior art for: (1) twin-engine vectored-thrust VTOL fighter architecture, (2) reaction-control hover puffer jets, (3) the conversion-corridor transition envelope from a different geographic and engineering tradition. Combined with Hawker P.1127 (1960) places vectored-thrust VTOL in two independently-developed prior-art lineages.

**Sources:**

1. Gordon, Yefim. Soviet/Russian VTOL Aircraft. Polygon, 2004.
2. Yakovlev OKB technical bulletins, post-1991 declassified, RGAE archives.
3. Gunston and Gordon. Yakovlev Aircraft Since 1924. Putnam, 1997.

---

### 1964-09-29 — LTV XC-142A

- **id:** `ltv-xc-142`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Ling-Temco-Vought / Hiller / Ryan / U.S. Tri-Service Program (Army, Navy, Air Force)
- **disclosure citation:** LTV XC-142A first conventional flight 1964-09-29 at Dallas; first full transition flight 1965-01-11. Documented in NASA TM and U.S. Air Force Flight Test Center reports.
- **disclosed subsystems:** `cert-military`, `lift-tilt-wing`, `propulsion-bldc-geared`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The XC-142A is the most thoroughly documented tilt-wing aircraft to fly. Establishes prior art for: (1) full-wing tilt with all four propulsors mounted on wing leading edge, (2) cross-shafted multi-engine drive of all lift rotors so any single engine loss does not cause hover lift loss (the eVTOL safety analogue is multiple battery buses powering all rotors), (3) coordinated pilot transition control across the entire conversion corridor. Anticipates: Canadair CL-84, modern eVTOL tilt-wing concepts (e.g., AVX/L3Harris, AeroMobil tilt-wing patents), and any tilt-wing claim asserting novelty over coordinated cross-shafted four-rotor tilt-wing geometry.

**Sources:**

1. NASA TM-X-1842, 'Flight Testing the XC-142A V/STOL Transport,' 1969.
2. Markman and Holder. Straight Up. Schiffer, 2000.
3. Vertica magazine retrospective on tilt-wing programs, Vol 14, 1990.

---

### 1965-05-07 — Canadair CL-84 Dynavert

- **id:** `canadair-cl-84`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Canadair (Bombardier predecessor)
- **disclosure citation:** Canadair CL-84 first flight 1965-05-07; first transition 1966-01-17. Documented in Royal Canadian Air Force / Canadian Forces test reports and Canadair Type 84 program archives.
- **disclosed subsystems:** `cert-military`, `lift-tilt-wing`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The CL-84 is the second tilt-wing aircraft to achieve full transition (after XC-142). Adds to the public-domain disclosure: (1) two-propulsor tilt-wing geometry (simpler than XC-142's four), (2) stern-mounted horizontal rotor for hover pitch trim (alternative to thrust-vectoring rear rotor), (3) achieved over 700 transitions during the program — the most complete tilt-wing transition envelope dataset in the public domain. Combined with LTV XC-142, places the tilt-wing architecture comprehensively in prior art.

**Sources:**

1. Pickler, Ronald and Milberry, Larry. Canadair: The First 50 Years. CANAV Books, 1995.
2. RCAF / Canadian Forces CL-84 test reports.
3. Bombardier corporate archives (Canadair Type 84 program).

---

### 1966-03-17 — Bell X-22A

- **id:** `bell-x-22`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Bell Aerosystems / U.S. Navy / U.S. Air Force / Tri-Service
- **disclosure citation:** Bell X-22A first flight 1966-03-17 at Niagara Falls; first transition from hover to cruise 1966-08-22. NASA, Air Force, and Navy joint test reports widely available.
- **disclosed subsystems:** `cert-military`, `lift-ducted-fan-array`, `lift-tilt-duct`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The X-22A is the most thoroughly tested tilt-duct VTOL aircraft. Establishes prior art for: (1) four-corner tilt-duct architecture, (2) ducted fans as primary lift with cross-shafted multi-engine drive, (3) variable-stability flight research providing 800+ flight hours of transition envelope data published in NASA reports. The X-22's combination of tilt and ducting anticipates modern ducted-fan-array concepts (Lilium Jet's 36 ducted fans is a multiplicity extension of this 4-fan arrangement). Combined with Doak VZ-4 (1958), places tilt-duct architectures comprehensively in the public domain by 1966.

**Sources:**

1. NASA TN D-7095, 'Flight Test Results of the X-22A V/STOL Aircraft,' 1972.
2. Bell Aerospace / Textron X-22 program archives.
3. Markman and Holder. Straight Up. Schiffer, 2000.

---

### 1967-02-10 — Dornier Do 31

- **id:** `dornier-do-31`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** Dornier Flugzeugwerke / German Federal Republic / NATO
- **disclosure citation:** Dornier Do 31E-1 first conventional flight 1967-02-10; first untethered hover 1967-11-22; first transition 1967-12-16. Program funded by West German government and NATO; documented in Dornier company archives, German aviation press 1965–1970, and Markman & Holder.
- **disclosed subsystems:** `cert-military`, `lift-vectored-thrust`, `transition-lift-fan-clutched`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> The Do 31 is the only jet-VTOL transport aircraft to have flown, and the West German contribution to the 1960s VTOL prior-art base. Establishes prior art for: (1) hybrid main-engine-vectored + dedicated-lift-jet architecture (anticipating F-35B's main 3BSM + lift-fan combination by four decades), (2) wingtip-mounted lift-augmentation jets, (3) vectored-thrust V/STOL transport configuration. The Do 31 is foundational anticipation prior art for any modern eVTOL combining cruise-mode propulsion with separate dedicated-lift propulsion.

**Sources:**

1. Markman and Holder. Straight Up. Schiffer, 2000.
2. Dornier Flugzeugwerke Do 31 program reports, Deutsches Museum archives.
3. Hirschel, E.H., Prem, H., Madelung, G. Aeronautical Research in Germany. Springer, 2004.

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

### 1971-09-10 — VFW-Fokker VAK 191B

- **id:** `vfw-fokker-vak-191b`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** VFW-Fokker (Vereinigte Flugtechnische Werke / West Germany)
- **disclosure citation:** VFW-Fokker VAK 191B first conventional flight 1971-09-10; first untethered hover 1971-10-19; first transition flight 1972-10-26. Program funded by West German Ministry of Defence; documented in Bundeswehr archives, BWB technical reports, and German aerospace press 1968-1975.
- **disclosed subsystems:** `cert-military`, `lift-vectored-thrust`, `transition-lift-fan-clutched`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> VFW-Fokker VAK 191B is the second major West German VTOL program (after Dornier Do 31). Establishes additional German prior-art lineage for vectored-thrust strike-aircraft configuration with main-engine + dedicated-lift-jet architecture. Combined with dornier-do-31, hawker-p-1127, and short-sc-1, comprehensively covers the European 1957-1971 vectored-thrust + dedicated-lift-jet design space in public-domain prior art.

**Sources:**

1. VFW-Fokker company archives and Bundeswehr / BWB technical reports.
2. Markman and Holder. Straight Up. Schiffer, 2000.
3. Schick and Meyer. Luftwaffe Secret Projects: Strategic Bombers 1935-1945. Midland, 1997 (provides P.1101 lineage context).

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

### 1982 — Williams X-Jet

- **id:** `williams-x-jet`
- **corpus:** private
- **ip status:** patented
- **creator:** Williams International / U.S. Army / DARPA
- **disclosure citation:** Williams International X-Jet (Williams Aerial Systems Platform) publicly demonstrated 1982-1983 under U.S. Army / DARPA evaluation. Williams International (the small-turbofan specialist) built a single-person standing platform powered by a Williams WR19 turbofan (the same engine class as cruise missiles). Documented in U.S. Army evaluation reports and Williams International materials.
- **disclosed subsystems:** `lift-vectored-thrust`, `cert-military`

**Prior art notes:**

> Williams International's X-Jet establishes prior art for the turbofan-powered standing personal VTOL platform — distinct from rocket-belt (Bell, 1961, ~21 sec endurance), ducted-fan (Hiller VZ-1, 1955), and modern jet-suit (Gravity Industries, 2017) variants by using a single compact turbofan for ~30-minute endurance. Establishes prior art for: (1) turbofan-powered single-person platform, (2) bifurcated-exhaust vane vectoring for personal-VTOL attitude. Williams' 1980s patents are expired. Combined with bell-rocket-belt, hiller-vz-1-pawnee, solotrek-xfv, gravity-industries-jet-suit, and martin-aircraft-jetpack, comprehensively places personal-VTOL platform architecture across rocket / ducted-fan / turbofan / turbojet propulsion in 1955-2017 prior art.

**Sources:**

1. U.S. Army / DARPA Williams Aerial Systems Platform evaluation reports.
2. Williams International corporate history materials.
3. Aviation Week coverage 1982-1983.

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

### 1987-03-09 — Yakovlev Yak-141

- **id:** `yak-141`
- **corpus:** academic
- **ip status:** patented
- **creator:** Yakovlev Design Bureau
- **disclosure citation:** Yak-141 (then Yak-41) first conventional flight 1987-03-09; first hover 1989-12-29; first transition 1990-06-13. Aircraft demonstrated at Farnborough Air Show 1992, with full design disclosure published in Yakovlev technical bulletins and Russian aviation press.
- **disclosed subsystems:** `cert-military`, `lift-vectored-thrust`, `transition-3-bearing-swivel-duct`, `transition-lift-fan-clutched`

**Prior art notes:**

> The Yak-141 is the foundational disclosure of the three-bearing swivel duct (3BSM/3BSD) for supersonic-capable vectored-thrust VTOL. Establishes prior art for: (1) the 3BSM aft-nozzle architecture, in which three rotating duct sections sequence to redirect main engine thrust from horizontal to vertical, (2) lift-jet augmentation forward of the main engine for hover trim and lift, (3) supersonic-capable VTOL airframe geometry. Lockheed Martin's F-35B, which uses an essentially identical 3BSM, descends directly from Yak-141 disclosure: documented technology transfer occurred c. 1995. The 3BSM patents have publicly known origins in Yakovlev work pre-1990.

**Sources:**

1. Gordon, Yefim and Komissarov, Dmitriy. Yakovlev Yak-141 'Freestyle.' Aerofax / Midland, 2008.
2. Yakovlev Design Bureau technical bulletins on Yak-141 / Yak-41M.
3. Bill, Wayne; Boeing/Lockheed F-35 history materials documenting 3BSM provenance.
4. Farnborough Air Show 1992 program materials.

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

### 2007 — Saab Skeldar V-200

- **id:** `saab-skeldar-v-200`
- **corpus:** private
- **ip status:** patented
- **creator:** UMS Skeldar (Saab AB / UMS Aero joint venture)
- **disclosure citation:** Saab Skeldar (originally Saab IsoMatic / Saab AERTEC) first flight 2007; in service with Spanish Armada 2018 and German Bundeswehr 2020. UMS Skeldar joint venture established 2015. Documented in Saab and UMS technical materials and naval procurement disclosures.
- **disclosed subsystems:** `autonomy-pilot-removed`, `cert-military`

**Prior art notes:**

> Saab Skeldar V-200 is Sweden's lead naval VTOL UAV — competitor to Schiebel Camcopter S-100 with similar architectural pattern but Swedish industrial provenance. Adds Saab as Swedish defense industrial prior-art anchor alongside jetson-one (Sweden consumer eVTOL).

**Sources:**

1. Saab AB and UMS Skeldar press releases 2007-2024.
2. Spanish Armada and German Bundeswehr procurement records.

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

### 2013-03-19 — Boeing Phantom Swift

- **id:** `boeing-phantom-swift`
- **corpus:** academic
- **ip status:** patented
- **creator:** Boeing Phantom Works
- **disclosure citation:** Boeing Phantom Swift design publicly disclosed at AHS Forum 2013-05 as Boeing's response to DARPA VTOL X-Plane Phase 1 (2013-03-19). Sub-scale tethered hover demonstrator flown 2014. Boeing did not advance to Phase 3 (Aurora won).
- **disclosed subsystems:** `cert-military`, `lift-ducted-fan-array`, `lift-tilt-duct`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Boeing Phantom Swift is Boeing's response to DARPA VTOL X-Plane (2013) — the architectural mirror to Aurora LightningStrike with hybrid fuselage-internal lift fans + wingtip tilt-ducts. Although not selected for Phase 3, the design disclosure is in the public domain via DARPA program documentation. Establishes additional US prior-art lineage for: (1) hybrid lift-fan + tilt-duct architecture, (2) lockheed-xv-4-hummingbird-style augmenter-wing lift fans in modern tilt-duct context.

**Sources:**

1. Boeing Phantom Works DARPA VTOL X-Plane white papers, 2013–2014.
2. DARPA VTOL X-Plane Phase 1 program reports, DTIC.
3. AHS Forum 2013 papers from Boeing engineering.

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

### 2016-03-03 — Aurora Flight Sciences LightningStrike XV-24A

- **id:** `aurora-lightningstrike-xv-24a`
- **corpus:** academic
- **ip status:** patented
- **creator:** Aurora Flight Sciences (Boeing subsidiary) / DARPA
- **disclosure citation:** Aurora Flight Sciences LightningStrike XV-24A awarded DARPA VTOL X-Plane Phase 3 contract 2016-03-03; sub-scale demonstrator first hover 2017-04. Program subsequently de-scoped without full-scale first flight, but Aurora's design and test data were extensively published in DARPA reports and AIAA papers.
- **disclosed subsystems:** `cert-military`, `control-rotor-failure-reconfiguration`, `lift-distributed-electric-propulsion`, `lift-ducted-fan-array`, `lift-tilt-wing`, `power-hybrid-genset`, `propulsion-hybrid-series`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> Aurora LightningStrike XV-24A is the most architecturally similar prior art to Lilium Jet's 36-fan ducted-fan-array eVTOL — also a tilt-wing distributed-electric-propulsion configuration with embedded ducted lift fans. The XV-24A's 24 ducted fans (2016) anticipate Lilium's 36 (2019) configuration by 3 years and DARPA-funded design publication is fully in the public domain. Establishes US prior-art lineage for: (1) high-multiplicity tilt-wing ducted-fan-array, (2) turbine-electric hybrid powerplant for VTOL, (3) the very-high-rotor-count distributed-electric-propulsion architecture. Filed against any post-2016 patent claim on similar ducted-fan-array tilt-wing configurations, this is anticipating prior art.

**Sources:**

1. Aurora Flight Sciences DARPA VTOL X-Plane technical white papers, 2014–2018.
2. DARPA VTOL X-Plane program reports, available DTIC.
3. AIAA SciTech / Aviation Forum papers from Aurora team 2014–2018.

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

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `d899fde`.*
