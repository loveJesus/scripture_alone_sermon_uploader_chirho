# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import logging
import os
import pocketbase
import sys

from dotenv import load_dotenv
from lib_chirho import command_line_parser_chirho

load_dotenv()

args_chirho = command_line_parser_chirho.parse_args_chirho()

logging.basicConfig(stream=sys.stderr, encoding='utf-8', level=logging.INFO)

SA_POCKETBASE_SERVER_URL_CHIRHO = args_chirho.pocketbase_server_url_chirho or os.getenv(
    "SA_POCKETBASE_SERVER_URL_CHIRHO", "https://staging.api.scripturealone.app")

SA_POCKETBASE_LOGIN_EMAIL_CHIRHO = args_chirho.pocketbase_login_email_chirho or os.getenv(
    "SA_POCKETBASE_LOGIN_EMAIL_CHIRHO", "email.fillme@aleluya")

SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO = args_chirho.pocketbase_login_password_chirho or os.getenv(
    "SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO", "password_fill_me_chirho")

POCKETBASE_CLIENT_CHIRHO = pocketbase.Client(SA_POCKETBASE_SERVER_URL_CHIRHO)
POCKETBASE_CLIENT_CHIRHO.admins.auth_via_email(
            SA_POCKETBASE_LOGIN_EMAIL_CHIRHO,
            SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO)
