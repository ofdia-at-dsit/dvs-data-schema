> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# Versions

This repository can host multiple published versions of the UK DVS trust framework data schema side by side. This page records the pattern and lists the versions currently in the repository.

## The pattern

Each published version of the data schema lives in its own top-level folder:

```text
dvs-data-schema/
├─ schema-1.0/       — version 1.0, covers GPG 45 and GPG 44
├─ schema-1.1/       — (future) minor revision
└─ schema-2.0/       — (future) major revision
```

Each version folder contains a parallel structure:

```text
schema-<version>/
├─ README.md        — version landing page
├─ gpg-45/          — identity checking data schema
│  ├─ README.md
│  ├─ 01-introduction.md
│  ├─ 02-data-taxonomy.md
│  ├─ 03-data-model.md
│  ├─ 04-data-dictionary.md
│  ├─ 05-predefined-lists.md
│  └─ 06-predefined-values.md
└─ gpg-44/          — authentication data schema
   ├─ README.md
   ├─ 01-introduction.md
   ├─ 02-data-taxonomy.md
   ├─ 03-data-model.md
   ├─ 04-data-dictionary.md
   ├─ 05-predefined-lists.md
   └─ 06-predefined-values.md
```

Versions are **never retro-edited**. If a published version receives a typo correction on GOV.UK, the workspace copy of that version is updated to match, and the change is recorded in [`CHANGELOG.md`](CHANGELOG.md) under a dated `[publication]` entry. The folder structure and file names for a given version do not change after publication.

## Supporting material

Supporting material (diagrams, machine-readable exports, mappings, scripts) lives in a single `supporting-material/` folder at the repository root, not inside each version folder. Each artefact in `supporting-material/` declares which version(s) it applies to in its own README or front-matter. This avoids duplicating artefacts when they apply equally to more than one version.

## Git tags

The Git tag for a repository release is independent of the publication version. Repository tags follow [SemVer](https://semver.org/) and look like `v0.1.0`, `v0.2.0`, `v1.0.0`. The publication version a given tag covers is recorded in the release notes.

## Versions currently in the repository

| Folder | Schema version | GOV.UK publication |
|---|---|---|
| [`schema-1.0/`](schema-1.0/README.md) | **1.0** | [data schema 1.0 on GOV.UK](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-data-schema-1-0) |

## Adding a new version

When OfDIA publishes a new data schema version:

1. Copy the existing `schema-<latest>/` folder to `schema-<new>/`.
2. Replace the contents of `schema-<new>/` with the new published text, split by section as before.
3. Update `schema-<new>/README.md` to reference the new GOV.UK publication URL.
4. Update this page's "Versions currently in the repository" table.
5. Update the top-level [`README.md`](README.md) if the "Which version this repository hosts" section needs to change.
6. Record the addition in [`CHANGELOG.md`](CHANGELOG.md) under `[repo]` (for the repository-structure change) and `[publication]` (for the new publication being hosted).
7. Do not delete earlier version folders. The repository keeps a full history of workspace copies.

## Back

- [Repository home](README.md)
