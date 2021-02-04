import os
from dotenv import load_dotenv
from src.app import create_app

load_dotenv('.env')

env = os.getenv('FLASK_ENV')
port = os.getenv('PORT')

app = create_app(env)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
