# Passport

```json
{
      "source": "Passport",
      "fields": [
        "CountryID",
        "DurationOfStay",
        "EnterBefore",
        "Expires",
        "FacilityAssociationId",
        "InUse",
        "IssueDate",
        "Number",
        "PassportCategoryID",
        "PassportID",
        "PassportTypeID",
        "ProviderID"
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
    

### Preferred Contact Methods

Preferred contact methods can be found on the [Demographic](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint#user-content-demographic) page.
    
    
```json
{
      "source": "PreferredContact",
      "fields": [
        "ContactMethodID",
        "Preference",
        "PreferredContactID",
        "ProviderID"
      ],
      "sort": [  
         {"ProviderID":"asc"},  
         {"Preference": "desc"}
      ],
      "settings": {
        "IncludeArchivedProviders": false,
        "IncludeApplicants": true
      },
      "resultsperpage": 10,
      "page": 1
    }
```
    

### Supervisor

Due to potentially high volumes of Supervisors, it's required to provide a `Sort`
    
    
```json
{
      "source": "Supervisor",
      "fields": [
        "Comments",
        "EndDate",
        "FacilityId",
        "InUse",
        "ProviderId",
        "Reason",
        "Relationship",
        "StartDate",
        "SupervisorId"
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