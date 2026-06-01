> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# GPG 45 — identity checking data schema (version 1.0)

This folder contains the data taxonomy, data model and data dictionary for the ['How to prove and verify someone's identity'](https://www.gov.uk/government/publications/how-to-check-someones-identity-1-0) guidance — Good Practice Guide (GPG) 45.

The authoritative publication lives on GOV.UK:

- [Data taxonomy, data model and data dictionary for GPG 45](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-data-schema-1-0/data-taxonomy-data-model-and-data-dictionary-for-gpg-45)

## Sections

- [1. Introduction](01-introduction.md) — what the GPG 45 schema is and what it covers.
- [2. Data taxonomy](02-data-taxonomy.md) — the hierarchy and classification of GPG 45 data. Covers identity claims, assurance processes and identity checking processes.
- [3. Data model](03-data-model.md) — the shape of the data. Defines `verified_claims`, `claims`, `verification`, `evidence`, `document`, `electronic_record`, `vouch`, the check and assurance objects, and the supporting sub-elements.
- [4. Data dictionary](04-data-dictionary.md) — the exact definitions and formats for shared data types (`country_code`, `date`, `encoding`, `language`, `nationality`, `timestamp`).
- [5. Predefined values](05-predefined-values.md) — the definitions of the enumerated values used across the schema (for example `passport`, `birth_certificate`, `bvp`, `kbv`, `score_3`).
- [6. Predefined lists](06-predefined-lists.md) — which schema elements are restricted to which sets of predefined values.

## Reading order

If you are new to the schema, read in order 1 → 6. If you are looking for a specific element, the data model (section 3) is the most useful jumping-off point; each element links forward to the dictionary, values and lists where relevant.

## Supporting material for GPG 45

Derived artefacts specific to GPG 45 — dot-path views, nested tree views, machine-readable exports, Mermaid diagrams — live under:

- [`supporting-material/machine-readable/gpg-45/`](../../supporting-material/machine-readable/gpg-45/)
- [`supporting-material/diagrams/`](../../supporting-material/diagrams/)

All supporting material is clearly labelled as derived and non-authoritative.

## Back

- [Schema 1.0 landing page](../README.md)
- [Repository home](../../README.md)
