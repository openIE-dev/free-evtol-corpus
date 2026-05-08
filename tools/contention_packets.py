#!/usr/bin/env python3
"""contention_packets.py — regenerate per-tag invalidity-contention packets.

Usage:
    python3 tools/contention_packets.py

Reads `corpus.jsonl` and groups entries by each tag in their
`disclosed_subsystems`. For each tag with two or more entries, writes a
markdown packet at `contention_packets/<tag>.md` formatted as a
structured invalidity-contention reference an attorney can use directly
when challenging a patent in that subsystem area.

Each packet:
  - is chronologically ordered, earliest disclosure first
  - reproduces every entry's `prior_art_notes` verbatim (the element-by-
    element 102/103 anticipation analysis)
  - lists `disclosure_citation`, `creator`, `ip_status`, `corpus`, and
    `sources` as citation-ready fields
  - is Jekyll-front-matter wrapped for nav integration

Hand-written patent-specific packets (e.g. `joby-aviation.md`,
`archer-aviation.md`) are preserved across regenerations — only files
matching the auto-generated name pattern are wiped.

Also writes:
  - `contention_packets/INDEX.md`  — table of contents for all packets
  - `contention_packets/README.md` — what these are and how to use them

These are derived artifacts. Re-run after any edit to corpus.jsonl.
"""
import json
import subprocess
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
OUT_DIR = ROOT / "contention_packets"

REPO_URL = "https://github.com/openIE-dev/free-evtol-corpus"


def load_corpus():
    return [json.loads(l) for l in CORPUS.read_text().splitlines() if l.strip()]


def date_key(e):
    return e.get("first_disclosure_date") or ""


def git_short_sha():
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(ROOT),
            stderr=subprocess.DEVNULL,
        )
        return out.decode("utf-8").strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def is_draft(e):
    return bool(e.get("draft"))


def fmt_date(d):
    return d if d else "?"


def render_packet(tag, entries, nav_order, generated_iso, git_sha):
    entries_sorted = sorted(entries, key=date_key)
    earliest = entries_sorted[0].get("first_disclosure_date") or "?"
    latest = entries_sorted[-1].get("first_disclosure_date") or "?"
    n = len(entries_sorted)
    n_draft = sum(1 for e in entries_sorted if is_draft(e))
    n_commons = n - n_draft

    lines = [
        "---",
        f'title: "{tag}"',
        'parent: "Invalidity Contentions"',
        f"nav_order: {nav_order}",
        "layout: default",
        "---",
        "",
        f"# Invalidity Contention Packet — `{tag}`",
        "",
        f"**Generated:** {generated_iso}  ",
        f"**Cross-cut tag:** `{tag}`  ",
        f"**Entries:** {n} ({n_commons} commons-grade, {n_draft} draft)  ",
        f"**Earliest disclosure:** {fmt_date(earliest)}  ",
        f"**Most recent disclosure:** {fmt_date(latest)}",
        "",
        "---",
        "",
        "## How to use this packet",
        "",
        "This document is an invalidity-contention packet — a chronologically-ordered",
        f"list of every disclosed prior art reference in the Free eVTOL Corpus that",
        f"bears on the subsystem `{tag}`.",
        "",
        "To use it:",
        "",
        "1. Identify the patent claim element being challenged.",
        "2. Match the element against the entries below in chronological order (earliest",
        "   first). The earliest entry that discloses the element is the strongest 102",
        "   anticipation candidate.",
        "3. For 103 obviousness contentions, identify the closest two-or-more entries",
        "   that together disclose all claim elements.",
        "4. Each entry's **prior_art_notes** field is element-by-element 102/103",
        "   anticipation analysis — citable as-is.",
        "5. Verify the timestamp authority via the procedures in the corpus repo's",
        "   release artifacts (FreeTSA RFC 3161, DigiCert RFC 3161, OpenTimestamps",
        "   Bitcoin-anchored).",
        "",
        "The Free eVTOL Corpus is licensed CC0 1.0; no permission is required to",
        "cite, copy, or redistribute these contentions.",
        "",
        "---",
        "",
        "## Entries (chronological)",
        "",
    ]

    for e in entries_sorted:
        d = fmt_date(e.get("first_disclosure_date"))
        name = e.get("canonical_name", "?")
        eid = e.get("id", "")
        corpus = e.get("corpus", "")
        ip_status = e.get("ip_status", "")
        creator = e.get("creator", "")
        citation = e.get("disclosure_citation", "")
        notes = e.get("prior_art_notes") or ""
        sources = e.get("sources") or []
        subs = e.get("disclosed_subsystems") or []
        draft_flag = " *(draft)*" if is_draft(e) else ""

        lines.append(f"### {d} — {name}{draft_flag}")
        lines.append("")
        lines.append(f"- **id:** `{eid}`")
        lines.append(f"- **corpus:** {corpus}")
        lines.append(f"- **ip status:** {ip_status}")
        if creator:
            lines.append(f"- **creator:** {creator}")
        if citation:
            lines.append(f"- **disclosure citation:** {citation}")
        if subs:
            lines.append(
                "- **disclosed subsystems:** "
                + ", ".join(f"`{s}`" for s in subs)
            )
        lines.append("")
        lines.append("**Prior art notes:**")
        lines.append("")
        if notes.strip():
            for nl in notes.splitlines() or [notes]:
                lines.append(f"> {nl}".rstrip())
        else:
            lines.append("> *(no prior_art_notes recorded for this entry)*")
        lines.append("")
        lines.append("**Sources:**")
        lines.append("")
        if sources:
            for i, src in enumerate(sources, 1):
                lines.append(f"{i}. {src}")
        else:
            lines.append("*(no sources listed)*")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines += [
        "## License",
        "",
        "CC0 1.0 Universal (public domain dedication). No copyright restrictions on",
        "use, citation, copying, or redistribution.",
        "",
        "---",
        "",
        f"*Generated from <{REPO_URL}> at corpus revision "
        f"{('`' + git_sha + '`') if git_sha else '(unknown)'}.*",
        "",
    ]

    return "\n".join(lines)


def write_index(packets_meta, generated_iso, git_sha, hand_packets):
    lines = [
        "---",
        'title: "Invalidity Contentions"',
        "has_children: true",
        "nav_order: 4",
        "permalink: /contention_packets/",
        "layout: default",
        "---",
        "",
        "# Invalidity Contention Packets",
        "",
        f"**Generated:** {generated_iso}  ",
        f"**Auto packets:** {len(packets_meta)}  ",
        f"**Hand-written packets:** {len(hand_packets)}  ",
        f"**Corpus revision:** {('`' + git_sha + '`') if git_sha else '(unknown)'}",
        "",
        "Each packet below is an attorney-ready invalidity-contention reference. Auto",
        "packets are generated from `corpus.jsonl` (one per `disclosed_subsystems` tag",
        "with two or more entries) and regenerated whenever the corpus changes.",
        "Hand-written packets target specific patent filings or company patent estates",
        "and walk through which corpus entries anticipate which claim areas.",
        "",
        "See [README](README.md) for usage and PDF conversion instructions.",
        "",
    ]

    if hand_packets:
        lines += [
            "## Hand-written (patent / company specific)",
            "",
            "| Packet | Target |",
            "|---|---|",
        ]
        for fname, target in hand_packets:
            lines.append(f"| [`{fname}`]({fname}) | {target} |")
        lines.append("")

    lines += [
        "## Auto-generated (per subsystem tag)",
        "",
        "Only tags with two or more disclosing entries get a packet (single-entry tags",
        "are covered by their cross-cut and do not yet form a contention chain).",
        "",
        "| Packet | Entries | Commons | Draft | Earliest | Most recent |",
        "|---|---|---|---|---|---|",
    ]

    for m in packets_meta:
        lines.append(
            f"| [`{m['tag']}`]({m['tag']}.md) "
            f"| {m['count']} "
            f"| {m['n_commons']} "
            f"| {m['n_draft']} "
            f"| {fmt_date(m['earliest'])} "
            f"| {fmt_date(m['latest'])} |"
        )

    (OUT_DIR / "INDEX.md").write_text("\n".join(lines) + "\n")


def write_readme(packets_meta, generated_iso, git_sha, hand_packets):
    n = len(packets_meta)
    total_entries = sum(m["count"] for m in packets_meta)

    lines = [
        "---",
        'title: "Contentions README"',
        'parent: "Invalidity Contentions"',
        "nav_order: 0",
        "layout: default",
        "---",
        "",
        "# Invalidity Contention Packets — README",
        "",
        "## What these are",
        "",
        "Each markdown file in this directory is an **invalidity-contention packet**:",
        "a chronologically-ordered, attorney-ready prior art reference. There are two",
        "kinds:",
        "",
        f"- **Auto-generated** ({n} packets). Derived from `corpus.jsonl` by grouping",
        "  entries on their `disclosed_subsystems` tags. Each tag with two or more",
        "  disclosing entries gets a packet. Each entry's `prior_art_notes` is",
        "  reproduced verbatim alongside the citation-ready metadata.",
        f"  Total entry-references across packets: **{total_entries}**.",
        f"- **Hand-written** ({len(hand_packets)} packets). Patent- or company-specific",
        "  contention packets that walk through architectural claim areas and map them",
        "  to corpus entries that anticipate each. These survive regeneration of the",
        "  auto packets.",
        "",
        "The packets are not a substitute for legal judgment. They are a pre-built",
        "structured reference that collapses the corpus down to the chain of",
        "disclosures relevant to a single claim area, with the timestamp anchors that",
        "establish pre-existence.",
        "",
        "## How to use",
        "",
        "1. **Identify the subsystem area** of the patent claim you want to challenge",
        "   (see [INDEX.md](INDEX.md)).",
        "2. **Open the matching packet** — for example, a claim about tilt-rotor",
        "   transition is addressed by [`lift-tilt-rotor.md`](lift-tilt-rotor.md).",
        "3. **Read the entries chronologically** (earliest first). The earliest entry",
        "   that discloses the claim element is the strongest 102 anticipation",
        "   candidate.",
        "4. **For 103 obviousness contentions**, identify the smallest set of entries",
        "   that together disclose all claim elements. Each entry's `prior_art_notes`",
        "   is written as element-by-element analysis.",
        "5. **Verify the timestamp authorities** for the corpus release using the",
        "   procedure in `tools/verify_release.sh` (when available). Three independent",
        "   timestamping layers (FreeTSA RFC 3161, DigiCert RFC 3161, OpenTimestamps",
        "   Bitcoin-anchored) will attest pre-existence as of each quarterly release.",
        "",
        "## Convert a packet to PDF",
        "",
        "These packets are plain CommonMark + GitHub-flavored markdown with Jekyll",
        "front matter. To produce an attorney-ready PDF from any single packet:",
        "",
        "```sh",
        "pandoc -o packet.pdf packet.md",
        "```",
        "",
        "## Licensing posture",
        "",
        "The Free eVTOL Corpus is licensed **CC0 1.0 Universal** (public domain",
        "dedication). These packets are generated artifacts from CC0 source data and",
        "are themselves CC0. No permission is required to cite, copy, redistribute,",
        "or incorporate them into legal filings.",
        "",
        "Cited primary sources (papers, books, episodes, patents) carry their own",
        "rights under separate copyright; the packets cite them as references only.",
        "Citation of a copyrighted work as prior art is fair use in every common-law",
        "jurisdiction the authors are aware of.",
        "",
        "## Regenerating",
        "",
        "Auto packets are regenerated by running:",
        "",
        "```sh",
        "python3 tools/contention_packets.py",
        "```",
        "",
        "from the repository root. The tool only wipes auto-generated files",
        "(matching `INDEX.md` and any subsystem-tag name like `lift-tilt-rotor.md`).",
        "Hand-written packets in this directory are preserved.",
        "",
        "## Provenance",
        "",
        f"- **Generated:** {generated_iso}",
        f"- **Source:** <{REPO_URL}>",
        f"- **Corpus revision:** {('`' + git_sha + '`') if git_sha else '(unknown)'}",
        "",
    ]

    (OUT_DIR / "README.md").write_text("\n".join(lines) + "\n")


def collect_hand_packets(known_subsystem_tags):
    """Find hand-written packets — anything in OUT_DIR that is not INDEX/README and
    not named like an auto-generated subsystem tag."""
    hand = []
    for f in OUT_DIR.glob("*.md"):
        if f.name in ("INDEX.md", "README.md"):
            continue
        stem = f.stem
        if stem in known_subsystem_tags:
            continue
        # Look for a "title:" line in the front matter to use as display.
        title = stem
        try:
            for line in f.read_text().splitlines()[:10]:
                if line.startswith("title:"):
                    title = line.split(":", 1)[1].strip().strip('"').strip("'")
                    break
        except Exception:
            pass
        hand.append((f.name, title))
    return sorted(hand)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    entries = load_corpus()
    by_tag = defaultdict(list)
    for e in entries:
        for tag in e.get("disclosed_subsystems") or []:
            by_tag[tag].append(e)

    eligible = {tag: es for tag, es in by_tag.items() if len(es) >= 2}

    # Identify hand-written packets BEFORE wiping auto ones.
    hand_packets = collect_hand_packets(set(eligible.keys()))

    # Wipe only auto-generated files (subsystem-tag-named .md and INDEX/README).
    for f in OUT_DIR.glob("*.md"):
        if f.stem in eligible.keys() or f.name in ("INDEX.md", "README.md"):
            f.unlink()

    generated_iso = date.today().isoformat()
    git_sha = git_short_sha()

    sorted_tags = sorted(eligible.keys())

    packets_meta = []
    for nav_order, tag in enumerate(sorted_tags, start=1):
        es = eligible[tag]
        es_sorted = sorted(es, key=date_key)
        text = render_packet(tag, es, nav_order, generated_iso, git_sha)
        (OUT_DIR / f"{tag}.md").write_text(text)
        n_draft = sum(1 for e in es if is_draft(e))
        packets_meta.append({
            "tag": tag,
            "count": len(es),
            "n_commons": len(es) - n_draft,
            "n_draft": n_draft,
            "earliest": es_sorted[0].get("first_disclosure_date") or "",
            "latest": es_sorted[-1].get("first_disclosure_date") or "",
        })

    packets_meta.sort(key=lambda m: m["tag"])

    write_index(packets_meta, generated_iso, git_sha, hand_packets)
    write_readme(packets_meta, generated_iso, git_sha, hand_packets)

    skipped = len(by_tag) - len(eligible)
    print(f"  contention_packets: {len(eligible)} auto packets written, "
          f"{len(hand_packets)} hand packets preserved "
          f"({skipped} single-entry tags skipped)")
    print(f"  corpus revision: {git_sha or '(unavailable)'}")


if __name__ == "__main__":
    main()
