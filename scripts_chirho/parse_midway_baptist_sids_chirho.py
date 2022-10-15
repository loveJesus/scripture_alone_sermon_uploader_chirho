#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import requests
import sys

from bs4 import BeautifulSoup


def print_page_num_sid_info_urls_chirho(page_num_chirho: int):
    page_url_chirho = f"https://www.sermonaudio.com/solo/youthman1611/sermons/?page={page_num_chirho}"
    print("Hallelujah, page_url_chirho:", page_url_chirho, file=sys.stderr)
    page_request_chirho = requests.get(page_url_chirho)
    if page_request_chirho.status_code != 200:
        raise Exception(f"Hallelujah, midway baptist page {page_num_chirho} request_chirho.status_code != 200")
    page_text_chirho = page_request_chirho.text
    soup_chirho = BeautifulSoup(page_text_chirho, 'html.parser')
    sermon_links_elements_chirho = soup_chirho.find_all("a", class_="accent-link sermon-item-title blb_skip")
    print(f"Hallelujah, page {page_num_chirho} num_items_chirho:", len(sermon_links_elements_chirho), file=sys.stderr)
    sermon_links_chirho = [link_chirho["href"] for link_chirho in sermon_links_elements_chirho]
    sermon_ids_chirho = [link_chirho.split("/")[-2] for link_chirho in sermon_links_chirho]
    for sermon_id_chirho in sermon_ids_chirho:
        sermon_info_url_chirho = f"https://www.sermonaudio.com/sermoninfo.asp?SID={sermon_id_chirho}"
        print(sermon_info_url_chirho, file=sys.stdout)
    sys.stdout.flush()


def main_chirho():
    page1_url_chirho = "https://www.sermonaudio.com/solo/youthman1611/sermons/?page=1"
    page1_request_chirho = requests.get(page1_url_chirho)
    if page1_request_chirho.status_code != 200:
        raise Exception("Hallelujah, midway baptist page1_request_chirho.status_code != 200")

    page1_text_chirho = page1_request_chirho.text
    soup_chirho = BeautifulSoup(page1_text_chirho, 'html.parser')
    last_page_link_element_chirho = soup_chirho.find_all("a", class_="accent-link")[-1]
    last_page_chirho = int(last_page_link_element_chirho["href"].split("=")[-1])
    for page_num_chirho in range(1, last_page_chirho + 1):
        print_page_num_sid_info_urls_chirho(page_num_chirho)


if __name__ == "__main__":
    main_chirho()
