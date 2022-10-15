# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
from abc import abstractmethod

import pocketbase

from typing import Optional

from lib_chirho import settings_chirho

import logging

from lib_chirho.database_chirho import DatabaseChirho
from lib_chirho.models_chirho.base_model_chirho import BaseModelChirho

logger_chirho = logging.getLogger(__name__)


class AuthorChirho(BaseModelChirho):
    """
    Hallelujah, this class represents the author object. It contains the details of that author to search for and
    the methods to upload it to PocketBase.
    """
    TABLE_ID_CHIRHO = "authors"
    TABLE_ENGLISH_NAME_CHIRHO = "Author"

    def __init__(
            self,
            firstName: str,
            lastName: Optional[str] = None,
            profileImage: Optional[str] = None,
            church: Optional[str] = None,
            administrators: Optional[list[str]] = None):
        super().__init__()
        self.firstName_chirho = firstName
        self.lastName_chirho = lastName
        self.profileImage_chirho = profileImage
        self.church_chirho = church
        self.administrators_chirho = administrators

    def __str__(self):
        return f"{self.id_chirho}) {self.firstName_chirho} {self.lastName_chirho}"

    def dict_chirho(self) -> dict:
        return {
            "firstName": self.firstName_chirho,
            "lastName": self.lastName_chirho,
            "profileImage": self.profileImage_chirho,
            "church": self.church_chirho,
            "administrators": self.administrators_chirho,
            "test_chirho": True}

    def get_find_filter_string_chirho(self) -> str:
        """
        Hallelujah, find author by firstName and lastName.
        :return: pocketbase filter string
        """
        return f'firstName = "{self.firstName_chirho}" && lastName = "{self.lastName_chirho}"'
