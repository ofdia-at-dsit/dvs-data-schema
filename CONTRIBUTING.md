> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# Contributing

Thank you for considering a contribution to the DVS trust framework data schema workspace.

This repository is a workspace copy of the [UK digital verification services trust framework data schema](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-data-schema-1-0). It is not the authoritative publication. Contributions here improve how the schema is navigated, presented and reused — they do not on their own change government policy.

## What kinds of contribution we welcome

- **Typo and formatting corrections** to the workspace text where the workspace diverges from the GOV.UK publication by mistake.
- **Presentation improvements** — clearer tables, navigation, heading wording, cross-references.
- **Accessibility improvements** — alt text, table structure, heading levels.
- **Feedback on the data schema itself** — clarifications, ambiguities, suggested improvements. These do not change the publication in this repository, but we collect them so OfDIA and the wider community can consider them for future revisions.
- **New supporting material** — diagrams, machine-readable exports, mappings to OIDC, OID4IDA or Verifiable Credentials. These must be clearly labelled as derived and non-authoritative.
- **Repository tooling** — CI workflows, templates, scripts, site layouts.

## What we cannot change here

This repository **cannot** change:

- the underlying data model,
- data definitions,
- field names,
- hierarchy,
- cardinality, or
- the semantic meaning of any schema element.

Examples of schema content, objects, properties and relationships must remain substantively identical to the GOV.UK source.

Substantive changes to the data schema are made by OfDIA and published on GOV.UK. Where a contributor thinks such a change is warranted, they are welcome to open a **schema feedback** issue here so the suggestion can be considered upstream.

## How to contribute

### Small changes

For typos, broken links, formatting tidy-ups and clear factual mistakes:

1. Fork the repository.
2. Make the change on a branch.
3. Open a pull request using the template. Fill in the "nature of change" section so reviewers can tell at a glance whether this is a `[repo]` or `[publication]` change.
4. The PR template will remind you to:
   - preserve the caution block at the top of every workspace Markdown file,
   - update [`CHANGELOG.md`](CHANGELOG.md) under the right heading,
   - add or update a navigation footer if you add a new page.

### Larger changes

For new supporting material, new presentation views, or CI changes:

1. Open an issue first using the most relevant template under [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/). This helps other contributors and maintainers weigh in before you invest time.
2. After discussion, raise a pull request as above.

### Feedback on the data schema itself

Use the **schema feedback** issue template. These issues are not acted on in this repository's text — they are collected to inform future GOV.UK revisions.

## Style notes

- Use British English spelling for prose (for example "organisation", "licence" as a noun).
- Keep the full name "UK digital verification services trust framework" for first references; "DVS trust framework" or just "the trust framework" is fine thereafter.
- Prefer Markdown tables over HTML tables; GitHub renders them reliably and they are easier to diff.
- Keep one sentence per line in long paragraphs where it makes diffs clearer, but do not enforce this aggressively.
- Do not remove or weaken the caution block.

## Where to ask questions

If a contribution does not obviously fit any of the issue templates, open a generic issue and a maintainer will route it.

## Reporting security concerns

Security concerns about this repository or its CI workflows should follow [`SECURITY.md`](SECURITY.md), not the public issue tracker.

## Back

- [Repository home](README.md)
