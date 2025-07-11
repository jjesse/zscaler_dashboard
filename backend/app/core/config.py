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
    
    # ZPA Configuration
    ZPA_CLIENT_ID: str
    ZPA_CLIENT_SECRET: str
    ZPA_CUSTOMER_ID: str
    ZPA_BASE_URL: str = "https://config.private.zscaler.com"
    ZPA_API_VERSION: str = "v1"
    
    # ZIA Configuration
    ZIA_USERNAME: str
    ZIA_PASSWORD: str
    ZIA_API_KEY: str
    ZIA_CLOUD_NAME: str
    ZIA_BASE_URL: str = "https://admin.{cloud_name}.net"
    ZIA_API_VERSION: str = "v1"
    
    # ZDX Configuration
    ZDX_API_KEY: str
    ZDX_KEY_SECRET: str
    ZDX_BASE_URL: str = "https://api.zdxcloud.net"
    ZDX_API_VERSION: str = "v1"
    
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
    def zia_formatted_base_url(self) -> str:
        """Format ZIA base URL with cloud name"""
        return self.ZIA_BASE_URL.format(cloud_name=self.ZIA_CLOUD_NAME)
    
    @property
    def zpa_api_url(self) -> str:
        """Complete ZPA API URL"""
        return f"{self.ZPA_BASE_URL}/mgmtconfig/{self.ZPA_API_VERSION}"
    
    @property
    def zia_api_url(self) -> str:
        """Complete ZIA API URL"""
        return f"{self.zia_formatted_base_url}/api/{self.ZIA_API_VERSION}"
    
    @property
    def zdx_api_url(self) -> str:
        """Complete ZDX API URL"""
        return f"{self.ZDX_BASE_URL}/{self.ZDX_API_VERSION}"


# Create global settings instance
settings = Settings()
