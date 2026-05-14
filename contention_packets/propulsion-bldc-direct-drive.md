---
title: "propulsion-bldc-direct-drive"
parent: "Invalidity Contentions"
nav_order: 38
layout: default
---

# Invalidity Contention Packet — `propulsion-bldc-direct-drive`

**Generated:** 2026-05-14  
**Cross-cut tag:** `propulsion-bldc-direct-drive`  
**Entries:** 60 (60 commons-grade, 0 draft)  
**Earliest disclosure:** 2011-10-21  
**Most recent disclosure:** 2024-04-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `propulsion-bldc-direct-drive`.

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

### 2011-10-21 — e-volo VC1 (Volocopter precursor)

- **id:** `volocopter-vc1`
- **corpus:** private
- **ip status:** patented
- **creator:** e-volo GmbH (later Volocopter GmbH)
- **disclosure citation:** e-volo / Stephan Wolf, Thomas Senkel, Alexander Zosel: first manned multicopter flight, 2011-10-21 at Karlsruhe-Forchheim airfield; documented in DLR aviation news and academic press.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-experimental`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`, `power-li-po`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`

**Prior art notes:**

> The e-volo VC1 is the first manned electric multicopter to achieve flight, predating EHang, Joby S2/S4, and Volocopter VoloCity. Establishes prior art for: (1) electric manned multicopter passenger air-mobility architecture, (2) sixteen-rotor circular lift configuration with differential-thrust attitude control, (3) the underlying Volocopter patent family (DE102010032217 and continuations). Anticipates virtually all current commercial electric multirotor air-taxi claims (EHang EH216, Volocopter VoloCity, Hyundai Supernal multirotor configurations).

**Sources:**

1. Senkel, T., Zosel, A., Wolf, S. e-volo flight test reports, 2011.
2. Volocopter GmbH patent family, esp. DE102010032217.
3. DLR magazine coverage 2011–2012 of first manned multicopter flight.

---

### 2012 — Flying Whales LCA60T

- **id:** `flying-whales-lca60t`
- **corpus:** private
- **ip status:** patented
- **creator:** Flying Whales (Bordeaux, France) — backed by the French state and Quebec
- **disclosure citation:** Flying Whales (founded 2012 in Bordeaux, originally to support French national forestry log extraction) developing the LCA60T — a rigid airship designed to carry 60 tonnes of cargo with load/unload while hovering (no landing required). Backed by Bpifrance, the Nouvelle-Aquitaine region, the government of Quebec, and ADP (Aéroports de Paris). First flight targeted ~2027. Documented in Flying Whales technical materials and French government investment disclosures.
- **disclosed subsystems:** `lift-buoyant-hybrid`, `lift-distributed-electric-propulsion`, `propulsion-hybrid-series`, `propulsion-bldc-direct-drive`, `cert-part-23`

**Prior art notes:**

> Flying Whales LCA60T establishes French prior art for the heavy-lift cargo airship with hover-mode load/unload — a 60-tonne-capacity rigid airship with 32 distributed electric propellers, designed to deliver cargo from a stationary hover without landing or ground infrastructure. Establishes prior art for: (1) heavy-lift buoyant-hybrid cargo architecture, (2) distributed-electric-propeller precision hover on a large airship, (3) crane-mode hovering cargo delivery. Together with lta-research-pathfinder-1 and hybrid-air-vehicles-airlander-10, establishes the modern hybrid-airship / buoyant-VTOL prior-art base. Adds another French entry alongside the Eurocopter X3 / Airbus RACER compound-helicopter lineage and the SNECMA / Cyrano / Verne French VTOL heritage.

**Sources:**

1. Flying Whales technical materials and press releases 2012-2025.
2. Bpifrance / Nouvelle-Aquitaine / government of Quebec investment disclosures.
3. Flying Whales patent filings, INPI / EPO records.

---

### 2013-01-31 — Bitcraze Crazyflie

- **id:** `bitcraze-crazyflie`
- **corpus:** open
- **ip status:** open-permissive
- **creator:** Bitcraze AB
- **disclosure citation:** Bitcraze Crazyflie 1.0 publicly released 2013-01-31 as open hardware (BSD/CERN-OHL licensed); subsequent Crazyflie 2.X (2016) widely adopted in academic robotics research. Hardware design files openly published at github.com/bitcraze. Founded by Arnaud Taffanel, Tobias Antonsson, and Marcus Eliasson.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `propulsion-bldc-direct-drive`, `cert-experimental`

**Prior art notes:**

> Bitcraze Crazyflie is the canonical open-hardware micro-quadrotor reference platform — used in 1000+ academic papers and hundreds of university research labs worldwide as the standard small-quadrotor experimental platform. Establishes Swedish prior art for open-hardware quadrotor design and substantially places small-quadrotor architecture in the open-hardware public domain via CERN-OHL/BSD/GPL licensing. Combined with ardupilot-quadplane and px4-vtol, comprehensively places open-source / open-hardware multirotor design in prior art.

**Sources:**

1. Bitcraze AB Crazyflie repository, github.com/bitcraze.
2. Honegger, D. et al. 'An Open Source Indoor Visual Odometry.' ICRA 2013.
3. Multiple academic papers using Crazyflie as research platform 2013-2024.

---

### 2014-06 — Malloy Aeronautics Hoverbike / US Army JTARV

- **id:** `malloy-aeronautics-hoverbike`
- **corpus:** private
- **ip status:** patented
- **creator:** Malloy Aeronautics (United Kingdom; founder Chris Malloy, Australian) — later partnered with SURVICE Engineering / U.S. Army; acquired by BAE Systems 2024
- **disclosure citation:** Malloy Aeronautics publicly unveiled the Hoverbike (a quadcopter straddle vehicle) at Paris Air Show 2014; partnered with SURVICE Engineering for the U.S. Army's Joint Tactical Aerial Resupply Vehicle (JTARV) programme 2015; the cargo variant became the TRV-150 Tactical Resupply UAS for the U.S. Marine Corps. Malloy Aeronautics acquired by BAE Systems 2024. Documented in Malloy materials and U.S. Army/USMC contract records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `autonomy-pilot-removed`, `cert-military`

**Prior art notes:**

> Malloy Aeronautics' Hoverbike / U.S. Army JTARV / USMC TRV-150 establishes prior art for the four-ducted-rotor hover-bike-and-cargo-quad family that reached U.S. military service — the crewed Hoverbike and the uncrewed TRV-150 cargo variant on a shared four-ducted-rotor airframe. Establishes prior art for: (1) ducted-rotor hover-bike architecture, (2) crewed-and-uncrewed variants on a common airframe, (3) operational military deployment of a hover-bike-class platform. Acquired by BAE Systems 2024. Together with aerofex-aero-x (2008), hoversurf-s3 (2017), jetpack-aviation-speeder (2021), and the historical personal-platform anchors, comprehensively places hover-bike architecture in commercial and military prior art. (Note: the Malloy TRV-150 is closely related to but distinct from the Skyways/Orb Aerospace TRV-150 lineage — both used the 'TRV-150' designation for USMC tactical-resupply VTOL.)

**Sources:**

1. Malloy Aeronautics Hoverbike / TRV-150 technical materials 2014-2024.
2. U.S. Army JTARV / USMC TRV-150 Tactical Resupply UAS contract records.
3. BAE Systems acquisition of Malloy Aeronautics, 2024.

---

### 2014-07 — H3 Dynamics HyFly hydrogen-electric eVTOL

- **id:** `h3-dynamics-hyfly`
- **corpus:** private
- **ip status:** patented
- **creator:** H3 Dynamics (Singapore) / H3 Dynamics SAS (France)
- **disclosure citation:** H3 Dynamics founded 2014-07 in Singapore by Taras Wankewycz; hydrogen fuel-cell UAS commercialized starting 2019; H3 Dynamics demonstrated long-endurance hydrogen UAS at Singapore Airshow 2022 and 2024.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `propulsion-hydrogen-fuel-cell`, `propulsion-bldc-direct-drive`, `control-differential-thrust-attitude`, `cert-easa-special-condition-vtol`

**Prior art notes:**

> H3 Dynamics establishes Singapore prior art for hydrogen-fuel-cell VTOL UAS. The Singapore/France dual-headquarters structure is increasingly common for aerospace startups operating across multiple regulatory regimes. Adds Singapore to the eVTOL OEM map and establishes hydrogen-electric VTOL architecture prior art alongside AMSL Vertiia (AU passenger-class hydrogen).

**Sources:**

1. H3 Dynamics press releases 2014-2024.
2. Singapore Airshow 2022 and 2024 exhibitor materials.

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

### 2015-08 — Joby S2

- **id:** `joby-s2`
- **corpus:** private
- **ip status:** patented
- **creator:** Joby Aviation (Santa Cruz, California)
- **disclosure citation:** Joby S2 design publicly disclosed by JoeBen Bevirt and Joby Aviation August 2015 (technical white paper and Vertical Flight Society Forum presentation); first untethered transition flight 2017-08. The single-pilot predecessor that established Joby Aviation's six-rotor tilt-rotor architecture later scaled up for the S4 production design. Documented in Joby technical white papers and AHS/VFS Forum presentations 2015-2018.
- **disclosed subsystems:** `lift-tilt-rotor`, `lift-distributed-electric-propulsion`, `transition-thrust-borne-to-wing-borne`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> Joby Aviation's S2 (2015) is the architectural prototype for Joby's six-tilt-rotor distributed-electric-propulsion eVTOL — establishing the 4-wing + 2-stabilator tilt-rotor configuration two years before the public S4 unveil (joby-s4, 2018) and anchoring the Joby Aviation patent estate priority chain. The 2015 disclosure makes Joby's architectural choices public prior art before any patent dates that depend on the S4 disclosure date. Important for invalidity-contention purposes: any Joby patent claiming priority later than 2015 against S2-disclosed elements has prior art from Joby's own earlier disclosure.

**Sources:**

1. Bevirt, JoeBen et al. Joby S2 technical white paper, 2015.
2. Joby Aviation S-1 SEC filing 2020 (history section).
3. Vertical Flight Society Forum technical papers from Joby engineering 2015-2018.

---

### 2016-06-17 — NASA X-57 Maxwell

- **id:** `nasa-x-57-maxwell`
- **corpus:** academic
- **ip status:** public-domain
- **creator:** NASA Armstrong Flight Research Center / Empirical Systems Aerospace (ESAero)
- **disclosure citation:** NASA X-57 Maxwell publicly designated 2016-06-17; foundational design papers by Borer, Patterson et al. published 2014–2018. Program experimental flight test cancelled before powered flight 2023-06-23 due to budget constraints, but design and ground-test data are comprehensively documented in NASA TM and TP series.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-experimental`

**Prior art notes:**

> NASA X-57 Maxwell is the foundational disclosure of distributed electric propulsion (DEP) for fixed-wing aircraft — the 'high-lift blown-wing' approach where many small electric propellers along the wing leading edge augment wing circulation. Although STOL rather than VTOL, X-57 establishes prior art for: (1) high-multiplicity DEP architecture (12 leading-edge propellers + 2 wingtip), (2) BLDC direct-drive propulsion at scale, (3) lithium-ion battery propulsion at certified-aircraft scale. Combined with NASA GL-10 (2014, VTOL DEP), comprehensively places DEP architecture in U.S. government public-domain prior art for both fixed-wing and VTOL applications. Cited extensively in commercial eVTOL technical white papers as the canonical DEP design reference.

**Sources:**

1. Borer, N.K., Patterson, M.D. et al. 'Design and Performance of the NASA SCEPTOR Distributed Electric Propulsion Flight Demonstrator.' AIAA SciTech 2016.
2. NASA TM-2017-219653, NASA TP-2018-219898, and many other X-57 / SCEPTOR papers.
3. NASA Armstrong Flight Research Center X-57 program archive.

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

### 2017 — Alauda Aeronautics Airspeeder (Mk3 / Mk4)

- **id:** `alauda-airspeeder`
- **corpus:** private
- **ip status:** patented
- **creator:** Alauda Aeronautics / Airspeeder (Adelaide, Australia) / Matthew Pearson
- **disclosure citation:** Alauda Aeronautics (founded 2016 in Adelaide by Matthew Pearson) developed the Airspeeder racing eVTOL — the Mk3 (uncrewed remote-piloted racer, first flew 2021, raced in the 'EXA Series' 2022) and the Mk4 (crewed racer, unveiled 2022, designed for the manned Airspeeder Grand Prix). The world's first eVTOL racing series. Documented in Alauda/Airspeeder materials and Australian CASA filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> Alauda Aeronautics' Airspeeder (Mk3 uncrewed 2021, Mk4 crewed 2022) establishes Australian prior art for the racing eVTOL — a high-power-to-weight single-seat (or uncrewed) octocopter designed for close-formation pylon racing, the world's first eVTOL racing series. Establishes prior art for: (1) racing-tuned eVTOL flight envelope and aggressive-maneuvering control, (2) the racing-eVTOL operational concept, (3) crewed/uncrewed variants on a racing airframe. Together with amsl-vertiia (AU, hydrogen passenger eVTOL), deepens Australia's eVTOL footprint. The racing-eVTOL niche is a distinct application alongside passenger air taxi, cargo, personal, and military eVTOL — and Airspeeder is its foundational disclosure.

**Sources:**

1. Alauda Aeronautics / Airspeeder Mk3 / Mk4 technical materials 2017-2024.
2. Airspeeder EXA Series race records 2022.
3. Australian CASA (Civil Aviation Safety Authority) Airspeeder filings.

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

### 2017-03-07 — Airbus Pop.Up / Pop.Up Next

- **id:** `airbus-popup`
- **corpus:** private
- **ip status:** patented
- **creator:** Airbus / Italdesign / Audi
- **disclosure citation:** Airbus Pop.Up modular ground-and-air mobility concept unveiled 2017-03-07 at the Geneva International Motor Show, by Airbus and Italdesign (Volkswagen Group / Audi subsidiary); Pop.Up Next (adding Audi as full partner) unveiled 2018-03-06 at Geneva. Documented in Airbus and Italdesign press materials and design patents. The system is a passenger capsule that docks to either a ground-vehicle skateboard module or a quadrotor air module.
- **disclosed subsystems:** `lift-modular-docking`, `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `autonomy-pilot-removed`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`

**Prior art notes:**

> Airbus Pop.Up / Pop.Up Next (Airbus + Italdesign + Audi, 2017-2018) is the foundational commercial disclosure of the modular-docking passenger-mobility concept: a passenger capsule that docks to either a ground-vehicle module or an air module (a large coaxial-octorotor frame), with the air module lifting the docked capsule mid-journey. Establishes prior art for: (1) modular passenger-capsule + interchangeable-propulsion-module architecture, (2) in-journey transfer of a passenger pod between ground and air carriers, (3) the multi-modal modular-mobility thesis. Together with xpeng-aeroht-modular (2024), bell-apt (2018), and the academic modular-aerial-robot lineage (eth-distributed-flight-array, upenn-modquad), comprehensively places modular-docking eVTOL architecture in commercial and academic prior art from 2010 forward.

**Sources:**

1. Airbus press release, 'Pop.Up: the modular ground-and-air passenger concept vehicle system,' 2017-03-07.
2. Italdesign / Audi Pop.Up Next materials, Geneva Motor Show 2018.
3. Airbus / Italdesign Pop.Up design patents, EUIPO records.

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

### 2017-04-28 — Hoversurf Scorpion-3

- **id:** `hoversurf-s3`
- **corpus:** private
- **ip status:** patented
- **creator:** Hoversurf Inc (Russia / United States)
- **disclosure citation:** Hoversurf Scorpion-3 prototype publicly unveiled 2017-04-28 in Moscow; first paying customer (Dubai Police) publicly disclosed 2017-10-13; FAA Part 103 Special Light-Sport Aircraft compliance evaluation 2018. Hoversurf founded 2014 by Alexander Atamanov.
- **disclosed subsystems:** `cert-part-103-ultralight`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`

**Prior art notes:**

> Hoversurf Scorpion-3 is the leading commercial hover-bike — Russian-founded company with US operations, sold to Dubai Police as the first operational hover-bike patrol vehicle (2017). Establishes Russian prior-art lineage for the hover-bike form factor and confirms operational deployment pre-2018.

**Sources:**

1. Hoversurf press releases 2017–2024.
2. Dubai Police adoption announcement 2017-10-13.
3. FAA Part 103 ultralight registration records.

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

### 2018 — Skygauge Robotics inspection drone

- **id:** `skygauge-robotics`
- **corpus:** private
- **ip status:** patented
- **creator:** Skygauge Robotics (Toronto, Canada)
- **disclosure citation:** Skygauge Robotics (founded 2018 in Toronto by Maks Zubko and Linar Ismagilov) developed a tilting-rotor industrial-inspection drone capable of stable contact with vertical surfaces; first commercial deployment 2021. Designed for ultrasonic-thickness inspection of tall industrial structures (oil storage tanks, refineries, pressure vessels). Documented in Skygauge materials and Canadian industrial-inspection records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-fully-actuated-omnidirectional`, `lift-tilt-rotor`, `propulsion-bldc-direct-drive`, `cert-easa-special-condition-vtol`

**Prior art notes:**

> Skygauge Robotics (CA 2018-) establishes Canadian prior art for the tilting-arm quadrotor industrial-inspection drone — independently-tilting rotor arms enabling controlled horizontal thrust during hover for contact-based surface inspection (ultrasonic thickness measurement on industrial structures). Smaller-scale industrial counterpart to Voliro (CH, omnidirectional hexrotor inspection). Adds Canadian depth alongside Jaunt Air Mobility (slowed-rotor compound eVTOL), Horizon Aircraft Cavorite X5 (fan-in-wing eVTOL), and the Avro Canada Avrocar heritage.

**Sources:**

1. Skygauge Robotics technical materials 2018-2024.
2. Skygauge Robotics patent filings, Canadian Intellectual Property Office and USPTO.

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

### 2018-07-12 — Pivotal Helix (formerly Opener BlackFly)

- **id:** `pivotal-blackfly`
- **corpus:** private
- **ip status:** patented
- **creator:** Opener Inc / Pivotal LLC
- **disclosure citation:** Opener / BlackFly publicly unveiled 2018-07-12 with first flight video and FAA Part 103 ultralight categorization; subsequent customer deliveries 2022 (Pivotal Helix branding 2023).
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-part-103-ultralight`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `transition-tail-sitter-pitch-up`

**Prior art notes:**

> Pivotal Helix (formerly Opener BlackFly) is a single-pilot tail-sitter eVTOL operating under FAA Part 103 ultralight rules — the first commercially-delivered eVTOL in the U.S. market. Architecturally a tail-sitter (descended from XFY-1 Pogo, 1954) with eight distributed electric rotors. Establishes prior art for: (1) eight-rotor tail-sitter eVTOL geometry, (2) Part 103 ultralight-class commercial eVTOL deployment basis, (3) the design tradeoff of pilot pitch reorientation as an alternative to tilt-rotor or tilt-wing transition mechanisms.

**Sources:**

1. Opener Inc press releases 2018-07-12 onward.
2. Pivotal LLC product disclosures and FAA Part 103 ultralight registrations.
3. Page, Marcus et al. US Patent 11,066,162 (Opener).

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

### 2018-08 — Bell APT (Autonomous Pod Transport)

- **id:** `bell-apt`
- **corpus:** private
- **ip status:** patented
- **creator:** Bell Textron
- **disclosure citation:** Bell APT (Autonomous Pod Transport) publicly disclosed August 2018; APT 70 (70 lb / ~32 kg payload variant) first flight 2019-08; demonstrated package delivery and NASA UTM integration trials 2020-2021. Documented in Bell Textron press materials, NASA UTM program reports, and FAA filings.
- **disclosed subsystems:** `transition-tail-sitter-pitch-up`, `lift-modular-docking`, `lift-distributed-electric-propulsion`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `autonomy-pilot-removed`, `autonomy-utm-integration`, `autonomy-bvlos-detect-and-avoid`, `cert-faa-bvlos-waiver`, `airframe-composite-monocoque`

**Prior art notes:**

> Bell APT (Autonomous Pod Transport) establishes US prior art for the modular-cargo-pod tail-sitter eVTOL — a reusable quad-rotor tail-sitter airframe carrying a swappable cargo pod mounted between the rotor booms. Establishes prior art for: (1) modular swappable cargo pod + reusable propulsion airframe architecture in tail-sitter form, (2) NASA UTM-integrated autonomous cargo eVTOL operations (2020-2021 trials), (3) the pod-as-deliverable design pattern. Together with airbus-popup (modular passenger capsule), elroy-air-chaparral (modular cargo pod), and the academic modular-aerial-robot lineage, places modular-pod eVTOL architecture in commercial prior art from 2017-2018 forward.

**Sources:**

1. Bell Textron press releases on APT, 2018-2021.
2. NASA UAS Traffic Management (UTM) program reports including Bell APT trials.
3. FAA Part 107 / BVLOS waiver records for Bell APT operations.

---

### 2018-09 — Jetson ONE

- **id:** `jetson-one`
- **corpus:** private
- **ip status:** patented
- **creator:** Jetson AB (Italy / Sweden joint operation)
- **disclosure citation:** Jetson AB founded 2018-09 by Tomasz Patan (Polish-Swedish) and Peter Ternström (Swedish); Jetson ONE design unveiled 2020-04-21; first manned flight 2020-09; first customer deliveries 2023-09.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-part-103-ultralight`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `lift-coaxial-rotor`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`

**Prior art notes:**

> Jetson ONE is the leading consumer ultralight-class single-seat eVTOL — the Swedish/Italian/Polish realization of the open-frame multirotor design originally disclosed by Curtiss-Wright VZ-7 (1958). Operates under FAA Part 103 ultralight rules with no pilot license required. Establishes Northern European prior-art lineage for consumer-grade ultralight eVTOL with open-rotor architecture and rotor-failure reconfiguration.

**Sources:**

1. Jetson AB press releases 2018–2024.
2. Jetson ONE technical specifications, jetsonaero.com.
3. FAA Part 103 ultralight registration records (Jetson ONE customer aircraft).

---

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

### 2019 — teTra Mk-5

- **id:** `tetra-mk-5`
- **corpus:** private
- **ip status:** patented
- **creator:** teTra Aviation Corporation (Tokyo, Japan) / Tasuku Nakai
- **disclosure citation:** teTra Aviation Corporation (founded 2018 in Tokyo, an outgrowth of GoFly Prize-competing students) revealed the Mk-3 personal eVTOL (2020, GoFly Prize 'Pratt & Whitney Disruptor Award' winner) and subsequently the production Mk-5 single-seat personal eVTOL (2021); first crewed flights and FAA Special Airworthiness Certificate process underway. Documented in teTra materials and GoFly Prize records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `transition-mode-shutdown`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-103-ultralight`

**Prior art notes:**

> teTra Mk-5 establishes Japanese prior art for the high-rotor-count single-seat personal eVTOL — a fixed-wing airframe with 32 small distributed lift rotors for hover redundancy plus wing lift for cruise efficiency. A GoFly Prize-derived design. Establishes prior art for: (1) very-high-rotor-count (~32) personal eVTOL with fixed wings, (2) the GoFly Prize lineage of personal-flight designs. Together with skydrive-sd-05 (JP, multirotor air taxi), aska-a5 (JP/US, drive+fly), honda-evtol (JP, hybrid), and the Japanese fictional VTOL anchors, deepens Japan's eVTOL footprint. Together with lift-aircraft-hexa (US, 18-rotor) and ehang-eh216 (CN, 16-rotor), places high-rotor-count personal/small eVTOL architecture in prior art.

**Sources:**

1. teTra Aviation Mk-3 / Mk-5 technical materials 2019-2024.
2. GoFly Prize competition records (teTra Mk-3, Pratt & Whitney Disruptor Award).

---

### 2019 — Bellwether Industries Volar

- **id:** `bellwether-volar`
- **corpus:** private
- **ip status:** patented
- **creator:** Bellwether Industries (London, United Kingdom)
- **disclosure citation:** Bellwether Industries (founded 2019 in London by Kai-Hsiang Lin) publicly disclosed the Volar — a four-seat ducted-fan flying-car concept designed to look like a luxury car — through 2021-2024 design and sub-scale-prototype releases. The 'Antelope' 1/6-scale demonstrator made tethered flights 2021. Documented in Bellwether materials.
- **disclosed subsystems:** `lift-ducted-fan-array`, `lift-distributed-electric-propulsion`, `lift-vectored-thrust`, `propulsion-hybrid-series`, `propulsion-bldc-direct-drive`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`

**Prior art notes:**

> Bellwether Industries' Volar concept (UK, 2019-) establishes prior art for the 'luxury-car-aesthetic flying car with internal ducted fans' — eight electric ducted lift fans buried inside a sleek closed-body vehicle with no exposed rotors, smooth aerodynamic surface in cruise. Distinct from Alef Model A (rotors under mesh skin, whole-body rotation) and from open-rotor multirotor eVTOLs. Adds UK depth to the flying-car / ducted-fan-array prior-art base alongside Lilium (DE), Aurora LightningStrike (US), Bell X-22 (US), Bell Nexus (US), Doak VZ-4 (US), Pegasus VBJ (ZA), Boeing Phantom Swift (US), and Horizon Aircraft Cavorite X5 (CA).

**Sources:**

1. Bellwether Industries Volar / Antelope technical materials 2019-2024.

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

### 2019-06 — Jaunt Air Mobility Journey

- **id:** `jaunt-air-mobility`
- **corpus:** private
- **ip status:** patented
- **creator:** Jaunt Air Mobility LLC (Montreal, Canada / Texas, USA) — subsidiary of AIRO Group; licensed Carter Aviation SR/C technology
- **disclosure citation:** Jaunt Air Mobility (founded 2019, headquartered in Montreal with Texas operations, a subsidiary of the AIRO Group) unveiled the Journey eVTOL — a slowed-rotor compound electric VTOL using 'ROSA' (Reduced rOtor Speed Aircraft) technology licensed from Carter Aviation — in 2019; selected for the U.S. Air Force AFWERX Agility Prime programme 2020. Documented in Jaunt Air Mobility materials, AFWERX records, and AIRO Group SEC filings (NASDAQ: AIRO).
- **disclosed subsystems:** `lift-compound-rotorcraft`, `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-23`, `airframe-composite-monocoque`

**Prior art notes:**

> Jaunt Air Mobility's Journey eVTOL establishes Canadian/US prior art for the slowed-rotor-compound electric VTOL — a single large rotor that spins fast for jump-takeoff then slows dramatically in cruise while a wing carries lift and electric pushers provide thrust ('ROSA', licensed from Carter Aviation). A distinct eVTOL architecture from the multirotor and tilt-rotor approaches. Establishes prior art for: (1) slowed-rotor-compound electric VTOL, (2) jump-takeoff stored-inertia rotor in an electric eVTOL, (3) the wing-offloads-slowed-rotor-in-cruise eVTOL configuration. Together with cartercopter (1998, the SR/C origin), karem-ar40 (2008, optimum-speed rotor), and overair-butterfly (2020, OSR eVTOL), comprehensively places slowed/variable-RPM-rotor compound eVTOL architecture in prior art. Adds another Canadian entry alongside Horizon Aircraft and the Avro Canada Avrocar heritage.

**Sources:**

1. Jaunt Air Mobility Journey technical materials 2019-2024.
2. U.S. Air Force AFWERX Agility Prime contract records (Jaunt).
3. AIRO Group SEC filings (NASDAQ: AIRO).

---

### 2019-08-14 — Volocopter VoloCity

- **id:** `volocopter-volocity`
- **corpus:** private
- **ip status:** patented
- **creator:** Volocopter GmbH
- **disclosure citation:** VoloCity production-design unveiling 2019-08-14 at Helsinki ITS World Congress; precursor VC-200 first manned flight 2013-11-17; first public manned demo at Singapore 2019-10-22. EASA SC-VTOL certification process actively pursued; targeted operations Paris 2024 / 2026 commercial rollouts.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`

**Prior art notes:**

> Volocopter VoloCity is the production design descending from e-volo VC1 (2011, first manned multicopter flight). 18-rotor circular-ring multirotor architecture, EASA SC-VTOL certification basis. Establishes the German prior-art lineage from e-volo through Volocopter for circular-ring multirotor passenger eVTOL — foundational and predates EHang in manned-flight precedence.

**Sources:**

1. Volocopter press releases 2013–2024.
2. EASA SC-VTOL filings, public docket.
3. Vertical Flight Society Forum technical papers from Volocopter 2014–2024.

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

### 2019-10-15 — Pipistrel Nuuva V300

- **id:** `pipistrel-nuuva-v300`
- **corpus:** private
- **ip status:** patented
- **creator:** Pipistrel (Slovenia; acquired by Textron 2022)
- **disclosure citation:** Pipistrel (a Slovenian light-aircraft maker, the manufacturer of the Velis Electro — the first type-certified electric aeroplane) unveiled the Nuuva V300 hybrid VTOL cargo aircraft 2019-10-15; Pipistrel acquired by Textron 2022-04. The Nuuva V300 is intended as a heavy-cargo lift+cruise hybrid-electric eVTOL. Documented in Pipistrel/Textron materials and EASA filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-hybrid-series`, `power-hybrid-genset`, `propulsion-bldc-direct-drive`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`

**Prior art notes:**

> Pipistrel Nuuva V300 establishes Slovenian prior art for the hybrid-electric heavy-cargo eVTOL — eight electric lift rotors plus a single combustion-driven cruise pusher, designed for ~460 kg cargo over ~2,500 km range. Adds Slovenia (SI) to the global eVTOL OEM map. Pipistrel's parent company is Textron (also owner of Bell Textron) — the Pipistrel-Textron-Bell axis creates an integrated tilt-rotor + hybrid-cargo + electric-fixed-wing eVTOL family. Together with elroy-air-chaparral, sabrewing-rhaegal-a, wingcopter-198, pyka-pelican, amsl-vertiia, autoflight-prosperity-i, dji-flycart-30, and orb-aerospace-nomad, comprehensively places hybrid-electric cargo eVTOL architecture in commercial prior art across nine national/regional lineages.

**Sources:**

1. Pipistrel Nuuva V300 technical materials 2019-2024.
2. Textron acquisition of Pipistrel, 2022-04 disclosures.
3. EASA SC-VTOL public docket (Pipistrel).

---

### 2019-10-30 — Volocopter VoloDrone

- **id:** `volocopter-volodrone`
- **corpus:** private
- **ip status:** patented
- **creator:** Volocopter GmbH (Bruchsal, Germany)
- **disclosure citation:** Volocopter VoloDrone publicly demonstrated 2019-10-30 at the Volocopter facility in Bruchsal, Germany — a heavy-cargo unmanned variant of the Volocopter 18-rotor multirotor architecture. Subsequently demonstrated for DB Schenker cargo logistics and at the Volocopter Hamburg test campaign. Documented in Volocopter press materials and EASA filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `autonomy-pilot-removed`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`, `safety-redundant-bus`

**Prior art notes:**

> Volocopter VoloDrone establishes German prior art for the cargo-variant-of-passenger-multirotor pattern — unmanned heavy-cargo operations on the same 18-rotor airframe as the VoloCity passenger eVTOL, with up to 200 kg payload. Establishes prior art for: (1) shared-airframe passenger/cargo eVTOL family architecture, (2) underslung cargo and swappable container variants of a multirotor passenger eVTOL. Adds the cargo dimension to the Volocopter prior-art lineage (alongside the passenger volocopter-vc1 / volocopter-volocity).

**Sources:**

1. Volocopter VoloDrone press materials and demonstrations 2019-2024.
2. DB Schenker / Volocopter cargo logistics partnership records.

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

### 2020-10-15 — Overair Butterfly

- **id:** `overair-butterfly`
- **corpus:** private
- **ip status:** patented
- **creator:** Overair Inc (Santa Ana, California) — Karem Aircraft spinoff; partnered with Hanwha Systems (Korea)
- **disclosure citation:** Overair (spun out of Karem Aircraft in 2020, with investment from Hanwha Systems of South Korea) unveiled the Butterfly eVTOL — a tilt-rotor eVTOL using Karem's 'Optimum Speed Tilt-Rotor' (OSTR) technology (large slow-turning prop-rotors with continuously-variable RPM) — in October 2020. Documented in Overair materials, Hanwha Systems disclosures, and U.S. Air Force AFWERX Agility Prime records.
- **disclosed subsystems:** `lift-tilt-rotor`, `lift-distributed-electric-propulsion`, `transition-thrust-borne-to-wing-borne`, `transition-conversion-corridor`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-23`, `airframe-composite-monocoque`

**Prior art notes:**

> Overair's Butterfly establishes prior art for the optimum-speed tilt-rotor eVTOL — a tilt-rotor eVTOL with four very large, slow-turning prop-rotors whose RPM is continuously varied with flight regime ('OSTR', from Karem Aircraft's OSR technology), giving low disk loading for quiet, efficient hover. Distinct from the small-fast-prop tilt-rotor eVTOLs (Joby S4, TCab E20) by the large-slow-prop approach. Establishes prior art for: (1) continuously-variable-RPM tilt-rotor in an eVTOL, (2) very-low-disk-loading large slow prop-rotors for quiet hover, (3) the OSR-applied-to-eVTOL configuration. Hanwha Systems (Korea) partnership ties this to the Korean eVTOL ecosystem (Hyundai Supernal, Plana). Together with karem-ar40 (2008, OSTR origin), cartercopter (1998), and jaunt-air-mobility (2019), comprehensively places variable-RPM / slowed-rotor / optimum-speed-rotor eVTOL architecture in prior art.

**Sources:**

1. Overair Butterfly technical materials 2020-2024.
2. Hanwha Systems (Korea) Overair investment disclosures.
3. U.S. Air Force AFWERX Agility Prime contract records (Overair).
4. Karem Aircraft / Overair OSR / OSTR patents, USPTO.

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

### 2021-07 — CycloTech CruiseUp / CCY-5

- **id:** `cyclotech-cruiseup`
- **corpus:** private
- **ip status:** patented
- **creator:** CycloTech GmbH (Linz, Austria)
- **disclosure citation:** CycloTech GmbH (founded 2004 as D-Dalus successor, rebranded CycloTech 2020) unveiled the CruiseUp passenger eVTOL concept 2022-09; the CCY-5 technology demonstrator (a sub-scale flying testbed using six CycloRotors) achieved first untethered flight 2024-04-17 at Wels, Austria. CycloTech holds an extensive cycloidal-rotor patent estate.
- **disclosed subsystems:** `lift-cyclorotor`, `control-fully-actuated-omnidirectional`, `lift-distributed-electric-propulsion`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`

**Prior art notes:**

> CycloTech CruiseUp / CCY-5 is the modern production-oriented disclosure of cyclorotor (cyclogiro) eVTOL — six electric CycloRotors giving omnidirectional fully-actuated thrust via azimuthal blade-pitch modulation. Establishes Austrian prior art for: (1) passenger-scale cyclorotor eVTOL architecture, (2) electric CycloRotor propulsion with 360° in-plane thrust vectoring, (3) the omnidirectional fully-actuated cyclorotor control. Builds on the D-Dalus research demonstrator (2011) and the foundational Pescara cyclogiro patents (1928, long expired). Together with d-dalus and eth-omnicopter, comprehensively places cyclorotor and omnidirectional VTOL architecture in prior art.

**Sources:**

1. CycloTech GmbH technical white papers and press releases 2020-2024.
2. CycloTech CCY-5 first flight, Wels Austria, 2024-04-17.
3. Pescara cyclogiro patents (1928, foundational, expired).

---

### 2021-09 — Horizon Aircraft Cavorite X5

- **id:** `horizon-aircraft-cavorite-x5`
- **corpus:** private
- **ip status:** patented
- **creator:** New Horizon Aircraft Ltd (Lindsay, Ontario, Canada)
- **disclosure citation:** New Horizon Aircraft (Canadian, founded 2013, public on NASDAQ as HOVR via SPAC merger 2024) unveiled the Cavorite X5 hybrid eVTOL in 2021; 50%-scale prototype first conventional flight 2023-11 and first full transition 2024-11. The Cavorite uses a 'fan-in-wing' design — fourteen lift fans embedded in the wings, covered by sliding panels in cruise so the aircraft flies as a conventional fixed-wing. Documented in Horizon Aircraft materials and SEC filings (named for H.G. Wells's anti-gravity material 'Cavorite').
- **disclosed subsystems:** `lift-ducted-fan-array`, `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-hybrid-series`, `power-hybrid-genset`, `propulsion-bldc-direct-drive`, `cert-part-23`, `airframe-composite-monocoque`

**Prior art notes:**

> Horizon Aircraft Cavorite X5 establishes Canadian prior art for the modern 'fan-in-wing' hybrid eVTOL — fourteen electric lift fans embedded in the wing structure, covered by sliding panels in cruise so the wing becomes a clean conventional wing with a single pusher. Establishes prior art for: (1) modern panel-covered fan-in-wing eVTOL, (2) hybrid-electric fan-in-wing architecture, (3) the wing-as-clean-wing-in-cruise design. Directly descended in concept from vanguard-omniplane (1959) and ryan-xv-5-vertifan (1964). Together with these and lilium-jet (ducted-fan-array), aurora-lightningstrike-xv-24a (tilt-wing ducted-fan), and bell-nexus-4ex (tilt-duct), comprehensively places ducted-fan / fan-in-wing eVTOL architecture in prior art. Adds Canadian depth alongside Jaunt Air Mobility and the Avro Canada Avrocar heritage.

**Sources:**

1. New Horizon Aircraft Cavorite X5 technical materials 2021-2024.
2. New Horizon Aircraft SEC filings (NASDAQ: HOVR).

---

### 2021-09 — Maca Carcopter S11

- **id:** `maca-carcopter`
- **corpus:** private
- **ip status:** patented
- **creator:** MACA Industries (Toulouse, France) / Michaël Carchidi
- **disclosure citation:** MACA Industries (founded 2019 in Toulouse, France) unveiled the S11 Carcopter — a hydrogen-fuel-cell racing eVTOL — at the September 2021 Munich IAA Mobility show. Designed for an envisioned hydrogen racing league. Documented in MACA materials and aerospace press.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `lift-coaxial-rotor`, `propulsion-hydrogen-fuel-cell`, `propulsion-bldc-direct-drive`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> MACA Carcopter establishes French prior art for the hydrogen-fuel-cell racing eVTOL — distinct from Alauda Airspeeder (AU, battery-electric racing) by the hydrogen powertrain. Together with airspeeder (AU) and amsl-vertiia (AU, hydrogen passenger), places hydrogen and racing eVTOL architecture in cross-national prior art. Adds another French entry to the deep French VTOL heritage (SNECMA Coléoptère, Eurocopter X3, Airbus RACER, Flying Whales, Cornu, Oehmichen, d'Amécourt, Lazareth, Airbus Vahana, Airbus Pop.Up, Verne).

**Sources:**

1. MACA Industries S11 Carcopter technical materials and IAA Mobility 2021 unveiling.
2. MACA Industries press materials 2021-2024.

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

### 2021-09-21 — Airbus CityAirbus NextGen

- **id:** `airbus-cityairbus-nextgen`
- **corpus:** private
- **ip status:** patented
- **creator:** Airbus Helicopters (Donauwörth, Germany) / Airbus Defence and Space
- **disclosure citation:** Airbus CityAirbus NextGen design publicly unveiled 2021-09-21 at Airbus Summit; first scaled prototype hover 2024-09. EASA SC-VTOL type-certification process initiated 2022. Predecessor CityAirbus demonstrator first hover 2019-05-03.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `control-fly-by-wire-triplex`, `cert-easa-special-condition-vtol`, `airframe-composite-monocoque`, `safety-ballistic-parachute`, `safety-redundant-bus`, `autonomy-utm-integration`

**Prior art notes:**

> Airbus CityAirbus NextGen is the production-track lift+cruise successor to the Vahana research program. Establishes German industrial prior-art lineage for production-scale lift+cruise passenger eVTOL with V-strut lift-rotor mounting geometry distinct from boom-mounted competitors (Beta Alia, Eve, Wisk). Airbus's industrial certification scale and EASA insider position make this a particularly important commons-grade entry.

**Sources:**

1. Airbus Helicopters press releases 2019–2024.
2. Airbus Summit 2021 unveiling materials.
3. EASA SC-VTOL public docket.

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

### 2021-10 — REGENT Viceroy seaglider

- **id:** `regent-viceroy-seaglider`
- **corpus:** private
- **ip status:** patented
- **creator:** REGENT Craft Inc (Rhode Island, USA) — founded by Boeing / Aurora Flight Sciences alumni
- **disclosure citation:** REGENT Craft (founded 2020 by Billy Thalheimer and Mike Klinker, ex-Aurora Flight Sciences / Boeing) unveiled the Viceroy seaglider 2021-10; quarter-scale prototype first flight 2022-08; full-scale Viceroy prototype rollout / first sea trials 2024-2025. The seaglider operates in three modes — floating (hull), foiling (hydrofoils), and flying (wing-in-ground-effect, ~9 m altitude). Documented in REGENT technical materials, U.S. Marine Corps / Navy contracts, and patent filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-23`, `airframe-composite-monocoque`

**Prior art notes:**

> REGENT Viceroy is the foundational modern disclosure of the electric wing-in-ground-effect (WIG) 'seaglider' — a distributed-electric-propulsion craft that transitions floating → hydrofoiling → ground-effect flight, operating a few meters above water. Establishes prior art for: (1) electric WIG / ekranoplan-class craft with distributed blown-wing propulsion, (2) the hull/foil/flight three-mode transition, (3) retractable-hydrofoil takeoff for a winged aircraft. While not vertical-takeoff in the classical sense, it is eVTOL-adjacent (the corpus scope covers ground-effect hybrids with VTOL-like operations) and shares DEP blown-wing architecture with eVTOL. Anticipates other electric-WIG and seaglider claims (a growing segment — also pursued by Wigetworks AirFish and others).

**Sources:**

1. REGENT Craft technical white papers and press releases 2021-2025.
2. U.S. Marine Corps / Navy seaglider contract records.
3. REGENT Craft patent filings, USPTO.

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

### 2021-12-13 — AutoFlight Prosperity I

- **id:** `autoflight-prosperity-i`
- **corpus:** private
- **ip status:** patented
- **creator:** AutoFlight (Shanghai)
- **disclosure citation:** AutoFlight Prosperity I publicly unveiled 2021-12-13; first untethered hover flight 2022-04; full-scale prototype transition flight 2023-02-23 at Kunshan; cross-Pearl River Delta demonstration flight Hong Kong → Macau 2024-04-29. AutoFlight founded by Tian Yu (former co-founder of EHang).
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-ballistic-parachute`, `safety-redundant-bus`, `transition-mode-shutdown`

**Prior art notes:**

> AutoFlight Prosperity I is the leading Chinese lift+cruise eVTOL — architectural sibling to Beta Alia-250 with eight rather than four lift rotors. The 250 km Hong Kong-Macau demonstration flight (2024-04-29) is the longest eVTOL flight publicly documented as of mid-2024. Establishes Chinese prior-art lineage for lift+cruise architecture and supports EASA SC-VTOL certification basis dual-track with EHang's CAAC certification.

**Sources:**

1. AutoFlight press releases 2021–2024.
2. China Daily and Xinhua coverage of 2024-04-29 Hong Kong-Macau flight.
3. AutoFlight technical white papers (Chinese and English editions).

---

### 2022-06 — Doroni H1 / H1-X

- **id:** `doroni-h1`
- **corpus:** private
- **ip status:** patented
- **creator:** Doroni Aerospace (Fort Lauderdale, Florida) / Doron Merdinger
- **disclosure citation:** Doroni Aerospace (founded 2016 by Doron Merdinger) unveiled the H1 two-seat personal eVTOL in 2022; first crewed test flight 2023-05; received an FAA Special Airworthiness Certificate (Experimental) 2023; developing the H1-X for FAA Part 23 certification. Designed to fit in a two-car garage and operate from driveways under (intended) Part 103 ultralight or LSA rules. Documented in Doroni materials and FAA filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `control-simplified-vehicle-operations`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> Doroni H1 establishes US prior art for the garage-storable enclosed-rotor two-seat personal eVTOL — eight ducted lift rotors housed within the airframe body (not on exposed booms), small fixed wings, car-like footprint, driveway operation. Establishes prior art for: (1) fully-enclosed-within-body lift rotors on a personal eVTOL, (2) garage-storable / driveway-operable two-seat personal eVTOL form factor. Together with pivotal-blackfly, jetson-one, lift-aircraft-hexa, alef-model-a, and the historical personal-platform anchors, comprehensively places small-personal eVTOL architecture in prior art.

**Sources:**

1. Doroni Aerospace H1 / H1-X technical materials 2022-2024.
2. FAA Special Airworthiness Certificate dossier (Doroni H1).

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

### 2022-08 — Plana Aero CP-01

- **id:** `plana-cp-01`
- **corpus:** private
- **ip status:** patented
- **creator:** Plana Aerospace Inc (Seongnam, South Korea)
- **disclosure citation:** Plana Aerospace (founded 2021 in South Korea by Braden Kim) unveiled the CP-01 hybrid-electric eVTOL in 2022; sub-scale prototype flight tests 2023-2024; targeting Korean (MOLIT) and FAA certification for regional air mobility. Documented in Plana materials and Korean Ministry of Land, Infrastructure and Transport (MOLIT) records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-mode-shutdown`, `propulsion-hybrid-series`, `power-hybrid-genset`, `propulsion-bldc-direct-drive`, `cert-part-23`, `airframe-composite-monocoque`

**Prior art notes:**

> Plana Aero CP-01 establishes Korean prior art for the hybrid-electric regional eVTOL — a lift+cruise eVTOL with a turbine-genset-electric hybrid powertrain for ~500 km range, targeting intercity routes. Distinct from the urban-air-taxi-focused Korean peer Hyundai Supernal (battery-electric, 100 km). Establishes Korean depth in the hybrid-electric eVTOL space alongside Honda (JP), Zuri (CZ), Elroy Air (US), and AMSL Vertiia (AU). Together with hyundai-supernal-sa2, the Hanwha-Systems-backed overair-butterfly, and (fictionally) space-sweepers-victory, deepens Korea's eVTOL footprint.

**Sources:**

1. Plana Aerospace CP-01 technical materials 2022-2024.
2. Korean MOLIT (Ministry of Land, Infrastructure and Transport) UAM programme records.

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

### 2022-10-19 — Alef Aeronautics Model A

- **id:** `alef-model-a`
- **corpus:** private
- **ip status:** patented
- **creator:** Alef Aeronautics Inc (San Mateo, California)
- **disclosure citation:** Alef Aeronautics Model A publicly unveiled 2022-10-19; received FAA Special Airworthiness Certificate (Experimental) 2023-06-12 — the first 'flying car' to receive an FAA airworthiness certificate. Alef (founded 2015) demonstrated a full-scale prototype driving and (briefly) lifting 2022-2023. Documented in Alef press materials, FAA filings, and Alef patent filings.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `transition-tail-sitter-pitch-up`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-experimental`, `airframe-composite-monocoque`

**Prior art notes:**

> Alef Aeronautics Model A establishes US prior art for the rotors-under-mesh-skin drive+fly transformer — a road-legal car with eight electric lift rotors hidden under a perforated upper skin, taking off vertically through the mesh and then rotating the whole body (cabin gimballed level) to fly as a biplane-wing. The first 'flying car' to receive an FAA airworthiness certificate (2023). Establishes prior art for: (1) mesh-skin / perforated-surface lift-rotor concealment architecture, (2) whole-body-rotation drive+fly transition with gimballed cabin, (3) the car-body-as-biplane-wing configuration. Distinct from the folding-wing transformers (Klein Vision, AeroMobil, ASKA) and modular-capsule transformers (Airbus Pop.Up, XPENG AeroHT). Together with these and pal-v-liberty (autogyro transformer), comprehensively places drive+fly transformer architecture in prior art across folding-wing / modular-capsule / whole-body-rotation / autogyro variants.

**Sources:**

1. Alef Aeronautics press releases 2022-2024.
2. FAA Special Airworthiness Certificate dossier (Alef Model A), 2023-06-12.
3. Alef Aeronautics patent filings, USPTO (incl. US 11,167,839).

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

### 2023-08-16 — DJI FlyCart 30

- **id:** `dji-flycart-30`
- **corpus:** private
- **ip status:** patented
- **creator:** SZ DJI Technology Co Ltd (Shenzhen)
- **disclosure citation:** DJI FlyCart 30 publicly unveiled 2023-08-16 in Shenzhen; CAAC type certification application 2023; commercial deliveries to Chinese and international markets 2024. DJI is the world's largest drone manufacturer and holds an extensive multirotor patent estate.
- **disclosed subsystems:** `airframe-composite-monocoque`, `autonomy-bvlos-detect-and-avoid`, `autonomy-pilot-removed`, `autonomy-utm-integration`, `cert-easa-special-condition-vtol`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `lift-coaxial-rotor`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`

**Prior art notes:**

> DJI FlyCart 30 is the entry of the world's largest drone manufacturer into the heavy-cargo eVTOL category. DJI's massive patent estate and operational scale (millions of multirotor flights/day globally) constitute foundational prior-art coverage for: (1) coaxial-pair multirotor manufacturing at scale, (2) autonomous multirotor cargo delivery, (3) consumer-priced multirotor architecture migration to commercial cargo class. Establishes Chinese prior-art lineage for heavy-payload multirotor cargo eVTOL with explicit Beyond Visual Line of Sight (BVLOS) operational basis.

**Sources:**

1. DJI press releases and product disclosures 2023–2024.
2. CAAC type certification dossier (DJI FlyCart 30).
3. DJI patent estate, USPTO and CNIPA records.

---

### 2023-11 — Sarla Aviation Shunya

- **id:** `sarla-aviation-shunya`
- **corpus:** private
- **ip status:** patented
- **creator:** Sarla Aviation (Bangalore, India)
- **disclosure citation:** Sarla Aviation (founded 2023 in Bangalore by Adrian Schmidt, Rakesh Gaonkar, and Shivam Chauhan; named after Sarla Thakral, India's first woman pilot) unveiled the Shunya eVTOL air taxi in November 2023, with production targeted for ~2028 in Indian cities (Bangalore, Mumbai, Delhi, Pune); sub-scale prototype work 2024. Documented in Sarla materials and Indian DGCA engagement records.
- **disclosed subsystems:** `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `control-rotor-failure-reconfiguration`, `propulsion-bldc-direct-drive`, `power-li-ion-pouch`, `cert-part-23`, `airframe-composite-monocoque`

**Prior art notes:**

> Sarla Aviation Shunya establishes additional Indian prior art for the urban-air-taxi multirotor eVTOL — a five-seat eVTOL designed for short hops in dense Indian cities, the second major Indian eVTOL OEM after ePlane. Establishes Indian depth alongside eplane-company-e200 (IN, lift+cruise) and the Indian fictional flight anchor (Krrish). Together with ehang-eh216 (CN), volocopter-volocity (DE), and the global multirotor air-taxi cluster, places urban-air-taxi multirotor eVTOL architecture in prior art across US, EU, China, India, Japan, Korea, and Brazil lineages.

**Sources:**

1. Sarla Aviation Shunya technical materials 2023-2024.
2. Indian DGCA (Directorate General of Civil Aviation) UAM engagement records.

---

### 2023-11-08 — LTA Research Pathfinder 1

- **id:** `lta-research-pathfinder-1`
- **corpus:** private
- **ip status:** patented
- **creator:** LTA Research and Exploration (Mountain View, CA) — funded by Sergey Brin
- **disclosure citation:** LTA Research Pathfinder 1 received FAA Special Airworthiness Certificate (Experimental) 2023-09; first untethered flight 2023-11-08 at Moffett Field, CA. LTA Research (funded by Google co-founder Sergey Brin since ~2016) builds rigid electric airships for humanitarian cargo and disaster relief. Documented in FAA filings and LTA Research materials.
- **disclosed subsystems:** `lift-buoyant-hybrid`, `lift-distributed-electric-propulsion`, `propulsion-bldc-direct-drive`, `cert-experimental`

**Prior art notes:**

> LTA Research Pathfinder 1 establishes modern prior art for the electric rigid airship with vectored-thrust VTOL augmentation — buoyant helium lift augmented by distributed electric propellers for controlled vertical takeoff/landing without ground infrastructure. Establishes prior art for: (1) modern rigid electric airship architecture, (2) lidar-based ballast/lift management, (3) the buoyant-hybrid VTOL concept (static lift + vectored thrust). The corpus scope includes buoyant-hybrid craft with VTOL-like operations. Together with hybrid-air-vehicles-airlander (2012) and flying-whales-lca60t (2012), establishes the modern hybrid-airship / buoyant-VTOL prior-art base.

**Sources:**

1. LTA Research and Exploration technical materials and press releases 2023-2025.
2. FAA Special Airworthiness Certificate dossier (Pathfinder 1).
3. Pathfinder 1 first flight, Moffett Field CA, 2023-11-08.

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

### 2024-04-04 — XPENG AeroHT Land Aircraft Carrier

- **id:** `xpeng-aeroht-modular`
- **corpus:** private
- **ip status:** patented
- **creator:** AeroHT (XPENG flying car subsidiary)
- **disclosure citation:** XPENG AeroHT Land Aircraft Carrier publicly unveiled 2024-04-04 at Beijing Auto Show; production target 2026. Combines a road-legal 6x6 ground vehicle ('Mothership') containing a fold-out manned eVTOL drone.
- **disclosed subsystems:** `airframe-composite-monocoque`, `cert-easa-special-condition-vtol`, `control-differential-thrust-attitude`, `lift-distributed-electric-propulsion`, `power-li-ion-pouch`, `propulsion-bldc-direct-drive`, `safety-redundant-bus`

**Prior art notes:**

> XPENG AeroHT Land Aircraft Carrier is the most ambitious modular drive+fly transformer architecture publicly disclosed: a separate ground vehicle that carries and deploys a manned eVTOL. Establishes Chinese prior-art lineage for modular vehicle-eVTOL architectures, distinct from integrated transformer-eVTOL designs (ASKA A5, AeroMobil) where one vehicle physically transforms. Anticipates future modular-carrier patent filings.

**Sources:**

1. XPENG AeroHT Beijing Auto Show 2024-04-04 unveiling materials.
2. AeroHT / XPENG technical disclosures 2024.
3. Reuters and South China Morning Post coverage 2024-04-04.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `7ec5755`.*
