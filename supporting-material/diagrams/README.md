> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# Diagrams

Text-based Mermaid diagrams of the schema. Each `.mmd` file is valid Mermaid
syntax that renders in GitHub previews, the docs-site, and most Markdown
tools.

Every diagram is **derived, non-authoritative and for implementation support
only**. The authoritative definition is the publication text.

## Available diagrams

### GPG 45
- [`gpg-45-top-level-containment.mmd`](gpg-45-top-level-containment.mmd) —
  `verified_claims` containing `claims` and `verification`, and
  `verification` containing evidence and the assurance process.
- [`gpg-45-evidence-structure.mmd`](gpg-45-evidence-structure.mmd) —
  the three evidence types (`document`, `electronic_record`, `vouch`) and
  their shared `attachments` and `check_details` sub-elements.

### GPG 44
- [`gpg-44-authentication-structure.mmd`](gpg-44-authentication-structure.mmd)
  — `authentication` and its array of `authenticator` objects.

## Regenerating

Unlike the CSV and YAML exports, these diagrams are hand-drawn rather than
machine-derived. If the schema containment relationships change, edit the
`.mmd` file directly and update this README.

## Back

- [Supporting material](../README.md)
- [Repository home](../../README.md)
