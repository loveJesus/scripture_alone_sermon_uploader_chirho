# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import pocketbase

from icecream import ic
from typing import Optional

from lib_chirho import settings_chirho

import logging
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
        pass

    def create_chirho(self) -> None:
        """
        Hallelujah, this method creates a new author in PocketBase.
        """
        logger_chirho.info("create author: ", self.dict_chirho())
        client_chirho = pocketbase.Client(settings_chirho.SA_POCKETBASE_SERVER_URL_CHIRHO)
        client_chirho.admins.auth_via_email(
            settings_chirho.SA_POCKETBASE_LOGIN_EMAIL_CHIRHO, settings_chirho.SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO)
        pb_sermon_created_chirho = client_chirho.records.create(self.TABLE_ID_CHIRHO, self.dict_chirho())
        self.id_chirho = pb_sermon_created_chirho.id
        logger_chirho.info("New author id: ", self.id_chirho)
        return self.id_chirho