"""
Health check endpoints
"""

from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from typing import Dict, Any
import time
import psutil
import platform

router = APIRouter()

class HealthStatus(BaseModel):
    status: str
    service: str
    version: str
    timestamp: float
    system_info: Dict[str, Any]
    services: Dict[str, str]

@router.get("/", response_model=HealthStatus)
async def health_check():
    """Comprehensive health check endpoint"""
    
    # System information
    system_info = {
        "platform": platform.platform(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent if platform.system() != 'Windows' else psutil.disk_usage('C:\\').percent
    }
    
    # Service status checks
    services = {
        "database": "healthy",  # TODO: Implement actual database check
        "redis": "healthy",     # TODO: Implement actual Redis check
        "zpa_api": "unknown",   # TODO: Implement ZPA API check
        "zia_api": "unknown",   # TODO: Implement ZIA API check
        "zdx_api": "unknown"    # TODO: Implement ZDX API check
    }
    
    return HealthStatus(
        status="healthy",
        service="Zscaler Mission Control Dashboard",
        version="1.0.0",
        timestamp=time.time(),
        system_info=system_info,
        services=services
    )

@router.get("/ready")
async def readiness_check():
    """Kubernetes readiness probe endpoint"""
    # TODO: Check if all required services are ready
    return {"status": "ready"}

@router.get("/live")
async def liveness_check():
    """Kubernetes liveness probe endpoint"""
    return {"status": "alive"}
