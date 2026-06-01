> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# Machine-readable exports

CSV, YAML, dot-path and nested-tree views of the schema. Organised by guide:

- [`gpg-45/`](gpg-45/README.md) — GPG 45 exports.
- [`gpg-44/`](gpg-44/README.md) — GPG 44 exports.

Every file here is **derived, non-authoritative and for implementation
support only**. The authoritative definition is the publication text under
`schema-1.0/`.

## Formats

- **`data-dictionary.csv`** — flat CSV of element name, description and any
  notes. Useful for pulling into spreadsheets and data-cataloguing tools.
- **`data-dictionary.yaml`** — same content as the CSV but structured so
  that nested relationships and data types can be expressed more clearly.
- **`predefined-values.csv` / `.yaml`** — the enumerated values and their
  definitions.
- **`predefined-lists.csv` / `.yaml`** — which elements are restricted to
  which sets of values, with notes.
- **`dot-path-view.md`** — every element and sub-element rendered as a
  dot-separated path (for example `verified_claims.verification.evidence.
  document.document_details.type`). Useful when referencing a specific
  field in an issue, ticket or PR.
- **`nested-tree-view.md`** — indented tree view of the same content.

## Generation

These files are produced by scripts under `../scripts/`. Re-run the scripts
after any change to `schema-1.0/` so the exports stay in sync.

## Back

- [Supporting material](../README.md)
- [Repository home](../../README.md)
