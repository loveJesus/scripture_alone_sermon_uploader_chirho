#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son,
# that all who believe in Him should not perish but have everlasting life
import logging
import re
from typing import Optional

import requests

from bs4 import BeautifulSoup

from lib_chirho.models_chirho.church_chirho import ChurchChirho
from lib_chirho.sermon_audio_sermon_html_parser_chirho import SermonAudioSermonHtmlParserChirho

logger_chirho = logging.getLogger(__name__)


class SermonAudioChurchShortNameCrawlerChirho:
    def __init__(self, church_short_name_chirho: str):
        self.church_short_name_chirho = church_short_name_chirho
        self.sermon_audio_church_base_url_chirho = f"https://www.sermonaudio.com/solo/{church_short_name_chirho}/sermons/?page="
        logger_chirho.info(f"Hallelujah - initiation search for sermons at {self.sermon_audio_church_base_url_chirho}")
        self._get_pb_church_chirho()

    def _get_pb_church_chirho(self) -> ChurchChirho:
        self.church_chirho = ChurchChirho(sermonAudioShortName=self.church_short_name_chirho)
        self.church_id_chirho = self.church_chirho.find_id_chirho()
        self.church_name_chirho = self.church_chirho.find_name_chirho()

    def crawl_chirho(self):
        num_pages_chirho = self._get_num_pages_chirho()
        for page_num_chirho in range(1, num_pages_chirho + 1):
            sids_chirho = self._crawl_church_page_for_sids_chirho(page_num_chirho)
            for sid_chirho in sids_chirho:
                try:
                    sermon_info_url_chirho = f"https://www.sermonaudio.com/sermoninfo.asp?SID={sid_chirho}"
                    logger_chirho.info(sermon_info_url_chirho)
                    sermon_html_parser_chirho = SermonAudioSermonHtmlParserChirho(
                        url_chirho=sermon_info_url_chirho, church_id_chirho=self.church_id_chirho)
                    sermon_html_parser_chirho.parse_chirho()
                except Exception as e_chirho:
                    logger_chirho.exception(e_chirho)

    def _get_num_pages_chirho(self) -> int:
        page1_url_chirho = self.sermon_audio_church_base_url_chirho + "1"
        page1_request_chirho = requests.get(page1_url_chirho)
        if page1_request_chirho.status_code != 200:
            raise Exception(f"Hallelujah, {self.church_name_chirho} page1_request_chirho.status_code != 200")

        page1_text_chirho = page1_request_chirho.text
        soup_chirho = BeautifulSoup(page1_text_chirho, 'html.parser')
        last_page_link_element_chirho = soup_chirho.find_all("a", class_="accent-link")[-1]
        last_page_num_chirho = int(last_page_link_element_chirho["href"].split("=")[-1])
        self.num_pages_chirho = last_page_num_chirho
        logger_chirho.info(f"Hallelujah - {self.church_name_chirho} num_pages_chirho: {self.num_pages_chirho}")
        return last_page_num_chirho

    def _crawl_church_page_for_sids_chirho(self, page_num_chirho: int) -> list[str]:
        page_url_chirho = self.sermon_audio_church_base_url_chirho + str(page_num_chirho)
        logger_chirho.info("Hallelujah, crawling for sids page_url_chirho:" + page_url_chirho)
        page_request_chirho = requests.get(page_url_chirho)
        if page_request_chirho.status_code != 200:
            raise Exception(f"Hallelujah, {self.church_name_chirho} page #{page_num_chirho} status_code != 200")
        page_text_chirho = page_request_chirho.text
        soup_chirho = BeautifulSoup(page_text_chirho, 'html.parser')
        sermon_links_elements_chirho = soup_chirho.find_all("a", class_="accent-link sermon-item-title blb_skip")
        logger_chirho.info(f"Hallelujah, page {page_num_chirho} num_items_chirho: {len(sermon_links_elements_chirho)}")
        sermon_links_chirho = [link_chirho["href"] for link_chirho in sermon_links_elements_chirho]
        sermon_ids_chirho = [link_chirho.split("/")[-2] for link_chirho in sermon_links_chirho]
        return sermon_ids_chirho



