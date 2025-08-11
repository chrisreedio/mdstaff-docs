# Provider Entities

Provider Entities can be found and managed from the provider's record in Managed Care facilities.
    
    
```json
{
      "source": "ProviderEntity",
      "fields": [
        "Comments",
        "EndDate",
        "EntityID",
        "FacilityID",
        "InUse",
        "ProviderEntityID",
        "ProviderID",
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