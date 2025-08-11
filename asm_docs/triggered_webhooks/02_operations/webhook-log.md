# 5. Enabling the Webhook Log

The Webhook log is disabled by default. To enable logging all Webhook Json body requests sent by your Webhook endpoints. Please note you Webhook Log can be enabled for specific Facilities/Markets or globally.

Log into MD-Staff and navigate to Setup > Application Settings > App Settings and add a new App Setting. The name should be **WebhookLogEnabled** and the setting value should be set to **True**. 

[![2023-05-26_08_26_09-Window.png](../images/2023-05-26%2008_26_09-Window.png)](../images/2023-05-26%2008_26_09-Window.png)

If you want to extract data from the Webhook Log, you can use the [Query](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint) endpoint and target the source of **WebhookLog**. 

[![2023-05-26_08_28_57-Window.png](../images/2023-05-26%2008_28_57-Window.png)](../images/2023-05-26%2008_28_57-Window.png)

[](https://support.asm-inc.com/hc/en-us/articles/6527040404891-Triggered-Webhooks#)