# Employment

Employment refers to the provider's Employment record, for Employment history, see [Reference/Other References](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint#user-content-education-hospital-affiliation-peer-references-other-references) with a type of `Employment`  _(Pending future release. Not currently supported)_.
    
    
```json
{
      "source": "Employment",
      "fields": [
        "AccountID",
        "ActivityCode",
        "ApprovalDate",
        "Comments",
        "ContractExpires",
        "ContractStart",
        "DepartmentID",
        "DivisionID",
        "EmploymentCategoryID",
        "EmploymentID",
        "EndDate",
        "FacilityID",
        "FTE",
        "FundID",
        "InUse",
        "IsPrimary",
        "LastUpdated",
        "NormalHours",
        "PositionNumber",
        "ProviderID",
        "SectionID",
        "StartDate",
        "StatusChangedDate",
        "StepDate",
        "TotalHours",
        "TotalWageRate",
        "WageRate",
        "WageStepID",
        "WageTypeID",
        "WorkUnit"
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