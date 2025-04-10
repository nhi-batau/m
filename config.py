#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os
from pymongo import MongoClient

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7803831518:AAED-lKGreyYe9idQkLMzAIsA953s4HODgs")
    API_ID = int(os.environ["API_ID", 20868701]
    API_HASH = os.environ["API_HASH", "9bf50346c886503948931272bbdab967"]
    AUTH_USERS = "7834875502"
    #MONGO_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://mpsystem05:ZzYGIZ0a4PCUQkKm@cluster0.eppygqi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
