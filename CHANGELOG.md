> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# Changelog

This changelog records changes to the **repository** (structure, tooling, navigation, supporting material, workflows) and changes to the **publication text** it hosts. The two are tracked distinctly.

The format loosely follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the repository follows [Semantic Versioning](https://semver.org/) for its own release tags, independently of the data schema publication version.

## Legend

- **[publication]** — changes to the text of a published data schema version. These should always cite the upstream GOV.UK publication and the reason (typo correction, editorial fix, formal revision).
- **[repo]** — changes to repository structure, navigation, READMEs, CI, templates, supporting material and other non-publication assets.

---

## [Unreleased]

### Changed

- **[publication]** Editor's note added to the `### Attachment` section of
  [`schema-1.0/gpg-45/03-data-model.md`](schema-1.0/gpg-45/03-data-model.md)
  pointing readers at the 13 April 2026 GOV.UK correction that swapped
  `content_type` for `content_format`. The note is explicitly marked as
  a workspace navigation aid, not part of the published schema text.
  Resolves KI-3.
- **[publication]** `$E ... $E` fenced-block markers inside the workspace
  schema text have been converted to HTML `<pre class="schema-example">`
  blocks. 30 blocks were converted (22 in GPG 45 data model, 6 in GPG 45
  data dictionary, 2 in GPG 44 data model). Inside each block, `&nbsp;`
  entities became regular spaces, Markdown inline links became HTML `<a>`
  elements so the links stay clickable, and blank-line export artefacts
  between each field were collapsed. No schema element name, type,
  cardinality or description changed. Applied deterministically by
  [`supporting-material/scripts/convert_schema_examples.py`](supporting-material/scripts/convert_schema_examples.py);
  the script is idempotent. Resolves KI-1.
- **[publication]** Same-file fragment links inside
  `schema-1.0/gpg-45/03-data-model.md` that pointed at anchors now living
  in `04-data-dictionary.md` or `06-predefined-lists.md` have been
  rewritten to their cross-file form (26 rewrites). Same-file anchors
  were left alone. Applied deterministically by
  [`supporting-material/scripts/apply_cross_file_links.py`](supporting-material/scripts/apply_cross_file_links.py);
  the script is idempotent. Resolves KI-4.

### Added

- **[repo]** Initial repository scaffold for the DVS trust framework data schema. Hosts version 1.0 of the schema, split into one Markdown file per section under `schema-1.0/gpg-45/` and `schema-1.0/gpg-44/`.
- **[repo]** Caution block on every workspace Markdown file reminding readers this is a workspace, not the official publication. Enforced by CI.
- **[repo]** Top-level `README.md`, per-version `README.md`, per-guide `README.md` (GPG 45 and GPG 44) and folder READMEs for `media/` and `supporting-material/`.
- **[repo]** Licence statement: OGL v3.0 for documentation, MIT License for code. Aligned with the [GDS Way licensing manual](https://gds-way.digital.cabinet-office.gov.uk/manuals/licensing.html).
- **[repo]** `CONTRIBUTING.md`, `SECURITY.md`, `CODEOWNERS`, `.editorconfig`, `.gitattributes`, `.gitignore`, `.eleventyignore`.
- **[repo]** Issue templates and pull-request template under `.github/`.
- **[repo]** CI workflows: caution-block integrity check, Markdown lint, weekly external-link check, docs-site build and deploy to GitHub Pages.
- **[repo]** Previous / guide / version / home / next navigation footers on each official section file.
- **[repo]** `supporting-material/` with four sub-folders: `diagrams/` for Mermaid diagrams, `machine-readable/` for CSV/YAML exports of the data dictionary and dot-path views, `mappings/` for future OIDC / OID4IDA / Verifiable Credentials cross-references, and `scripts/` for regeneration tooling. Everything in this folder is clearly labelled derived and non-authoritative.
- **[repo]** `docs-site/` — Eleventy-based GOV.UK-styled rendered view of the repository, modelled on the trust framework web repo pattern. Publication source Markdown is unchanged — the site uses the repository root as its input directory and adds layouts, includes, a GOV.UK-publishing `govspeak.js` markdown-it plugin, a `.eleventyignore` at the repo root, and a GitHub Actions workflow that builds and deploys to GitHub Pages. The build reads a `BASEURL` environment variable (populated automatically by `actions/configure-pages` in CI) and rewrites `govuk-frontend`'s asset URLs so the site works on both root-domain and repository-subpath deploys.
- **[repo]** `supporting-material/presentation-experiments/` — colour-coded renderings of selected GPG 45 and GPG 44 data-model tables, inspired by the 1.3 internal GPG 45 draft whose colour-coded cells were not achievable on GOV.UK. The colours indicate the field's type category (primitive, reference, array, fixed literal, predefined-list value). Clearly labelled as derived and non-authoritative; the authoritative text under `schema-1.0/` is unchanged. Resolves KI-6.
- **[repo]** `docs-site/.eleventy.js` — markdown-it `linkify` disabled. With it enabled, the string "GOV.UK" (which appears in every caution block) was being auto-linked to `http://GOV.UK` across all 38 rendered pages. The source uses explicit `[text](url)` syntax everywhere it wants a link, so turning off linkify is safe and fixes all 38 pages at once.
- **[repo]** `supporting-material/scripts/apply_cross_file_links.py` and `supporting-material/scripts/convert_schema_examples.py` — deterministic, idempotent scripts that performed the KI-4 and KI-1 cleanups and can be re-run if future publication changes reintroduce the patterns.
- **[repo]** `supporting-material/mappings/` seeded with three files that
  document the DVS schema's relationship to adjacent standards, addressing
  the KI-7 and KI-8 venues for the OIDF alignment conversation without
  pre-empting the policy question. Files added:
  [`oid4ida-mapping.yaml`](supporting-material/mappings/oid4ida-mapping.yaml)
  (64 entries mapping DVS to the OpenID Identity Assurance Schema
  Definition 1.0 — exact/renamed/restructured/dvs-only/target-only
  categories, with the biggest structural divergence around
  `check_details` vs `validation_method` / `verification_method` called
  out explicitly);
  [`oidc-core-mapping.yaml`](supporting-material/mappings/oidc-core-mapping.yaml)
  (14 entries covering the basic identity-claim fields under
  `verified_claims.claims.*`); and
  [`w3c-vc-notes.md`](supporting-material/mappings/w3c-vc-notes.md)
  (discussion-format note on embedding `verified_claims` inside a
  Verifiable Credential — explicitly not a field-by-field map). All three
  files are clearly labelled derived and non-authoritative.
- **[repo]** `docs-site/package-lock.json` committed after the first successful `npm install`, so CI can use `npm ci` for reproducible installs. First end-to-end `npm install && npm run build` verified: 38 rendered pages, 23 passthrough assets, build time 1.7s, `<pre class="schema-example">` blocks and cross-file pretty-URL link rewrites all verified in the rendered HTML. Resolves KI-9.

### Known issues seeded

- **[repo]** Nine items seeded in [`KNOWN-ISSUES.md`](KNOWN-ISSUES.md). Five have been resolved in this changelog window (KI-1, KI-3, KI-4, KI-6, KI-9). Four remain open: KI-2 and KI-7/KI-8 are reminder-only items not actionable in this repository, and KI-5 (real CODEOWNERS handles) is owned by a maintainer with access to the GitHub organisation.

---

## Publication history

### 2026-04-13 (upstream GOV.UK correction)

- **[publication]** The GOV.UK landing page for the data schema was updated to correct a typo where `content_format` had incorrectly been shown as `content_type` within the attachment element definition, and to fix links and formatting issues. This repository reflects the corrected GOV.UK text.

### Version 1.0 (initial publication)

- **[publication]** Version 1.0 of the data schema was published to coincide with the 1.0 pre-release of the UK DVS trust framework. It covers both GPG 45 and GPG 44.

## Back

- [Repository home](README.md)
