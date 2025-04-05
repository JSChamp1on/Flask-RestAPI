from gevent.pywsgi import WSGIServer

from app import create_app
from app.config import SERV_HOST, SERV_PORT, NODE_ENV, ENV_DEVl, ENV_PROD


if __name__ == '__main__':
    app = create_app()

    if NODE_ENV == ENV_DEVl:
        app.run(
            debug=True,
            host=SERV_HOST,
            port=SERV_PORT,
        )

    if NODE_ENV == ENV_PROD:
        svr = WSGIServer(
            (SERV_HOST, int(SERV_PORT)),
            app,
        )
        svr.serve_forever()
