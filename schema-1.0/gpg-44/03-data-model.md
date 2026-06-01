> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

## Data model

The data model provides a description of the data element name, the relevant sub-elements and the data type.

### Overview

This nested view shows the relationship between elements and their sub‑elements.

<pre class="schema-example">
authentication
    authenticator_protection: string
    multifactor: string
    monitoring: string
    authenticators: array (authenticator)
</pre>

An authenticator is defined as:

<pre class="schema-example">
authenticator
    authenticator_type: string
    authenticator_quality: string
</pre>

---

**Previous:** [2. Data taxonomy](02-data-taxonomy.md)  
**Next:** [4. Data dictionary](04-data-dictionary.md)  
**Guide:** [GPG 44 landing page](README.md)  
**Version:** [Schema 1.0](../README.md)  
**Repository home:** [README](../../../README.md)

