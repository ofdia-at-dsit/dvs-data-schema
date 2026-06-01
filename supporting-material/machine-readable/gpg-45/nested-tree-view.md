> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

> Derived, non-authoritative, for implementation support only.  
> Authoritative definition: the publication text under `schema-1.0/`.

# GPG 45 — nested tree view

Same content as the [dot-path view](dot-path-view.md), rendered as an indented tree.

```text
verified_claims
    claims
        given_name
        family_name
        transliteration_status
            original_language
            transliterated_language
            transliteration_type
        biometric_information[]
            biometric_modality
            attachments[]
        birthdate
        nationalities[]
        address
            street_address
            locality
            postal_code
            country
            transliteration_status
        age
        is_under
        is_over
    verification
        trust_framework
        dvs_registration
            registered_name
            registration_id
        evidence[]
            document
                type
                document_details
                    type
                    document_number
                    serial_number
                    personal_number
                    date_of_issuance
                    date_of_expiry
                    issuer
                    transliteration_status
                attachments[]
                check_details
            electronic_record
                type
                record
                    type
                    reference_number
                    created_at
                    date_of_expiry
                    source
                    transliteration_status
                attachments[]
                check_details
            vouch
                type
                attestation
                    type
                    reference_number
                    date_of_issuance
                    date_of_expiry
                    voucher
                        name
                        birthdate
                        address
                        country_code
                        occupation
                        organisation
                    transliteration_status
                attachments[]
                check_details
        assurance_level
        assurance_process
            policy
            procedure
            assurance_details[]
                assurance_type
                assurance_classification
                evidence_ref[]
                    check_id
                    evidence_ref

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
