---
title: Release runbook
layout: default
nav_order: 7
---

# Release Runbook — 2026.Q3

This is the step-by-step procedure for cutting the first quarterly
release of the Free eVTOL Corpus.

## Step 1: Create the GitHub repo

Either via the GitHub CLI:

```bash
gh repo create openie-dev/free-evtol-corpus \
  --public \
  --description "Public-domain prior art commons for eVTOL and eVTOL-adjacent aircraft. CC0." \
  --homepage "https://openie-dev.github.io/free-evtol-corpus"
```

Or via the web UI at https://github.com/organizations/openie-dev/repositories/new
with the same name, public, no README/license/gitignore (those are in
the directory already).

## Step 2: Push the prepared directory

From your local copy of this directory:

```bash
git init -b main
git add .
git commit -m "Initial commit: free-evtol-corpus seed

Schema v0.1. CC0-1.0.
See SCHEMA.md and README.md for context."

git remote add origin git@github.com:openie-dev/free-evtol-corpus.git
git push -u origin main
```

## Step 3: Install OpenTimestamps client

The release script needs `ots` for Bitcoin anchoring. Install it once:

```bash
pip install opentimestamps-client
# or
pipx install opentimestamps-client
```

Confirm:
```bash
ots --version
```

## Step 4: Run a dry-run release

```bash
./release.sh 2026.Q3 --dry-run
```

This validates the corpus, regenerates derived artifacts, and builds
the deterministic tarball without any TSA submissions or git tagging.
Inspect `releases/2026.Q3/` to confirm the tarball contents and SHA-256.

## Step 5: Run the actual release

```bash
rm -rf releases/2026.Q3
./release.sh 2026.Q3
```

The script will:

1. Validate the corpus passes strict mode
2. Regenerate CORPUS_INDEX.md, lineage.json, per-corpus mirrors, cross-cuts
3. Build the deterministic tarball
4. Submit the hash to FreeTSA (RFC 3161, free)
5. Submit the hash to DigiCert (RFC 3161, free)
6. Submit to OpenTimestamps (Bitcoin anchoring, free)
7. Write `MANIFEST.md` documenting the release
8. Commit the release directory and tag the commit `2026.Q3`

If FreeTSA or DigiCert is temporarily down, the script will warn and
continue — as long as at least one RFC 3161 layer succeeds plus
OpenTimestamps, the release is valid.

## Step 6: Push the release

```bash
git push origin main
git push origin 2026.Q3
```

## Step 7: Upgrade the OpenTimestamps proof (in ~6 hours)

```bash
ots upgrade releases/2026.Q3/corpus-2026.Q3.tar.gz.ots
git add releases/2026.Q3/corpus-2026.Q3.tar.gz.ots
git commit -m "release: upgrade 2026.Q3 OpenTimestamps proof"
git push
```

## Step 8: Discoverability submissions

After the release tag is pushed and the OTS proof upgraded, the corpus
exists publicly with cryptographic proof of pre-existence. The remaining
work is making sure examiners and invalidity-contention attorneys
actually find it.

In rough priority order:

### 8a. Zenodo for DOI assignment

1. Go to https://zenodo.org/account/settings/github/
2. Sign in with GitHub
3. Find `openie-dev/free-evtol-corpus` and toggle it on
4. Trigger a Zenodo deposit by creating a GitHub release pointing at
   the `2026.Q3` tag
5. Zenodo automatically mints a DOI and archives the release tarball

Once the DOI is assigned, add it to the README and to MANIFEST.md.

### 8b. arXiv preprint

A 2-3 page methods paper is sufficient: schema, quality bar, timestamping
ceremony, intended use as defensive publication. Submit to cs.RO or
eess.SY.

### 8c. Google Patents non-patent literature

Google Patents indexes a subset of the open web. To accelerate:

1. Add the repo URL to openie-dev.github.io with descriptive anchor text
2. Submit the URL to Google Search Console
3. If you've gone the arXiv route, the arXiv URL is already in Google
   Patents' NPL corpus

### 8d. Internet Archive / Wayback Machine

Submit the GitHub repo URL and the release tarball URL to the Wayback
Machine:

```
https://web.archive.org/save/https://github.com/openie-dev/free-evtol-corpus
https://web.archive.org/save/https://github.com/openie-dev/free-evtol-corpus/releases/tag/2026.Q3
```

### 8e. Strategic announcements

- Blog post on openie.dev or openie-dev.github.io
- Posts to relevant communities (r/eVTOL, r/aviation, Hacker News,
  AIAA mailing lists, Vertical Flight Society)
- Direct outreach to academic labs working on eVTOL (NASA Langley/Glenn,
  Georgia Tech rotorcraft, TU Delft, DLR) — they are likely contributors
  and benefit from the commons existing
- Direct outreach to patent attorneys working invalidity contention
  in aerospace — they are the consumers of the cross-cuts

## Quarterly cadence

After 2026.Q3 ships, the cadence is:

- 2026.Q4 in early October 2026
- 2027.Q1 in early January 2027
- 2027.Q2 in early April 2027

Each quarter captures the corpus state at that moment with full
timestamping.

## If something goes wrong

The release script is idempotent within a version. If a step fails, fix
the underlying issue and re-run — the deterministic tarball means the
hash stays stable.

The one thing that can't be retried: once a git tag is pushed to the
public remote, deleting and re-tagging is bad form. So don't push the
tag until you're confident the release directory is correct.

If you need to fix something **after** the tag is pushed, cut a new tag
(`2026.Q3.1` or move on to `2026.Q4`) rather than rewriting history.
