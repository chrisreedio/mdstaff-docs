# Date Filter:

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
    	],
    	"dynamicFilterParameters":{
    		"TableName": "dbo.Societies",
    		"Action":"Insert",
    		"StartDate":"04/10/2022",
    		"EndDate":"04/10/2022"
    	},
    	"filter": {
    		"DateChanged": [ {"type": "between", "values": ["04/10/2022 09:00:00", "04/10/2022 13:00:00"]}]
    	}
    }
```