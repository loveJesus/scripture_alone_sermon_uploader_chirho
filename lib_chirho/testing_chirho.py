# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
from icecream import ic
from lib_chirho import settings_chirho
import pocketbase

from lib_chirho.classes_chirho.sermon_chirho import SermonChirho


def testing_chirho():
    client_chirho = pocketbase.Client(settings_chirho.SA_POCKETBASE_SERVER_URL_CHIRHO)
    client_chirho.admins.auth_via_email(
        settings_chirho.SA_POCKETBASE_LOGIN_EMAIL_CHIRHO, settings_chirho.SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO)

    sermons_chirho = client_chirho.records.get_list('sermons', 1, 50, {
        filter: 'created >= "2022-01-01 00:00:00"',
    })
    sermon1_chirho = client_chirho.records.get_one('sermons', sermons_chirho.items[0].id)

    my_sermon_chirho = SermonChirho(
        title="test_aleluya", description="test", sermonDate="2022-01-01 10:00:00", duration=123)
    ic(my_sermon_chirho.create_chirho())
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
    ic(sermon_create_chirho)
    sermon_delete_chirho = client_chirho.records.delete('sermons', sermon_create_chirho.id)
    ic(sermon_delete_chirho)