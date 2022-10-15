# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
# Scripture Alone Sermon Uploader Additional Scripts Chirho

## parse_midway_baptist_sids_chirho.py
This script will print to stdout all the Sermon info page urls that are
in the listing for the Midway Baptist Church sermon series url 
https://www.sermonaudio.com/solo/youthman1611/sermons/?page=1

Pipe to an output to a file, you can then pass the list of urls to
`scripture_alone_sermon_uploader_chirho.py` to upload the sermons to
Scripture Alone. Or you can use the `download_sids_chirho.py` script to download 
all the raw html files to `./tmp_chirho/` and then run 
`scripture_alone_sermon_uploader_chirho.py` on those files.

## download_sids_chirho.py
This script will download all the raw html files that have the urls
in the Sermon Audio Sermon info page format to `./tmp_chirho/`

You can then do something like
`for html_file_chirho in ./tmp_chirho/*.html; do scripture_alone_sermon_uploader_chirho.py -t "$html_file_chirho"; done`
