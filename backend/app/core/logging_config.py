"""
Logging configuration for Zscaler Mission Control Dashboard
"""

import logging
import logging.handlers
import sys
import structlog
from pathlib import Path
from app.core.config import settings


def setup_logging():
    """Configure application logging"""
    
    # Create log directory if it doesn't exist
    log_file_path = Path(settings.LOG_FILE_PATH)
    log_file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Configure standard library logging
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.handlers.RotatingFileHandler(
                settings.LOG_FILE_PATH,
                maxBytes=10*1024*1024,  # 10MB
                backupCount=settings.LOG_BACKUP_COUNT
            )
        ]
    )
    
    # Configure structlog
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.dev.ConsoleRenderer() if settings.LOG_FORMAT == "console" else structlog.processors.JSONRenderer()
        ],
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, settings.LOG_LEVEL.upper())
        ),
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )
