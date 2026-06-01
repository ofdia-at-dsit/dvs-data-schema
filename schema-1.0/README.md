> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# UK DVS trust framework data schema — version 1.0

This folder contains the **1.0 pre-release** publication of the UK digital verification services (DVS) trust framework data schema, split by main section and by guide.

The files in this folder mirror the official publication text as published by the Office for Digital Identities and Attributes (OfDIA). They are maintained here to make the schema easier to navigate, review, version and reuse. The authoritative version is the publication on GOV.UK:

- [Data schema landing page on GOV.UK](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-data-schema-1-0)

## About this version

- **Published:** to coincide with the 1.0 pre-release of the UK DVS trust framework.
- **Scope:** covers both GPG 45 (identity checking) and GPG 44 (authentication).
- **Optional use:** the data schema is optional for certified services. It exists to help services demonstrate interoperability.
- **Upstream correction (13 April 2026):** a typo was corrected on GOV.UK where `content_format` had incorrectly been shown as `content_type` within the attachment element. The text hosted here matches the corrected GOV.UK version.

## GPG 45 — identity checking data schema

The schema for the identity checking process described in [How to prove and verify someone's identity](https://www.gov.uk/government/publications/how-to-check-someones-identity-1-0).

- [GPG 45 landing page](gpg-45/README.md)
  - [1. Introduction](gpg-45/01-introduction.md)
  - [2. Data taxonomy](gpg-45/02-data-taxonomy.md)
  - [3. Data model](gpg-45/03-data-model.md)
  - [4. Data dictionary](gpg-45/04-data-dictionary.md)
  - [5. Predefined values](gpg-45/05-predefined-values.md)
  - [6. Predefined lists](gpg-45/06-predefined-lists.md)

## GPG 44 — authentication data schema

The schema for the authentication process described in [How to use authenticators to protect an online service](https://www.gov.uk/government/publications/how-to-use-authenticators-to-protect-an-online-service-1-0).

- [GPG 44 landing page](gpg-44/README.md)
  - [1. Introduction](gpg-44/01-introduction.md)
  - [2. Data taxonomy](gpg-44/02-data-taxonomy.md)
  - [3. Data model](gpg-44/03-data-model.md)
  - [4. Data dictionary](gpg-44/04-data-dictionary.md)
  - [5. Predefined values](gpg-44/05-predefined-values.md)
  - [6. Predefined lists](gpg-44/06-predefined-lists.md)

## How the guides differ

GPG 45 and GPG 44 share the same overall structure (taxonomy, model, dictionary, predefined values, predefined lists) but the schemas themselves are very different in size and shape:

- **GPG 45** is considerably larger. It describes identity claims, evidence (documents, electronic records and vouches), the checks performed on that evidence, and how the whole thing maps onto a GPG 45 level of confidence. Many sub-elements reference each other, so the data model reads as a tree of nested objects.
- **GPG 44** is compact. Authentication is modelled as a top-level `authentication` object with a small number of fields and an array of `authenticator` objects, each with a type and a quality.

Both guides follow the same principle: a **taxonomy** explains the ideas, a **data model** shows the shape of the data, and a **data dictionary** gives the exact names, formats and allowed values.

## Supporting material

Diagrams, machine-readable exports and implementation-oriented views live in the [supporting-material](../supporting-material/README.md) folder at the top of the repository. Anything in that folder is clearly labelled as derived and non-authoritative.

## Back

- [Repository home](../README.md)
