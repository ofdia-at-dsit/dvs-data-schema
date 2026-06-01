# docs-site

The GOV.UK-styled static site for this repository. Built with
[Eleventy (11ty)](https://www.11ty.dev/) and the official
[govuk-frontend](https://github.com/alphagov/govuk-frontend) npm package,
following the same pattern as the trust framework web repo.

> [!IMPORTANT]
> The rendered site is a **view** of the repository. It is not the
> authoritative publication. The authoritative version of the UK DVS trust
> framework data schema lives on GOV.UK. See
> [`../LICENCE.md`](../LICENCE.md) and the repository
> [`../README.md`](../README.md) for context.

## Architecture

- The Markdown source lives at the repository root (`schema-1.0/**`,
  top-level READMEs, `supporting-material/**`, `CONTRIBUTING.md`, etc.).
  This folder does not duplicate any of it.
- Eleventy's input directory is `..` (the repo root), with
  [`../.eleventyignore`](../.eleventyignore) excluding build tooling and CI
  config from the build.
- Layouts, includes, data and the `govspeak.js` markdown-it plugin all live
  inside this folder.
- The site builds into `_site/` (git-ignored).

```
docs-site/
├── package.json              deps: eleventy, markdown-it, markdown-it-anchor, govuk-frontend
├── .eleventy.js              config: permalinks, md-link rewrite, govuk-frontend assets
├── govspeak.js               markdown-it plugin for GOV.UK GovSpeak ($CTA, $E, %…%, ^…^)
├── _layouts/
│   ├── default.html          full GOV.UK page chrome
│   └── page.html             adds a one-quarter TOC sidebar when headings exist
├── _includes/
│   ├── skip-link.html
│   ├── govuk-header.html
│   ├── service-navigation.html
│   ├── phase-banner.html
│   ├── page-title.html
│   ├── page-footer.html      edit-on-GitHub + raise-an-issue links
│   └── govuk-footer.html
└── _data/
    ├── site.json             title, caption, phase banner text, repo URL
    └── eleventyComputed.js   default layout + permalink scheme + title fallback
```

## Local development

```bash
cd docs-site
npm install
npm start       # eleventy --serve, watches the repo, hot-reloads
```

Open <http://localhost:8080/>.

To build once without the dev server:

```bash
npm run build   # outputs to docs-site/_site/
```

## Deployment

The workflow at
[`../.github/workflows/build-docs-site.yml`](../.github/workflows/build-docs-site.yml)
builds the site on pushes to `main` and deploys to GitHub Pages using
GitHub's native `actions/deploy-pages` action.

Before first deploy, in the repository settings under **Pages**, set the
source to **GitHub Actions**.

### Subpath deployments

`govuk-frontend`'s CSS references assets under `/assets/...` (an absolute
path from the site root). Out of the box this works for root-domain
deployments (e.g. `dvs-data-schema.ofdia.gov.uk`).

For subpath deployments (e.g.
`username.github.io/dvs-data-schema/`), the build reads a `BASEURL`
environment variable and rewrites `govuk-frontend`'s asset URLs at build
time. The CI workflow passes
`steps.pages.outputs.base_path` into the build as `BASEURL`, so the site
works whether deployed at a domain root (BASEURL empty) or a repo subpath.

## Back

- [Repository home](../README.md)
