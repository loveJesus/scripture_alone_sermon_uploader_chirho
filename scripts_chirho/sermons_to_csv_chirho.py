#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import json
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


def parse_json2_for_author_sermon_audio_urls_chirho():
    with open('sermon_audio_author_matcher_v2_chirho.json', 'r') as infile_chirho:
        dict_chirho = json.load(infile_chirho)

    for author_chirho in dict_chirho.values():
        name_chirho = f"{author_chirho['first_name_chirho']} {author_chirho['last_name_chirho']}"
        try:
            churches_chirho = set()
            for sermon_chirho in author_chirho['sermons_chirho']:
                churches_chirho.add(sermon_chirho['church_chirho'])
            first_sermon_chirho = author_chirho['sermons_chirho'][0]
            sermon_audio_url_chirho = f"https://www.sermonaudio.com/sermoninfo.asp?SID={first_sermon_chirho['sermon_audio_id_chirho']}"

            print(f"☧ {name_chirho} #churches: {len(churches_chirho)} #sermons: {len(author_chirho['sermons_chirho'])} url: {sermon_audio_url_chirho}")
        except IndexError as e_chirho:
            print(f"author_chirho: {name_chirho} likely has no sermons_chirho")


def parse_json_for_author_sermon_audio_urls_chirho():
    with open('sermon_audio_author_matcher_chirho.json', 'r') as infile_chirho:
        dict_chirho = json.load(infile_chirho)

    sermons_chirho = {
        sermon_chirho["id_chirho"]: sermon_chirho
        for sermon_chirho in dict_chirho["sermons"]
    }
    authors_chirho = {
        author_chirho["id_chirho"]: author_chirho
        for author_chirho in dict_chirho["authors"]
    }
    for author_chirho in authors_chirho.values():
        author_chirho["sermons_chirho"] = []

    for sermon_chirho in sermons_chirho.values():
        try:
            authors_chirho[sermon_chirho["author_chirho"]]["sermons_chirho"].append(sermon_chirho)
        except KeyError:
            logger_chirho.warning("Hallelujah Sermon %s has an unknown author %s", sermon_chirho["id_chirho"], sermon_chirho["author_chirho"])
            continue

    with open('sermon_audio_author_matcher_v2_chirho.json', 'w') as outfile_chirho:
        json.dump(authors_chirho, outfile_chirho, indent=2)


def make_json_for_author_sermon_audio_urls_chirho():
    client_chirho = ScriptDatabaseChirho.get_client_chirho()
    re_chirho = re.compile(r'[0-9]+\.mp3')

    sermons_chirho = []
    authors_chirho = []

    for page_chirho in range(8):  # 8
        author_list_chirho = client_chirho.records.get_list("authors", page_chirho + 1, 100)
        for count_chirho, author_chirho in enumerate(author_list_chirho.items):
            author_dict_chirho = {
                "id_chirho": author_chirho.id,
                "first_name_chirho": author_chirho.first_name,
                "last_name_chirho": author_chirho.last_name,
                "church_chirho": author_chirho.church,}
            authors_chirho.append(author_dict_chirho)
            print(f"{author_chirho.id}|{author_chirho.first_name}|{author_chirho.last_name}|{author_chirho.church}")

    for page_chirho in range(137):  # 137
        sermon_list_chirho = client_chirho.records.get_list("sermons", page_chirho + 1, 100)
        for count_chirho, sermon_chirho in enumerate(sermon_list_chirho.items):
            try:
                sa_id_chirho = re_chirho.findall(sermon_chirho.external_audio_file_url)[0].split('.')[0]
                sermon_dict_chirho = {
                    "id_chirho": sermon_chirho.id,
                    "title_chirho": sermon_chirho.title,
                    "author_chirho": sermon_chirho.author,
                    "church_chirho": sermon_chirho.church,
                    "sermon_audio_id_chirho": sa_id_chirho,}
                sermons_chirho.append(sermon_dict_chirho)
                sa_id_chirho = re_chirho.findall(sermon_chirho.external_audio_file_url)[0].split('.')[0]
                print(f"{sermon_chirho.id}:{sa_id_chirho}:{sermon_chirho.author}:{sermon_chirho.church}")
            except Exception as e_chirho:
                pass

    final_dict_chirho = {
        "sermons": sermons_chirho,
        "authors": authors_chirho,}

    with open('sermon_audio_author_matcher_chirho.json', 'w') as outfile_chirho:
        json.dump(final_dict_chirho, outfile_chirho, indent=4)

    print("Done - HALLELUJAH")


def main_chirho():
    logger_chirho.info("------------------------------------------------------------------")
    parse_json2_for_author_sermon_audio_urls_chirho()


if __name__ == "__main__":
    main_chirho()
