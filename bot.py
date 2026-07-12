import asyncio
import os
import re
import socket
import subprocess
import sqlite3
import requests
import hashlib
import json
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bs4 import BeautifulSoup
import aiohttp
import aiodns
import base64
import zlib
from cryptography.fernet import Fernet
import numpy as np
from scapy.all import *
import nmap
import paramiko
import pymongo
import redis
import dns.resolver
import whois
import phonenumbers
from phonenumbers import carrier, geocoder

# ===== CONFIGURATION =====
API_ID = 34644436 # ضع رقم الـ API_ID الخاص بك هنا
API_HASH = "2d0a19706e5c3de7fa2969250ad66ad7" # ضع الـ API_HASH هنا
BOT_TOKEN = "8192761045:AAHWGKwdB6s0cYoixwFK--NiQy31PMyHVs0" # ضع التوكن هنا
ADMIN_ID = 8461970177 # ضع الأيدي الرقمي الخاص بك هنا

# ===== DATABASE SETUP =====
conn = sqlite3.connect('hack_suite.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT,
        phone TEXT,
        last_seen TEXT,
        osint_data TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        project_id INTEGER PRIMARY KEY,
        project_name TEXT
    )
''')
conn.commit()

print("Bot is ready and running!")