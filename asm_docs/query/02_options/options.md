# Options

Options are not required and the query endpoint will return results with default options if the options are not specified.

Options require MD-Staff 9.7 and WebApi 3.52 or higher. To determine your WebApi version, see [WebApi Version](https://support.asm-inc.com/hc/en-us/articles/1260804603269).

### Fields

For the fields portion of the query you can optionally adjust the `alias` (the name being returned) and the `type`/format for Date and Boolean Fields.

Field options are formatted as shown:
    
    
    { 
    	name: 'FieldName', 
    	alias: 'FieldNameAlias', // Optional (defaults to the `FieldName`)
    	type: 'deafult' // Optional (defaults to "default", see below for more details)
    }
    

The fields array can be a mixture of options and non-options, as follows:
    
    
    fields: [
    	"ProviderName",
    	"AcceptNewPatient",
    	{ name: "AcceptNewPatient", alias: "AcceptNewPatientYesNo", type: "Yes/No" },
    	"BirthDate",
    	{ name: "BirthDate", alias: "BirthDate_Sortable", type: "sortable" },
    ]
    

Would output fields:
    
    
```json
{
    	"ProviderName": "Bell, Kenneth",
    	"AcceptNewPatient": true,
    	"AcceptNewPatientYesNo": "Yes",
    	"BirthDate": "07/24/1971",
    	"BirthDate_Sortable": "1971/07/24 00:00"
    }
```
    

All available fields for a Query data object can be returned by using "*" inside of the fields array in your Query.
    
    
    fields: ["*"]
    

This is a useful feature for:

  1. Added convenience if you're accessing a new object, rather than accessing the WebApi documentation.
  2. Showcasing custom fields that may be available to the data object.
  3. For general browsing of a data object.

**Using fields["*"] in a production integration is inadvisable as the response/output is subject to change at any time.**

#### `alias`

Alias can be any string, the field named will be returned with that Alias. Alias values **must be unique** across names and other aliases.

#### `type`

For date/dateime and boolean fields, there are several type options available:

##### Date/DateTime

  * `default`: "05/24/2019" if its a date field or "05/24/2019 17:04" if its a datetime field
  * `sortable`: "2020/05/24 17:04"
  * `raw`: "2020/05/24T17:04:12.5432Z" is a ISO 8601 string representation of a date field

##### Boolean

  * `default`: true / false (bool)
  * `1/0` => 1 / 0 (int)
  * `T/F`, `t/f`, `Y/N`, `y/n`, `Yes/No`, `yes/no`, `True/False`, `true/false` will return the string representation of its value. 
    * i.e. `t/f` will return either "t" or "f"

### Filter

By default (and in prior versions), the query filters are filtering by values in a list, using a type of `in`. There are two other filter types, `between` and `search`.

#### `in`

When no filter type is specified, the query endpoint will assume that the type is `in` and match the values in the query.
    
    
    	// 1. Fiter a field on a single value
    	{ 
    		... other query props
    		filter: {
    			Status: "Current"
    		}
    	}
    	// 2. Filter a field on a multiple values
    	{
    		... other query props
    		filter: {
    			Status: ["Current", "Error"]
    		}
    	}
    	// 3. Filter a field with other values
    	{
    		... other query props
    		filter: {
    			Status: [ { type: "in", values: ["Current", "Error"] } ]
    		}
    	}
     	// 4. Filter for values in a field not containing NULL
    	{
    		... other query props
    		filter: {
    			Status: [ { type: "not in", values: [null] } ]
    		}
    	}
    

#### `between` for Dates

When filtering on dates, you can use the type `between` to filter all items between a date range, as shown below:
    
    
    	{
    		... other query props
    		filter: {
    			DateArchived: [ {type: "between", values: ["01/01/1950", "12/31/1959"]}],
    			
    			// Will return between dates and any null dates
    			AnotherDateField: [
    			  {type: "between", values: ["01/01/1950", "12/31/1959"]},
    			  {type: "in", values: [null]}
    		  ]
    		}
    	}
    

#### `search`

When filtering on a string, you can use `%` as a wildcard to search for items. Each filter item with type search can only have a single value.
    
    
    	{
    		... other query props
    		filter: {
    			ProviderName: [ 
    				{
    					type: "search", 
    					values: ["bell%"] // There can only be a single search value per item
    				},
    				{
    					type: "search", 
    					values: ["%stotch%"] // There can only be a single search value per item
    				},
    			]
    		}
    	}
    

###  Sort 

By default, the data object's primary key will be used for sorting in an ascending order. 

You can specify your own Sort filter
    
    
    	{ 
    		... other query props
    		"sort": [{ "FieldName1": "desc" }],
    	}
    

You can apply multiple Sort filter rules:
    
    
    	{ 
    		... other query props
    		"sort": [
    				{ "FieldName1": "desc" },
    				{ "FieldName2": "asc" }
    		],
    	}
    

### Counts

If you want to know how many of an item there are without returning all the details you can use the `counts` property. The counts property can be used with other fields, automatically grouping by those fields, to return the number of items per-specified field, as follows:

Options require MD-Staff 9.8 and WebApi 3.53 or higher. To determine your WebApi version, see [WebApi Version](https://support.asm-inc.com/hc/en-us/articles/1260804603269).
    
    
    {
    	source: "Applicants",
    	fields: [ "ApplicationStatus" ],  
    	counts: true
    }
    

Will return:
    
    
    [
    	{ApplciationStatus: "Status1", Counts: 4},
    	{ApplciationStatus: "Status2", Counts: 7},
    	{ApplciationStatus: "Status3", Counts: 1}
    ]
    

Only use 'Counts' option for aggregation purposes. It is inadvisable to use 'Counts' for result pagination.

If you want to obtain a total record count for a Source data object based on the scope of your Authorization Token context, you can send a request to the Query endpoint like the following:
    
    
```json
{
    	"source": "Appointment",
    	"counts": true
    }
```

The response may look something like the following
    
    
```json
[
      {
        "Counts": 3915
      }
    ]
```

If you want to include Archived Providers and/or Applicants in the record count, your request may look like the following:
    
    
```json
{
        "source": "Appointment",
        "counts": "true",
        "settings": {
            "IncludeArchivedProviders": "true",
            "IncludeApplicants": "true"
        }
    }
```

The response may look something like the following
    
    
```json
[
      {
        "Counts": 7315
      }
    ]
```

If you want to include a record count between a date range, your request may look like the following:
    
    
```json
{
    	"source": "Appointment",
    	"counts": true,
    	"filter":{
    		"LastUpdated": [ {"type": "between", "values": ["01/01/2025", "03/01/2025"]}]
    	}
    }
```

The response may look something like the following
    
    
```json
[
      {
        "Counts": 105
      }
    ]
```

Recommended best practice is to use ResultsPerPage and Pages options for pagination. When you reach the final page of the results, either the results will be less than the designated page size or no results will be returned. 

### Pagination

The Query endpoint does not freeze records to obtain a static index of all results, the Query endpoint is real-time, so results returned over multiple pages could shift. 

For instance, if you're targeting a data source subject to frequent change and your integration is extracting multiple pages of records, if records are added/modified during your integration processing, this could shift the indexed results and the last X number of results on a previous page could get pushed to the next page of results.

As a result, records that fall into this situation will appear as duplicates, however, please note it’s real-time data and the indexed data has just shifted between your paginated requests.

Below is the best recommended ways to account for this scenario:

  1. Obtain incremental changes only. Add a Filter to obtain records over the Query endpoint where the LastUpdated value is between last run and now. This will reduce the volume of data to be indexed and extracted. A prerequisite is to perform a one-time data load, then going forward deploy incremental changes.
  2. Program logic into your integration to elegantly handle Primary Ids that may occur on multiple pages of results due to the above mentioned scenario.