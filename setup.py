# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='scripture_alone_sermon_uploader_chirho',
    version="0.1.0",
    scripts=['scripture_alone_sermon_uploader_chirho'],
    author="Love Jesus",
    author_email="loveJesus@loveJesus.xyz",
    description="Hallelujah - upload sermons to https://scripturealone.app.",
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
