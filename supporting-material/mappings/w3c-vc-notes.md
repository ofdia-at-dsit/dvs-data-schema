> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

# DVS ↔ W3C Verifiable Credentials — notes

> Derived, non-authoritative, for implementation support only.
> Authoritative DVS definition: [`schema-1.0/gpg-45/`](../../schema-1.0/gpg-45/).
> W3C reference: [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/).

This is **not** a field-by-field mapping of DVS to the W3C Verifiable
Credentials Data Model. A full mapping would be a larger piece of work and
would live in a separate YAML file alongside `oid4ida-mapping.yaml` and
`oidc-core-mapping.yaml`. These are discussion notes to help contributors
think about the relationship.

## Why a field-by-field mapping is harder here

DVS `verified_claims` and OID4IDA `verified_claims` describe **the outcome
of a verification process** — who was verified, how, with what evidence,
to what assurance level. VC describes **a credential envelope** — issuer,
subject, claims, proof. The two are not the same shape of thing:

- OID4IDA is a claim structure that goes inside an ID Token, a UserInfo
  response, or an access token.
- VC is a credential format that can be exchanged independently and
  verified on its own.

A DVS verification outcome can be **embedded inside** a VC rather than
**translated field-for-field** into VC.

## The natural embedding

The least-contested way to put a DVS verification into a VC:

```json
{
  "@context": ["https://www.w3.org/ns/credentials/v2"],
  "type": ["VerifiableCredential", "DVSVerifiedClaimsCredential"],
  "issuer": "<DID or URL of the certified DVS>",
  "validFrom": "<ISO 8601 time>",
  "credentialSubject": {
    "id": "<subject DID or identifier>",
    "verified_claims": {
      "claims":       { ...DVS claims... },
      "verification": { ...DVS verification... }
    }
  },
  "proof": { ... }
}
```

Notes on this embedding:

- `verified_claims` sits inside `credentialSubject` unchanged. The DVS
  structure is preserved.
- The `issuer` of the VC is the DVS that performed the verification — the
  same organisation named inside DVS `verification.dvs_registration`.
  Having the name in both places is redundant but harmless, and each side
  has consumers that expect it in its own shape.
- `proof` is the VC layer's cryptographic proof of issuance. DVS does not
  currently model a signature over the verification outcome at the schema
  level; the VC wrapper adds that.
- `validFrom` and `validUntil` belong to the VC. DVS does not carry a
  freshness or expiry timestamp at the top of `verified_claims`; per-
  evidence `date_of_expiry` exists but is per-piece-of-evidence, not for
  the verification as a whole.

## Claim collisions

Some DVS / VC field names look similar but mean different things:

- **`type`**. DVS uses `type` as a discriminator inside each evidence
  item (`'document'`, `'electronic_record'`, `'vouch'`) and inside
  `document_details.type` and `record.type`. VC uses `type` at the
  credential envelope level as a URI array (`"VerifiableCredential"` plus
  the credential type). These are unrelated and do not collide when
  `verified_claims` sits inside `credentialSubject` — they are at
  different nesting levels.
- **`issuer`**. In VC this is the credential issuer (typically a DID).
  In DVS, `document_details.issuer` is the document's issuing authority
  (a country authority with an address and jurisdiction). Again, no
  collision by nesting.
- **`credentialSubject`** has no DVS counterpart because DVS does not
  identify a "subject" DID — the identity being verified is described by
  `claims`, not labelled by a subject identifier. Adding a subject id
  is a VC-level concern.

## Adjacent work

The OpenID Foundation is standardising VC-based identity assurance in the
`openid4vc` family (OID4VCI, OID4VP, SD-JWT VC, etc.). These specs define
credential formats and transport protocols in which DVS-shaped
verification data can travel. A DVS ↔ OID4VC mapping would be useful but
is out of scope for this file.

## What this page is for

If a contributor wants to build a DVS → VC adapter, this page documents:

1. That the natural embedding is `verified_claims` → `credentialSubject.verified_claims`.
2. That the issuer metadata is redundant between DVS and VC.
3. That freshness / validity timestamps belong to the VC, not DVS.
4. That `type` and `issuer` collisions are superficial, not semantic.

If a field-by-field mapping is wanted, open a `supporting-material` issue
and we can draft `w3c-vc-mapping.yaml` alongside the OID4IDA and OIDC Core
mappings.

## Back

- [Mappings](README.md)
- [Supporting material](../README.md)
- [Repository home](../../README.md)
