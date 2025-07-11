"""
API Router for Zscaler Mission Control Dashboard
"""

from fastapi import APIRouter
from app.api.endpoints import health, zpa, zia, zdx, dashboard

# Create main API router
api_router = APIRouter()

# Include endpoint routers
api_router.include_router(
    health.router,
    prefix="/health",
    tags=["Health Check"]
)

api_router.include_router(
    zpa.router,
    prefix="/zpa",
    tags=["ZPA - Zero Trust Private Access"]
)

api_router.include_router(
    zia.router,
    prefix="/zia",
    tags=["ZIA - Zero Trust Internet Access"]
)

api_router.include_router(
    zdx.router,
    prefix="/zdx",
    tags=["ZDX - Digital Employee Experience"]
)

api_router.include_router(
    dashboard.router,
    prefix="/dashboard",
    tags=["Dashboard"]
)
