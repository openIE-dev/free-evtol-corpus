---
title: Home
layout: home
nav_order: 1
description: "A public-domain prior art commons for eVTOL and eVTOL-adjacent aircraft. CC0."
permalink: /
---

# Free eVTOL Corpus
{: .fs-9 }

A public-domain prior art commons covering eVTOL aircraft and eVTOL-adjacent flying machines — passenger air taxis, jetpacks, hover bikes, personal VTOL, tilt-rotor and tilt-wing demonstrators, military VTOL, ducted-fan and vectored-thrust craft, and the science fiction and academic literature that anticipated all of them.
{: .fs-6 .fw-300 }

[Browse the corpus](browse/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Cross-cuts](cross_cuts/){: .btn .fs-5 .mb-4 .mb-md-0 .mr-2 }
[GitHub](https://github.com/openIE-dev/free-evtol-corpus){: .btn .fs-5 .mb-4 .mb-md-0 }

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](https://github.com/openIE-dev/free-evtol-corpus/blob/main/LICENSE)

---

**The corpus IS the prior art commons.** Every entry, at the moment of timestamped commit and quarterly release, is a defensive publication. There is no separate commons layer above this catalog — the structured data here, combined with the cryptographic timestamping in `releases/`, is itself the invalidity-contention material.

---

## Use it from the command line

```bash
git clone https://github.com/openIE-dev/free-evtol-corpus.git
cd free-evtol-corpus

# Validate the corpus and your local edits
python3 tools/validate.py corpus.jsonl --strict

# Regenerate derived artifacts after editing corpus.jsonl
python3 tools/index.py .
python3 tools/cross_cuts.py
```

---

## License

CC0 1.0. Public domain dedication. The corpus exists to be cited, copied, indexed, mirrored, embedded, ingested, and built upon. No usage license required.
