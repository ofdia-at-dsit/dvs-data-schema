> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# Supporting material

Everything in this folder is **derived** from the publication text under
`schema-1.0/`. None of it is authoritative in its own right. It exists to
help implementers, reviewers and readers work with the schema — by giving
them machine-readable exports, alternative views, diagrams and mappings to
other standards.

If a derived artefact ever conflicts with the publication text, the
publication wins and the artefact is corrected.

## What lives where

- [`diagrams/`](diagrams/README.md) — Mermaid diagrams of the top-level
  containment of GPG 45 and GPG 44, plus selected sub-structures. Text-based,
  diff-friendly.
- [`machine-readable/`](machine-readable/README.md) — CSV and YAML exports of
  the data dictionary and predefined value tables, plus dot-path and nested
  tree views of the model. Separate sub-folders for GPG 45 and GPG 44.
- [`presentation-experiments/`](presentation-experiments/README.md) —
  colour-coded renderings of selected data-model tables, inspired by the 1.3
  internal GPG 45 draft. Purely presentational.
- [`mappings/`](mappings/README.md) — cross-references between schema fields
  and other widely-used standards (OIDC, OID4IDA, W3C Verifiable Credentials).
  Empty at launch; seeded by contribution.
- [`scripts/`](scripts/README.md) — Python scripts that regenerate the
  derived artefacts from the split source files.

## Labelling rule

Every artefact in this folder must make three things clear:

1. **Derived** from the authoritative publication under `schema-1.0/`.
2. **Non-authoritative** in its own right.
3. **For implementation support only** — do not cite in place of the
   publication.

The convention in this repository is to put a short header at the top of
each artefact (or its accompanying README for binary formats) stating these
three things.

## Regeneration

When the publication text changes, the derived artefacts need regenerating.
Run the scripts under `scripts/` — each one states what it reads and writes.
Keep the scripts deterministic so that running them on unchanged input
produces byte-identical output.

## Back

- [Repository home](../README.md)
