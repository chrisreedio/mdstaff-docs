# 6. Troubleshooting

**Scenario 1:** The Triggered Message rule(s) you configured isn't sending Json request bodies from MD-Staff to your Webhook endpoint.

  * It would be recommended to use a tool like ngrok, RequestBin or webhook.site to eliminate the possibility that your Webhook endpoint is blocking the request or your endpoint has configuration issues. These tools will supply public facing endpoints that will listen/accept any JSON payloads sent to it. We highly recommend **against** sending payloads containing sensitive information. Only consider using these tools as a way to test your webhook payloads or troubleshooting potential connection/network issues with your Webhook Endpoints.

**Scenario 2:** Triggered Messages are failing/erroring when triggered.

  * You can obtain data from the Webhook Error Log by using the [Query](https://support.asm-inc.com/hc/en-us/articles/360049346594-Query-Endpoint) endpoint and targeting the source of **WebhookErrorLogData**.
  * By obtaining the errored messages, you can see what attempted to be sent and incorporate retry logic to resend the message if necessary.

If you're still having issues, please email [integrations.api@mdstaff.com](mailto:integrations.api@mdstaff.com&subject=ASM:%20Web%20API%20inquiry) to receive assistance.