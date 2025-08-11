# Security

### User
    
    
```json
{
      "source": "User",
      "fields": [
        "UserID",
        "UserName",
        "PasswordReset",
        "FirstName",
        "LastName",
        "Email",
        "Telephone",
        "Credentials",
        "Title",
        "Fax",
        "LabelLanguage",
        "ExpirationDate",
        "IsActive",
        "LastLogin",
        "InactivityExpiration",
        "UsesLDAP",
        "IsLocked",
        "LockExpirationDate",
        "EmailConfirmedDate",
        "PasswordLastUpdated",
        "DateCreated",
        "CreatedBy",
        "LastUpdated",
        "UpdatedBy",
        "UserDateFormat",
        "UserDateTimeFormat"
      ],
      "filter": [{"IsActive": [true]}],
      "sort": [{"UserName": "ASC"}],
      "resultsperpage": 10,
      "page": 1
    }
```
    

### User Roles

Users can belong to multiple groups, the read-only object `UserRole` will return unique results for User, Role, and Facility/Market—de-duplicating the multiple the same way that MD-Staff evaluates the permissions. When multiple groups are present, `GroupID` and `GroupName` represents the group used to determine the permission.
    
    
```json
{
      "source": "UserRole",
      "fields": [
        "SecurityPermissionID",
        "RoleID",
        "RoleName",
        "UserID",
        "UserName",
        "FacilityOrMarketID",
        "FacilityOrMarketName",
        "IsAllowed",
        "IsDenied",
        "GroupID",
        "GroupName"
      ],
      "sort": [{"UserName": "ASC"}],
      "resultsperpage": 10,
      "page": 1
    }
```
    

Related objects:

  * `UserID` → [User](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint#user-content-user)
  * `FacilityOrMarketID` → Facility/Market
  * `GroupID` → [Group](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint#user-content-group)

### Group
    
    
```json
{
      "source": "Group",
      "fields": [
        "Uid",
        "Name",
        "Description",
        "FacilityOrMarketID"
      ],
      "sort": [{"Name": "ASC"}],
      "resultsperpage": 10,
      "page": 1
    }
```
    

### Group Membership
    
    
```json
{
      "source": "GroupMembership",
      "fields": [
        "Uid",
        "GroupId",
        "UserId"
      ],
      "resultsperpage": 10,
      "page": 1
    }
```
    

Related objects:

  * `GroupID` → [Group](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint#user-content-group)
  * `UserID` → [User](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint#user-content-user)

### Security Permissions

`ObjectID` represents either a `UserID` or `GroupID`. `FacilityID` can be either a facility or market
    
    
```json
{
      "source": "SecurityPermission",
      "fields": [
        "Uid",
        "ObjectId",
        "ObjectType",
        "RoleId",
        "FacilityId",
        "AllowRole",
        "DenyRole"
      ],
      "sort": [{"ObjectType": "ASC"}],
      "resultsperpage": 10,
      "page": 1
    }
```