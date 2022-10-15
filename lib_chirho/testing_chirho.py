# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import logging
import pocketbase

from lib_chirho import settings_chirho

from lib_chirho.models_chirho.author_chirho import AuthorChirho
from lib_chirho.models_chirho.sermon_chirho import SermonChirho
from lib_chirho.sermon_audio_sermon_url_parser_chirho import SermonAudioSermonUrlParserChirho

logger_chirho = logging.getLogger(__name__)


def testing_chirho():
    parser_chirho = SermonAudioSermonUrlParserChirho("https://www.sermonaudio.com/sermoninfo.asp?SID=92522120176322")
    parser_chirho.parse_url_chirho()
    my_author_chirho = AuthorChirho(firstName="TestFirstChirho", lastName="TestLastChirho")
    my_author_chirho.find_or_create_chirho()
    my_sermon_chirho = SermonChirho(
        title="test_aleluya", description="test", sermonDate="2022-01-01 10:00:00", duration=123,
        author=my_author_chirho.id_chirho)
    my_sermon_chirho.create_chirho()


def testing_old1_chirho():
    client_chirho = pocketbase.Client(settings_chirho.SA_POCKETBASE_SERVER_URL_CHIRHO)
    client_chirho.admins.auth_via_email(
        settings_chirho.SA_POCKETBASE_LOGIN_EMAIL_CHIRHO, settings_chirho.SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO)

    sermons_chirho = client_chirho.records.get_list('sermons', 1, 50, {
        filter: 'created >= "2022-01-01 00:00:00"',
    })
    sermon1_chirho = client_chirho.records.get_one('sermons', sermons_chirho.items[0].id)

    my_sermon_chirho = SermonChirho(
        title="test_aleluya", description="test", sermonDate="2022-01-01 10:00:00", duration=123)
    my_sermon_chirho.create_chirho()
    sermon_data_chirho = {
        "title": "test_aleluya",
        "description": "test",
        "externalAudioFileUrl": "",
        # "externalVideoFileUrl": "test",
        # "transcript": "test",
        # "categories": [
        #     "TEST_RELATION_RECORD_ID"
        # ],
        # "externalCoverImageUrl": "test",
        # "audioFile": "filename.jpg",
        # "coverImage": "filename.jpg",
        "sermonDate": "2022-01-01 10:00:00",
        # "author": "RELATION_RECORD_ID",
        "duration": 123
    }

    sermon_create_chirho = client_chirho.records.create('sermons', sermon_data_chirho)
    sermon_delete_chirho = client_chirho.records.delete('sermons', sermon_create_chirho.id)
