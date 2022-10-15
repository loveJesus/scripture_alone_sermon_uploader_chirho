# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
from lib_chirho import settings_chirho
import pocketbase


class DatabaseChirho:
    POCKETBASE_CLIENT_CHIRHO = pocketbase.Client(settings_chirho.SA_POCKETBASE_SERVER_URL_CHIRHO)
    POCKETBASE_CLIENT_CHIRHO.admins.auth_via_email(
        settings_chirho.SA_POCKETBASE_LOGIN_EMAIL_CHIRHO,
        settings_chirho.SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO)

    @classmethod
    def get_client_chirho(cls) -> pocketbase.Client:
        return cls.POCKETBASE_CLIENT_CHIRHO
