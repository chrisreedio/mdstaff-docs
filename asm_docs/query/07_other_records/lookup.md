# LookUp

```json
{
      "source": "LookUp",
      "fields": [
        "Archived",
        "Code",
        "Description",
        "FacilityID",
        "IsNegative",
        "LookUpID",
        "LookUpType",
        "ReadOnly",
        "SortOrder",
        "VerifyUsing"
      ],
      "sort": [{
        "Archived": "desc"
      }],
      "settings": {
        "IncludeArchivedProviders": false,
        "IncludeApplicants": true
      },  
      "filter": {"LookUpType":"Degree"},
      "resultsperpage": 10,
      "page": 1
    }
```