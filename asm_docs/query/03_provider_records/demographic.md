# Demographic

Demographic includes detailed provider information. Information stored alongside Demographic will be the same across all facilities.

**You will not be able to obtain Demographic records over the API that are not associated to at least 1 Appointment record. 

For more information about the Demographic data, [click here](https://support.asm-inc.com/hc/en-us/articles/115013509888-Demographic-Screen).
    
    
```json
{
      "source": "Demographic",
      "fields": [
        "AcceptMedicaid",
        "AcceptMedicare",
        "AcceptNewPatient",
        "AnsweringService",
        "Associate1",
        "Associate2",
        "Associate3",
        "Associate4",
        "Associate5",
        "AssociateTelephone",
        "BirthCity",
        "BirthCountry",
        "BirthDate",
        "BirthPlace",
        "BirthStateProvence",
        "CellPhone",
        "CitizenshipID",
        "Comments",
        "DegreeID_1",
        "DegreeID_2",
        "DegreeID_3",
        "Email",
        "EthnicityID",
        "FieldOfLicensureID",
        "FieldOfLicensureOther",
        "FirstName",
        "FormalName",
        "FormalNameWithDegree",
        "FormattedName",
        "FormattedNameWithDegree",
        "GenderID",
        "Graduate",
        "IsIndianHealthProvider",
        "IsQualifiedMedicalInterpreter",
        "LanguageID_1",
        "LanguageID_2",
        "LanguageID_3",
        "LanguageID_4",
        "LanguageID_5",
        "LastName",
        "LastUpdated",
        "MaritalStatusID",
        "MedicaidNumber",
        "MedicalSanction",
        "MedicareNumber",
        "MiddleName",
        "NotifyBy",
        "NPI",
        "OtherFirstName",
        "OtherID",
        "OtherLastName",
        "OtherMiddleName",
        "Pager",
        "Practice",
        "PreferredName",
        "PrefixID",
        "ProviderID",
        "RaceID",
        "Salutation",
        "SpecialtyID_1",
        "SpecialtyID_2",
        "SpecialtyID_3",
        "SpecialtyID_4",
        "SpouseName",
        "SSN",
        "SuffixID",
        "TaxID",
        "TaxonomyID_1",
        "TaxonomyID_2",
        "TaxonomyID_3",
        "TaxonomyID_4",
        "UPIN"
      ],
      "sort": [{
        "FormattedNameWithDegree": "asc"
      }],
      "settings": {
        "IncludeArchivedProviders": false,
        "IncludeApplicants": true
      },
      "resultsperpage": 10,
      "page": 1
    }
```