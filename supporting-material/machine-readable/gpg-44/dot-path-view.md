> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published DVS trust framework data schema, visit GOV.UK.

> Derived, non-authoritative, for implementation support only.  
> Authoritative definition: the publication text under `schema-1.0/`.

# GPG 44 — dot-path view

Every field of the GPG 44 data model as a dot-separated path.

```text
authentication
authentication.authenticator_protection
authentication.multifactor
authentication.monitoring
authentication.authenticators[]
authentication.authenticators[].authenticator_type
authentication.authenticators[].authenticator_quality
```
