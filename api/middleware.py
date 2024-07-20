
import logging
import time
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class LogRequestMiddleware(MiddlewareMixin):
    """
    Промежуточное программное обеспечение,
    которое регистрирует каждый запрос и его продолжительность.
    """
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        duration = time.time() - request.start_time
        logger.info(
            f"Request: {request.method} {request.path} "
            f"Params: {request.GET} Duration: {duration:.2f}s "
            f"Response status: {response.status_code}"
        )
        return response
