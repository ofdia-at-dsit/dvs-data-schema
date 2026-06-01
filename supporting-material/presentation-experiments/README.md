> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# Presentation experiments

Alternative, visual-first renderings of the data schema. Inspired by the 1.3
internal GPG 45 draft, whose data-model tables used colour-coded cells to
help readers scan the model at a glance.

Draft comments on that 1.3 document noted that colour coding was not
expected to be achievable on GOV.UK. This repository's rendered site and
GitHub Markdown view can both render inline styled HTML tables, so the
experiment lives here — as a clearly-labelled alternative view, not a
replacement for the authoritative text.

Everything in this folder is **derived, non-authoritative and for
implementation support only**. The authoritative text remains the
publication in [`schema-1.0/`](../../schema-1.0/README.md).

## Available experiments

- [`gpg-45-colour-coded-model.md`](gpg-45-colour-coded-model.md) — four key
  GPG 45 element tables (`claims`, `verification`, `evidence`,
  `document_details`, plus a legend), rendered with colour-coded type cells.
- [`gpg-44-colour-coded-model.md`](gpg-44-colour-coded-model.md) — the
  `authentication` and `authenticator` tables in the same style.

## The colour scheme

Each row is coloured by the **type** of the field. The legend is repeated
at the top of each experiment file; the palette is deliberately muted so
the page remains readable if the colours are not visible.

| Colour | Meaning |
|---|---|
| Light yellow  | Primitive type (`string`, `number`, `date`, `timestamp`) |
| Light blue    | Reference to another object defined elsewhere in the data model |
| Light green   | Array of a type |
| Light grey    | Fixed literal value (for example `'uk_dvstf'`, `'document'`, `'gpg45'`) |
| Light orange  | Restricted to a set of predefined values listed in `06-predefined-lists.md` |

The colour is applied via a `background-color` inline style on each row's
type cell. Inline styles are preserved by GitHub's Markdown renderer and by
the docs-site layer; in less capable renderers the colour simply drops
away and the text remains.

## Accessibility note

Colour is an **additional** signal, not the only signal. Every row also
states its type as text in the cell next to the colour, so readers who
cannot see the colour still get the same information. If you find a row
where the text does not carry the same meaning as the colour, please raise
an `Accessibility issue`.

## Scope and boundaries

- These files do not change the data model. They are a parallel view.
- These files do not and must not change a field's name, type, cardinality
  or description. Any discrepancy between an experiment file and the
  authoritative text under `schema-1.0/` is a bug in the experiment file.
- The experiments are hand-authored. If the schema changes upstream, the
  experiments need to be edited by hand to stay in sync — they are not
  machine-generated.

## Back

- [Supporting material](../README.md)
- [Repository home](../../README.md)
