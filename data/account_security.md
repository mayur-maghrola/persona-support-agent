# Account Security

## Multi-Factor Authentication (MFA)
- Enable MFA from Account > Security > Multi-Factor Authentication.
- Supported methods: Authenticator app (TOTP), SMS, and hardware security keys (FIDO2).
- MFA is mandatory for admin accounts.

## Login Activity
- Review recent login history at Account > Security > Login Activity.
- Suspicious sessions can be terminated immediately from this page.
- Alerts are sent for logins from new devices or locations.

## Password Best Practices
- Use a unique, strong password (12+ characters recommended).
- Change your password every 90 days.
- Never share your password or store it in plain text.

## API Key Security
- Rotate API keys regularly from Account > API Keys.
- Never expose API keys in client-side code or public repositories.
- Use environment variables or secret managers (e.g., AWS Secrets Manager).

## Phishing & Social Engineering
- We will never ask for your password via email or chat.
- Verify email sender addresses before clicking any links.
- Report suspicious emails to security@example.com.

## Account Recovery
- Add a backup email and phone number in Account > Security > Recovery Options.
- Store MFA backup codes in a safe location.

## Data Encryption
- All data is encrypted at rest (AES-256) and in transit (TLS 1.3).
- End-to-end encryption is available on Enterprise plans.
