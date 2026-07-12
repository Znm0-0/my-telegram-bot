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

# ===== PYROGRAM CLIENT SETUP =====
app = Client(
    "my_bot",
    api_id=int(API_ID),
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ===== MAIN HANDLER =====
@app.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    """Handle /start command"""
    await message.reply_text("Welcome to the bot! 🔥")

@app.on_message(filters.command("help"))
async def help_handler(client, message: Message):
    """Handle /help command"""
    help_text = """
Available commands:
/start - Start the bot
/help - Show this help message
/ping - Check bot status
"""
    await message.reply_text(help_text)

@app.on_message(filters.command("ping"))
async def ping_handler(client, message: Message):
    """Handle /ping command"""
    await message.reply_to(message, "Pong! 🏓 Bot is running.")

# ===== RUN BOT =====
if __name__ == "__main__":
    print("✅ Bot is running...")
    app.run()