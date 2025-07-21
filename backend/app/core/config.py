"""
Configuration management for Zscaler Mission Control Dashboard
"""

from pydantic_settings import BaseSettings
from typing import List, Optional
import os


class Settings(BaseSettings):
    """Application settings and configuration"""
    
    # Application Configuration
    APP_NAME: str = "Zscaler Mission Control Dashboard"
    APP_VERSION: str = "1.0.0"
    APP_DEBUG: bool = False
    APP_SECRET_KEY: str
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    APP_CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    
    # Zscaler OneAPI Configuration
    ZSCALER_ONEAPI_BASE_URL: str = "https://api.zscaler.com"
    ZSCALER_ONEAPI_VERSION: str = "v1"
    ZSCALER_CLIENT_ID: str
    ZSCALER_CLIENT_SECRET: str
    ZSCALER_ORGANIZATION_ID: str
    
    # OAuth 2.0 Configuration for OneAPI
    ZSCALER_OAUTH_URL: str = "https://auth.zscaler.com/oauth/token"
    ZSCALER_SCOPE: str = "zpa:read zia:read zdx:read"
    
    # Legacy API Support (Optional fallback)
    ENABLE_LEGACY_API: bool = False
    
    # ZPA Legacy Configuration (if needed)
    ZPA_CLIENT_ID: Optional[str] = None
    ZPA_CLIENT_SECRET: Optional[str] = None
    ZPA_CUSTOMER_ID: Optional[str] = None
    ZPA_BASE_URL: str = "https://config.private.zscaler.com"
    
    # ZIA Legacy Configuration (if needed)
    ZIA_USERNAME: Optional[str] = None
    ZIA_PASSWORD: Optional[str] = None
    ZIA_API_KEY: Optional[str] = None
    ZIA_CLOUD_NAME: Optional[str] = None
    ZIA_BASE_URL: str = "https://admin.{cloud_name}.net"
    
    # ZDX Legacy Configuration (if needed)
    ZDX_API_KEY: Optional[str] = None
    ZDX_KEY_SECRET: Optional[str] = None
    ZDX_BASE_URL: str = "https://api.zdxcloud.net"
    
    # Database Configuration
    DATABASE_URL: str
    DATABASE_POOL_SIZE: int = 10
    DATABASE_MAX_OVERFLOW: int = 20
    DATABASE_ECHO: bool = False
    
    # Redis Configuration
    REDIS_URL: str
    REDIS_PASSWORD: Optional[str] = None
    REDIS_DB: int = 0
    REDIS_MAX_CONNECTIONS: int = 10
    
    # Security Configuration
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # Logging Configuration
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"
    LOG_FILE_PATH: str = "/var/log/mission_control/app.log"
    LOG_MAX_SIZE: str = "10MB"
    LOG_BACKUP_COUNT: int = 5
    
    # Monitoring Configuration
    ENABLE_METRICS: bool = True
    METRICS_PORT: int = 9090
    
    # Alert Configuration
    ALERT_EMAIL_SMTP_SERVER: Optional[str] = None
    ALERT_EMAIL_SMTP_PORT: int = 587
    ALERT_EMAIL_USERNAME: Optional[str] = None
    ALERT_EMAIL_PASSWORD: Optional[str] = None
    ALERT_EMAIL_FROM: Optional[str] = None
    ALERT_EMAIL_TO: Optional[str] = None
    
    # Rate Limiting
    RATE_LIMIT_REQUESTS_PER_MINUTE: int = 100
    RATE_LIMIT_BURST_SIZE: int = 10
    
    # WebSocket Configuration
    WEBSOCKET_ENABLED: bool = True
    WEBSOCKET_PING_INTERVAL: int = 30
    WEBSOCKET_PING_TIMEOUT: int = 10
    
    # Development Configuration
    DEVELOPMENT_MODE: bool = False
    HOT_RELOAD: bool = False
    API_DOCS_ENABLED: bool = True
    
    # External Services
    SLACK_WEBHOOK_URL: Optional[str] = None
    TEAMS_WEBHOOK_URL: Optional[str] = None
    SERVICENOW_INSTANCE_URL: Optional[str] = None
    SERVICENOW_USERNAME: Optional[str] = None
    SERVICENOW_PASSWORD: Optional[str] = None
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
    
    @property
    def oneapi_url(self) -> str:
        """Complete Zscaler OneAPI URL"""
        return f"{self.ZSCALER_ONEAPI_BASE_URL}/{self.ZSCALER_ONEAPI_VERSION}"
    
    @property
    def oneapi_zpa_url(self) -> str:
        """OneAPI ZPA endpoint"""
        return f"{self.oneapi_url}/zpa"
    
    @property
    def oneapi_zia_url(self) -> str:
        """OneAPI ZIA endpoint"""
        return f"{self.oneapi_url}/zia"
    
    @property
    def oneapi_zdx_url(self) -> str:
        """OneAPI ZDX endpoint"""
        return f"{self.oneapi_url}/zdx"


# Create global settings instance
settings = Settings()
