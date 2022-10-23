# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
# Scripture Alone Sermon Uploader Chirho

[Scripture Alone](https://scripturealone.app) is an application that makes doctrinally healthy resources available to Christians. 
This utility is a companion to the app, to aid with linking to sermons from [SermonAudio.com](https://sermonaudio.com)

## Install and Run
```shell
# 1) Create a virtual environment to test if desired, if not skip to #2
mkdir test_scripture_alone_sermon_uploader_chirho
cd test_scripture_alone_sermon_uploader_chirho
python3 -m venv venv_chirho
source venv_chirho/bin/activate
pip install --upgrade pip

# 2) Install
pip install git+https://github.com/loveJesus/scripture_alone_sermon_uploader_chirho.git

# 3) You can optionally set the following environment variables, or have a .env in your current directory, 
# if not set them via the command line flags (look at the help text)
export SA_POCKETBASE_SERVER_URL_CHIRHO="https://staging.api.scripturealone.app/"
export SA_POCKETBASE_LOGIN_EMAIL_CHIRHO="email@aleluya.church"
export SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO="password_aleluyas"

# 4) Assuming your python pip path is in $PATH like if you activate above
# scripture_alone_sermon_uploader_chirho -a <sermon_audio_sermon_info_page_url>, example:
scripture_alone_sermon_uploader_chirho -a "https://www.sermonaudio.com/sermoninfo.asp?SID=92522121496393"

# You can also download a raw html file and use that with the -t <html_file_path> flag
```

### Help
```text
usage: scripture_alone_sermon_uploader_chirho.py [-h] [-u POCKETBASE_SERVER_URL_CHIRHO] [-e POCKETBASE_LOGIN_EMAIL_CHIRHO] [-p POCKETBASE_LOGIN_PASSWORD_CHIRHO]
                                                 (-a SERMON_AUDIO_URL_CHIRHO | -t SERMON_AUDIO_PATH_CHIRHO | -c SERMON_AUDIO_CHURCH_SHORT_NAME_CHIRHO)

Scripture Alone Sermon Uploader. Give a Sermon Audio URL or path to downloaded HTML file, and post its details to the Scripture Alone Backend.

options:
  -h, --help            show this help message and exit
  -u POCKETBASE_SERVER_URL_CHIRHO, --pocketbase_server_url_chirho POCKETBASE_SERVER_URL_CHIRHO
                        The URL of the PocketBase server to use, or set environment variable SA_POCKETBASE_SERVER_URL_CHIRHO
  -e POCKETBASE_LOGIN_EMAIL_CHIRHO, --pocketbase_login_email_chirho POCKETBASE_LOGIN_EMAIL_CHIRHO
                        The email address to use to log into the PocketBase server, or set environment variable SA_POCKETBASE_LOGIN_EMAIL_CHIRHO
  -p POCKETBASE_LOGIN_PASSWORD_CHIRHO, --pocketbase_login_password_chirho POCKETBASE_LOGIN_PASSWORD_CHIRHO
                        The password to use to log into the PocketBase server, or set environment variable SA_POCKETBASE_LOGIN_PASSWORD_CHIRHO
  -a SERMON_AUDIO_URL_CHIRHO, --sermon_audio_url_chirho SERMON_AUDIO_URL_CHIRHO
                        A Sermon Audio main site URL to import, God willing
  -t SERMON_AUDIO_PATH_CHIRHO, --sermon_audio_path_chirho SERMON_AUDIO_PATH_CHIRHO
                        A path of a downloaded Sermon Audio raw HTML file to import, Hallelujah
  -c SERMON_AUDIO_CHURCH_SHORT_NAME_CHIRHO, --sermon_audio_church_short_name_chirho SERMON_AUDIO_CHURCH_SHORT_NAME_CHIRHO
                        The short name of the church to download sermons from, e.g. "youthman1611" for Midway Baptist Church
```

### Notes:
Thank You Jesus for https://dzone.com/articles/executable-package-pip-install
```
pip install --upgrade pip setuptools wheel tqdm twine

python setup.py bdist_wheel

python -m pip install dist/sheepit_team_clean_aleluya-0.1.4-py3-none-any.whl

python -m twine upload dist/*
```