> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

> Derived, non-authoritative, for implementation support only.  
> Authoritative definition: the publication text under `schema-1.0/`.

# GPG 45 — dot-path view

Every field of the GPG 45 data model as a dot-separated path. Arrays are marked `[]`. Use these when referencing a specific field in an issue, ticket or PR.

```text
verified_claims
verified_claims.claims
verified_claims.claims.given_name
verified_claims.claims.family_name
verified_claims.claims.transliteration_status
verified_claims.claims.transliteration_status.original_language
verified_claims.claims.transliteration_status.transliterated_language
verified_claims.claims.transliteration_status.transliteration_type
verified_claims.claims.biometric_information[]
verified_claims.claims.biometric_information[].biometric_modality
verified_claims.claims.biometric_information[].attachments[]
verified_claims.claims.birthdate
verified_claims.claims.nationalities[]
verified_claims.claims.address
verified_claims.claims.address.street_address
verified_claims.claims.address.locality
verified_claims.claims.address.postal_code
verified_claims.claims.address.country
verified_claims.claims.address.transliteration_status
verified_claims.claims.age
verified_claims.claims.is_under
verified_claims.claims.is_over
verified_claims.verification
verified_claims.verification.trust_framework
verified_claims.verification.dvs_registration
verified_claims.verification.dvs_registration.registered_name
verified_claims.verification.dvs_registration.registration_id
verified_claims.verification.evidence[]
verified_claims.verification.evidence[].document
verified_claims.verification.evidence[].document.type
verified_claims.verification.evidence[].document.document_details
verified_claims.verification.evidence[].document.document_details.type
verified_claims.verification.evidence[].document.document_details.document_number
verified_claims.verification.evidence[].document.document_details.serial_number
verified_claims.verification.evidence[].document.document_details.personal_number
verified_claims.verification.evidence[].document.document_details.date_of_issuance
verified_claims.verification.evidence[].document.document_details.date_of_expiry
verified_claims.verification.evidence[].document.document_details.issuer
verified_claims.verification.evidence[].document.document_details.transliteration_status
verified_claims.verification.evidence[].document.attachments[]
verified_claims.verification.evidence[].document.check_details
verified_claims.verification.evidence[].electronic_record
verified_claims.verification.evidence[].electronic_record.type
verified_claims.verification.evidence[].electronic_record.record
verified_claims.verification.evidence[].electronic_record.record.type
verified_claims.verification.evidence[].electronic_record.record.reference_number
verified_claims.verification.evidence[].electronic_record.record.created_at
verified_claims.verification.evidence[].electronic_record.record.date_of_expiry
verified_claims.verification.evidence[].electronic_record.record.source
verified_claims.verification.evidence[].electronic_record.record.transliteration_status
verified_claims.verification.evidence[].electronic_record.attachments[]
verified_claims.verification.evidence[].electronic_record.check_details
verified_claims.verification.evidence[].vouch
verified_claims.verification.evidence[].vouch.type
verified_claims.verification.evidence[].vouch.attestation
verified_claims.verification.evidence[].vouch.attestation.type
verified_claims.verification.evidence[].vouch.attestation.reference_number
verified_claims.verification.evidence[].vouch.attestation.date_of_issuance
verified_claims.verification.evidence[].vouch.attestation.date_of_expiry
verified_claims.verification.evidence[].vouch.attestation.voucher
verified_claims.verification.evidence[].vouch.attestation.voucher.name
verified_claims.verification.evidence[].vouch.attestation.voucher.birthdate
verified_claims.verification.evidence[].vouch.attestation.voucher.address
verified_claims.verification.evidence[].vouch.attestation.voucher.country_code
verified_claims.verification.evidence[].vouch.attestation.voucher.occupation
verified_claims.verification.evidence[].vouch.attestation.voucher.organisation
verified_claims.verification.evidence[].vouch.attestation.transliteration_status
verified_claims.verification.evidence[].vouch.attachments[]
verified_claims.verification.evidence[].vouch.check_details
verified_claims.verification.assurance_level
verified_claims.verification.assurance_process
verified_claims.verification.assurance_process.policy
verified_claims.verification.assurance_process.procedure
verified_claims.verification.assurance_process.assurance_details[]
verified_claims.verification.assurance_process.assurance_details[].assurance_type
verified_claims.verification.assurance_process.assurance_details[].assurance_classification
verified_claims.verification.assurance_process.assurance_details[].evidence_ref[]
verified_claims.verification.assurance_process.assurance_details[].evidence_ref[].check_id
verified_claims.verification.assurance_process.assurance_details[].evidence_ref[].evidence_ref

# Shared sub-elements referenced from multiple places:
#   check_details.check_method
#   check_details.check_id
#   check_details.time
#   check_details.organisation
#   attachment.desc
#   attachment.content_type
#   attachment.content_format
#   attachment.content
#   authority.name
#   authority.address
#   authority.country_code
#   authority.jurisdiction
```
