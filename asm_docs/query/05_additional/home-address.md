# Home Address

Home address is separated from office addresses. The `Credentialing_Sensitive` role is required in order to access home addresses.
    
    
```json
{
      "source": "HomeAddress",
      "fields": [
        "Address",
        "Address2",
        "City",
        "Comments",
        "CountryID",
        "CountyID",
        "Email",
        "FacilityAssociationID",
        "Fax",
        "HomeAddressID",
        "InUse",
        "LastUpdated",
        "ProviderID",
        "State",
        "Telephone",
        "Zip"
      ],
      "sort": [{
        "InUse": "desc"
      }],
      "settings": {
        "IncludeArchivedProviders": false,
        "IncludeApplicants": true
      },
      "resultsperpage": 10,
      "page": 1
    }
```