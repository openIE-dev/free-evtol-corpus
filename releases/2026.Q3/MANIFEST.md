# Release 2026.Q3

| | |
|---|---|
| Date (UTC) | 2026-05-08T13:31:45Z |
| Tarball | `corpus-2026.Q3.tar.gz` |
| SHA-256 | `764c959368732665aba6f73b41768107fde864156cf83afc3a5ff1f04e671688` |
| Entries |      114 |

## Timestamping artifacts

| Layer | File | Status |
|---|---|---|
| RFC 3161 (FreeTSA) | `freetsa.tsr` | ✓ |
| RFC 3161 (DigiCert) | `digicert.tsr` | ✓ |
| OpenTimestamps | `corpus-2026.Q3.tar.gz.ots` | ✓ (initially unconfirmed) |

## Verification

```
# Verify hash
sha256sum -c SHA256SUMS

# Verify FreeTSA timestamp
openssl ts -verify -in freetsa.tsr \
  -data corpus-2026.Q3.tar.gz \
  -CAfile cacert.pem -untrusted tsa.crt

# Verify DigiCert timestamp
openssl ts -verify -in digicert.tsr \
  -data corpus-2026.Q3.tar.gz \
  -CAfile digicert-chain.pem

# Verify OpenTimestamps proof
ots verify corpus-2026.Q3.tar.gz.ots -f corpus-2026.Q3.tar.gz
```

## What this release attests

The exact byte sequence of `corpus-2026.Q3.tar.gz` (SHA-256 `764c959368732665aba6f73b41768107fde864156cf83afc3a5ff1f04e671688`)
existed at or before the timestamps recorded in the .tsr and .ots files.
The contents of that tarball — including `corpus.jsonl` with its
     114 entries — are therefore public disclosures as of those
timestamps, citable as 102 prior art against any patent with a later
effective filing date.

## Discoverability

After release, this tarball should be:

- [ ] Submitted to Google Patents non-patent literature corpus
- [ ] Registered with Crossref / Zenodo for DOI assignment
- [ ] Posted to arXiv (cs.RO or eess.SY) as a citeable preprint
- [ ] Linked from openie-dev.github.io / openie.dev for crawler discovery
- [ ] Optionally: high-value entries submitted individually to IP.com

See `TIMESTAMPING.md` for full discoverability checklist.
