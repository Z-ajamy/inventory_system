import logging
import time
from typing import Any, Protocol

class UseCaseProtocol(Protocol):
    def execute(self, request: Any) -> Any: ...

class LoggingUseCaseDecorator:
    def __init__(self, use_case: UseCaseProtocol):
        self._use_case = use_case
        self._logger = logging.getLogger(use_case.__class__.__name__)

    def execute(self, request: Any) -> Any:
        start_time = time.perf_counter()
        
        request_data = request.__dict__ if hasattr(request, "__dict__") else str(request)
        
        self._logger.info(
            "Executing UseCase", 
            extra={"context": {"payload": request_data}}
        )

        try:
            result = self._use_case.execute(request)
            
            execution_time = round((time.perf_counter() - start_time) * 1000, 2)
            self._logger.info(
                "UseCase executed successfully", 
                extra={"context": {"execution_time_ms": execution_time}}
            )
            return result
            
        except Exception as e:
            self._logger.error(
                "UseCase execution failed", 
                exc_info=True, 
                extra={"context": {"error_type": type(e).__name__}}
            )
            raise
