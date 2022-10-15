# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life

import argparse


def parse_args_chirho():
    """
    God be praised, set up argparser to work with -h, as well as parse the command line arguments.
    These will overwrite the environment variables.
    :return: the parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='Scripture Alone Sermon Uploader. Give a Sermon Audio URL and post its details to the Scripture Alone Backend.')
    parser.add_argument(
        "-a", "--sermon_audio_url_chirho",
        help="The URL of the PocketBase server to use, or set environment variable SA_POCKETBASE_SERVER_URL_CHIRHO",
        required=True)
    parser.add_argument(
        "-u", "--pocketbase_server_url_chirho",
        help="The URL of the PocketBase server to use, or set environment variable SA_POCKETBASE_SERVER_URL_CHIRHO",
        default="https://staging.api.scripturealone.app")
    parser.add_argument(
        "-e", "--pocketbase_login_email_chirho",
        help="The email address to use to log into the PocketBase server, or set environment variable SA_POCKETBASE_LOGIN_EMAIL_CHIRHO")
    parser.add_argument(
        "-p", "--pocketbase_login_password_chirho",
        help="The password to use to log into the PocketBase server, or set environment variable SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO")
    return parser.parse_args()