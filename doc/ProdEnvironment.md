# Prod environment
Prod environment is now on Aliyun. The runtime environment is python3.4. Always use the following to do python command on prod machine:

# Command line tool
> $ python3.4 [args]
> $ sudo pip3.4 install [package name]

## How to import initial data
> $ python3.4 migrate loaddata all-stocks

You can also change 'all-stocks' to other json fixtures at stocks/fixtures


# Filenames are shown as \uxxx\uxxx
http://stackoverflow.com/questions/20923663/unicodeencodeerror-ascii-codec-cant-encode-character-in-position-0-ordinal
try PYTHONIOENCODING=utf-8 on prod-box(morro-bwg) so that the filename will be displayed in Chinese in putty console