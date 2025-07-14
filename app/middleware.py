import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Logger propio para el middleware
logger = logging.getLogger("app.middleware")

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        method = request.method
        path = request.url.path
        logger.info(f"Request: {method} {path}")
        try:
            response = await call_next(request)
        except Exception as exc:
            logger.error(f"Error in {method} {path}: {exc}")
            raise
        process_time = (time.time() - start_time) * 1000
        logger.info(f"Completed {method} {path} in {process_time:.2f}ms")
        return response
