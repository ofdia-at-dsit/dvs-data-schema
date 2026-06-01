> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# UK digital verification services trust framework data schema

This repository is a workspace copy of the [UK digital verification services (DVS) trust framework data schema](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-data-schema-1-0), split into one Markdown file per main section under versioned folders. It is designed to make the schema easier to navigate, review, version and reuse.

The authoritative version of the data schema is the publication on GOV.UK. The text hosted here is a workspace mirror.

## What the data schema is

The DVS trust framework data schema describes how DVS providers and relying parties can organise and exchange information in a consistent way to enable interoperability. It covers two good practice guides:

- **GPG 45** — the identity checking process described in [How to prove and verify someone's identity](https://www.gov.uk/government/publications/how-to-check-someones-identity-1-0).
- **GPG 44** — the authentication process described in [How to use authenticators to protect an online service](https://www.gov.uk/government/publications/how-to-use-authenticators-to-protect-an-online-service-1-0).

For each guide, the schema provides:

- a **data taxonomy** (a description of the hierarchy and classification of the data),
- a **data model** (a description of the data element names, sub-elements and data types), and
- a **data dictionary** (names, definitions and attributes for the data elements, plus predefined lists and values).

Use of the data schema is **optional** for certified services. It is provided to help services demonstrate interoperability with others in the UK and internationally.

## Which version this repository hosts

This repository currently hosts **version 1.0** of the data schema, published to coincide with the 1.0 pre-release of the DVS trust framework.

See [`VERSIONS.md`](VERSIONS.md) for how future versions will sit side by side in this repository.

## How to navigate

- [Schema 1.0 landing page](schema-1.0/README.md)
  - [GPG 45 — identity checking data schema](schema-1.0/gpg-45/README.md)
  - [GPG 44 — authentication data schema](schema-1.0/gpg-44/README.md)
- [Supporting material](supporting-material/README.md) — derived artefacts, diagrams, machine-readable exports and scripts. Clearly marked as derived and non-authoritative.
- [Media](media/README.md) — shared images referenced from workspace pages.

## Repository design and versioning

- [`ARCHITECTURE.md`](ARCHITECTURE.md) — design decisions behind the repository layout, and how it relates to the GOV.UK publication.
- [`VERSIONS.md`](VERSIONS.md) — how multiple publication versions sit side by side in this repository over time.
- [`CHANGELOG.md`](CHANGELOG.md) — notable changes to the repository and to the publication text, tracked separately.
- [`KNOWN-ISSUES.md`](KNOWN-ISSUES.md) — items identified by maintainers that are not yet fixed, seeded before public push.
- [`docs-site/`](docs-site/README.md) — Eleventy-based GOV.UK-styled rendered view of the repository, deployed to GitHub Pages. Not authoritative; the authoritative publication stays on GOV.UK.

## Contributing, licence, security

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to suggest edits, raise issues and propose new supporting material.
- [`LICENCE.md`](LICENCE.md) — Open Government Licence v3.0 for documentation, MIT License for code, aligned with the GDS Way licensing manual.
- [`SECURITY.md`](SECURITY.md) — how to report security concerns about the repository or its CI workflows.

## Related repositories

This repository is part of a family of workspace copies for the UK DVS trust framework:

- Trust framework text: [mf-henri-v2/dvs-wip-4](https://github.com/mf-henri-v2/dvs-wip-4)
- Trust framework rendered site: [mf-henri-v2/dvs-wip-5-web-2](https://github.com/mf-henri-v2/dvs-wip-5-web-2)
- Data schema (this repository)

## Note on the authoritative publication

The authoritative version of the UK DVS trust framework data schema is the publication on GOV.UK. This repository is a workspace copy and is not the official statement of government policy.
