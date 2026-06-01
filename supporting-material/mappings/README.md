> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# Mappings

Cross-references between DVS data schema fields and other widely-used
standards — OpenID Connect, the OpenID Identity Assurance family (OID4IDA),
W3C Verifiable Credentials, and IANA registries.

Every mapping in this folder is **derived, non-authoritative and for
implementation support only**. Where a mapping is a judgement call, the
mapping file says so clearly and links to the relevant source.

## Seed mappings

- [`oid4ida-mapping.yaml`](oid4ida-mapping.yaml) — maps DVS schema fields
  to the OpenID Identity Assurance Schema Definition 1.0 (the closest
  relative of the DVS `verified_claims` structure). Covers the most
  commonly-needed fields and flags DVS-only and OID4IDA-only elements
  explicitly.
- [`oidc-core-mapping.yaml`](oidc-core-mapping.yaml) — maps the DVS
  identity-claim fields under `verified_claims.claims.*` to the
  corresponding standard claims in OpenID Connect Core and the IANA JWT
  Claims Registry. Much shorter than the OID4IDA mapping.
- [`w3c-vc-notes.md`](w3c-vc-notes.md) — discussion-format note on how a
  DVS `verified_claims` object can be embedded inside a W3C Verifiable
  Credential. Not a field-by-field mapping; a field-by-field mapping of VC
  to DVS is a larger piece of work and would live in a separate YAML file.

## File format for YAML mappings

Each mapping YAML file has two top-level sections:

- `standard` — name, URL, version and date of the target standard the
  mapping references.
- `mappings` — a flat list of entries, each naming a DVS dot-path, the
  target dot-path, a `kind` category, and free-text notes.

The `kind` categories are:

| Kind           | Meaning |
|----------------|---------|
| `exact`        | Same name, same structure, same semantics. |
| `renamed`      | Different name, equivalent semantics. |
| `restructured` | Equivalent semantics, different shape (different nesting, split/merged fields). |
| `dvs_only`     | No counterpart in the target standard. |
| `target_only`  | Target has something DVS does not. Included for completeness. |

A flat list was chosen over a nested structure because it diffs cleanly in
pull requests and is easy for tooling to consume.

## What does not belong here

- Re-hosted copies of the target standards themselves. Link to the source.
- Proposals to change the DVS schema. Use the `schema-feedback` issue
  template instead. Mapping entries can note that a discrepancy exists but
  cannot, on their own, change the published schema.

## Background context

Internal notes record feedback from the OpenID Foundation on the 1.0
schema, including suggestions to align more closely with OID4IDA structure
and with IANA / OIDC-style claim names, plus counter-arguments preferring
current names for flexibility. See `KNOWN-ISSUES.md` items KI-7 and KI-8
for detail. The seed mappings here document the current alignment without
pre-empting the policy question of whether or how to align further.

## Regeneration

The mappings are **hand-authored**, not generated. When either the DVS
schema or a target standard changes, the mapping files need to be updated
by a human contributor. Automation belongs in a test workflow that checks
every DVS dot-path in a mapping file still exists in the published schema
— not in a script that rewrites the mappings.

## Back

- [Supporting material](../README.md)
- [Repository home](../../README.md)
