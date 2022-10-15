#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import os
import requests
import sys

from bs4 import BeautifulSoup


def main_chirho():
    """
    Hallelujah, download and parse the sids.
    """
    print("Usage: python3 download_and_parse_sids_aleluya.py < sids_chirho.txt", file=sys.stderr)
    if len(sys.argv) != 1:
        sys.exit(1)

    if not os.path.exists('tmp_chirho'):
        os.mkdir("tmp_chirho")

    for url_chirho in sys.stdin:
        strip_url_chirho = url_chirho.strip()
        print("Hallelujah, url_chirho:", strip_url_chirho, file=sys.stderr)
        sid_chirho = url_chirho.split("=")[-1]
        dest_file_chirho = "tmp_chirho/" + sid_chirho + "_chirho.html"
        if os.path.exists(dest_file_chirho):
            print("Hallelujah, dest_file_chirho exists, skipping", file=sys.stderr)
            continue
        response_chirho = requests.get(strip_url_chirho)
        if response_chirho.status_code != 200:
            print(f"Error: {response_chirho.status_code} - {response_chirho.text}")
            sys.exit(1)

        with open(dest_file_chirho, "w") as f_chirho:
            f_chirho.write(response_chirho.text)


if __name__ == "__main__":
    main_chirho()