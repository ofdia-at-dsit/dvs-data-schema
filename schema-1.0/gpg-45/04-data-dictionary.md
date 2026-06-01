> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

## GPG 45 data dictionary

To make sure there is consistency in how the data about identity proofing and verification is exchanged some of the elements must have a set format and use shared terms. The following section defines both allowed values and formats for a number of the elements in the GPG 45 data model.

### Data definitions

Some elements of this data model must have defined structure so that they are constructed and understood by all participants in the DVS trust framework.

#### Country code

Country codes should be 3-letter codes following ISO 3166-1 or ICAO Doc 9303. Other 2-letter and single codes may be used in some circumstances for compatibility reasons, for example Germany often uses 'D' as its issuer country code.

<pre class="schema-example">
country_code: string
</pre>

#### Date

Dates must always be in ISO 8601 'YYYY-MM-DD' format

<pre class="schema-example">
date: string
</pre>

#### Encoding

This describes the type of encoding used for the corresponding data. This should use media types as defined by [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml), or interchange formats defined by ISO/IEC 19794-5, ISO/IEC 39794-5, ANSI/NIST-ITL, or ISO/IEC 18013

<pre class="schema-example">
encoding: string
</pre>

#### Language

Language codes must follow ISO 639-1 or RFC 5646

<pre class="schema-example">
language: string
</pre>

#### Nationality

Nationality should use 3-letter codes following ISO 3166-1 or ICAO Doc 9303. Other 2-letter and single codes may be used in some circumstances for compatibility reasons.

<pre class="schema-example">
nationality: string
</pre>

#### Timestamp

Time stamps must always be in ISO 8601 'YYYY-MM-DDThh:mm(:ss)TZD' format

<pre class="schema-example">
date: string
</pre>

---

**Previous:** [3. Data model](03-data-model.md)  
**Next:** [5. Predefined values](05-predefined-values.md)  
**Guide:** [GPG 45 landing page](README.md)  
**Version:** [Schema 1.0](../README.md)  
**Repository home:** [README](../../../README.md)

