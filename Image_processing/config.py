# Filename: config.py
# Description: This file fetches all the constants required for operations from config.properties
# Author: Ajay Vanara

import configparser

CONF = configparser.ConfigParser()
CONF.read('config.properties')
