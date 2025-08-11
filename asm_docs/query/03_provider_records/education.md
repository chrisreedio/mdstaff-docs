# Education, Hospital Affiliation, Peer References, Other References

Education/Training, Hospital Affiliations, Peer References, and Other References can all be found under the `Reference` endpoint. Some fields will return blank for certain types (such as `DegreeEarnedID` for non-Education/Training. _(ReferenceTypes: Hospital, Medical Education, Undergraduate, Graduate School, Internship, Residency, Fellowship, Employment, Teaching, Military, Gap, Other, Peer Reference)_
    
    
```json
{
      "source": "Reference",
      "fields": [
        "Attention",
        "Comments",
        "Contact1",
        "Contact2",
        "Contact3",
        "DegreeEarnedID",
        "EndDate",
        "FacilityAssociationID",
        "HasAdmittingPrivileges",
        "InUse",
        "ProviderID",
        "ReferenceID",
        "ReferenceSourceID",
        "ReferenceStatusID",
        "ReferenceType",
        "ReferenceVerificationID",
        "SourceAddress",
        "SourceAddress2",
        "SourceBackline",
        "SourceCity",
        "SourceComments",
        "SourceCountryID",
        "SourceCountyID",
        "SourceEmail",
        "SourceFax",
        "SourceManager",
        "SourceState",
        "SourceTaxID",
        "SourceTelephone",
        "SourceURL",
        "SourceZip",
        "StartDate",
        "Subject"
      ],
      "sort": [{
        "InUse": "desc"
      }],
      "settings": {
        "IncludeArchivedProviders": false,
        "IncludeApplicants": true
      },  
      "filter": {"ReferenceType":["Medical Education","Residency"], "InUse":true},
      "resultsperpage": 10,
      "page": 1
    }
```