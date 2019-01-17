from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing     # importing apps routing file.

# AuthMiddleware : used for authentication  combination  of  Session, CookieMiddleware
# ProtocoltypeRouter :top level , lets send to one of ASGI appn.
# URLRouter : routes http request of websocket via path.


application = ProtocolTypeRouter({      #
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})