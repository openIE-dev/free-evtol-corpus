---
title: "cert-faa-bvlos-waiver"
parent: "Invalidity Contentions"
nav_order: 7
layout: default
---

# Invalidity Contention Packet — `cert-faa-bvlos-waiver`

**Generated:** 2026-05-11  
**Cross-cut tag:** `cert-faa-bvlos-waiver`  
**Entries:** 2 (2 commons-grade, 0 draft)  
**Earliest disclosure:** 2017  
**Most recent disclosure:** 2018-04

---

## How to use this packet

This document is an invalidity-contention packet — a chronologically-ordered
list of every disclosed prior art reference in the Free eVTOL Corpus that
bears on the subsystem `cert-faa-bvlos-waiver`.

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

### 2018-04 — Volansi VBAT

- **id:** `volansi-vbat`
- **corpus:** private
- **ip status:** patented
- **creator:** Volansi Inc / Martin UAV (acquired by Shield AI 2021)
- **disclosure citation:** Volansi VBAT autonomous tail-sitter cargo VTOL publicly disclosed April 2018; Volansi delivered medical and military supplies operationally 2019-2022. Acquired by Shield AI 2021-08. Volans-i original company ceased independent operation 2022 after acquisition by Shield AI.
- **disclosed subsystems:** `transition-tail-sitter-pitch-up`, `lift-ducted-fan-array`, `autonomy-pilot-removed`, `autonomy-bvlos-detect-and-avoid`, `cert-faa-bvlos-waiver`

**Prior art notes:**

> Volansi VBAT is the leading autonomous tail-sitter cargo VTOL deployed operationally for medical/military supply runs 2019-2022. Establishes prior art for: (1) ducted-fan tail-sitter cargo VTOL architecture, (2) operational FAA BVLOS waiver framework for autonomous tail-sitter UAS. Together with aerovironment-skytote and pivotal-blackfly, comprehensively places tail-sitter VTOL architecture in modern operational coverage.

**Sources:**

1. Volans-i / Volansi press releases 2018-2022.
2. Shield AI acquisition disclosures 2021.
3. FAA Part 137 / UAS operational approvals public records.

---

## License

CC0 1.0 Universal (public domain dedication). No copyright restrictions on
use, citation, copying, or redistribution.

---

*Generated from <https://github.com/openIE-dev/free-evtol-corpus> at corpus revision `7e83101`.*
