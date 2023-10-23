import os

from dotenv import load_dotenv
# -----------------------
# DB_NAME = <Paste your database name here>
# DB_USER = <Paste your user name here>
# DB_PASSWORD = <Paste your password here>
# -----------------------
# Then you should be able to run the project.
load_dotenv()
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
