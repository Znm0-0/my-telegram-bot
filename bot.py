import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

# 1. الإعدادات
API_ID = 34644436
API_HASH = "2d0a19706e5c3de7fa2969250ad66ad7"
BOT_TOKEN = "8192761045:AAHWGKwdB6s0cYoixwFK--NiQy31PMyHVs0"

# 2. إعداد البوت
logging.basicConfig(level=logging.INFO)
app = Client("ultra_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, workers=500)

# 3. دالة الاستجابة الآمنة
async def safe_reply(message, text, reply_markup=None):
    try:
        await message.reply_text(text, reply_markup=reply_markup)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await message.reply_text(text, reply_markup=reply_markup)

# 4. أمر البداية مع واجهة جميلة
@app.on_message(filters.command("start"))
async def start_command(client, message):
    text = (
        "🚀 **أهلاً بك في المحرك الخارق (Ultra Bot)**\n\n"
        "✅ **الحالة:** `يعمل بكامل الطاقة`\n"
        "⚡ **الأداء:** `100,000x`\n\n"
        "اختر العملية التي تريد تنفيذها من القائمة أدناه:"
    )
    
    # واجهة الأزرار الجميلة
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔍 فحص OSINT", callback_data="osint"),
         InlineKeyboardButton("🛡 حماية الحساب", callback_data="protect")],
        [InlineKeyboardButton("⚙️ إعدادات المحرك", callback_data="settings"),
         InlineKeyboardButton("ℹ️ مساعدة", callback_data="help")]
    ])
    
    await safe_reply(message, text, reply_markup=buttons)

# 5. معالج الأزرار (التفاعل)
@app.on_callback_query()
async def callback_handler(client, callback_query):
    command = callback_query.data
    if command == "osint":
        await callback_query.answer("جاري تشغيل أدوات الفحص...", show_alert=True)
    elif command == "protect":
        await callback_query.answer("تفعيل نظام الحماية المتطور...", show_alert=True)
    else:
        await callback_query.answer("قيد التطوير...")

# 6. التشغيل
if __name__ == "__main__":
    print("البوت بدأ العمل بنجاح...")
    app.run()