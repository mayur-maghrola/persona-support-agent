# API Troubleshooting Guide

## Common API Errors

### 401 Unauthorized
- Verify your API key is valid and not expired
- Ensure the `Authorization` header is correctly formatted: `Bearer <token>`
- Check if your API key has the required scopes/permissions

### 403 Forbidden
- Your account may lack permissions for this endpoint
- Contact your admin to grant the necessary roles

### 429 Too Many Requests
- You have exceeded the rate limit
- Implement exponential backoff and retry logic
- Review your plan's rate limits in the dashboard

### 500 Internal Server Error
- Retry the request after a short delay
- Check the [status page](https://status.example.com) for ongoing incidents

## Authentication Methods
- **API Key**: Pass via `x-api-key` header
- **OAuth 2.0**: Use the `/oauth/token` endpoint to obtain a bearer token
- **JWT**: Tokens expire after 1 hour; refresh using the `/auth/refresh` endpoint

## Debugging Tips
1. Enable verbose logging in your SDK
2. Log full request/response headers
3. Use tools like Postman or curl to isolate issues
4. Check SDK version compatibility with the API version
