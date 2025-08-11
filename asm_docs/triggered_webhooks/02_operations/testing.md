# 4. Testing your Triggered Message & Webhook Endpoint

If you successfully configured your Triggered Message with your Webhook Endpoint. You can attempt to trigger the rule directly from MD-Staff. 

For this example, the Rule to be tested is:

  * Trigger a message anytime Address.InUse has been changed to "False".

#### Example Json request body:
    
    
```json
{
      "DataObject": {
        "AddressID": "681ceaf0-5593-444d-bc47-32d4ba6eb878",
        "ProviderID": "27efee9f-8cc4-48e9-9bb3-c15bcf610fd9",
        "AddressType": "Office0",
        "MedicalGroupID": null,
        "Address": "198 Seaside Drive",
        "Address2": null,
        "City": "San Diego ",
        "State": "CA",
        "Zip": "92113",
        "CountyID": null,
        "CountryID": "80181af6-6146-4fe4-8bce-0183ce815af8",
        "Email": null,
        "Telephone": null,
        "Fax": null,
        "Backline": null,
        "Manager": null,
        "URL": null,
        "NPI": null,
        "MedicareNumber": null,
        "MedicaidNumber": null,
        "MondayHours": null,
        "TuesdayHours": null,
        "WednesdayHours": null,
        "ThursdayHours": null,
        "FridayHours": null,
        "SaturdayHours": null,
        "SundayHours": null,
        "TaxID": null,
        "ReviewDate": null,
        "ReviewedBy": null,
        "NextReviewDate": null,
        "Comments": null,
        "ReviewScore": null,
        "LastUpdated": "2023-01-09T14:53:11.753",
        "UpdatedBy": "rbakerink@mdstaff.com",
        "InUse": {
          "Value": false,
          "IntValue": 0
        },
        "IDNumber": null,
        "Location": null,
        "PCPLimitID": null,
        "MedicaidPanelStatusID": null,
        "CommercialPanelStatusID": null,
        "WheelchairAccess": {
          "Value": false,
          "IntValue": 0
        },
        "StartDate": null,
        "EndDate": null,
        "AccreditationDate": null,
        "Publish": {
          "Value": false,
          "IntValue": 0
        },
        "AgeRangeID": null,
        "Contact": null,
        "FacilityAssociationID": null,
        "BillingAddress": null,
        "BillingAddress2": null,
        "BillingCity": null,
        "BillingState": null,
        "BillingZip": null,
        "BillingCountyID": null,
        "BillingCountryID": null,
        "BillingTelephone": null,
        "BillingFax": null,
        "BillingNPI": null,
        "BillingTaxID": null,
        "BillingAddressSourceID": null,
        "BillingEmail": null,
        "BillingURL": null,
        "MailingAddress": null,
        "MailingAddress2": null,
        "MailingCity": null,
        "MailingState": null,
        "MailingZip": null,
        "MailingCountyID": null,
        "MailingCountryID": null,
        "MailingTelephone": null,
        "MailingFax": null,
        "MailingNPI": null,
        "MailingTaxID": null,
        "MailingAddressSourceID": null,
        "MailingEmail": null,
        "MailingURL": null,
        "SundayHoursFrom": null,
        "SundayHoursTo": null,
        "MondayHoursFrom": null,
        "MondayHoursTo": null,
        "TuesdayHoursFrom": null,
        "TuesdayHoursTo": null,
        "WednesdayHoursFrom": null,
        "WednesdayHoursTo": null,
        "ThursdayHoursFrom": null,
        "ThursdayHoursTo": null,
        "FridayHoursFrom": null,
        "FridayHoursTo": null,
        "SaturdayHoursFrom": null,
        "SaturdayHoursTo": null,
        "ProviderClassificationID": null,
        "GenderLimitationID": null,
        "ProviderAddressBlock": "198 Seaside Drive\r\nSan Diego, CA  92113",
        "ProviderBillingAddressBlock": null,
        "ProviderMailingAddressBlock": null,
        "Synchronized": {
          "Value": false,
          "IntValue": 0
        },
        "CustomAddressID": "681ceaf0-5593-444d-bc47-32d4ba6eb878"
      },
      "ChangeSet": {
        "ObjectID": "681ceaf0-5593-444d-bc47-32d4ba6eb878",
        "ObjectType": "Address",
        "TriggeringFacilityOrMarketID": "2fd7e487-158a-44ca-b60b-69fb6f46a7b9",
        "TriggeringUserID": "92a2c005-8cfb-4c3a-9cf6-5ab5c44d8542",
        "TriggeringUserName": "rbakerink@mdstaff.com",
        "Fields": {
          "InUse": {
            "OldValue": "1",
            "NewValue": "N"
          }
        },
        "IsDeleted": false,
        "IsNew": false,
        "Count": 1
      },
      "Metadata": {
        "WebhookName": "Webhook Endpoint for Testing",
        "WorkflowName": "Track New Address"
      }
    }
```

[](https://support.asm-inc.com/hc/en-us/articles/6527040404891-Triggered-Webhooks#)