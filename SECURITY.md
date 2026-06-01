> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# Security policy

This repository is a workspace copy of a published government document and its supporting material. It hosts no production services, no user data and no secrets. Security concerns are still welcome — the scope is narrow.

## What to report here

- Vulnerabilities in the repository's CI workflows.
- Vulnerabilities in scripts under `supporting-material/scripts/`.
- Vulnerabilities in the docs-site build pipeline or its dependencies.
- Supply-chain concerns with any dependency this repository pulls in.

## What to report elsewhere

- Vulnerabilities in a specific certified digital verification service should be reported to that service provider directly, and where appropriate to their Conformity Assessment Body (CAB) and to OfDIA.
- Vulnerabilities in GOV.UK, the register of digital identity and attribute services, or other government services are reported through those services' own disclosure channels, not via this repository.

## How to report

Please **do not raise a public GitHub issue** for security matters.

Contact the repository maintainers listed in [`.github/CODEOWNERS`](.github/CODEOWNERS) via a private channel, or email the Office for Digital Identities and Attributes through the contact route listed on their [GOV.UK page](https://www.gov.uk/government/organisations/office-for-digital-identities-and-attributes).

We will acknowledge receipt, work with you on a reasonable disclosure timeline, and credit the reporter in any resulting advisory unless you prefer otherwise.

## Scope

In scope:

- This repository and its CI workflows.
- The docs-site Eleventy build.

Out of scope:

- Third-party services linked to from the repository.
- The authoritative GOV.UK publication (report via GOV.UK).
- Any downstream fork or mirror of this repository.

## Back

- [Repository home](README.md)
