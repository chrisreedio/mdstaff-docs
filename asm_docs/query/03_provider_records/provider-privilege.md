# Provider Privilege

Provider privileges refer to the raw, individual items that the provider has been granted or has requested. To see whether the form is active, archived, or draft/scheduled see [Provider Privilege Forms.](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint#user-content-provider-privilege-forms)

If the corresponding element type is `CustomPrivilege`, the `CustomContent` field should be used.
    
    
```json
{
      "source": "ProviderPrivilege",
      "fields": [
        "CasesCompleted",
        "CasesRequired",
        "Comments",
        "CustomContent",
        "Expired",
        "FacilityID",
        "FormTypeVersion",
        "Granted",
        "PrivilegeFormID",
        "PrivilegeStatusID",
        "ProctoringRequired",
        "ProviderID",
        "ProviderPrivilegeFormID",
        "ProviderPrivilegeID"
      ],
      "sort": [{
        "ProviderPrivilegeFormID": "asc"
      }],
      "settings": {
        "IncludeArchivedProviders": false,
        "IncludeApplicants": true
      },
      "resultsperpage": 10,
      "page": 1
    }
```