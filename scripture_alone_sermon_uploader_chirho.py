#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
from lib_chirho import settings_chirho
from lib_chirho.sermon_audio_sermon_url_parser_chirho import SermonAudioSermonUrlParserChirho


def main_chirho():
    args_chirho = settings_chirho.args_chirho
    parser_chirho = SermonAudioSermonUrlParserChirho(args_chirho.sermon_audio_url_chirho)
    parser_chirho.parse_url_chirho()


if __name__ == '__main__':
    main_chirho()