---
title: transition-mode-shutdown
parent: Cross-cuts
layout: default
---

# Cross-cut: `transition-mode-shutdown`

**20 corpus entries disclose this subsystem.**

Earliest disclosure: 1986-12-02

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Sikorsky/DARPA X-Wing (1986-12-02)

- **id**: `sikorsky-x-wing`
- **corpus**: academic
- **creator**: Sikorsky Aircraft / NASA / DARPA / U.S. Army
- **disclosure**: RSRA/X-Wing technology demonstrator first flight (fixed-wing mode, rotor stopped) 1986-12-02 at NASA Ames; program cancelled 1988 before in-flight rotor stop/start was demonstrated. Built on the Sikorsky S-72 RSRA airframe with a four-bladed rigid rotor that could be stopped in flight to act as an X-shaped fixed wing. Documented in NASA / DARPA technical reports.
- **ip status**: public-domain
- **prior art notes**: The Sikorsky/DARPA X-Wing (RSRA-based, 1986) is the foundational disclosure of the stopped-rotor / rotor-wing architecture: a rigid rotor with circulation control that spins for hover, then stops to act as a fixed X-shaped wing for high-speed cruise. Establishes prior art for: (1) stoppable-in-flight rigid rotor that doubles as a fixed wing, (2) circulation-control (blown) rotor blades enabling lift across the full azimuth, (3) the rotor-stop-and-restart transition concept. Although in-flight rotor stop was never demonstrated before cancellation, the design disclosure is complete in NASA/DARPA documentation. Anticipates: any modern eVTOL claim involving stoppable lift rotors that become fixed lifting surfaces (a recurring concept in high-speed-cruise VTOL proposals).

## PX4 VTOL flight stack (2014-09)

- **id**: `px4-vtol`
- **corpus**: open
- **creator**: PX4 / Dronecode Foundation / Lorenz Meier et al.
- **disclosure**: PX4 VTOL framework first merged 2014-09 (canonical PX4 git history at github.com/PX4/PX4-Autopilot); foundational paper Meier, L. et al. 'PX4: A Node-Based Multithreaded Open Source Robotics Framework for Deeply Embedded Platforms,' ICRA 2015.
- **ip status**: open-permissive
- **prior art notes**: PX4 is the BSD-licensed reference flight stack for VTOL aircraft, used in commercial products and academic research worldwide. Establishes prior art for: (1) modular VTOL transition state machine with named airframe types (Standard, Tail-sitter, Tilt-rotor), (2) EKF2-based state estimation across regime transitions, (3) open-source rotor-failure handling. Like ArduPilot, the BSD license lets PX4 disclosures function unambiguously as prior art.

## ArduPilot QuadPlane VTOL (2015-04)

- **id**: `ardupilot-quadplane`
- **corpus**: open
- **creator**: ArduPilot Project / Andrew Tridgell et al.
- **disclosure**: ArduPilot QuadPlane functionality first merged into ArduPlane main branch 2015-04 (commit history available at github.com/ArduPilot/ardupilot); first general public release with QuadPlane support: ArduPlane 3.5.0, 2015-12-14.
- **ip status**: open-copyleft
- **prior art notes**: ArduPilot QuadPlane is the GPL-licensed reference implementation of generic VTOL flight control. Establishes prior art (under GPL, but the architectural disclosure is unencumbered as prior art for patent purposes) for: (1) generic transition controller for lift+cruise, tilt-rotor, tilt-wing, and tail-sitter VTOLs, (2) rotor-failure detection and reconfiguration in multirotor lift, (3) Q_ASSIST transitional thrust assist algorithms. The git commit history provides timestamped disclosure of every subsystem-level innovation. Filed against any post-2015 patent claim on basic VTOL transition control or rotor-failure reconfiguration in multirotor lift, this is anticipating prior art.

## Orb Aerospace Nomad (2017)

- **id**: `orb-aerospace-nomad`
- **corpus**: private
- **creator**: Orb Aerospace / Skyways Inc
- **disclosure**: Skyways Inc founded ~2017 in Austin, Texas. Skyways A22 autonomous VTOL cargo aircraft publicly demonstrated for USMC Naval Air Systems Command (NAVAIR) starting 2019; awarded USMC Tactical Resupply Vehicle (TRV-150) contract 2020. Orb Aerospace product line including the Orb Nomad publicly disclosed via Air Force AFWERX program records, Skyways press materials, and U.S. defense contracting disclosures. Distinct architectural commitment to industrial / defense / emergency-response cargo missions rather than urban passenger air taxi.
- **ip status**: patented
- **prior art notes**: Orb Aerospace / Skyways establishes US prior art for the industrial / defense / emergency-response cargo eVTOL category — distinct architectural and operational commitment from urban passenger air taxi. The USMC TRV-150 contract (2020) is among the earliest production-track autonomous VTOL cargo deployments in U.S. military service. Establishes prior art for: (1) hybrid-electric autonomous cargo eVTOL specifically designed for unprepared / austere site operations, (2) the industrial-first eVTOL deployment thesis (cargo and defense use cases preceding consumer urban air taxi). Together with elroy-air-chaparral, pyka-pelican, sabrewing-rhaegal-a, volansi-vbat, wingcopter-198, dji-flycart-30, and amsl-vertiia, comprehensively places autonomous hybrid-electric cargo eVTOL architecture in 2017-2024 commercial prior art across US, DE, AU, and CN industrial lineages.

## Zuri eVTOL (2017-03)

- **id**: `zuri-evtol`
- **corpus**: private
- **creator**: Zuri s.r.o (Prague, Czech Republic)
- **disclosure**: Zuri founded 2017-03 by Michal Illich, Stanislav Saling, and Daniel Hadacek; first sub-scale prototype publicly demonstrated 2018-09; full-scale Zuri 2.0 prototype unveiled 2021-10-12 in Pisek and reached first hover 2023-09-22. EASA Special Condition VTOL certification dialogue 2022 onward.
- **ip status**: patented
- **prior art notes**: Zuri eVTOL is the lead Czech (and Central European) commercial eVTOL — hybrid-electric lift+cruise distinct from pure-battery competitors in its 700 km range targeting. Establishes Czech prior-art lineage for hybrid-electric eVTOL and adds to the global hybrid-eVTOL prior-art base alongside Honda eVTOL, AMSL Aero Vertiia, and Elroy Air Chaparral.

## Wisk Aero Cora / Gen 6 (2018-03-13)

- **id**: `wisk-cora`
- **corpus**: private
- **creator**: Wisk Aero LLC (Boeing / Kitty Hawk joint venture)
- **disclosure**: Cora aircraft publicly unveiled 2018-03-13 by Kitty Hawk; first untethered hover earlier in 2017 (test campaign in New Zealand); Wisk Aero JV with Boeing announced 2019-12-19; Gen 6 production design unveiled 2022-10-03; Boeing acquired Kitty Hawk's interest 2023-05, making Wisk a Boeing subsidiary.
- **ip status**: patented
- **prior art notes**: Wisk Cora / Gen 6 is the leading US autonomous (no on-board pilot) passenger eVTOL — distinct architectural commitment to autonomy from Joby, Archer, Beta. Lift+cruise architecture with 12+1 propulsor count. Establishes US prior-art lineage for autonomous-passenger commercial lift+cruise eVTOL targeting FAA Part 23 / Special Conditions.

## EmbraerX eVTOL concept (2018) (2018-05-09)

- **id**: `embraerx-evtol-concept`
- **corpus**: private
- **creator**: EmbraerX (Embraer S.A. internal venture)
- **disclosure**: Embraer publicly unveiled its eVTOL air taxi concept design at the Uber Elevate Summit, Los Angeles, 2018-05-09. EmbraerX (Embraer's internal venture launched 2017-10) led the design. The 2018 concept preceded Eve UAM Solutions (Embraer subsidiary, 2020-10-08) and Eve Holding spinoff (NYSE: EVEX SPAC merger, 2022-05-09).
- **ip status**: patented
- **prior art notes**: EmbraerX 2018 is the original Brazilian disclosure of the lift+cruise architecture that subsequently became Eve Air Mobility's production design. Establishes Brazilian / Latin American prior-art lineage two years earlier than the 2020 Eve Air Mobility entity. The Uber Elevate Summit 2018 unveiling makes this a publicly-dated Embraer corporate disclosure with documented engineering depth in subsequent Embraer technical materials. Combined with eve-air-mobility (2020), provides a multi-year Embraer lineage for the 8+1 lift+cruise architecture.

## Pyka Pelican Cargo (2018-08)

- **id**: `pyka-pelican`
- **corpus**: private
- **creator**: Pyka (Oakland, California)
- **disclosure**: Pyka founded 2018; Egret (predecessor agricultural eVTOL) operational since 2019; Pelican Cargo unveiled 2022-06-21; FAA Part 137 ag operations approval (Pelican Spray) 2023-04. Pyka's autonomy stack documented in open technical white papers.
- **ip status**: patented
- **prior art notes**: Pyka Pelican is the leading US autonomous cargo eVTOL targeting agricultural and middle-mile logistics. Establishes prior art for: (1) autonomous lift+cruise cargo eVTOL operating under Part 137 / Part 23, (2) electric agricultural-spray eVTOL (Pelican Spray variant operational since 2023). Distinct architectural commitment from passenger eVTOL: prioritizes payload, range, and short-strip operation over hover endurance.

## Pegasus Vertical Business Jet (2018-11-08)

- **id**: `pegasus-universal-aerospace`
- **corpus**: private
- **creator**: Pegasus Universal Aerospace (Johannesburg, South Africa)
- **disclosure**: Pegasus Vertical Business Jet design publicly unveiled 2018-11-08 at Aero South Africa; subsequent design refinements 2020–2024. Pegasus Universal Aerospace founded 2017 by Reza Mia. South African Civil Aviation Authority engagement on certification framework 2021 onward.
- **ip status**: patented
- **prior art notes**: Pegasus Vertical Business Jet is South Africa's lead commercial VTOL design — distinct architectural commitment to executive-jet operations (2,200 km range, 400 kt cruise) with VTOL hover capability. Establishes African continental prior-art lineage for commercial VTOL business aviation distinct from urban air taxi. Architecturally similar to Lockheed Martin / Aurora LightningStrike (XV-24A, US military 2016) in fuselage-internal lift fan + cruise jet topology.

## Elroy Air Chaparral C1 (2019-01-30)

- **id**: `elroy-air-chaparral`
- **corpus**: private
- **creator**: Elroy Air Inc (San Francisco)
- **disclosure**: Elroy Air founded 2016 by David Merrill and Kofi Asante; sub-scale Chaparral demonstrator publicly unveiled 2019-01-30; full-scale C1 first hover flight 2023-11-12 at Camarillo, CA. Air Force AFWERX / USAF Agility Prime contracts 2021-09 onward.
- **ip status**: patented
- **prior art notes**: Elroy Air Chaparral establishes prior art for: (1) hybrid-electric (turbine-genset + battery) cargo eVTOL, distinct from pure-battery designs by extending range to 500+ km, (2) modular swappable cargo-pod architecture decoupled from aircraft turnaround. Hybrid powerplant anticipates similar claims on series-hybrid eVTOL propulsion topology.

## Sabrewing Rhaegal-A (2019-04)

- **id**: `sabrewing-rhaegal-a`
- **corpus**: private
- **creator**: Sabrewing Aircraft Company
- **disclosure**: Sabrewing Aircraft Rhaegal-A unveiled April 2019; sub-scale prototype hover trials 2020. Designed for 4,500 lb (2,040 kg) cargo capacity in unmanned configuration. Documented in Sabrewing technical materials and FAA filings.
- **ip status**: patented
- **prior art notes**: Sabrewing Rhaegal-A establishes US prior art for heavy-cargo (2-ton class) hybrid-electric eVTOL with ducted-fan architecture. Distinct from Elroy Air Chaparral by larger payload and ducted-fan rather than open-rotor lift. Anticipates other heavy-cargo eVTOL claims filed post-2019.

## Beta Technologies Alia-250 (2020-03-10)

- **id**: `beta-alia-250`
- **corpus**: private
- **creator**: Beta Technologies
- **disclosure**: Beta Technologies / Kyle Clark publicly unveiled Alia-250 design 2020-03-10; first hover flight 2020-05; first full transition flight 2021-04; multiple cross-country flights 2022–2024 publicly documented.
- **ip status**: patented
- **prior art notes**: Beta Alia-250 is the canonical commercial lift+cruise eVTOL: lift rotors stop and shut down in cruise, with a separate pusher providing forward propulsion. Architecturally simpler than tilt-rotor (no transition envelope coupling between lift and cruise), at cost of cruise drag from stopped lift rotors. Establishes prior art for: (1) production-scale lift+cruise architecture with mode-shutdown transition, (2) coaxial lift-pair geometry with single pusher cruise. Cited extensively by NASA Langley as the lift+cruise reference design.

## Eve Air Mobility eVTOL (2020-10-08)

- **id**: `eve-air-mobility`
- **corpus**: private
- **creator**: Eve Holding Inc (Embraer S.A. spinoff)
- **disclosure**: Eve UAM Solutions launched as Embraer subsidiary 2020-10-08; spun off as standalone Eve Holding via SPAC merger 2022-05-09 (NYSE: EVEX). Aircraft design publicly unveiled 2022; first prototype unveiled 2024.
- **ip status**: patented
- **prior art notes**: Eve Air Mobility is Brazil's lead commercial eVTOL, backed by Embraer's 100+-year aerospace heritage. The 8+1 lift+cruise architecture is architecturally similar to Beta Alia and AutoFlight Prosperity I; establishes Brazilian / Latin American prior-art lineage for commercial lift+cruise eVTOL. Eve has the deepest commercial aerospace certification experience among any eVTOL company by virtue of Embraer parentage.

## AMSL Aero Vertiia (2021-03)

- **id**: `amsl-vertiia`
- **corpus**: private
- **creator**: AMSL Aero Pty Ltd (Bankstown, Australia)
- **disclosure**: AMSL Aero Vertiia design publicly unveiled March 2021; sub-scale prototype hover testing 2022; first hover flight 2023-02-15. AMSL Aero founded 2017 by Andrew Moore (former CSIRO and Boeing engineer) and Siobhan Lyndon. Targeted at hydrogen-fuel-cell-powered eVTOL ambulance and regional connectivity missions.
- **ip status**: patented
- **prior art notes**: AMSL Aero Vertiia is Australia's lead commercial eVTOL with a distinctive commitment to hydrogen-fuel-cell propulsion for 1,000 km range — addressing the energy-density limitation of pure-battery eVTOL. Establishes Australian prior-art lineage for hydrogen-eVTOL and for long-range regional eVTOL distinct from short-range urban air taxi. Anticipates other hydrogen-fuel-cell eVTOL claims (e.g., Joby's post-acquisition H2 program, Airbus ZEROe rotorcraft).

## Airbus CityAirbus NextGen (2021-09-21)

- **id**: `airbus-cityairbus-nextgen`
- **corpus**: private
- **creator**: Airbus Helicopters (Donauwörth, Germany) / Airbus Defence and Space
- **disclosure**: Airbus CityAirbus NextGen design publicly unveiled 2021-09-21 at Airbus Summit; first scaled prototype hover 2024-09. EASA SC-VTOL type-certification process initiated 2022. Predecessor CityAirbus demonstrator first hover 2019-05-03.
- **ip status**: patented
- **prior art notes**: Airbus CityAirbus NextGen is the production-track lift+cruise successor to the Vahana research program. Establishes German industrial prior-art lineage for production-scale lift+cruise passenger eVTOL with V-strut lift-rotor mounting geometry distinct from boom-mounted competitors (Beta Alia, Eve, Wisk). Airbus's industrial certification scale and EASA insider position make this a particularly important commons-grade entry.

## Honda eVTOL (2021-09-30)

- **id**: `honda-evtol`
- **corpus**: private
- **creator**: Honda Motor Company / Honda Aircraft Company
- **disclosure**: Honda Motor Company eVTOL program publicly disclosed 2021-09-30 at 'Honda Dream Loop' announcement; design materials and target specifications subsequently disclosed in Honda investor briefings 2022–2024. Targeted commercial operation 2030.
- **ip status**: patented
- **prior art notes**: Honda eVTOL establishes prior art for hybrid-turbine-electric passenger eVTOL — Honda's specific architecture decision is to use a gas-turbine genset (leveraging HondaJet experience) for range extension. Anticipates other turbine-hybrid eVTOL claims (Elroy Air Chaparral, AMSL Aero Vertiia variants).

## REGENT Viceroy seaglider (2021-10)

- **id**: `regent-viceroy-seaglider`
- **corpus**: private
- **creator**: REGENT Craft Inc (Rhode Island, USA) — founded by Boeing / Aurora Flight Sciences alumni
- **disclosure**: REGENT Craft (founded 2020 by Billy Thalheimer and Mike Klinker, ex-Aurora Flight Sciences / Boeing) unveiled the Viceroy seaglider 2021-10; quarter-scale prototype first flight 2022-08; full-scale Viceroy prototype rollout / first sea trials 2024-2025. The seaglider operates in three modes — floating (hull), foiling (hydrofoils), and flying (wing-in-ground-effect, ~9 m altitude). Documented in REGENT technical materials, U.S. Marine Corps / Navy contracts, and patent filings.
- **ip status**: patented
- **prior art notes**: REGENT Viceroy is the foundational modern disclosure of the electric wing-in-ground-effect (WIG) 'seaglider' — a distributed-electric-propulsion craft that transitions floating → hydrofoiling → ground-effect flight, operating a few meters above water. Establishes prior art for: (1) electric WIG / ekranoplan-class craft with distributed blown-wing propulsion, (2) the hull/foil/flight three-mode transition, (3) retractable-hydrofoil takeoff for a winged aircraft. While not vertical-takeoff in the classical sense, it is eVTOL-adjacent (the corpus scope covers ground-effect hybrids with VTOL-like operations) and shares DEP blown-wing architecture with eVTOL. Anticipates other electric-WIG and seaglider claims (a growing segment — also pursued by Wigetworks AirFish and others).

## AIR ONE (eVTOL) (2021-10-04)

- **id**: `air-one`
- **corpus**: private
- **creator**: AIR Mobility Ltd (Pardes Hanna, Israel)
- **disclosure**: AIR ONE publicly unveiled 2021-10-04 in San Francisco; first untethered manned hover flight 2023-06-19 at AIR Pardes Hanna test site, Israel. AIR Mobility founded by Rani Plaut and Chen Rosen, 2018.
- **ip status**: patented
- **prior art notes**: AIR ONE is Israel's lead consumer-grade eVTOL — distinct from CityHawk (commercial ducted-fan) by addressing the personal-recreational segment. Lift+cruise architecture targeting Part 23 certification with consumer operability emphasis. Establishes Israeli prior-art lineage for consumer/recreational eVTOL distinct from passenger air taxi.

## AutoFlight Prosperity I (2021-12-13)

- **id**: `autoflight-prosperity-i`
- **corpus**: private
- **creator**: AutoFlight (Shanghai)
- **disclosure**: AutoFlight Prosperity I publicly unveiled 2021-12-13; first untethered hover flight 2022-04; full-scale prototype transition flight 2023-02-23 at Kunshan; cross-Pearl River Delta demonstration flight Hong Kong → Macau 2024-04-29. AutoFlight founded by Tian Yu (former co-founder of EHang).
- **ip status**: patented
- **prior art notes**: AutoFlight Prosperity I is the leading Chinese lift+cruise eVTOL — architectural sibling to Beta Alia-250 with eight rather than four lift rotors. The 250 km Hong Kong-Macau demonstration flight (2024-04-29) is the longest eVTOL flight publicly documented as of mid-2024. Establishes Chinese prior-art lineage for lift+cruise architecture and supports EASA SC-VTOL certification basis dual-track with EHang's CAAC certification.

## ePlane Company e200 (2022-08)

- **id**: `eplane-company-e200`
- **corpus**: private
- **creator**: The ePlane Company (IIT Madras spinout)
- **disclosure**: The ePlane Company e200 unveiled 2022-08; first sub-scale prototype hover flight 2022-12; full-scale prototype rolled out 2023-09 at IIT Madras Research Park. Founded 2017 by Prof. Satya Chakravarthy. Awarded Anjani Mashelkar Inclusive Innovation Award 2023.
- **ip status**: patented
- **prior art notes**: ePlane e200 is India's lead commercial eVTOL — IIT Madras research spinout with explicit design constraint for compact urban Indian airspace. Establishes Indian prior-art lineage for commercial lift+cruise eVTOL and the design philosophy of compact-footprint operation in dense urban environments. Targeted at DGCA (Directorate General of Civil Aviation, India) certification.
