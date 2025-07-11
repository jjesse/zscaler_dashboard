# API Documentation

This document provides detailed information about the Zscaler Mission Control Dashboard API endpoints.

## Base URL

- Development: `http://localhost:8000`
- Production: `https://your-domain.com`

## Authentication

The API uses JWT tokens for authentication. Include the token in the Authorization header:

```
Authorization: Bearer <your-jwt-token>
```

## API Endpoints

### Health Check

#### GET /health
Returns the overall health status of the application and its dependencies.

**Response:**
```json
{
  "status": "healthy",
  "service": "Zscaler Mission Control Dashboard",
  "version": "1.0.0",
  "timestamp": 1641234567.89,
  "system_info": {
    "platform": "Linux-5.4.0",
    "cpu_percent": 15.2,
    "memory_percent": 45.8,
    "disk_usage": 67.3
  },
  "services": {
    "database": "healthy",
    "redis": "healthy",
    "zpa_api": "healthy",
    "zia_api": "healthy",
    "zdx_api": "healthy"
  }
}
```

### ZPA (Zero Trust Private Access)

#### GET /api/v1/zpa/connectors
Returns status information for all ZPA connectors.

#### GET /api/v1/zpa/applications
Returns application access metrics and statistics.

#### GET /api/v1/zpa/analytics
Returns comprehensive ZPA analytics and metrics.

### ZIA (Zero Trust Internet Access)

#### GET /api/v1/zia/traffic
Returns traffic metrics including requests, bandwidth, and categories.

#### GET /api/v1/zia/security
Returns security metrics including threats blocked and policy violations.

#### GET /api/v1/zia/analytics
Returns comprehensive ZIA analytics.

### ZDX (Digital Employee Experience)

#### GET /api/v1/zdx/experience-score
Returns overall digital experience scores.

#### GET /api/v1/zdx/applications
Returns application performance metrics.

#### GET /api/v1/zdx/analytics
Returns comprehensive ZDX analytics.

### Dashboard

#### GET /api/v1/dashboard/overview
Returns dashboard overview with key metrics.

#### GET /api/v1/dashboard/service-status
Returns status of all Zscaler services.

#### GET /api/v1/dashboard/alerts
Returns active alerts and notifications.

## Error Responses

All API endpoints return standard HTTP status codes:

- `200 OK` - Request successful
- `400 Bad Request` - Invalid request parameters
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource not found
- `429 Too Many Requests` - Rate limit exceeded
- `500 Internal Server Error` - Server error

Error response format:
```json
{
  "error": "error_type",
  "message": "Human readable error message",
  "details": "Additional error details",
  "request_id": "unique-request-id"
}
```

## Rate Limiting

API requests are rate-limited to prevent abuse:
- 100 requests per minute per IP address
- Burst size of 10 requests

Rate limit headers are included in responses:
- `X-RateLimit-Limit`: Requests allowed per window
- `X-RateLimit-Remaining`: Requests remaining in current window
- `X-RateLimit-Reset`: Timestamp when rate limit resets

## WebSocket Endpoints

### Real-time Updates

Connect to `ws://localhost:8000/ws` for real-time updates.

Message format:
```json
{
  "type": "update",
  "service": "zpa|zia|zdx",
  "data": { ... }
}
```

## SDK and Libraries

Official SDKs and libraries will be available for:
- Python
- JavaScript/TypeScript
- PowerShell
- Go

## Examples

### Python Example
```python
import requests

# Get dashboard overview
response = requests.get("http://localhost:8000/api/v1/dashboard/overview")
data = response.json()
print(f"Total users: {data['total_users']}")
```

### JavaScript Example
```javascript
// Get ZPA analytics
fetch('http://localhost:8000/api/v1/zpa/analytics')
  .then(response => response.json())
  .then(data => console.log('ZPA Analytics:', data));
```

### PowerShell Example
```powershell
# Get service status
$response = Invoke-RestMethod -Uri "http://localhost:8000/api/v1/dashboard/service-status"
$response | Format-Table
```
