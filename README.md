# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
# Scripture Alone Sermon Uploader Chirho

[Scripture Alone](https://scripturealone.app) is an application that makes doctrinally healthy resources available to Christians. 
This utility is a companion to the app, to aid with linking to sermons from [SermonAudio.com](https://sermonaudio.com)

## Install and Run
```shell
# pip install scripture_alone_sermon_uploader_chirho # Work in Progress

# Make sure to properly set the following environment variables, or have a .env in your current directory
export SA_POCKETBASE_SERVER_URL_CHIRHO="https://staging.api.scripturealone.app/"
export SA_POCKETBASE_LOGIN_EMAIL_CHIRHO="email@aleluya.church"
export SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO="password_aleluyas"

# Assuming your python pip path is in $PATH 
scripture_alone_sermon_uploader_chirho <sermon_audio_url>
```

### Help
```text
usage: scripture_alone_sermon_uploader_chirho.py [-h] [-a SERMON_AUDIO_URL_CHIRHO] [-u POCKETBASE_SERVER_URL_CHIRHO] [-e POCKETBASE_LOGIN_EMAIL_CHIRHO] [-p POCKETBASE_LOGIN_PASSWORD_CHIRHO]

Scripture Alone Sermon Uploader. Give a Sermon Audio URL and post its details to the Scripture Alone Backend.

options:
  -h, --help            show this help message and exit
  -a SERMON_AUDIO_URL_CHIRHO, --sermon_audio_url_chirho SERMON_AUDIO_URL_CHIRHO
                        The URL of the PocketBase server to use, or set environment variable SA_POCKETBASE_SERVER_URL_CHIRHO
  -u POCKETBASE_SERVER_URL_CHIRHO, --pocketbase_server_url_chirho POCKETBASE_SERVER_URL_CHIRHO
                        The URL of the PocketBase server to use, or set environment variable SA_POCKETBASE_SERVER_URL_CHIRHO
  -e POCKETBASE_LOGIN_EMAIL_CHIRHO, --pocketbase_login_email_chirho POCKETBASE_LOGIN_EMAIL_CHIRHO
                        The email address to use to log into the PocketBase server, or set environment variable SA_POCKETBASE_LOGIN_EMAIL_CHIRHO
  -p POCKETBASE_LOGIN_PASSWORD_CHIRHO, --pocketbase_login_password_chirho POCKETBASE_LOGIN_PASSWORD_CHIRHO
                        The password to use to log into the PocketBase server, or set environment variable SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO
```

### Notes:
Thank You Jesus for https://dzone.com/articles/executable-package-pip-install
```
pip install --upgrade pip setuptools wheel tqdm twine

python setup.py bdist_wheel

python -m pip install dist/sheepit_team_clean_aleluya-0.1.4-py3-none-any.whl

python -m twine upload dist/*
```