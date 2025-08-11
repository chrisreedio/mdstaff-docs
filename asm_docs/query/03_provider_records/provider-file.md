# Provider File

Due to potentially high volumes of ProviderFiles, it's required to provide a `Sort`
    
    
```json
{
      "source": "ProviderFile",
      "fields": [
        "Comments",
        "DateExpired",
        "DateUploaded",
        "FacilityID",
        "FileDescription",
        "FileTypeID",
        "FileURL",
        "InUse",
        "ProviderID",
        "RecordID",
        "RecordType"
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