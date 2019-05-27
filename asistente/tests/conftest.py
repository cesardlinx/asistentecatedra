from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.middleware import SessionMiddleware


def add_middleware_to_request(request):
    """
    Función para agregar middleware a un request creado con RequestFactory
    """
    # Add session middleware
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()

    # Add messages middleware
    messages = FallbackStorage(request)
    request._messages = messages
    return request
