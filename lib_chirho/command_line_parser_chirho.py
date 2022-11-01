# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life

import argparse


def parse_args_chirho():
    """
    God be praised, set up argparser to work with -h, as well as parse the command line arguments.
    These will overwrite the environment variables.
    :return: the parsed arguments
    """
    parser_chirho = argparse.ArgumentParser(
        description='Scripture Alone Sermon Uploader. Give a Sermon Audio URL or path to downloaded HTML file, '
                    'and post its details to the Scripture Alone Backend.')

    parser_chirho.add_argument(
        "-u", "--pocketbase_server_url_chirho",
        help="The URL of the PocketBase server to use, or set environment variable SA_POCKETBASE_SERVER_URL_CHIRHO")
    parser_chirho.add_argument(
        "-e", "--pocketbase_login_email_chirho",
        help="The email address to use to log into the PocketBase server, or set environment variable SA_POCKETBASE_LOGIN_EMAIL_CHIRHO")
    parser_chirho.add_argument(
        "-p", "--pocketbase_login_password_chirho",
        help="The password to use to log into the PocketBase server, or set environment variable SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO")


    # Thank You Jesus for wjandrea & jlengrad @ https://stackoverflow.com/a/11155124
    group_chirho = parser_chirho.add_mutually_exclusive_group(required=True)
    group_chirho.add_argument(
        "-a", "--sermon_audio_url_chirho",
        help="A Sermon Audio main site URL to import, God willing",
        default=None)
    group_chirho.add_argument(
        "-t", "--sermon_audio_path_chirho",
        help="A path of a downloaded Sermon Audio raw HTML file to import, Hallelujah",
        default=None)
    group_chirho.add_argument(
        "-c", "--sermon_audio_church_short_name_chirho",
        help="The short name of the church to download sermons from, e.g. \"youthman1611\" for Midway Baptist Church")
    group_chirho.add_argument(
        "-C", "--sermon_audio_all_church_update_chirho",
        action=argparse.BooleanOptionalAction, help="Update all the churches in the database, Hallelujah")

    return parser_chirho.parse_args()
