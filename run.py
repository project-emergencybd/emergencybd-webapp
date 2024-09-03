from app import create_webapp

from dotenv import load_dotenv

from os import getenv

load_dotenv(".env")

app = create_webapp(
    app_key=f'{getenv('APP_KEY')}', database_uri=f'{getenv("DATABASE_URI")}'
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
