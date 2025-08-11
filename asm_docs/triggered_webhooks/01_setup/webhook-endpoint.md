# 2. Creating the Webhook Endpoint in MD-Staff

You can create Triggered Webhooks at the Market or Facility level. To configure a Webhook Endpoint in MD-Staff, please follow the steps defined below:

####  **2.1** : Navigate to the menu option **Setup / Aiva Credentialing / Webhook Endpoints**. Add a new Webhook Endpoint.

[![2023-01-09_14_14_41-MD-Staff___Setup___Triggered_Messages.png](../images/2023-01-09%2014_14_41-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)](../images/2023-01-09%2014_14_41-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)

####  **2.2** : Supply the Webhook Endpoint details and save. 

[![2023-01-09_14_19_54-MD-Staff___Setup_Workflow.png](../images/2023-01-09%2014_19_54-MD-Staff%20_%20Setup%20Workflow.png)](../images/2023-01-09%2014_19_54-MD-Staff%20_%20Setup%20Workflow.png)

  1. Provide a conventional name for the new Webhook endpoint.
  2. Supply a valid URL to receive Json body requests from MD-Staff when an object/action is triggered. 
  3. Select the correct API User aka API Access Key.
  4. Add any required Custom Headers. 
  5. Save your Webhook Endpoint.

####  **2.3** : Test a Triggered Message to the configured Webhook Endpoint

[![2023-01-09_15_15_14-MD-Staff___Setup___Triggered_Messages.png](../images/2023-01-09%2015_15_14-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)](../images/2023-01-09%2015_15_14-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)

Test Json request body will look similar to below:
    
    
    {
      "DataObject": {
        "ProviderID": "b466996b-11a0-4390-b745-e9a719c513b9",
        "SSN": null,
        "FirstName": "TestFirstName",
        "MiddleName": null,
        "LastName": "TestLastName",
        "SuffixID": null,
        "Salutation": null,
        "PrefixID": null,
        "PreferredName": null,
        "DegreeID_1": null,
        "DegreeID_2": null,
        "DegreeID_3": null,
        "SpecialtyID_1": null,
        "SpecialtyID_2": null,
        "SpecialtyID_3": null,
        "SpecialtyID_4": null,
        "OtherFirstName": null,
        "OtherMiddleName": null,
        "OtherLastName": null,
        "GenderID": null,
        "MaritalStatusID": null,
        "SpouseName": null,
        "BirthPlace": null,
        "BirthCity": null,
        "BirthStateProvence": null,
        "BirthCountry": null,
        "BirthDate": null,
        "CitizenshipID": null,
        "EthnicityID": null,
        "RaceID": null,
        "Graduate": null,
        "AssociateTelephone": null,
        "Associate1": null,
        "Associate2": null,
        "Associate3": null,
        "Associate4": null,
        "Associate5": null,
        "Pager": null,
        "Practice": null,
        "TaxID": null,
        "OtherID": null,
        "AnsweringService": null,
        "CellPhone": null,
        "Email": null,
        "AcceptNewPatient": {
          "Value": false,
          "IntValue": 0
        },
        "AcceptMedicare": {
          "Value": false,
          "IntValue": 0
        },
        "MedicareNumber": null,
        "AcceptMedicaid": {
          "Value": false,
          "IntValue": 0
        },
        "MedicaidNumber": null,
        "MedicalSanction": null,
        "UPIN": null,
        "LastUpdated": null,
        "UpdatedBy": null,
        "NPI": null,
        "NotifyBy": null,
        "LanguageID_1": null,
        "LanguageID_2": null,
        "LanguageID_3": null,
        "LanguageID_4": null,
        "LanguageID_5": null,
        "TaxonomyID_1": null,
        "TaxonomyID_2": null,
        "TaxonomyID_3": null,
        "TaxonomyID_4": null,
        "FieldOfLicensureID": null,
        "FieldOfLicensureOther": null,
        "FormattedName": null,
        "FormattedNameWithDegree": null,
        "FormalName": null,
        "FormalNameWithDegree": null,
        "Comments": null,
        "IsQualifiedMedicalInterpreter": {
          "Value": false,
          "IntValue": 0
        },
        "IsIndianHealthProvider": {
          "Value": false,
          "IntValue": 0
        },
        "PhotoLastUpdated": null,
        "CustomProviderID": "b466996b-11a0-4390-b745-e9a719c513b9",
        "AppliedStatus": null,
        "PetsName": null,
        "PetBirthday": null,
        "PetIsAGoodDog": {
          "Value": false,
          "IntValue": 0
        },
        "PetBreedID": null
      },
      "ChangeSet": {
        "ObjectID": "b466996b-11a0-4390-b745-e9a719c513b9",
        "ObjectType": "Demographic",
        "TriggeringFacilityOrMarketID": "2fd7e487-158a-44ca-b60b-69fb6f46a7b9",
        "TriggeringUserID": "92a2c005-8cfb-4c3a-9cf6-5ab5c44d8542",
        "TriggeringUserName": "rbakerink@mdstaff.com",
        "Fields": {
          "FirstName": {
            "OldValue": "Old First Name",
            "NewValue": "TestLastName"
          }
        },
        "IsDeleted": false,
        "IsNew": false,
        "Count": 1
      },
      "Metadata": {
        "WebhookName": "Webhook Endpoint for Testing",
        "WorkflowName": "Test Workflow Name"
      }
    }

[](https://support.asm-inc.com/hc/en-us/articles/6527040404891-Triggered-Webhooks#)