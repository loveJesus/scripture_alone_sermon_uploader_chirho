#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import logging
import os
import pocketbase
import re
import sys

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(stream=sys.stderr, encoding='utf-8', level=logging.INFO)
logger_chirho = logging.getLogger(__name__)


class ScriptDatabaseChirho:
    """
    Hallelujah, make a singleton type connection to the pocketbase database.
    """
    SA_POCKETBASE_SERVER_URL_CHIRHO = os.getenv(
        "SA_POCKETBASE_SERVER_URL_CHIRHO", "https://staging.api.scripturealone.app")

    SA_POCKETBASE_LOGIN_EMAIL_CHIRHO = os.getenv(
        "SA_POCKETBASE_LOGIN_EMAIL_CHIRHO", "email.fillme@aleluya")

    SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO = os.getenv(
        "SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO", "password_fill_me_chirho")

    POCKETBASE_CLIENT_CHIRHO = pocketbase.Client(SA_POCKETBASE_SERVER_URL_CHIRHO)
    POCKETBASE_CLIENT_CHIRHO.admins.auth_via_email(
        SA_POCKETBASE_LOGIN_EMAIL_CHIRHO,
        SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO)

    logger_chirho.info("SA_POCKETBASE_SERVER_URL_CHIRHO: %s", SA_POCKETBASE_SERVER_URL_CHIRHO)

    @classmethod
    def get_client_chirho(cls) -> pocketbase.Client:
        return cls.POCKETBASE_CLIENT_CHIRHO


def list_sermons_chirho():
    pass


def deletedups_chirho():
    logger_chirho.info("------------------------------------------------------------------")
    find_titles_chirho = [
        "Arm Yourselves", "Ask What You Will", "Barabbas", "Christ Liveth In Me", "Contending For The Faith",
        "Dads That Made a Difference", "Dealing With Bitterness and Worry", "Doing By The Will Of God",
        "It's Natural To Pray", "Living In The Will Of God", "Our Hiding Place", "Planting The Seed",
        "Prevailing Prayer", "The Everlasting Gospel - Part 27", "The False Prophet - Part 26",
        "The Fruits Of A Christian", "The Greatest Sin In The Bible", "The Name Of Jesus",
        "The Rise Of The Antichrist(1) - Part 24", "The Rise Of The Antichrist(2) - Part 25", "The Shepherd",
        "The Vial Judgments - Part 29", "The Woman Riding The Beast - Part 30", "Uncomfortable Faith",
        "Walking Worthy For The Lord", "We Need Revival", "Why We Celebrate Christmas"]
    client_chirho = ScriptDatabaseChirho.get_client_chirho()
    for page_chirho in range(10):
        sermon_list_chirho = client_chirho.records.get_list("sermons", page_chirho + 1, 100)
        for count_chirho, sermon_chirho in enumerate(sermon_list_chirho.items):
            if sermon_chirho.title in find_titles_chirho:
                print("Aleluya deleting %s | %s" % (sermon_chirho.title, sermon_chirho.id))
                client_chirho.records.delete("sermons", sermon_chirho.id)


def showdups_chirho():
    find_titles_chirho = [
        "Arm Yourselves", "Ask What You Will", "Barabbas", "Christ Liveth In Me", "Contending For The Faith",
        "Dads That Made a Difference", "Dealing With Bitterness and Worry", "Doing By The Will Of God",
        "It's Natural To Pray", "Living In The Will Of God", "Our Hiding Place", "Planting The Seed",
        "Prevailing Prayer", "The Everlasting Gospel - Part 27", "The False Prophet - Part 26",
        "The Fruits Of A Christian", "The Greatest Sin In The Bible", "The Name Of Jesus",
        "The Rise Of The Antichrist(1) - Part 24", "The Rise Of The Antichrist(2) - Part 25", "The Shepherd",
        "The Vial Judgments - Part 29", "The Woman Riding The Beast - Part 30", "Uncomfortable Faith",
        "Walking Worthy For The Lord", "We Need Revival", "Why We Celebrate Christmas"]
    client_chirho = ScriptDatabaseChirho.get_client_chirho()
    for page_chirho in range(10):
        sermon_list_chirho = client_chirho.records.get_list("sermons", page_chirho + 1, 100)
        for count_chirho, sermon_chirho in enumerate(sermon_list_chirho.items):
            if sermon_chirho.title in find_titles_chirho:
                re_chirho = re.compile(r'[0-9]+\.mp3')
                id_chirho = re_chirho.findall(sermon_chirho.external_audio_file_url)[0].split('.')[0]
                print(f"https://www.sermonaudio.com/sermoninfo.asp?SID={id_chirho}")


def main_chirho():
    logger_chirho.info("------------------------------------------------------------------")
    deletedups_chirho()


if __name__ == "__main__":
    main_chirho()
