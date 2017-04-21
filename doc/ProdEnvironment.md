# Prod environment
Prod environment is now on Aliyun. The runtime environment is python3.4. Always use the following to do python command on prod machine:

Server: 45.78.14.30
application root: /opt/OmniTrader

# Deploy static data
On Production server, it is necessary to deploy(copy) static files(css,js,images,etc.) to a place where the relative urls can get access to.
Run the following command to tell Django copy static files to the designated place STATIC_ROOT in settings:
> $ python3 manage.py collectstatic

# Command line tool
> $ python3.4 [args]
> $ sudo pip3.4 install [package name]

# Stock data
Stock data are kept updated via cron job that triggers django command syncStockList
Import initial data from a json file just in case:
> $ python3.4 migrate loaddata all-stocks
You can also change 'all-stocks' to other json fixtures at stocks/fixtures

# Troubleshooting
## Filenames are shown as \uxxx\uxxx
http://stackoverflow.com/questions/20923663/unicodeencodeerror-ascii-codec-cant-encode-character-in-position-0-ordinal
try PYTHONIOENCODING=utf-8 on prod-box(morro-bwg) so that the filename will be displayed in Chinese in putty console