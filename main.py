from app import create_app
from app.env import SERV_HOST, SERV_PORT

if __name__ == '__main__':
    create_app().run(
        debug=True,
        host=SERV_HOST,
        port=SERV_PORT,
        load_dotenv=True,
    )
