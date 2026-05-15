# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in this collection, please report it by emailing:

**sfulmer@redhat.com**

Please include the following information:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if available)

### What to Expect

- **Response Time**: You will receive an acknowledgment within 48 hours
- **Updates**: You will be updated on the progress every 5 business days
- **Disclosure**: We aim to patch critical vulnerabilities within 30 days
- **Credit**: Security researchers will be credited in the changelog (unless anonymity is requested)

### Security Best Practices

When using this collection:

1. **Authentication**: Always use secure credentials
   - Store credentials in Ansible Vault
   - Use environment variables rather than hardcoding
   - Rotate credentials regularly

2. **SSL/TLS**: Enable certificate validation
   - Set `validate_certs: true` (default)
   - Only disable for testing with self-signed certificates

3. **Network Security**: Restrict API access
   - Use firewalls to limit access to Weka management API
   - Use VPNs or bastion hosts for remote access

4. **Least Privilege**: Use minimal permissions
   - Create dedicated service accounts for automation
   - Grant only required API permissions

5. **Audit Logging**: Enable audit trails
   - Monitor API access logs
   - Track changes made via automation

## Known Security Considerations

1. **Token Storage**: API tokens are held in memory during playbook execution. Ensure playbooks are executed in secure environments.

2. **HTTPS Required**: Always use HTTPS for API communication in production. HTTP should only be used for testing.

3. **Credential Exposure**: Avoid logging API responses that may contain sensitive data. The collection filters sensitive fields, but review custom debug output.

## Security Updates

Security updates will be released as patch versions and documented in the CHANGELOG.md file with a `[SECURITY]` tag.

Subscribe to repository notifications to receive security announcements.
