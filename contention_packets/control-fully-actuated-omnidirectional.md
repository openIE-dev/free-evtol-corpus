---
title: "control-fully-actuated-omnidirectional"
parent: "Invalidity Contentions"
nav_order: 17
layout: default
---

# Invalidity Contention Packet — `control-fully-actuated-omnidirectional`

**Generated:** 2026-05-14  
**Cross-cut tag:** `control-fully-actuated-omnidirectional`  
**Entries:** 4 (4 commons-grade, 0 draft)  
**Earliest disclosure:** 2016-05  
**Most recent disclosure:** 2021-07

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `control-fully-actuated-omnidirectional`.

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

### 2016-05 — ETH Omnicopter

- **id:** `eth-omnicopter`
- **corpus:** academic
- **ip status:** patented
- **creator:** ETH Zurich Institute for Dynamic Systems and Control (Raffaello D'Andrea) / Dario Brescianini
- **disclosure citation:** Brescianini, Dario; D'Andrea, Raffaello. 'Design, modeling and control of an omni-directional aerial vehicle.' IEEE International Conference on Robotics and Automation (ICRA), Stockholm, May 2016; subsequent IEEE Transactions on Control Systems Technology and demonstration videos (catching and throwing a ball mid-air). ETH Zurich IDSC.
- **disclosed subsystems:** `control-fully-actuated-omnidirectional`, `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `cert-experimental`

**Prior art notes:**

> The ETH Omnicopter (Brescianini & D'Andrea, ICRA 2016) is the foundational disclosure of the fully-actuated omnidirectional multirotor — eight bidirectional propellers on a cubic frame giving independent control of force and torque in all six degrees of freedom, able to hover at arbitrary attitudes and recover from any orientation. Establishes prior art for: (1) fully-actuated (6-DOF) multirotor architecture, (2) bidirectional-propeller thrust vectoring, (3) arbitrary-attitude hover and orientation recovery. Anticipates: Voliro (omnidirectional tilt-rotor hexrotor), CycloTech (omnidirectional cyclorotor), and any commercial eVTOL claim asserting novelty over fully-actuated or arbitrary-attitude multirotor control.

**Sources:**

1. Brescianini, D., D'Andrea, R. 'Design, modeling and control of an omni-directional aerial vehicle.' ICRA 2016.
2. Brescianini, D., D'Andrea, R. 'An omni-directional multirotor vehicle.' Mechatronics, 2018.
3. ETH Zurich IDSC publications archive.

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

### 2018-05 — Voliro omnidirectional flying robot

- **id:** `voliro`
- **corpus:** private
- **ip status:** patented
- **creator:** Voliro Airborne Robotics (ETH Zurich spinout) / Marco Tognon / Mina Kamel / Roland Siegwart (ASL)
- **disclosure citation:** Voliro hexacopter with tiltable rotor arms first publicly disclosed 2018 (ETH Zurich Autonomous Systems Lab student project, then ETH spinout Voliro Airborne Robotics, founded 2019); academic paper Bodie, Karen et al. 'Towards Efficient Full Pose Omnidirectionality with Overactuated MAVs,' ISER 2018 / and related ASL publications. Commercialized for contact-based industrial inspection (Voliro X, 2022).
- **disclosed subsystems:** `control-fully-actuated-omnidirectional`, `lift-tilt-rotor`, `lift-distributed-electric-propulsion`, `control-differential-thrust-attitude`, `cert-experimental`

**Prior art notes:**

> Voliro establishes prior art for the tilting-arm omnidirectional multirotor — a hexacopter with six independently-tilting rotor arms giving full-pose (6-DOF) control via tilt geometry rather than bidirectional propellers. Distinct from the ETH Omnicopter approach. Establishes prior art for: (1) independently-tilting-arm omnidirectional multirotor, (2) contact-based aerial interaction (pressing sensors against surfaces). Commercialized for industrial inspection. Together with eth-omnicopter (2016) and cyclotech-cruiseup (2022), comprehensively places omnidirectional / fully-actuated multirotor architecture in academic and commercial prior art.

**Sources:**

1. Bodie, K. et al. 'Towards Efficient Full Pose Omnidirectionality with Overactuated MAVs.' ISER 2018.
2. Bodie, K. et al. 'An Omnidirectional Aerial Manipulation Platform for Contact-Based Inspection.' RSS 2019.
3. Voliro Airborne Robotics technical materials, voliro.com.

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

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `7ec5755`.*
