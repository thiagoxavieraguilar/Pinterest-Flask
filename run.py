from Pinterest import app
from asgiref.wsgi import WsgiToAsgi
import uvicorn

if __name__ == "__main__":
    asgi_app = WsgiToAsgi(app)
    uvicorn.run(asgi_app, host='0.0.0.0', port=8080)