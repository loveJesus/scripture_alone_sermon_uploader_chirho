# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import logging
import pocketbase

from icecream import ic
from typing import Optional

from lib_chirho import settings_chirho

logger_chirho = logging.getLogger(__name__)


class SermonChirho:
    """
    Hallelujah, this class represents the sermon object. It contains the details of that sermon and
    the methods to upload it to PocketBase.
    """

    TABLE_ID_CHIRHO = "sermons"

    def __init__(
            self,
            title: str,
            description: Optional[str] = None,  # ="test",
            externalAudioFileUrl: Optional[str] = None,  # ="test",
            externalVideoFileUrl: Optional[str] = None,  # ="test",
            transcript: Optional[str] = None,  # ="test",
            categories: Optional[list[str]] = None,  # =[ "TEST_RELATION_RECORD_ID"],
            externalCoverImageUrl: Optional[str] = None,  # ="test",
            audioFile: Optional[str] = None,  # ="filename.jpg",
            coverImage: Optional[str] = None,  # ="filename.jpg",
            sermonDate: Optional[str] = None,  # ="2022-01-01 10:00:00",
            author: Optional[str] = None,  # ="RELATION_RECORD_ID",
            duration: Optional[int] = None):  # =123):

        self.id_chirho: Optional[str] = None
        self.title_chirho = title
        self.description_chirho = description
        self.externalAudioFileUrl_chirho = externalAudioFileUrl
        self.externalVideoFileUrl_chirho = externalVideoFileUrl
        self.transcript_chirho = transcript
        self.categories_chirho = categories
        self.externalCoverImageUrl_chirho = externalCoverImageUrl
        self.audioFile_chirho = audioFile
        self.coverImage_chirho = coverImage
        self.sermonDate_chirho = sermonDate
        self.author_chirho = author
        self.duration_chirho = duration

    def __str__(self):
        return f"{self.id_chirho}) - {self.title_chirho} - {self.description_chirho}"

    def dict_chirho(self) -> dict:
        return {
            "title": self.title_chirho,
            "description": self.description_chirho,
            "externalAudioFileUrl": self.externalAudioFileUrl_chirho,
            "externalVideoFileUrl": self.externalVideoFileUrl_chirho,
            "transcript": self.transcript_chirho,
            "categories": self.categories_chirho,
            "externalCoverImageUrl": self.externalCoverImageUrl_chirho,
            "audioFile": self.audioFile_chirho,
            "coverImage": self.coverImage_chirho,
            "sermonDate": self.sermonDate_chirho,
            "author": self.author_chirho,
            "duration": self.duration_chirho
        }

    def create_chirho(self):
        logger_chirho.info(f"☧ Creating Sermon: {self.dict_chirho()}")
        client_chirho = settings_chirho.POCKETBASE_CLIENT_CHIRHO
        pb_sermon_created_chirho = client_chirho.records.create(self.TABLE_ID_CHIRHO, self.dict_chirho())
        self.id_chirho = pb_sermon_created_chirho.id
        logger_chirho.info(f"☧ Sermon Created with ID -> {self.id_chirho}")
        return self.id_chirho
