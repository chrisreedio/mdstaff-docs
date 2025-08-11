# Reference Source

Reference Source is used as the source addresses for [Education, Hosptials, Peer, and Other References](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint#user-content-education-hospital-affiliation-peer-references-other-references).

_(ReferenceTypes: Hospital, Medical Education, Undergraduate, Graduate School, Internship, Residency, Fellowship, Employment, Teaching, Military, Gap, Other, Peer Reference)_
    
    
```json
{
      "source": "ReferenceSource",
      "fields": [
        "Address",
        "Address2",
        "Backline",
        "City",
        "Code",
        "Comments",
        "Country",
        "County",
        "Degree",
        "Email",
        "Fax",
        "FirstName",
        "InternalId",
        "IsArchived",
        "IsMaster",
        "LastName",
        "Manager",
        "MiddleName",
        "Name",
        "ReferenceSourceID",
        "ReferenceType",
        "State",
        "TaxID",
        "Telephone",
        "URL",
        "VerifyURL",
        "VerifyUsing",
        "Zip"
      ],
      "sort": [{
        "Archived": "asc"
      }],
      "settings": {
        "IncludeArchivedProviders": false,
        "IncludeApplicants": true
      },  
      "filter": {"ReferenceType": "Hospital"},
      "resultsperpage": 10,
      "page": 1
    }
```