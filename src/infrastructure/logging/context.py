import contextvars
import uuid

request_id_var: contextvars.ContextVar[str] = contextvars.ContextVar(
    "request_id", default="SYSTEM-" + str(uuid.uuid4())[:8]
)
