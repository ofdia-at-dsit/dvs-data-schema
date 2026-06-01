> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# Media

This folder holds shared image assets referenced from workspace pages — banners, figures, and any illustrations that appear in more than one page.

It is empty at launch because the published GOV.UK pages for GPG 45 and GPG 44 do not currently embed figures. The folder is in place so that:

- if the schema publication later introduces images, they can land here without a structure change;
- presentation experiments under `supporting-material/` can share image assets with the main pages.

## What belongs here

- **Shared** images used by more than one page (banners, figures).
- **Published** images that are part of the upstream GOV.UK publication, re-hosted in this workspace so that workspace pages render the same image.

## What does not belong here

- **Derived** diagrams generated from the schema (Mermaid outputs, dot-path visualisations). Those live under `supporting-material/diagrams/` so they are clearly labelled as derived and non-authoritative.
- **Site chrome** (GOV.UK logos, crown logos, design-system images). Those are provided by the `govuk-frontend` package inside `docs-site/` and must not be vendored here.

## Accessibility

Every image referenced from a workspace page must have meaningful alt text. If an image is decorative, use empty alt text (`alt=""`). If an image carries meaning that the surrounding prose does not also carry, either rewrite the prose so the meaning is there in text too, or add a full text description in a nearby paragraph or in a linked longer description.

## Licensing

Images published by OfDIA as part of the authoritative publication are © Crown copyright and licensed under [OGL v3.0](../LICENCE.md) unless otherwise stated. Third-party images must not be added here without confirming the licence allows re-hosting.

## Back

- [Repository home](../README.md)
