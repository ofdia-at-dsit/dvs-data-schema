> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# GPG 44 — authentication data schema (version 1.0)

This folder contains the data taxonomy, data model and data dictionary for the ['How to use authenticators to protect an online service'](https://www.gov.uk/government/publications/how-to-use-authenticators-to-protect-an-online-service-1-0) guidance — Good Practice Guide (GPG) 44.

The authoritative publication lives on GOV.UK:

- [Data taxonomy, data model and data dictionary for GPG 44](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-data-schema-1-0/data-taxonomy-data-model-and-data-dictionary-for-gpg-44)

## Sections

- [1. Introduction](01-introduction.md) — what the GPG 44 schema is and what it covers.
- [2. Data taxonomy](02-data-taxonomy.md) — the hierarchy and classification of GPG 44 data. Covers authenticator type, authenticator quality and authenticator protection.
- [3. Data model](03-data-model.md) — the shape of the data. Defines the `authentication` object with its `authenticator_protection`, `multifactor` and `monitoring` fields and an array of `authenticator` objects (each with a `type` and `quality`).
- [4. Data dictionary](04-data-dictionary.md) — the data elements table (Table D1) with each element's description.
- [5. Predefined values](05-predefined-values.md) — the definitions of the allowed authenticator values (Table V1), including `pin`, `password`, `kbv`, `physical_token`, `digital_token`, `biometric`.
- [6. Predefined lists](06-predefined-lists.md) — which schema elements are restricted to which sets of predefined values (Table L1).

## Reading order

GPG 44 is considerably smaller than GPG 45. The six sections can be read end-to-end in a few minutes. If you are scanning for something specific:

- **shape of the authentication data** → section 3.
- **meaning of a specific field** → section 4.
- **allowed values for `authenticator_type` or `authenticator_quality`** → sections 5 and 6.

## Supporting material for GPG 44

Derived artefacts specific to GPG 44 — dot-path view, nested tree view, machine-readable exports, Mermaid diagram — live under:

- [`supporting-material/machine-readable/gpg-44/`](../../supporting-material/machine-readable/gpg-44/)
- [`supporting-material/diagrams/`](../../supporting-material/diagrams/)

All supporting material is clearly labelled as derived and non-authoritative.

## Back

- [Schema 1.0 landing page](../README.md)
- [Repository home](../../README.md)
