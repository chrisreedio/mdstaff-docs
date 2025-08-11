# Network Members

Network Membership can be found and managed from the provider's record in Managed Care facilities.
    
    
```json
{
      "source": "NetworkMember",
      "fields": [
    		"NetworkMemberID",
    		"NetworkID",
    		"Network.Name",
    		"ProviderID",
    		"Provider.LastName",
    		"StartDate",
    		"EndDate",
    		"StatusID",
    		"Status.Description",
    		"TypeID",
    		"Type.Description",
    		"AgeRange.Description",
    		"OnTheWeb",
    		"PCP",
    		"Archived",
    		"ReasonLeft",
    		"Comments",
    		"LastUpdated",
    		"UpdatedBy"
      ],
      "sort": [],
      "settings": {
        "IncludeArchivedProviders": false,
        "IncludeApplicants": true
      },
      "resultsperpage": 10,
      "page": 1
    }
```
    

Related Objects:

  * `NetworkID` → [Networks](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint#user-content-networks)
  * `ProviderID` → [Demographic](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint#user-content-demographic)
  * `TypeID` → [LookUp](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint#user-content-demographic)
  * `AgeRangeID` → [LookUp](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint#user-content-demographic)