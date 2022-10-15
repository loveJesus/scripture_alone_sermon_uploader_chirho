# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import pocketbase

from icecream import ic
from typing import Optional

from lib_chirho import settings_chirho

import logging

from lib_chirho.database_chirho import DatabaseChirho

logger_chirho = logging.getLogger(__name__)


class AuthorChirho:
    """
    Hallelujah, this class represents the author object. It contains the details of that author to search for and
    the methods to upload it to PocketBase.
    """

    TABLE_ID_CHIRHO = "authors"

    def __init__(
            self,
            firstName: str,
            lastName: Optional[str] = None,
            profileImage: Optional[str] = None,
            church: Optional[str] = None,
            administrators: Optional[list[str]] = None):
        self.id_chirho: Optional[str] = None
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
            "administrators": self.administrators_chirho}

    def find_or_create_chirho(self):
        """
        Hallelujah, this will attempt to find an author in PocketBase, based on first and last name, and retrieve the id.
        If the author does not exist, will create the author.
        """
        logger_chirho.info(f"☧ Finding or Creating Author: {self.dict_chirho()}")
        client_chirho = DatabaseChirho.get_client_chirho()
        pb_author_list_chirho = client_chirho.records.get_list(self.TABLE_ID_CHIRHO, 1, 50, {
            filter: f'firstName = "{self.firstName_chirho}" and lastName = "{self.lastName_chirho}"'})
        if len(pb_author_list_chirho.items) == 0:
            return self.create_chirho()
        self.id_chirho = pb_author_list_chirho.items[0].id
        logger_chirho.info(f"☧ Found Author with Id -> {self.id_chirho}")
        return self.id_chirho

    def create_chirho(self) -> None:
        """
        Hallelujah, this method creates a new author in PocketBase.
        """
        logger_chirho.info(f"☧ Creating Author: {self.dict_chirho()}")
        client_chirho = DatabaseChirho.get_client_chirho()
        pb_sermon_created_chirho = client_chirho.records.create(self.TABLE_ID_CHIRHO, self.dict_chirho())
        self.id_chirho = pb_sermon_created_chirho.id
        logger_chirho.info(f"☧ Created Author with Id -> {self.id_chirho}")
        return self.id_chirho
