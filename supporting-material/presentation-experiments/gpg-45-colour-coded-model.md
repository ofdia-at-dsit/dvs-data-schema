> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# GPG 45 — colour-coded data model (experiment)

> Derived, non-authoritative, for implementation support only.
> Authoritative definition: [`schema-1.0/gpg-45/03-data-model.md`](../../schema-1.0/gpg-45/03-data-model.md).

This page presents a selection of GPG 45 data-model elements as
colour-coded tables, inspired by the 1.3 internal draft. Colour is applied
by **type**; the text is the same as the authoritative model.

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
      <td><code>object (claims)</code>, <code>object (verification)</code></td>
    </tr>
    <tr>
      <td style="background-color:#e6ffe6">&nbsp;</td>
      <td>Array</td>
      <td><code>array (evidence)</code>, <code>array (attachment)</code></td>
    </tr>
    <tr>
      <td style="background-color:#f0f0f0">&nbsp;</td>
      <td>Fixed literal value</td>
      <td><code>'uk_dvstf'</code>, <code>'document'</code>, <code>'gpg45'</code></td>
    </tr>
    <tr>
      <td style="background-color:#ffeecc">&nbsp;</td>
      <td>Restricted to a predefined list</td>
      <td><code>document_type</code>, <code>assurance_level</code>, <code>procedure</code></td>
    </tr>
  </tbody>
</table>

## `verified_claims`

The top-level structure. Two sub-elements, both references.

<table>
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>claims</code></td>
      <td style="background-color:#e6f2ff"><code>object</code> (<a href="../../schema-1.0/gpg-45/03-data-model.md#claims">claims</a>)</td>
      <td>The identity information that represents the person making the claim.</td>
    </tr>
    <tr>
      <td><code>verification</code></td>
      <td style="background-color:#e6f2ff"><code>object</code> (<a href="../../schema-1.0/gpg-45/03-data-model.md#verification">verification</a>)</td>
      <td>Information about the checks done to prove the claims.</td>
    </tr>
  </tbody>
</table>

## `claims`

The identity information itself. A mix of primitives, references and
predefined-list values.

<table>
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>given_name</code></td>
      <td style="background-color:#fff9e6"><code>string</code></td>
      <td>Individual's given name(s).</td>
    </tr>
    <tr>
      <td><code>family_name</code></td>
      <td style="background-color:#fff9e6"><code>string</code></td>
      <td>Individual's family / surname name(s).</td>
    </tr>
    <tr>
      <td><code>transliteration_status</code></td>
      <td style="background-color:#e6f2ff"><code>object</code> (<a href="../../schema-1.0/gpg-45/03-data-model.md#transliteration-status">transliteration_status</a>)</td>
      <td>How the names have been transliterated from their original language.</td>
    </tr>
    <tr>
      <td><code>biometric_information</code></td>
      <td style="background-color:#e6ffe6"><code>array</code> (<a href="../../schema-1.0/gpg-45/03-data-model.md#biometric-information">biometric_information</a>)</td>
      <td>One or more biometric characteristics.</td>
    </tr>
    <tr>
      <td><code>birthdate</code></td>
      <td style="background-color:#fff9e6"><a href="../../schema-1.0/gpg-45/04-data-dictionary.md#date"><code>date</code></a></td>
      <td>Individual's birth date.</td>
    </tr>
    <tr>
      <td><code>nationalities</code></td>
      <td style="background-color:#ffeecc"><code>array</code> (<a href="../../schema-1.0/gpg-45/06-predefined-lists.md#predefined-lists">nationality</a>)</td>
      <td>One or more countries of citizenship.</td>
    </tr>
    <tr>
      <td><code>address</code></td>
      <td style="background-color:#e6f2ff"><code>object</code> (<a href="../../schema-1.0/gpg-45/03-data-model.md#address">address</a>)</td>
      <td>Individual's address.</td>
    </tr>
    <tr>
      <td><code>age</code></td>
      <td style="background-color:#fff9e6"><code>number</code></td>
      <td>The individual's age.</td>
    </tr>
    <tr>
      <td><code>is_under</code></td>
      <td style="background-color:#fff9e6"><code>number</code></td>
      <td>Whether they are under a specific age.</td>
    </tr>
    <tr>
      <td><code>is_over</code></td>
      <td style="background-color:#fff9e6"><code>number</code></td>
      <td>Whether they are over a specific age.</td>
    </tr>
  </tbody>
</table>

## `verification`

How the claims have been proven and linked to the person. This table is the
clearest example of the colour palette's purpose: at a glance you can see
one fixed literal, one reference, one array, one predefined-list value, and
one more reference.

<table>
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>trust_framework</code></td>
      <td style="background-color:#f0f0f0"><code>'uk_dvstf'</code></td>
      <td>The assurance framework; fixed string for DVS.</td>
    </tr>
    <tr>
      <td><code>dvs_registration</code></td>
      <td style="background-color:#e6f2ff"><code>object</code> (<a href="../../schema-1.0/gpg-45/03-data-model.md#dvs-registration">dvs_registration</a>)</td>
      <td>Which certified service performed the verification.</td>
    </tr>
    <tr>
      <td><code>evidence</code></td>
      <td style="background-color:#e6ffe6"><code>array</code> (<a href="../../schema-1.0/gpg-45/03-data-model.md#evidence">evidence</a>)</td>
      <td>The evidence used to prove the claim.</td>
    </tr>
    <tr>
      <td><code>assurance_level</code></td>
      <td style="background-color:#ffeecc"><a href="../../schema-1.0/gpg-45/06-predefined-lists.md#predefined-lists"><code>assurance_level</code></a></td>
      <td>The assurance level achieved.</td>
    </tr>
    <tr>
      <td><code>assurance_process</code></td>
      <td style="background-color:#e6f2ff"><code>object</code> (<a href="../../schema-1.0/gpg-45/03-data-model.md#assurance-process">assurance_process</a>)</td>
      <td>The processes performed to prove the claim.</td>
    </tr>
  </tbody>
</table>

## `evidence`

The three evidence types — document, electronic record, vouch — as
references.

<table>
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>document</code></td>
      <td style="background-color:#e6f2ff"><code>object</code> (<a href="../../schema-1.0/gpg-45/03-data-model.md#document">document</a>)</td>
      <td>A document used as evidence.</td>
    </tr>
    <tr>
      <td><code>electronic_record</code></td>
      <td style="background-color:#e6f2ff"><code>object</code> (<a href="../../schema-1.0/gpg-45/03-data-model.md#electronic-record">electronic_record</a>)</td>
      <td>An electronic record used as evidence.</td>
    </tr>
    <tr>
      <td><code>vouch</code></td>
      <td style="background-color:#e6f2ff"><code>object</code> (<a href="../../schema-1.0/gpg-45/03-data-model.md#vouch">vouch</a>)</td>
      <td>A vouch used as evidence.</td>
    </tr>
  </tbody>
</table>

## `document_details`

Where the predefined-list colour becomes useful. The document `type` is
restricted to values from `document_type` (see `06-predefined-lists.md`),
and the whole table mixes strings, dates, references and the restricted
list.

<table>
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>type</code></td>
      <td style="background-color:#ffeecc"><a href="../../schema-1.0/gpg-45/06-predefined-lists.md#predefined-lists"><code>document_type</code></a></td>
      <td>Type of document.</td>
    </tr>
    <tr>
      <td><code>document_number</code></td>
      <td style="background-color:#fff9e6"><code>string</code></td>
      <td>Unique document reference.</td>
    </tr>
    <tr>
      <td><code>serial_number</code></td>
      <td style="background-color:#fff9e6"><code>string</code></td>
      <td>Serial number identifying the physical document.</td>
    </tr>
    <tr>
      <td><code>personal_number</code></td>
      <td style="background-color:#fff9e6"><code>string</code></td>
      <td>Reference that uniquely identifies the person.</td>
    </tr>
    <tr>
      <td><code>date_of_issuance</code></td>
      <td style="background-color:#fff9e6"><a href="../../schema-1.0/gpg-45/04-data-dictionary.md#date"><code>date</code></a></td>
      <td>Date of issue.</td>
    </tr>
    <tr>
      <td><code>date_of_expiry</code></td>
      <td style="background-color:#fff9e6"><a href="../../schema-1.0/gpg-45/04-data-dictionary.md#date"><code>date</code></a></td>
      <td>Date of expiry.</td>
    </tr>
    <tr>
      <td><code>issuer</code></td>
      <td style="background-color:#e6f2ff"><a href="../../schema-1.0/gpg-45/03-data-model.md#authority"><code>authority</code></a></td>
      <td>Issuing authority.</td>
    </tr>
    <tr>
      <td><code>transliteration_status</code></td>
      <td style="background-color:#e6f2ff"><code>object</code> (<a href="../../schema-1.0/gpg-45/03-data-model.md#transliteration-status">transliteration_status</a>)</td>
      <td>How the document text has been transliterated.</td>
    </tr>
  </tbody>
</table>

## Back

- [Presentation experiments](README.md)
- [GPG 45 — data model (authoritative)](../../schema-1.0/gpg-45/03-data-model.md)
- [Supporting material](../README.md)
- [Repository home](../../README.md)
