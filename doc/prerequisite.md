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