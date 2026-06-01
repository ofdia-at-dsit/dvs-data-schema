> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# Architecture

This document records the design decisions behind the `dvs-data-schema` repository and how it relates to the GOV.UK publication. It is a companion to [`VERSIONS.md`](VERSIONS.md), which explains how multiple versions sit side by side, and [`CONTRIBUTING.md`](CONTRIBUTING.md), which explains how to propose changes.

## What this repository is

A workspace copy of the UK DVS trust framework data schema, hosted in version control so that:

- the text is easier to navigate than a single long page on GOV.UK,
- improvements to formatting, structure and presentation can be tested openly,
- derived and machine-readable artefacts (diagrams, data dictionary exports, dot-path views) sit alongside the source text,
- changes to the repository and changes to the publication text can be tracked distinctly in the [`CHANGELOG.md`](CHANGELOG.md).

It is **not** the authoritative publication. The authoritative version lives on GOV.UK.

## What this repository deliberately does not do

- It does not override or modify GOV.UK.
- It does not change the underlying data model, definitions, field names, hierarchy, cardinality, or the semantic meaning of any schema element. Formatting, structure, layout, heading wording and presentation can be improved for clarity; substance cannot.
- It does not enforce immutability of the publication text after launch. The repository is a living workspace.
- It does not store personal data or production secrets.

## Relationship to the GOV.UK publication

The repository reflects the GOV.UK publication of the DVS trust framework data schema. Where the published GOV.UK source and any earlier internal draft differ, **the published GOV.UK source takes priority** for the workspace text. Earlier drafts are useful only as inspiration for presentation improvements (clearer tables, multi-view layouts, derived diagrams).

Any change in this repository that affects the substance of the publication must:

- be recorded under `[publication]` in the [`CHANGELOG.md`](CHANGELOG.md),
- cite the upstream GOV.UK publication and the reason for the change (typo correction, editorial fix, formal revision),
- and round-trip cleanly back to the GOV.UK publication pipeline if requested.

Changes that only affect the repository, its tooling, navigation, supporting material or CI are recorded under `[repo]`.

## Content layout

```text
dvs-data-schema/
├─ README.md, ARCHITECTURE.md, CHANGELOG.md, CONTRIBUTING.md,
│  KNOWN-ISSUES.md, LICENCE.md, SECURITY.md, VERSIONS.md
├─ .github/
│  ├─ CODEOWNERS, pull_request_template.md
│  ├─ ISSUE_TEMPLATE/    — seeded templates for each feedback category
│  └─ workflows/         — caution-block check, markdown lint, link check, site build
├─ schema-1.0/           — version 1.0 publication text
│  ├─ README.md
│  ├─ gpg-45/            — identity checking data schema (split by section)
│  └─ gpg-44/            — authentication data schema (split by section)
├─ supporting-material/  — derived, non-authoritative material
│  ├─ diagrams/, machine-readable/, mappings/, scripts/
├─ media/                — shared image assets
└─ docs-site/            — Eleventy site rendering the repo with GOV.UK styling
```

## Why split each guide into one file per section

The GOV.UK publication renders each data schema guide as a single long page. That is hard to version and hard to review. This repository splits each guide into six sections — introduction, data taxonomy, data model, data dictionary, predefined lists, predefined values — so that pull requests can focus on a single section at a time, and each section can carry its own navigation footer.

Splitting does not change the substance of the text. The pre-split and post-split content must remain substantively identical.

## Caution block

Every workspace Markdown file starts with the same `> [!CAUTION]` block reminding the reader that this repository is not authoritative. This is enforced by a CI workflow at [`.github/workflows/caution-block.yml`](.github/workflows/caution-block.yml) and the exact wording is pinned there.

Files excluded from the check:

- anything under `.github/` (templates, CI config, CODEOWNERS) — those are tooling, not workspace content,
- `docs-site/README.md` and anything under `docs-site/node_modules/` — site tooling, not workspace content.

## Supporting material

`supporting-material/` holds artefacts **derived from** the publication text — machine-readable exports, dot-path views, Mermaid diagrams, mappings and scripts. Everything in this folder is clearly labelled as:

- **derived** from the authoritative publication,
- **non-authoritative** in its own right, and
- for **implementation support only**.

If the publication text and a derived artefact ever conflict, the publication wins and the derived artefact is corrected.

## Rendered site layer

A GOV.UK-styled rendered view of the workspace lives under [`docs-site/`](docs-site/README.md). It is built with [Eleventy](https://www.11ty.dev/) and the official [govuk-frontend](https://github.com/alphagov/govuk-frontend) package, using the same pattern as the trust framework web repo.

The rendered site is a **view**, not an authority. Three constraints follow:

- The Markdown source is not duplicated. Eleventy's input directory is the repository root; the site adds layouts, includes and data alongside it in `docs-site/` without touching any existing content.
- Cross-file `.md` links in publication content are rewritten to pretty URLs at output time, so source files stay `.md`-linked (which is what GitHub's native Markdown rendering expects) while the rendered site links resolve without `.md` suffixes.
- The site understands GOV.UK publishing "GovSpeak" block markup — `$CTA`, `$E`, `%…%` warnings, `^…^` help notices — via a `govspeak.js` markdown-it plugin.

If the site tooling were removed tomorrow, the repository would still be a coherent workspace copy.

## Versioning

Schema versions live in parallel folders (`schema-1.0/`, and later `schema-1.1/`, `schema-2.0/`, etc.). See [`VERSIONS.md`](VERSIONS.md) for the full pattern. The Git tag for a release is separate from the publication version and follows the repository's own SemVer.

## Back

- [Repository home](README.md)
