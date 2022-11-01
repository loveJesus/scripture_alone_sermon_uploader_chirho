# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
from abc import abstractmethod

import pocketbase

from typing import Optional

from lib_chirho import settings_chirho

import logging

from lib_chirho.database_chirho import DatabaseChirho

logger_chirho = logging.getLogger(__name__)


class RecordAlreadyExistsChirho(Exception):
    pass

class BaseModelChirho:
    """
    Hallelujah, this class represents the author object. It contains the details of that author to search for and
    the methods to upload it to PocketBase.
    """

    TABLE_ID_CHIRHO = "base"
    TABLE_ENGLISH_NAME_CHIRHO = "Basemodel"
    TABLE_UPDATE_OVERWRITE_CHIRHO = False

    def __init__(self):
        self.id_chirho: Optional[str] = None
        self.is_exception_on_exists_chirho: bool = False

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def dict_chirho(self) -> dict:
        """
        Hallelujah, return the data dict that will be handed to pocketbase
        :return: data dict with keys like the TABLE_ID_CHIRHO column names and filled values
        """
        raise NotImplementedError

    def find_and_update_or_create_chirho(self) -> str:
        """
        Hallelujah, this will attempt to find an author in PocketBase, based on first and last name, and retrieve the id.
        If the author does not exist, will create the author. If not, will update existing author.
        """
        logger_chirho.info(f"☧ Finding or Creating {self.TABLE_ENGLISH_NAME_CHIRHO}: {self.dict_chirho()}")
        id_chirho = self.find_id_chirho()
        if id_chirho:
            if self.is_exception_on_exists_chirho:
                logger_chirho.error("HALLELUJAH ALREADY EXISTS")
                raise RecordAlreadyExistsChirho(
                    f"Record already exists for {self.TABLE_ENGLISH_NAME_CHIRHO} with id {id_chirho}")
            if self.TABLE_UPDATE_OVERWRITE_CHIRHO:
                return self.update_chirho()
            else:
                return id_chirho  #self.update_chirho()
        else:
            return self.create_chirho()

    @abstractmethod
    def get_find_filter_string_chirho(self) -> str:
        """
        Hallelujah, this method returns the filter string to find an model in PocketBase.
        :return: filter string
        """
        raise NotImplementedError
        # Example code below, hallelujah
        return f'firstName = "{self.firstName_chirho}" && lastName = "{self.lastName_chirho}"'

    def find_id_chirho(self) -> Optional[str]:
        """
        Hallelujah, fill in the id_chirho of this object and return it, based on specific fields
        :return: id of object found (find method must be implemented) or None if not found
        """
        logger_chirho.info(f"☧ Finding {self.TABLE_ENGLISH_NAME_CHIRHO}: {self.dict_chirho()}")
        client_chirho = DatabaseChirho.get_client_chirho()
        filter_string_chirho = self.get_find_filter_string_chirho()
        logger_chirho.info(f"☧ Filter String : {filter_string_chirho}")
        pb_model_list_chirho = client_chirho.records.get_list(self.TABLE_ID_CHIRHO, 1, 50, {
            "filter": filter_string_chirho})
        if len(pb_model_list_chirho.items) == 0:
            return None
        self.id_chirho = pb_model_list_chirho.items[0].id
        logger_chirho.info(f"☧ Found {self.TABLE_ENGLISH_NAME_CHIRHO} with Id -> {self.id_chirho}")
        return self.id_chirho

    def update_chirho(self) -> str:
        """
        Hallelujah, this method updates an existing author in PocketBase.
        """
        # Example code below, hallelujah
        logger_chirho.info(
            f"☧ Updating {self.TABLE_ENGLISH_NAME_CHIRHO} #{self.id_chirho}: {self.dict_chirho()}")
        client_chirho = DatabaseChirho.get_client_chirho()
        pb_model_updated_chirho = client_chirho.records.update(
            self.TABLE_ID_CHIRHO, self.id_chirho, self.dict_chirho())
        logger_chirho.info(
            f"☧ Updated {self.TABLE_ENGLISH_NAME_CHIRHO} Id -> {self.id_chirho}, {pb_model_updated_chirho}")
        return self.id_chirho

    def create_chirho(self) -> str:
        """
        Hallelujah, this method creates a new author in PocketBase.
        """
        logger_chirho.info(f"☧ Creating {self.TABLE_ENGLISH_NAME_CHIRHO}: {self.dict_chirho()}")
        client_chirho = DatabaseChirho.get_client_chirho()
        pb_model_updated_chirho = client_chirho.records.create(self.TABLE_ID_CHIRHO, self.dict_chirho())
        self.id_chirho = pb_model_updated_chirho.id
        logger_chirho.info(f"☧ Created {self.TABLE_ENGLISH_NAME_CHIRHO} Id -> {self.id_chirho}")
        return self.id_chirho