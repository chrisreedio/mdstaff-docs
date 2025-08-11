# Covering Provider

Due to potentially high volumes of CoveringProviders, it's required to provide a `Sort`
    
    
```json
{
      "source": "CoveringProvider",
      "fields": [
        "Comments",
        "CoveringProviderAddressID",
        "CoveringProviderID",
        "EndDate",
        "FacilityID",
        "InUse",
        "ProviderID",
        "SortOrder",
        "StartDate"
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