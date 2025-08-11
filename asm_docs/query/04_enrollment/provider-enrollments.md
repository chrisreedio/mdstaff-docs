# Provider Enrollments/Provider Health Plans

Provider enrollments/provider health plans from the managed care view. `SiteHealthPlanID` and `EntityHealthPlanID` will be populated with the corresponding Site/Entity enrollment record if this provider enrollment record.

For more on provider enrollment, [click here](https://support.asm-inc.com/hc/en-us/articles/115013511008-Provider-Enrollment).
    
    
```json
{
      "source": "ProviderHealthPlan",
      "fields": [
        "Capacity",
        "Comments",
        "ContractID",
        "ContractName",
        "ContractTypeID",
        "DateApplicationSent",
        "DateExpires",
        "DateJoined",
        "DateLeft",
        "DateNotified",
        "EntityHealthPlanID",
        "FacilityID",
        "FeeTypeID",
        "HealthPlanID",
        "IDNumber",
        "InitialAppointment",
        "InUse",
        "Limitations",
        "NextAppointment",
        "ProviderHealthPlanID",
        "ProviderID",
        "Rate",
        "SiteHealthPlanID",
        "StatusID"
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