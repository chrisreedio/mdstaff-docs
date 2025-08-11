# Dues

```json
{
      "source": "Dues",
      "fields": [
        "DueDate",
        "DuesID",
        "DuesTypeID",
        "FacilityID",
        "PaymentAmount",
        "PaymentDate",
        "PaymentMethodID",
        "PaymentNumber",
        "ProviderID"
      ],
      "sort": [{
        "PaymentDate": "desc"
      }],
      "settings": {
        "IncludeArchivedProviders": false,
        "IncludeApplicants": true
      },
      "resultsperpage": 10,
      "page": 1
    }
```