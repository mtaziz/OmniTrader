# Install Python3.4 with django and pip on Ubuntu 12.04 LTS
http://ubuntuhandbook.org/index.php/2014/05/install-python-3-3-5-or-3-4-via-ppa-in-ubuntu-14-04-12-04/

# Use pip3.4 to install django, PyMySql and other dependencies.
pip3 install pymysql
pip3 install django-admin-bootstrapped
pip3 install django-autocomplete-light


# Run Django in different environment
Linux/Mac:
export DJANGO_SETTINGS_MODULE=OmniTrader.settings_qa
Windows:
set DJANGO_SETTINGS_MODULE=OmniTrader.settings_uat

# Connecting app to Aliyun db
Adding ip to Aliyun whitelist is a prerequisite

# Start server
Make sure your server ip is in the whitelist of the database.
manage.py runserver 0.0.0.0:80

# Load fixtures into database
Command:
manage.py loaddata [fixture-name-without-json-suffix] 
Note that if fixture contains Chinese character it needs to be stored as utf8 WITHOUT signature so that django could decode it. Change it via File-> Advanced save options

# Apply model changes
1. Make migration files and make sure they are all added to the repository. This needs to be done ONLY ONCE after the model change.
manage.py makemigrations
2. Apply the migration files. This needs to be done on all databases(Test/QA/UAT/PROD)
manage.py migrate