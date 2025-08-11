# Overview

The majority of interaction from the database can be done using the query endpoint. The query endpoint allows you to list the specific fields you want as well as how they should be filtered and sorted coming back from the server, reducing the need to store and filter data locally. For an overview of the WebApi and how to connect, [please see the WebApi article](https://support.asm-inc.com/hc/en-us/articles/115013514388).

### Using Query Batch

Refer to this [advanced article](https://support.asm-inc.com/hc/en-us/articles/35392052077979-Query-Batch-Endpoint) to learn more on how to query multiple objects in a single HTTP request. 

### Sub-Records

Fields in Records ending with ID often relate to a different source, typically a _LookUp_ , _Reference Source_ or different _data object_. Using these fields, you can access sub-properties directly from the query endpoint (can specify with or without the `ID` suffix).

Sub-Record behavior **is not** supported for `ID` fields subject to relating to difference sources. For example, the ProviderFile data object and the field `RecordID`. RecordID is a single column in the ProviderFile data object that could relate to different sources(BoardCertification, MedicalHistory, Credential, etc..) and Sub-Record behavior is not supported for this field.

Lookup sub-record field for example: `LicenseTypeID.Description` or `LicenseType.Description`.
    
    
```json
{
        "source": "Credential",
        "fields": [
            "CredentialID",
            "LicenseNumber",
            "LicenseType.LookupType",
            "LicenseType.Code",
            "LicenseType.Description"
        ]
    }
```
    

#### Example Response
    
    
```json
[
      {
        "CredentialID": "c3bde31e-daf3-4225-9137-001a82f71d6f",
        "LicenseNumber": "FS382384311123",
        "LicenseType_LookupType": "LicenseType",
        "LicenseType_Code": "DEA",
        "LicenseType_Description": "DEA"
      }
    ]
```
    

Reference Source sub-record field for example: `ReferenceSourceID.Name` or `ReferenceSource.Name`.
    
    
```json
{  
        "source": "BoardCertification",
        "fields": [
            "BoardCertificationID",
            "ProviderID",
            "CertificationNumber",
            "SpecialtyBoard.Name",
            "SpecialtyBoard.Code",
            "SpecialtyBoard.Address"
        ]    
    }
```
    

#### Example Response
    
    
```json
[
        {
            "BoardCertificationID": "c01b99b6-8e65-4594-bf75-0018a6fd5400",
            "CertificationNumber": "19272827444",
            "ProviderID": "da4909b3-a4c6-48a7-8e75-6e6ef749ddc1",
            "SpecialtyBoard_Address": "1010 Dixie Highway, Ste 313",
            "SpecialtyBoard_Code": null,
            "SpecialtyBoard_Name": "AOB of Obstetrics and Gynecology"
        }
    ]
```
    

For details on the relationships, see: [WebApi Provider Relationships](https://support.asm-inc.com/hc/en-us/articles/360051634534).

### Custom Fields

If your environment has custom fields, those fields can be included as one of the field names in the `fields` array.

### Security

All fields follow the permissions specified in MD-Staff, so if you do not have permission to access specific fields, you will not be able to access them in the API.