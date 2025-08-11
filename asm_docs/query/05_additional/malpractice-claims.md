# Malpractice Claims/Incidents

Malpractice Claims (also referred to as Incidents) can be facility-specific, market-specific, or global. The `FacilityID` returned may be blank, or may include a _Market_ ID.
    
    
```json
{
      "source": "MalpracticeClaim",
      "fields": [
        "ActionID",
        "Allegation",
        "Amount",
        "CarrierID",
        "CloseDate",
        "DateFiled",
        "FacilityID",
        "History",
        "HospitalID",
        "IncidentDate",
        "MalpracticeClaimID",
        "Notes",
        "ProviderID",
        "Status",
        "StatusComments",
        "Type"
      ],
      "sort": [{
        "IncidentDate": "asc"
      }],
      "settings": {
        "IncludeArchivedProviders": false,
        "IncludeApplicants": true
      },
      "resultsperpage": 10,
      "page": 1
    }
```