# History-with-Snapshot

#### Endpoint URL:
    
    
    https://{accountCode}.api.asm-cloud.com/api/{accountCode}/history-with-snapshot

**ASM highly recommends using the[Query endpoint](https://support.asm-inc.com/hc/en-us/articles/6354169565595-Get-Demographic-Changes) or [Triggered Webhooks](https://support.asm-inc.com/hc/en-us/articles/6527040404891-Triggered-Webhooks) to track object changes before resorting to the AuditLog/History-with-Snapshot endpoint. **

The History-with-Snapshot endpoint can be used to pull data in regards to historical changes made in MD-Staff as well as the actual changes at the field level(old value versus new value). This may be disabled in your system by default. If so, you will see the message: "AuditLog connection missing. History queries are unavailable without an AuditLog connection. Please contact support." Please create a new ticket <https://support.asm-inc.com/hc/en-us/requests/new> to request having the AuditLog Connection activated on your instance. 

Action types, you can target events such as 'Insert', 'Update', 'Delete' or 'All'.

#### ObjectSnapshot

The field ObjectSnapshot will contain the full snapshot of the Object at the time the action type was triggered. For the Action type "Update", the ObjectSnapshot contains XML and will include old values vs. new values. You will not be able to filter on values contained within the ObjectSnapshot, use the typical recommended filters such as "TableName", "Action", "StartDate", "EndDate" at a minimum.
    
    
```json
{
    	"fields": [
    		"AuditLogID"
    		,"DateChanged"
    		,"UserName"
    		,"TableName"
    		,"RecordID" ,
    		"ProviderID"
    		,"RelatedID"  
    		,"ObjectSnapshot"
    	],
    	"dynamicFilterParameters":{
    		"TableName": "dbo.Address",
    		"Action":"Update",
    		"StartDate":"03/10/2025",
    		"EndDate":"03/25/2025"
    	}
    }
```
    

#### Date Filter:

Note, the StartDate and EndDate values are treated as a Date type within the Date Range, not a datetime. If you need to incorporate a Datetime filter within the date range, you can apply a filter like the example below:
    
    
```json
{
    	"fields": [
    		"AuditLogID"
    		,"DateChanged"
    		,"UserName"
    		,"TableName"
    		,"RecordID" ,
    		"ProviderID"
    		,"RelatedID"  
    		,"ObjectSnapshot"
    	],
    	"dynamicFilterParameters":{
    		"TableName": "dbo.Address",
    		"Action":"Update",
    		"StartDate":"03/10/2025",
    		"EndDate":"03/25/2025"
    	},
    	"filter": {
    		"DateChanged": [ {"type": "between", "values": ["03/10/2025 09:00:00", "03/25/2025 13:00:00"]}]
    	}
    }
```

Related to 

  * [ Web API ](https://support.asm-inc.com/hc/en-us/search?content_tags=01JTR5R4YB20M8A4HS4XH551KR&utf8=%E2%9C%93 "Search results")