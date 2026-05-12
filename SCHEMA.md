---
title: Schema
layout: default
nav_order: 4
---

# Free eVTOL Corpus — Schema v0.1

## Status

v0.1 is the initial schema. Adapted from the Free Humanoid Corpus schema
v0.2, with humanoid-specific fields (morphology_family, dof_count, end_effector,
height_m, mass_kg, runtime_minutes) replaced by eVTOL-appropriate fields
(lift_architecture, rotor_count, mtow_kg, length_m, wingspan_m, pax_count,
endurance_minutes, range_km, cruise_speed_kt, transition_method, cert_path).

The tool-required fields (`id`, `canonical_name`, `corpus`,
`first_disclosure_date`, `schema_version`, `disclosure_citation`,
`prior_art_notes`, `sources`, `disclosed_subsystems`, `lineage_ancestors`,
`lineage_descendants`, `draft`, `last_updated`) are identical across both
corpora so tooling is shared.

## Purpose

A structured catalog of every eVTOL aircraft and eVTOL-adjacent flying
machine — current commercial air taxis, military VTOL demonstrators,
academic rotorcraft, jetpacks, hover bikes, flying-car concepts, and the
science fiction works that anticipated them.

**The corpus IS the prior art commons.** This is a load-bearing architectural
decision. Every entry is a defensive publication artifact, not a Wikipedia
entry. The commons does not sit on top of the corpus as a separate layer; the
structured data in this repository, timestamped at the moment of commit, is
itself the invalidity-contention material that future challenges will draw
from.

The corpus serves three functions, in priority order:

1. **Defensive publication.** Every entry, at the moment of merge and timestamp,
   is a public disclosure of the engineering, design, and prior art it
   describes. `prior_art_notes` is not editorial commentary — it is the
   element-by-element analysis a competent examiner or invalidity-contention
   attorney could cite.
2. **Design space map.** What has been imagined, what has been built, what has
   been claimed, and where the gaps are.
3. **Citation graph.** Who built on whom, what lineage each design belongs to,
   what intellectual debts are owed.

## Quality bar for entries

An entry is not done when the schema fields are filled. An entry is done when:

- `disclosure_citation` resolves to a primary source verifiable by a third party.
- `first_disclosure_date` is defensible against challenge — earliest verifiable
  public disclosure, not earliest plausible date.
- `prior_art_notes` reads as a 102/103 anticipation analysis someone unrelated
  to us could cite without rewriting. It identifies specific subsystems disclosed
  and what claims those disclosures could anticipate.
- `sources` cite primary references (papers, books, patents, episodes), not
  Wikipedia or aggregators, except where the aggregator is itself the primary
  source.
- For patented entries, `ip_citations` lists actual patent numbers, and
  `prior_art_notes` points back at anticipating prior art entries by id.

Entries below this bar may be merged with a `draft: true` flag to make
incremental progress visible, but they do not yet count as commons material.

## License posture

CC0-1.0. The corpus itself is public domain dedication. Individual entries cite
their sources but the structured catalog is unencumbered.

## Entry schema

Each entry is one record. Required fields are marked [R], optional [O].

```
id                      [R]  slug, kebab-case, globally unique within corpus
canonical_name          [R]  the name most commonly used in literature
aliases                 [O]  list of alternate names, model numbers, codenames
corpus                  [R]  one of: private | open | fictional | academic
first_disclosure_date   [R]  ISO 8601 date or year; earliest verifiable public reference
disclosure_citation     [R]  source for the first_disclosure_date (DOI, ISBN, URL, patent #, episode ID)
creator                 [R]  company / lab / studio / author / collective
creator_country         [O]  ISO country code of creator
lift_architecture       [R]  see lift-architecture taxonomy below
rotor_count             [O]  total lift rotor / propulsor count if disclosed
propulsion_type         [O]  electric | hybrid-series | hybrid-parallel | turbo-electric | hydrogen-fuel-cell | combustion | fictional | unknown
propulsion_details      [O]  motor topology, ducted vs. open, tip-speed, etc.
mtow_kg                 [O]  maximum takeoff weight in kg, if disclosed
empty_mass_kg           [O]  empty weight in kg, if disclosed
length_m                [O]  airframe length in meters, if disclosed
wingspan_m              [O]  wingspan or rotor-tip-to-rotor-tip in meters, if disclosed
pax_count               [O]  total seat count including pilot; 0 for cargo, null for fictional
payload_kg              [O]  payload capacity in kg, if disclosed
power_source            [O]  battery chemistry, fuel type, fuel cell, tethered, fictional
endurance_minutes       [O]  hover or total flight endurance, minutes, if disclosed
range_km                [O]  range in km, if disclosed
cruise_speed_kt         [O]  cruise speed in knots, if disclosed
hover_ceiling_m         [O]  service ceiling for hover, if disclosed
transition_method       [O]  how it transitions hover→cruise (none / tilt-rotor / tilt-wing / tilt-duct / vectored-thrust / clutched-lift-fan / tail-sitter-pitch-up / mode-shutdown / N/A)
control_architecture    [O]  fly-by-wire, mechanical, simplified-vehicle-operations, autonomous, fictional, etc.
sensing                 [O]  air data, IMU, radar altimeter, lidar, etc.
notable_capabilities    [O]  list of disclosed/claimed capabilities
cert_path               [O]  Part 23 | Part 25 | Part 27 | Part 29 | SC-VTOL | Part 103 | experimental | military | fictional | none
ip_status               [R]  patented | open-permissive | open-copyleft | public-domain | fictional | trade-secret | unknown
ip_citations            [O]  patent numbers, license identifiers, repo URLs
prior_art_notes         [O]  what subsystems/claims this entry could anticipate as 102/103 prior art
lineage_ancestors       [O]  ids of entries this design descends from
lineage_descendants     [O]  ids of entries that descend from this (filled in later passes)
sources                 [R]  list of citations (papers, books, articles, repos, episodes)
notes                   [O]  free-text observations
disclosed_subsystems    [O]  structured tags identifying specific subsystems disclosed
                             (see subsystem taxonomy below); enables targeted prior art search
cpc_classifications     [O]  CPC classification codes for examiner discoverability
                             (e.g., "B64C 29/00" for VTOL, "B64D 27/24" for electric propulsion)
draft                   [O]  boolean; true if the entry has not yet cleared the quality bar
schema_version          [R]  integer matching schema spec version
last_updated            [R]  ISO 8601 date
```

## Lift-architecture taxonomy

Single load-bearing axis for sorting entries.

- `multirotor` — fixed vertical rotors, often 4–18 (EHang, Volocopter, Jetson)
- `lift_plus_cruise` — separate lift rotors + pusher/puller cruise propulsion
  (Beta Alia, Wisk Cora)
- `tilt_rotor` — rotors tilt, wing fixed (Joby S4, Bell XV-15, V-22 Osprey)
- `tilt_wing` — wing and rotors tilt together (LTV XC-142, Canadair CL-84)
- `tilt_duct` — ducted fans tilt (Bell X-22, Doak VZ-4)
- `vectored_thrust` — single or few jets/fans with vectoring (Harrier, F-35B)
- `ducted_fan_array` — embedded ducted fans (Lilium, Aurora LightningStrike)
- `compound_rotorcraft` — main rotor + auxiliary thrust (Fairey Rotodyne, Jaunt)
- `cyclorotor` — cyclogyro / cycloidal propeller (D-Dalus, Pescara cyclogiro)
- `coleopter` — annular wing tail-sitter (SNECMA C.450)
- `tail_sitter` — fuselage rotates for transition (Convair XFY Pogo, X-13)
- `coanda_lift` — Avrocar-class
- `flapping_wing` — ornithopter (largely fictional)
- `jetpack_personal` — strap-on (Bell Rocket Belt, Gravity Industries, JetPack
  Aviation)
- `hover_bike` — open-rotor straddle (Aerofex, Hoversurf)
- `ground_effect_hybrid` — WIG / ekranoplan with VTOL-like operations (REGENT seaglider)
- `buoyant_hybrid` — airship with vectored-thrust VTOL augmentation; static
  (and partly aerodynamic) lift plus distributed/vectored electric thrust
  (LTA Pathfinder 1, Hybrid Air Vehicles Airlander 10, Flying Whales LCA60T)
- `transformer` — drive+fly or fold-out (ASKA A5, AeroMobil, PAL-V, Klein
  Vision AirCar, Alef Model A, Airbus Pop.Up, XPENG AeroHT)
- `fictional_repulsor` — anti-grav; useful as fictional-class anchor for
  generic "any VTOL" claims
- `other` — escape hatch with explanation in notes

## IP status definitions

- `patented` — known patents asserted, with patent numbers
- `open-permissive` — MIT, BSD, Apache, CERN-OHL-P, etc.
- `open-copyleft` — GPL, CERN-OHL-S, etc.
- `public-domain` — CC0 or equivalent dedication, or expired protection
- `fictional` — exists only in narrative; copyright on the depiction may exist
  but the engineering description is unencumbered as prior art
- `trade-secret` — claimed but not disclosed
- `unknown` — needs investigation

## Subsystem taxonomy

Tags applied to `disclosed_subsystems` to enable targeted prior art search. An
entry tags every subsystem it discloses with enough specificity to cite. Tags
are append-only to preserve cross-entry searchability.

**Lift architecture**
- `lift-distributed-electric-propulsion`
- `lift-tilt-rotor`
- `lift-tilt-wing`
- `lift-tilt-duct`
- `lift-vectored-thrust`
- `lift-ducted-fan-array`
- `lift-coaxial-rotor`
- `lift-cyclorotor`
- `lift-coanda-effect`
- `lift-tip-jet-rotor`
- `lift-compound-rotorcraft`
- `lift-modular-docking` — modular units that dock (in flight or on the ground)
  into a single composite multirotor airframe (ETH Distributed Flight Array,
  UPenn ModQuad, DRAGON, Airbus Pop.Up, Bell APT)
- `lift-buoyant-hybrid` — static (helium) lift augmented by distributed/vectored
  electric thrust for controlled VTOL (LTA Pathfinder 1, Airlander 10, Flying Whales)
- `lift-stopped-rotor` — rigid rotor that stops in flight to act as a fixed
  lifting surface (Sikorsky/DARPA X-Wing)

**Transition control**
- `transition-conversion-corridor`
- `transition-thrust-borne-to-wing-borne`
- `transition-3-bearing-swivel-duct`
- `transition-lift-fan-clutched`
- `transition-tail-sitter-pitch-up`
- `transition-mode-shutdown`

**Propulsion**
- `propulsion-bldc-direct-drive`
- `propulsion-bldc-geared`
- `propulsion-turbo-electric`
- `propulsion-hybrid-series`
- `propulsion-hybrid-parallel`
- `propulsion-hydrogen-fuel-cell`
- `propulsion-rim-driven-fan`
- `propulsion-tip-jet`

**Energy / power**
- `power-li-ion-pouch`
- `power-li-ion-cylindrical`
- `power-li-po`
- `power-solid-state`
- `power-battery-swap`
- `power-fast-charge-megawatt`
- `power-hybrid-genset`
- `power-tethered`

**Control allocation**
- `control-rotor-failure-reconfiguration`
- `control-differential-thrust-attitude`
- `control-fly-by-wire-triplex`
- `control-simplified-vehicle-operations`
- `control-trajectory-mpc`
- `control-zero-pilot-rl-policy`
- `control-fully-actuated-omnidirectional` — independent control of force and
  torque in all 6 DOF; arbitrary-attitude hover (ETH Omnicopter, Voliro, CycloTech)
- `control-swarm-coordinated-fleet` — one operator / planner controlling a fleet
  of N independent aircraft as a single coordinated system; formation flight and
  in-flight reconfiguration (KMel/UPenn nano-quad swarm, Intel Shooting Star,
  CollMot, ETH Flight Assembled Architecture)

**Autonomy**
- `autonomy-bvlos-detect-and-avoid`
- `autonomy-utm-integration`
- `autonomy-vertiport-approach`
- `autonomy-pilot-removed`

**Sensing**
- `sensing-air-data-boom`
- `sensing-radar-altimeter`
- `sensing-lidar-terrain`
- `sensing-rotor-icing-detection`
- `sensing-vibration-health-monitoring`
- `sensing-stereo-camera-daa`

**Safety / airframe**
- `safety-ballistic-parachute`
- `safety-rotor-burst-containment`
- `safety-emergency-autorotation`
- `safety-controlled-emergency-landing`
- `safety-redundant-bus`
- `airframe-composite-monocoque`
- `airframe-tilting-wing-spar`
- `airframe-in-flight-morphing` — airframe geometry actively reconfigures in
  flight (folding arms, transforming multilink body) with adaptive control
  allocation (EPFL folding drone, UZH Foldable Drone, DRAGON)
- `airframe-collision-resilient-cage` — rotating / decoupling protective cage
  enabling collision-tolerant flight and contact-based maneuvers (EPFL GimBall,
  ModQuad cuboid frame)

**Certification path**
- `cert-part-23`
- `cert-part-25`
- `cert-part-27`
- `cert-part-29`
- `cert-sc-vtol`
- `cert-part-103-ultralight`
- `cert-faa-bvlos-waiver`
- `cert-easa-special-condition-vtol`
- `cert-experimental`
- `cert-military`

This taxonomy is expected to grow. New tags are added with provenance — the
first entry to introduce a tag documents it in `notes`.

## Storage format

Master corpus: `corpus.jsonl` — one JSON object per line, append-only, git-tracked.
Per-corpus mirrors: `private.jsonl`, `open.jsonl`, `fictional.jsonl`, `academic.jsonl`.
Index: `CORPUS_INDEX.md` — generated, alphabetical by canonical_name with id and one-line summary.
Lineage graph: `lineage.json` — derived, ancestor/descendant DAG.

## Versioning

Schema version increments on breaking changes. Entries carry `schema_version` so
older entries can be migrated. v0.1 is the starting point and should be expected
to evolve once the seed slice exposes inadequacies.
