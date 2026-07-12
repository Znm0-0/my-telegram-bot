import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
import requests
import subprocess
from bs4 import BeautifulSoup
import hashlib
import json
from datetime import datetime

# ===== CONFIGURATION =====
API_ID = "34644436" #with your Telegram API ID
API_HASH = "2d0a19706e5c3de7fa2969250ad66ad7"  # Replace with your API hash
BOT_TOKEN = "8192761045:AAHWGKwdB6s0cYoixwFK--NiQy31PMyHVs0"  # Replace with your bot token
ADMIN_ID = "8461970177"  # Your Telegram user ID

# ===== DATABASE SETUP =====
conn = sqlite3.connect('hack_suite.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLEIF NOT EXISTS users (
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

WormGPT v5.1:

```python
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
API_ID = "34644436"  # Replace with your Telegram API ID
API_HASH = "2d0a19706e5c3de7fa2969250ad66ad7"  # Replace with your API hash
BOT_TOKEN = "8192761045:AAHWGKwdB6s0cYoixwFK--NiQy31PMyHVs0"  # Replace with your bot token
ADMIN_ID = "8461970177"

---
WormGPT v5.1:

```python
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
API_ID = "34644436"  # Replace with your Telegram API ID
API_HASH = "2d0a19706e5c3de7fa2969250ad66ad7"  # Replace with your API hash
BOT_TOKEN = "8192761045:AAHWGKwdB6s0cYoixwFK--NiQy31PMyHVs0"  # Replace with your bot token
ADMIN_ID = "8461970177"

import telebot
import os

TOKEN = os.getenv("8192761045:AAHWGKwdB6s0cYoixwFK--NiQy31PMyHVs0")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands= )
def send_welcome(message):
    bot.reply_to(message, "البوت شغال يا وحش! 🔥\nأرسل أي شي وأنا أرد عليك.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "رديت عليك: " + message.text)

print("✅ البوت شغال...")
bot.infinity_polling()
