# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
# Path: lib_chirho/models_chirho/church_chirho.py
from typing import Optional

import logging

from lib_chirho.database_chirho import DatabaseChirho
from lib_chirho.models_chirho.base_model_chirho import BaseModelChirho

logger_chirho = logging.getLogger(__name__)


class ChurchChirho(BaseModelChirho):
    """
    Hallelujah, this class represents the author object. It contains the details of that author to search for and
    the methods to upload it to PocketBase.
    """
    TABLE_ID_CHIRHO = "churches"
    TABLE_ENGLISH_NAME_CHIRHO = "Church"

    def __init__(
            self,
            name: Optional[str] = None,
            streetAddress1: Optional[str] = None,
            streetAddress2: Optional[str] = None,
            city: Optional[str] = None,
            region: Optional[str] = None,
            postalCode: Optional[str] = None,
            countryCode: Optional[str] = None,
            lat: Optional[str] = None,
            lng: Optional[str] = None,
            email: Optional[str] = None,
            phone: Optional[str] = None,
            website: Optional[str] = None,
            administrators: Optional[list[str]] = None,
            sermonAudioShortName: Optional[str] = None,
            socialmedia: Optional[str] = None):
        super().__init__()
        self.name_chirho = name
        self.streetAddress1_chirho = streetAddress1
        self.streetAddress2_chirho = streetAddress2
        self.city_chirho = city
        self.region_chirho = region
        self.postalCode_chirho = postalCode
        self.countryCode_chirho = countryCode
        self.lat_chirho = lat
        self.lng_chirho = lng
        self.email_chirho = email
        self.phone_chirho = phone
        self.website_chirho = website
        self.administrators_chirho = administrators
        self.sermonAudioShortName_chirho = sermonAudioShortName
        self.socialmedia_chirho = socialmedia

    def __str__(self):
        return f"{self.id_chirho}) {self.name_chirho}"

    def dict_chirho(self) -> dict:
        return {
            "name": self.name_chirho,
            "streetAddress1": self.streetAddress1_chirho,
            "streetAddress2": self.streetAddress2_chirho,
            "city": self.city_chirho,
            "region": self.region_chirho,
            "postalCode": self.postalCode_chirho,
            "countryCode": self.countryCode_chirho,
            "lat": self.lat_chirho,
            "lng": self.lng_chirho,
            "email": self.email_chirho,
            "phone": self.phone_chirho,
            "website": self.website_chirho,
            "administrators": self.administrators_chirho,
            "sermonAudioShortName": self.sermonAudioShortName_chirho,
            "socialmedia": self.socialmedia_chirho,}

    def get_find_filter_string_chirho(self) -> str:
        """
        Hallelujah, find author by firstName and lastName.
        :return: pocketbase filter string
        """
        return f'sermonAudioShortName = "{self.sermonAudioShortName_chirho}"'

    def find_name_chirho(self) -> Optional[str]:
        """
        Hallelujah, fill in the name_chirho of this object and return it, based on the churchs id
        :return: name of object found or None if not found
        """
        logger_chirho.info(f"☧ Finding {self.TABLE_ENGLISH_NAME_CHIRHO} name for: {self.id_chirho}")
        client_chirho = DatabaseChirho.get_client_chirho()
        filter_string_chirho = f'id = "{self.id_chirho}"'
        logger_chirho.info(f"☧ Filter String : {filter_string_chirho}")
        pb_model_list_chirho = client_chirho.records.get_list(self.TABLE_ID_CHIRHO, 1, 50, {
            "filter": filter_string_chirho})
        if len(pb_model_list_chirho.items) == 0:
            raise Exception("NO CHURCH FOUND WITH ID " + self.id_chirho)

        self.name_chirho = pb_model_list_chirho.items[0].name
        logger_chirho.info(f"☧ Found {self.TABLE_ENGLISH_NAME_CHIRHO} with Name -> {self.name_chirho}")
        return self.name_chirho
