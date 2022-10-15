# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements_chirho = [
    "pocketbase==0.1.0",
    "python-dotenv==0.14.0",
    "requests==2.24.0",
    "beautifulsoup4==4.9.1",
]

setuptools.setup(
    name='scripture_alone_sermon_uploader_chirho',
    version="0.1.0",
    scripts=['scripture_alone_sermon_uploader_chirho.py'],
    author="Love Jesus",
    author_email="loveJesus@loveJesus.xyz",
    description="Hallelujah - upload sermons to https://scripturealone.app.",
    install_requires=requirements_chirho,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/loveJesus/scripture_alone_sermon_uploader_chirho",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
