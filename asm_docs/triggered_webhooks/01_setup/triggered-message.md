# 3. Creating Triggered Message using Webhook

Navigate to the menu option **Setup / Aiva Credentialing / Triggered Messages.**

On the next screen, click the **New** button. You will also see any existing Triggered Messages in the grid. 

[![2023-01-09_15_18_11-MD-Staff___Setup___Triggered_Messages.png](../images/2023-01-09%2015_18_11-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)](../images/2023-01-09%2015_18_11-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)

The  _New Triggered Message_ window will open. Here you will:

  1. **Name** of your new Triggered Message
  2. The Object Type you're tracking. This dropdown contains all supported Objects. 
  3. Send Type of Webhook Endpoint. 
  4. Select the Webhook Endpoint you configured in the previous step.
  5. Click Save. 

[![2023-01-09_14_34_56-MD-Staff___Setup___Triggered_Messages.png](../images/2023-01-09%2014_34_56-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)](../images/2023-01-09%2014_34_56-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)

After clicking Save, a new window will pre-load. Provide the Effective Date, a small Description(optional), and any Rules that should trigger a Json request body to be sent to the designated Webhook Endpoint.

[![2023-01-09_14_37_35-MD-Staff___Setup___Triggered_Messages.png](../images/2023-01-09%2014_37_35-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)](../images/2023-01-09%2014_37_35-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)

#### Rules

By default there will already be a rule using the **IsNew** field found under the  _Rules_ section. For this example, you can edit this rule to track changes made to an **Address** field found on the provider's  _Address_ page. To do this, click the **pencil** [![mceclip0.png](../images/mceclip0.png)](../images/mceclip0.png) button to the far right of the **IsNew** rule. 

[![2023-01-09_15_20_51-MD-Staff___Setup___Triggered_Messages.png](../images/2023-01-09%2015_20_51-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)](../images/2023-01-09%2015_20_51-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)

The  _New Rule_ window will open up. For this example, we want a Triggered Message to send a Json request body when changes are made to an Address's **Address****** field. To do this, select the field "Address (Address)" under the **Field** drop down menu and set the **Operator** to "Has Changed". Click the **Update Rule** button. 

[![2023-01-09_14_43_19-MD-Staff___Setup___Triggered_Messages.png](../images/2023-01-09%2014_43_19-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)](../images/2023-01-09%2014_43_19-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)

There are a few different options for event tracking:

  * **Has Changed** \- This operator looks for any changes to the chosen **Field**. 
  * **Has Changed To** \- Used when you need Aiva to look for a field changed to a specific value.
  * **Has Value or Changed To** \- Aiva targets updated for a new and specific value. For example, targeting any status that has changed to "Leave of Absence".
  * **Has Value of Changed From** \- Aiva targets updates for the specific value. For example, targeting any status that has changed from "Active".

**Note -** If the field you are adding or changing is a **checkbox **remember that the rule value for that field** MUST be a True or False **operator.

[![2023-01-09_14_46_48-MD-Staff___Setup___Triggered_Messages.png](../images/2023-01-09%2014_46_48-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)](../images/2023-01-09%2014_46_48-MD-Staff%20_%20Setup%20_%20Triggered%20Messages.png)

**Note -**__ If multiple rules are added, they are treated as an "AND" condition, meaning all Rules/Conditions must be met to trigger the response.

When you are satisfied with your new Triggered Message, click on the top left **Save** button.

****Once the Triggered Message rule has been met, the Json request body will only be sent once per unique trigger & object type. **

[](https://support.asm-inc.com/hc/en-us/articles/6527040404891-Triggered-Webhooks#)