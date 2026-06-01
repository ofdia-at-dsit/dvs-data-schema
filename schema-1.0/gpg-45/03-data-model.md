> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

## GPG 45 Data model  

The data model provides a description of the data element name, the relevant sub-elements and the data type.

### Verified claims

This is made up from two pieces of data, the identity the person is claiming to be ('claims'), and the information about the checks that have been done to prove the identity exists and belongs to them ('verification')

<pre class="schema-example">
verified_claims:
     claims: object (<a href="#claims">claims</a>)
     verification: object (<a href="#verification">verification</a>)
</pre>

### Claims

This is the identity information that represents the person making the claim. This can include:

- their given name

- their family name

- whether the names have been transliteration from their original language

- their date of birth

- their nationalities

- their biometric information

- their address

- their age

- whether they are over a specific age

- whether they are under a specific age

These are represented like this:

<pre class="schema-example">
claims:
     given_name: string
     family_name: string
     transliteration_status: object (<a href="#transliteration-status">transliteration_status</a>)
     biometric_information: array (<a href="#biometric-information">biometric_information</a>)
     birthdate: <a href="04-data-dictionary.md#date">date</a>
     nationalities: array (<a href="06-predefined-lists.md#predefined-lists">nationality</a>)
     address: object (<a href="#address">address</a>)
     age: number
     is_under: number
     is_over: number
</pre>

### Transliteration status

Transliteration is the process of converting text from one writing system or language into another by focusing on how words sound. It tries to the reflect the pronunciation of the original word using similar sounds in the target language so that speakers of either language can recognise the word.

It is not the same as translation which focuses and converting the meaning of a word, for example 東京 translates to 'eastern capital' but is more commonly known in English in its transliterated form, Tokyo.

The transliteration status conveys information about the:

- original language the text was written in 

- language the text has been transliterated to

- the way the transliteration was done

<pre class="schema-example">
transliteration_status:
     original_language: <a href="04-data-dictionary.md#language">language</a>
     transliterated_language: <a href="04-data-dictionary.md#language">language</a>
     transliteration_type: <a href="06-predefined-lists.md#predefined-lists">transliteration_type</a>
</pre>

### Biometric information

The biometric information represents one or more biometric characteristics about the person making the claim. The biometric information can contain any type of biometric modality and be encoded using several different methods and standards. Biometric data can include the:

- biometric characteristic ('modality') that is being exchanged

- the biometric data ('attachments')

<pre class="schema-example">
biometric_information:
     biometric_modality: <a href="06-predefined-lists.md#predefined-lists">biometric_modality</a>
     attachments: array (<a href="#attachment">attachment</a>)
</pre>

### Address

This contains a physical address, it can include the:

- street address

- town or city ('locality')

- post code

- country

- whether the address has been transliteration from the original language

<pre class="schema-example">
address:
     street_address: string
     locality: string
     postal_code: string
     country: string
     transliteration_status: object (<a href="#transliteration-status">transliteration_status</a>)
</pre>

### Verification

This is the information about how the claims have been proven and linked to the person it includes:

- a way to identify the assurance framework ('trust framework') relevant to the claim, for the DVS trust framework this is always 'uk_dvstf'

- information about the certified service's entry in the DVS register

- the evidence that was used to prove the claim

- the assurance level achieved in the claim being true, for the DVS trust framework this is always a GPG 45 level of confidence

- the processes that were performed in order to prove the claim

<pre class="schema-example">
verification:
     trust_framework: 'uk_dvstf'
     dvs_registration: object (<a href="#dvs-registration">dvs_registration</a>)
     evidence: array (<a href="#evidence">evidence</a>)
     assurance_level: <a href="06-predefined-lists.md#predefined-lists">assurance_level</a>
     assurance_process: object (<a href="#assurance-process">assurance_process</a>)
</pre>

### DVS registration

The DVS registration information identifies which certified service was used to prove the claim. It contains:

- the name of the certified service

- an identifier that uniquely identifies the service in the DVS register

<pre class="schema-example">
dvs_registration:
     registered_name: string
     registration_id: string
</pre>

### Evidence

This describes the evidence that was used by the service to prove the claim to the identity by the person. This includes the:

- details of the documents, electronic records or vouches that were used for the verification

<pre class="schema-example">
evidence:
     document: object (<a href="#document">document</a>)
     electronic_record: object (<a href="#electronic-record">electronic_record</a>)
     vouch: object (<a href="#vouch">vouch</a>)
</pre>

### Document

This describes how a document was used by the service to prove the claim. This can include:

- details about the document

- a copy of the document ('attachments')

- details about the checks that were done to validate the document

- details about the checks that were done to verify the person matches the identity in the document

<pre class="schema-example">
document:
     type: 'document'
     document_details: object (<a href="#document-details">document_details</a>)
     attachments: array (<a href="#attachment">attachment</a>)
     check_details: object (<a href="#check-details">check_details</a>)
</pre>

### Document details

This describes the document that was used by the service to prove the claim. This can include:

- the type of document

- a document reference or identification number that uniquely identifies a document that was issued

- a reference or identification number that uniquely identifies the person that is independent of a specific issued document

- a serial number that identifies the document irrespective of any personalisation information (this is usually only present on physical materials and not part of the personalisation of the document)

- the date of issue

- the date of expiry

- details about the issuer of the document

- whether the information about the document has been transliteration from the original language

<pre class="schema-example">
document_details:
     type: <a href="06-predefined-lists.md#predefined-lists">document_type</a>
     document_number: string
     serial_number: string
     personal_number: string
     date_of_issuance: <a href="04-data-dictionary.md#date">date</a>
     date_of_expiry: <a href="04-data-dictionary.md#date">date</a>
     issuer: <a href="#authority">authority</a>
     transliteration_status: object (<a href="#transliteration-status">transliteration_status</a>)
</pre>

### Electronic record

This describes an electronic record that was used by the service to prove the claim. This can include:

- details about the electronic record

- a copy of the electronic record ('attachments')

- details about the checks that were done for the electronic record

- details about the checks that were done to verify the person matches the identity in the electronic record

<pre class="schema-example">
electronic_record:
     type: 'electronic_record'
     record: object (<a href="#record">record</a>)
     attachments: array (<a href="#attachment">attachment</a>)
     check_details: object (<a href="#check-details">check_details</a>)
</pre>

### Record

This describes a record that was used by the service to prove the claim. This can include:

- the type of record

- a reference number that uniquely identifies the record

- the time the record was created

- the date the record will expire

- details about the source of the record

- whether the information about the record has been transliteration from the original language

<pre class="schema-example">
record:
     type: <a href="06-predefined-lists.md#predefined-lists">record_type</a>
     reference_number: string
     created_at: <a href="04-data-dictionary.md#timestamp">timestamp</a>
     date_of_expiry: <a href="04-data-dictionary.md#timestamp">timestamp</a>
     source: object (<a href="#authority">authority</a>)
     transliteration_status: object (<a href="#transliteration-status">transliteration_status</a>)
</pre>

### Vouch

This contains the information about a vouch that was used by the service to prove the claim. This can include:

- details about the vouch ('attestation') itself

- electronic version or copy of the vouch ('attachments')

- details about the checks that were done to validate the vouch

- details about the checks that were done to verify the person matches the identity in the vouch

<pre class="schema-example">
vouch:
     type: 'vouch'
     attestation: object (<a href="#attestation">attestation</a>)
     attachments: array (<a href="#attachment">attachment</a>)
     check_details: object (<a href="#check-details">check_details</a>)
</pre>

### Attestation

This contains the information about a vouch that was used by the service to prove the claim. This can include:

- a reference number that uniquely identifies the vouch

- the date the vouch was issued

- the date the evidence will expire

- details about the person that is providing the vouch

- whether the information about the attestation has been transliteration from the original language

<pre class="schema-example">
attestation:
     type: 'vouch'
     reference_number: string
     date_of_issuance: <a href="04-data-dictionary.md#date">date</a>
     date_of_expiry: <a href="04-data-dictionary.md#date">date</a>
     voucher: object (<a href="#voucher">voucher</a>)
     transliteration_status: object (<a href="#transliteration-status">transliteration_status</a>)
</pre>

### Authority

This identifies an authority that is able to issue or create evidence. This can include the:

- name of the authority

- address of the authority

- identifying code of the country or supranational organisation where the authority is based

- region(s)/state(s)/province(s)/municipality(ies) within the country where authority has jurisdiction to issue or create evidence

<pre class="schema-example">
authority:
     name: string
     address: <a href="#address">address</a>
     country_code: <a href="04-data-dictionary.md#country-code">country_code</a>
     jurisdiction: string
</pre>

### Voucher

This identifies the person that vouched for the person's claim to the identity. This can include the:

- name of the person providing the vouch

- date of birth of the person providing the vouch

- address of the person providing the vouch

- identifying code of the country or supranational organisation where the voucher is based

- occupation of the person providing the vouch

- name of the organisation that the voucher is representing

<pre class="schema-example">
voucher:
     name: string
     birthdate: <a href="04-data-dictionary.md#date">date</a>
     address: <a href="#address">address</a>
     country_code: <a href="04-data-dictionary.md#country-code">country_code</a>
     occupation: string
     organisation: object (<a href="#authority">authority</a>)
</pre>

### Check details

This contains the information about the checks that were performed. This can include:

- an identifier that describes what processes were followed to perform the check ('check method'), this can either be the process that was followed to validate the evidence, or verify the person's claim to the identity

- a unique reference number representing the check that was performed

- the time when the check was performed

- the name of the organisation that performed the check if the service did not perform the check itself

The check_id is a method to link the check performed with the evidence with the requirements of the trust framework, if this is present there should be a matching entry in [evidence_ref](#evidence-references) that demonstrates how it fits into the overall proofing and verification process required by the trust framework.

<pre class="schema-example">
check_details:
     check_method: <a href="06-predefined-lists.md#predefined-lists">check_method</a>
     check_id: string
     time: <a href="04-data-dictionary.md#timestamp">timestamp</a>
     organisation: string
</pre>

### Attachment

This provides the ability to exchange image or other binary data that may be needed, including scans of documents, photographs, video recordings, certificates, as well as other electronic data such as digital or verifiable credentials. This includes:

- a description of the attachment

- the type of data that has been encoded in the attachment

- the format of the encoding

- the encoded attachment data

<pre class="schema-example">
attachment:
     desc: string
     content_type: <a href="04-data-dictionary.md#encoding">encoding</a>
     content_format: <a href="06-predefined-lists.md#predefined-lists">encoding_format</a>
     content: data
</pre>

> **Editor's note — 13 April 2026 upstream correction.** The GOV.UK page for
> this data schema was updated on 13 April 2026 to correct a typo where
> `content_format` had previously been shown as `content_type` within the
> attachment element. The workspace text above matches the corrected GOV.UK
> version (`content_type` → `encoding`, `content_format` → `encoding_format`).
> This editor's note is not part of the published schema text; it is a
> workspace navigation aid for readers who remember the pre-correction
> wording. See the `[publication]` entry for 2026-04-13 in
> [`CHANGELOG.md`](../../../CHANGELOG.md).

### Assurance process

This contains detailed information about:

- the standard or policy that was followed in order to verify the claim ('policy'), for the DVS trust framework this is always GPG 45

- the specific procedure from the policy was followed ('procedure'), for the DVS trust framework this is always a GPG 45 profile

- how the details on which assurance processes were followed and how they meet the DVS trust framework

<pre class="schema-example">
assurance_process:
     policy: 'gpg45'
     procedure: <a href="06-predefined-lists.md#predefined-lists">procedure</a>
     assurance_details: array (<a href="#assurance-details">assurance_details</a>)
</pre>

### Assurance details

This contains information about the checks and processes that were performed to support the claim to the identity by the person. This includes:

- the type of check performed, for example validation, verification, counter fraud

- how the assurance process is classified in the trust framework, for the DVS trust framework this is always a score given by one of the steps in the proofing and verification process

- the evidence used to get the assurance in the claims and the person

<pre class="schema-example">
assurance_details:
     assurance_type: <a href="06-predefined-lists.md#predefined-lists">assurance_type</a>
     assurance_classification: <a href="06-predefined-lists.md#predefined-lists">assurance_classification</a>
     evidence_ref: array (<a href="#evidence-references">evidence_references</a>)
</pre>

### Evidence references

This contains:

- a unique reference number representing the check that was performed with the evidence

- other data about the checks or evidence that is required by the assurance process in order to demonstrate compliance with the trust_framework

The check_id is a method to link the checks performed with the evidence to the assurance processes, if check_id is present there must be a matching check_id in a [check_details](#check-details) object

<pre class="schema-example">
evidence_ref:
     check_id: string
     evidence_ref: object (<a href="#evidence-metadata">evidence_metadata</a>)
</pre>

### Evidence metadata

This contains:

- information on how the process used in [check_details](#check-details) demonstrates compliance with the assurance_type. This is additional information that may be needed in order to fully explain how the evidence was used in the assurance process.

<pre class="schema-example">
evidence_metadata:
     evidence_classification: <a href="06-predefined-lists.md#predefined-lists">evidence_classification</a>
</pre>

---

**Previous:** [2. Data taxonomy](02-data-taxonomy.md)  
**Next:** [4. Data dictionary](04-data-dictionary.md)  
**Guide:** [GPG 45 landing page](README.md)  
**Version:** [Schema 1.0](../README.md)  
**Repository home:** [README](../../../README.md)

