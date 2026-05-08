---
title: "lift-tilt-wing"
parent: "Invalidity Contentions"
nav_order: 21
layout: default
---

# Invalidity Contention Packet — `lift-tilt-wing`

**Generated:** 2026-05-08  
**Cross-cut tag:** `lift-tilt-wing`  
**Entries:** 5 (5 commons-grade, 0 draft)  
**Earliest disclosure:** 1964-09-29  
**Most recent disclosure:** 2018-01-31

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `lift-tilt-wing`.

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

### 2014-08 — NASA GL-10 Greased Lightning

- **id:** `nasa-gl-10`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** NASA Langley Research Center
- **disclosure citation:** Fredericks, William J. et al. 'Aerodynamic Characteristics of an Electric Distributed Propulsion Wind Tunnel Model.' AHS International Forum 70, May 2014; subsequent flight test reports through 2015 documented in NASA TM-2017-219653 and related.
- **disclosed subsystems:** `cert-experimental`, `control-rotor-failure-reconfiguration`, `lift-distributed-electric-propulsion`, `lift-tilt-wing`, `power-hybrid-genset`, `propulsion-bldc-direct-drive`, `transition-thrust-borne-to-wing-borne`

**Prior art notes:**

> GL-10 is NASA's foundational disclosure of distributed electric propulsion (DEP) applied to tilt-wing VTOL. Establishes prior art for: (1) ten-rotor wing-distributed electric lift architecture, (2) hybrid genset+battery propulsion topology for VTOL, (3) DEP-specific control allocation including rotor-failure reconfiguration. NASA's publication of GL-10 design and test data is comprehensive and CC-licensed by virtue of being U.S. government work. Anticipates: lift-plus-cruise commercial eVTOLs that use DEP across a wing (Beta Alia, Wisk Cora variants), and any DEP-specific control allocation patents filed post-2014. Combined with X-57 Maxwell, GL-10 places DEP comprehensively in the public domain.

**Sources:**

1. Fredericks, W.J. et al. AHS International Forum 70, May 2014.
2. Fredericks, W.J., Moore, M.D., Busan, R.C. NASA TM-2017-219653.
3. Rothhaar, P.M. et al. 'NASA Langley Distributed Propulsion VTOL Tiltwing Aircraft Simulation Modeling.' AIAA SciTech 2014.

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

### 2018-01-31 — Airbus A^3 Vahana

- **id:** `airbus-vahana`
- **corpus:** private
- **ip status:** patented
- **creator:** Acubed (Airbus Silicon Valley) / Airbus SAS
- **disclosure citation:** Airbus A^3 Vahana sub-scale demonstrator first untethered hover 2018-01-31 at Pendleton OR (Acubed test site); first transition flight 2018-05-15. Vahana flight-test program completed 2019-11 with 138 successful flights. Acubed published Vahana technical papers and design data openly.
- **disclosed subsystems:** `lift-tilt-wing`, `lift-distributed-electric-propulsion`, `transition-thrust-borne-to-wing-borne`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `autonomy-pilot-removed`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> Airbus Vahana is the first fully-autonomous tilt-wing eVTOL to achieve transition flight (2018) — a distinct architectural achievement combining tilt-wing geometry with BLDC distributed electric propulsion and full-autonomy control, all flying 138+ missions in 2018-2019. Establishes prior art for: (1) tilt-wing passenger eVTOL with eight-rotor configuration, (2) full-autonomy transition control across the conversion corridor, (3) production-ready electric tilt-wing flight-control architecture. Acubed published Vahana data openly, putting comprehensive engineering disclosure in the public domain.

**Sources:**

1. Acubed / Airbus A^3 press releases 2018–2019.
2. Vahana flight-test technical papers, Vertical Flight Society Forum 2019–2020.
3. Smith, Zach. 'Vahana: Lessons Learned.' Acubed publication, 2019-11.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision (unknown).*
