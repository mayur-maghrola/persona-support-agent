# Outage Resolution

## Identifying an Outage
- Check the [status page](https://status.example.com) for real-time service status.
- Subscribe to status updates via email or SMS on the status page.
- Outages are classified as: Degraded Performance, Partial Outage, Full Outage.

## During an Outage

### What We Do
1. On-call engineer is paged within 5 minutes of alert trigger.
2. Incident channel opened in Slack (#incidents).
3. Initial status page update posted within 15 minutes.
4. Root cause investigation begins immediately.
5. Status updates are posted every 30 minutes until resolution.

### What You Can Do
- Monitor the status page for live updates.
- Avoid repeatedly retrying failed requests (use exponential backoff).
- Check your application logs for specific error codes to share with support.

## After an Outage

### Post-Incident Report (PIR)
- A detailed PIR is published within 48 hours of resolution.
- Reports include: timeline, root cause, impact summary, and corrective actions.
- Available at [status.example.com/history](https://status.example.com/history).

### SLA Credits
- If the outage breaches our SLA (99.9% uptime), you are eligible for service credits.
- Credits are calculated based on downtime duration and applied automatically to your next invoice.
- Review the SLA terms in your subscription agreement.

## Contacting Support During an Outage
- Enterprise customers: Use the dedicated priority support line.
- All others: Email support@example.com with subject "Outage Impact - [Your Account ID]".
- Include error messages, affected features, and business impact in your report.
