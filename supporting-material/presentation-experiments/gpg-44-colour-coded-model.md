> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# GPG 44 — colour-coded data model (experiment)

> Derived, non-authoritative, for implementation support only.
> Authoritative definition: [`schema-1.0/gpg-44/03-data-model.md`](../../schema-1.0/gpg-44/03-data-model.md).

The GPG 44 schema is small — two elements — so the colour-coded view is
short. It is useful here for the same reason as GPG 45: the type of each
field is readable at a glance, and the two `*_protection` and `*_quality`
fields are visibly restricted to predefined lists.

## Legend

<table>
  <thead>
    <tr><th>Colour</th><th>Type category</th><th>Example</th></tr>
  </thead>
  <tbody>
    <tr>
      <td style="background-color:#fff9e6">&nbsp;</td>
      <td>Primitive</td>
      <td><code>string</code>, <code>number</code>, <code>date</code>, <code>timestamp</code></td>
    </tr>
    <tr>
      <td style="background-color:#e6f2ff">&nbsp;</td>
      <td>Reference to another object</td>
      <td><code>object (authenticator)</code></td>
    </tr>
    <tr>
      <td style="background-color:#e6ffe6">&nbsp;</td>
      <td>Array</td>
      <td><code>array (authenticator)</code></td>
    </tr>
    <tr>
      <td style="background-color:#f0f0f0">&nbsp;</td>
      <td>Fixed literal value</td>
      <td>none in GPG 44</td>
    </tr>
    <tr>
      <td style="background-color:#ffeecc">&nbsp;</td>
      <td>Restricted to a predefined list</td>
      <td><code>authenticator_type</code>, <code>authenticator_quality</code>, <code>authenticator_protection</code></td>
    </tr>
  </tbody>
</table>

## `authentication`

The top-level object. Three predefined-list fields and one array.

<table>
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>authenticator_protection</code></td>
      <td style="background-color:#ffeecc"><code>string</code> (<a href="../../schema-1.0/gpg-44/06-predefined-lists.md">authenticator_protection</a>)</td>
      <td>Level of protection achieved according to GPG 44.</td>
    </tr>
    <tr>
      <td><code>multifactor</code></td>
      <td style="background-color:#fff9e6"><code>string</code></td>
      <td>The number of factors used in the authentication.</td>
    </tr>
    <tr>
      <td><code>monitoring</code></td>
      <td style="background-color:#fff9e6"><code>string</code></td>
      <td>Whether monitoring is being performed.</td>
    </tr>
    <tr>
      <td><code>authenticators</code></td>
      <td style="background-color:#e6ffe6"><code>array</code> (<code>authenticator</code>)</td>
      <td>Array of authenticator objects.</td>
    </tr>
  </tbody>
</table>

## `authenticator`

Each item in the `authenticators` array. Two predefined-list fields.

<table>
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>authenticator_type</code></td>
      <td style="background-color:#ffeecc"><code>string</code> (<a href="../../schema-1.0/gpg-44/06-predefined-lists.md">authenticator_type</a>)</td>
      <td>The type of authenticator according to GPG 44.</td>
    </tr>
    <tr>
      <td><code>authenticator_quality</code></td>
      <td style="background-color:#ffeecc"><code>string</code> (<a href="../../schema-1.0/gpg-44/06-predefined-lists.md">authenticator_quality</a>)</td>
      <td>The quality of the authenticator according to GPG 44.</td>
    </tr>
  </tbody>
</table>

## What the palette makes visible in GPG 44

The four orange cells out of a total of six non-primitive cells tell you,
without reading a single word, that most of GPG 44's fields are restricted
to enumerated values. That is consistent with what the schema is for —
pick an authenticator type and quality from a known list, rather than
freeform text.

## Back

- [Presentation experiments](README.md)
- [GPG 44 — data model (authoritative)](../../schema-1.0/gpg-44/03-data-model.md)
- [Supporting material](../README.md)
- [Repository home](../../README.md)
