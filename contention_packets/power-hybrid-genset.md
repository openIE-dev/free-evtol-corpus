---
title: "power-hybrid-genset"
parent: "Invalidity Contentions"
nav_order: 26
layout: default
---

# Invalidity Contention Packet — `power-hybrid-genset`

**Generated:** 2026-05-11  
**Cross-cut tag:** `power-hybrid-genset`  
**Entries:** 11 (11 commons-grade, 0 draft)  
**Earliest disclosure:** 2014-08  
**Most recent disclosure:** 2021-09-30

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `power-hybrid-genset`.

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

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `7e83101`.*
