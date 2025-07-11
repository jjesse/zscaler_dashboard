"""
Zscaler Mission Control Dashboard - Main Application Entry Point
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import uvicorn
import logging
import time

from app.core.config import settings
from app.core.logging_config import setup_logging
from app.api.router import api_router

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager for startup and shutdown events
    """
    # Startup
    logger.info("🚀 Starting Zscaler Mission Control Dashboard")
    logger.info(f"Version: {settings.APP_VERSION}")
    logger.info(f"Environment: {'Development' if settings.APP_DEBUG else 'Production'}")
    
    # Initialize database connections, Redis, etc.
    # await init_database()
    # await init_redis()
    
    yield
    
    # Shutdown
    logger.info("🛑 Shutting down Zscaler Mission Control Dashboard")
    # Clean up resources
    # await close_database()
    # await close_redis()


# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="A comprehensive monitoring and management dashboard for Zscaler Zero Trust services",
    version=settings.APP_VERSION,
    docs_url="/docs" if settings.API_DOCS_ENABLED else None,
    redoc_url="/redoc" if settings.API_DOCS_ENABLED else None,
    openapi_url="/openapi.json" if settings.API_DOCS_ENABLED else None,
    lifespan=lifespan
)

# Add security middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"] if settings.APP_DEBUG else ["localhost", "127.0.0.1"]
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.APP_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add request timing middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Add response time header to all requests"""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    
    # Log request
    logger.info(
        f"{request.method} {request.url.path} - "
        f"Status: {response.status_code} - "
        f"Time: {process_time:.4f}s"
    )
    
    return response

# Include API routes
app.include_router(api_router, prefix="/api/v1")

# Health check endpoint
@app.get("/health", include_in_schema=False)
async def health_check():
    """Health check endpoint for load balancers and monitoring"""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "service": "Zscaler Mission Control Dashboard",
            "version": settings.APP_VERSION,
            "timestamp": time.time()
        }
    )

# Root endpoint
@app.get("/", include_in_schema=False)
async def root():
    """Root endpoint with basic application information"""
    return JSONResponse(
        content={
            "message": "Zscaler Mission Control Dashboard API",
            "version": settings.APP_VERSION,
            "docs": "/docs" if settings.API_DOCS_ENABLED else "Documentation disabled",
            "health": "/health"
        }
    )

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler for unhandled errors"""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": "An unexpected error occurred",
            "request_id": getattr(request.state, "request_id", "unknown")
        }
    )


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.APP_DEBUG,
        log_level="debug" if settings.APP_DEBUG else "info"
    )
