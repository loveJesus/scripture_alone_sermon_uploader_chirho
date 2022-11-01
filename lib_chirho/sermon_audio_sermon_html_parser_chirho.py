# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import logging
import re
from typing import Optional

import requests

from bs4 import BeautifulSoup

from lib_chirho.models_chirho.author_chirho import AuthorChirho
from lib_chirho.models_chirho.sermon_chirho import SermonChirho

logger_chirho = logging.getLogger(__name__)


class SermonAudioSermonHtmlParserChirho:
    """
    Hallelujah, class that will parse a sermon audio URL and create the relevant Scripture Alone Database Records
    """
    def __init__(
            self,
            url_chirho: Optional[str] = None,
            path_chirho: Optional[str] = None,
            html_chirho: Optional[str] = None,
            church_id_chirho: Optional[str] = None):
        self.url_chirho = url_chirho
        self.path_chirho = path_chirho
        self.html_chirho = html_chirho
        self.church_id_chirho = church_id_chirho

    def parse_chirho(self):
        if self.html_chirho:
            self.parse_html_chirho(self.html_chirho)
        if self.path_chirho:
            self.parse_path_chirho()
        else:
            self.parse_url_chirho()

    def parse_url_chirho(self):
        """
        Hallelujah, parse the sermon audio URL and store the relevant data in the object.
        """
        logger_chirho.info("☧ Retrieving the sermon audio URL: %s", self.url_chirho)
        response_chirho = requests.get(self.url_chirho)
        if response_chirho.status_code != 200:
            raise Exception(f"Failed to get the sermon audio URL: {self.url_chirho}")

        logger_chirho.info("☧ Parsing the sermon audio URL: %s", self.url_chirho)

        self.parse_html_chirho(response_chirho.text)

    def parse_path_chirho(self):
        with open(self.path_chirho, "r") as f_chirho:
            self.parse_html_chirho(f_chirho.read())

    def parse_html_chirho(self, html_chirho: str):
        soup_chirho = BeautifulSoup(html_chirho, "html.parser")

        sermon_title_chirho = soup_chirho.find(
            "font", {"class": "ar10 noblb"}).text
        sermon_month_chirho, sermon_day_chirho, sermon_year_chirho = map(int, soup_chirho.find(
            "a", {"class": "navleftblack5b", "style": "color:bb8844"}).text.split("/"))
        sermon_duration_minutes_chirho, sermon_duration_seconds_chirho = map(int, soup_chirho.find(
            "font", {"class": "ve1", "color": "565656"}).text.split(" ")[0].split(":"))
        sermon_author_full_name_chirho = soup_chirho.find(
            "a", {"class": "navleftblack12c"}).text
        sermon_audio_link_1_chirho = soup_chirho.find(
            "a", {"rel": "nofollow", "href": re.compile(r'.*mp3$')})["href"]
        sermon_video_link_element_chirho = soup_chirho.find(
            "a", {"rel": "nofollow", "href": re.compile(r'download.*mp4$')})

        sermon_id_chirho = sermon_audio_link_1_chirho.split("/")[-1].split(".")[0]

        sermon_audio_link_chirho = f"https://media-cloud.sermonaudio.com/audio/{sermon_id_chirho}.mp3"

        sermon_author_first_name_chirho = " ".join(sermon_author_full_name_chirho.split(" ")[0:-1])
        sermon_author_last_name_chirho = sermon_author_full_name_chirho.split(" ")[-1]
        sermon_video_link_chirho = f"https://media-cloud.sermonaudio.com/video/{sermon_id_chirho}.mp4" if sermon_video_link_element_chirho else None
        sermon_duration_ms_chirho = (sermon_duration_minutes_chirho * 60 + sermon_duration_seconds_chirho) * 1000
        sermon_out_date_chirho = f"{sermon_year_chirho}-{sermon_month_chirho:02d}-{sermon_day_chirho:02d} 10:00:00"

        author_chirho = AuthorChirho(
            firstName=sermon_author_first_name_chirho, lastName=sermon_author_last_name_chirho)
        author_chirho.find_and_update_or_create_chirho()
        sermon_chirho = SermonChirho(
            title=sermon_title_chirho,
            sermonDate=sermon_out_date_chirho,
            duration=sermon_duration_ms_chirho,
            author=author_chirho.id_chirho,
            externalAudioFileUrl=sermon_audio_link_chirho,
            externalVideoFileUrl=sermon_video_link_chirho,
            church=self.church_id_chirho)
        sermon_chirho.is_exception_on_exists_chirho = True
        sermon_chirho.find_and_update_or_create_chirho()
