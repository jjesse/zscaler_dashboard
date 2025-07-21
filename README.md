# Zscaler Mission Control Dashboard

A comprehensive monitoring and management dashboard for Zscaler Zero Trust services including ZPA (Zero Trust Private Access), ZIA (Zero Trust Internet Access), and ZDX (Digital Employee Experience), leveraging the **Zscaler OneAPI** for unified data access.

## Overview

The Mission Control dashboard provides real-time visibility and insights across your entire Zscaler environment, utilizing the **Zscaler OneAPI** to aggregate data from multiple services into a unified view. This modern approach replaces the need for separate API integrations and provides a streamlined, consistent interface.

## Features

### Unified OneAPI Integration
- **Single Authentication**: OAuth 2.0 authentication for all Zscaler services
- **Consistent Data Models**: Standardized data formats across ZPA, ZIA, and ZDX
- **Simplified Integration**: One API client for all Zscaler services
- **Real-time Data**: Unified real-time data streaming from all services
- **Enhanced Security**: Modern OAuth 2.0 with scope-based access control

### ZPA (Zero Trust Private Access) Monitoring
- Application connector status and health
- Active user sessions and connections
- Application access policies and rules
- Connector group performance metrics
- Real-time threat detection and blocking

### ZIA (Zero Trust Internet Access) Monitoring
- Internet traffic analytics and trends
- Security policy enforcement status
- Malware and threat detection rates
- Bandwidth utilization and performance
- User activity and web categorization

### ZDX (Digital Employee Experience) Monitoring
- End-user experience scores and metrics
- Application performance monitoring
- Network path analysis and optimization
- Device health and compliance status
- Proactive issue identification and alerts

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  Zscaler OneAPI                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   ZPA API   │  │   ZIA API   │  │   ZDX API   │        │
│  │  (Private   │  │ (Internet   │  │  (Digital   │        │
│  │   Access)   │  │   Access)   │  │Experience)  │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────┬───────────────────────────────────────┘
                      │ OAuth 2.0 Authentication
          ┌───────────▼───────────┐
          │   Mission Control     │
          │   OneAPI Client       │
          └───────────┬───────────┘
                      │
          ┌───────────▼───────────┐
          │   Mission Control     │
          │   Dashboard           │
          │   (Web Interface)     │
          └───────────────────────┘
```

## Technology Stack

- **Backend**: Python with FastAPI framework
- **API Integration**: Zscaler OneAPI with OAuth 2.0
- **Frontend**: React with TypeScript
- **Data Visualization**: Chart.js / D3.js
- **Real-time Updates**: WebSocket connections
- **Database**: PostgreSQL for data persistence
- **Caching**: Redis for performance optimization
- **Authentication**: OAuth 2.0 integration with Zscaler OneAPI
- **Deployment**: Docker containers with Kubernetes orchestration

## Quick Start

### Prerequisites

- Python 3.9+
- Node.js 16+
- Docker and Docker Compose
- **Zscaler OneAPI credentials** (Client ID, Client Secret, Organization ID)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd zscaler-mission-control
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your Zscaler OneAPI credentials
```

3. Install dependencies:
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd ../frontend
npm install
```

4. Run with Docker Compose:
```bash
docker-compose up -d
```

## Configuration

### OneAPI Configuration

Create a `.env` file with your Zscaler OneAPI credentials:

```env
# Zscaler OneAPI Configuration
ZSCALER_ONEAPI_BASE_URL=https://api.zscaler.com
ZSCALER_CLIENT_ID=your_oneapi_client_id
ZSCALER_CLIENT_SECRET=your_oneapi_client_secret
ZSCALER_ORGANIZATION_ID=your_organization_id
ZSCALER_OAUTH_URL=https://auth.zscaler.com/oauth/token
ZSCALER_SCOPE=zpa:read zia:read zdx:read

# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/mission_control
REDIS_URL=redis://localhost:6379

# Legacy API Support (Optional)
ENABLE_LEGACY_API=false
```

## API Documentation

The dashboard integrates with the **Zscaler OneAPI**, providing:

- **Unified Authentication**: Single OAuth 2.0 flow for all services
- **Consistent Data Models**: Standardized response formats
- **Comprehensive Coverage**: Full access to ZPA, ZIA, and ZDX data
- **Real-time Capabilities**: WebSocket support for live updates

### OneAPI Benefits

1. **Simplified Integration**: One client, one authentication method
2. **Better Performance**: Optimized data delivery and caching
3. **Enhanced Security**: Modern OAuth 2.0 with granular scopes
4. **Future-Proof**: Built for Zscaler's evolving platform
5. **Consistent Experience**: Unified data models across services

Detailed API documentation is available in the `/docs` directory.

## Development

### Project Structure

```
zscaler-mission-control/
├── backend/                 # Python FastAPI backend
│   ├── app/
│   │   ├── api/            # API route definitions
│   │   ├── core/           # Core application logic
│   │   ├── models/         # Database models
│   │   ├── services/       # Business logic services
│   │   │   └── oneapi_client.py  # Zscaler OneAPI client
│   │   └── utils/          # Utility functions
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/               # React TypeScript frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── services/       # API service calls
│   │   ├── types/          # TypeScript type definitions
│   │   └── utils/          # Utility functions
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── docs/                   # Documentation
```

### Running in Development Mode

```bash
# Start backend
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Start frontend
cd frontend
npm start
```

## Migration from Legacy APIs

If you're currently using separate ZPA, ZIA, and ZDX APIs, this dashboard provides a migration path:

1. **Enable Legacy Support**: Set `ENABLE_LEGACY_API=true` in your `.env`
2. **Gradual Migration**: Run both OneAPI and legacy APIs in parallel
3. **Data Validation**: Compare results between OneAPI and legacy APIs
4. **Full Cutover**: Disable legacy APIs once validation is complete

## Security Considerations

- **OAuth 2.0**: Modern authentication with scope-based access control
- **Token Management**: Automatic token refresh and secure storage
- **Secure Communication**: All API communications use HTTPS/TLS encryption
- **Rate Limiting**: Built-in protection against API abuse
- **Audit Logging**: Comprehensive logging of all API interactions

## Monitoring and Alerts

The dashboard includes built-in monitoring capabilities:

- Health checks for OneAPI connectivity
- Automated alerting for service disruptions
- Performance metrics and SLA tracking
- Custom alert thresholds and notifications
- Real-time status monitoring across all services

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions, issues, or feature requests, please open an issue in the GitHub repository or contact the development team.

## Roadmap

See [TODO.md](TODO.md) for current development tasks and future enhancements.

---

**Note**: This dashboard is designed for the **Zscaler OneAPI**. For legacy API support, please refer to the migration documentation.