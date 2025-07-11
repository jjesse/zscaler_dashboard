# Zscaler Mission Control Dashboard

A comprehensive monitoring and management dashboard for Zscaler Zero Trust services including ZPA (Zero Trust Private Access), ZIA (Zero Trust Internet Access), and ZDX (Digital Employee Experience).

## Overview

The Mission Control dashboard provides real-time visibility and insights across your entire Zscaler environment, leveraging the Zscaler OneAPI to aggregate data from multiple services into a unified view.

## Features

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
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   ZPA API       │    │   ZIA API       │    │   ZDX API       │
│   (Private      │    │   (Internet     │    │   (Digital      │
│    Access)      │    │    Access)      │    │   Experience)   │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                    ┌─────────────▼─────────────┐
                    │   Zscaler OneAPI          │
                    │   Integration Layer       │
                    └─────────────┬─────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │   Mission Control         │
                    │   Dashboard               │
                    │   (Web Interface)         │
                    └───────────────────────────┘
```

## Technology Stack

- **Backend**: Python with FastAPI framework
- **Frontend**: React with TypeScript
- **Data Visualization**: Chart.js / D3.js
- **Real-time Updates**: WebSocket connections
- **Database**: PostgreSQL for data persistence
- **Caching**: Redis for performance optimization
- **Authentication**: OAuth 2.0 integration with Zscaler
- **Deployment**: Docker containers with Kubernetes orchestration

## Quick Start

### Prerequisites

- Python 3.9+
- Node.js 16+
- Docker and Docker Compose
- Zscaler API credentials for ZPA, ZIA, and ZDX

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd zscaler-mission-control
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your Zscaler API credentials
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

### API Configuration

Create a `.env` file with your Zscaler API credentials:

```env
# ZPA Configuration
ZPA_CLIENT_ID=your_zpa_client_id
ZPA_CLIENT_SECRET=your_zpa_client_secret
ZPA_CUSTOMER_ID=your_zpa_customer_id
ZPA_BASE_URL=https://config.private.zscaler.com

# ZIA Configuration
ZIA_USERNAME=your_zia_username
ZIA_PASSWORD=your_zia_password
ZIA_API_KEY=your_zia_api_key
ZIA_CLOUD_NAME=your_zia_cloud

# ZDX Configuration
ZDX_API_KEY=your_zdx_api_key
ZDX_KEY_SECRET=your_zdx_key_secret
ZDX_BASE_URL=https://api.zdxcloud.net

# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/mission_control
REDIS_URL=redis://localhost:6379
```

## API Documentation

The dashboard integrates with multiple Zscaler APIs:

- **ZPA API**: Private application access and connector management
- **ZIA API**: Internet security and traffic analytics
- **ZDX API**: Digital experience monitoring and analytics

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
│   │   └── services/       # Business logic services
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

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security Considerations

- API credentials are stored securely using environment variables
- All API communications use HTTPS/TLS encryption
- Rate limiting is implemented to prevent API abuse
- Authentication tokens are automatically refreshed
- Sensitive data is encrypted at rest

## Monitoring and Alerts

The dashboard includes built-in monitoring capabilities:

- Health checks for all Zscaler services
- Automated alerting for service disruptions
- Performance metrics and SLA tracking
- Custom alert thresholds and notifications

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions, issues, or feature requests, please open an issue in the GitHub repository or contact the development team.

## Roadmap

See [TODO.md](TODO.md) for current development tasks and future enhancements.