import os
import json
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Environment variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

WHITELIST_FILE = "whitelist.json"
DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR")
PUBLIC_URL = os.getenv("PUBLIC_URL")

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

if not os.path.exists(WHITELIST_FILE):
    with open(WHITELIST_FILE, "w") as file:
        json.dump([], file)

app = Client(
    "restricted_access_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def sanitize_file_name(file_name):
    return file_name.replace(" ", "_")

def load_whitelist():
    with open(WHITELIST_FILE, "r") as file:
        return json.load(file)

def save_whitelist(whitelist):
    with open(WHITELIST_FILE, "w") as file:
        json.dump(whitelist, file)

@app.on_message(filters.private & ~filters.text)
async def download_file(client, message):
    whitelist = load_whitelist()

    if message.from_user.id not in whitelist:
        await message.reply_text("❌ شما دسترسی به این ربات ندارید.")
        return

    if not (message.document or message.video or message.audio or message.photo):
        await message.reply_text("❌ این پیام شامل فایل قابل دانلود نیست.")
        return

    if message.document:
        file_name = message.document.file_name
    elif message.video:
        file_name = message.video.file_name or f"video_{message.id}.mp4"
    elif message.audio:
        file_name = message.audio.file_name or f"audio_{message.id}.mp3"
    else:
        file_name = f"photo_{message.id}.jpg"

    sanitized = sanitize_file_name(file_name)

    buttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("📂 ذخیره عادی", callback_data=f"default_{message.id}"),
            InlineKeyboardButton("✏️ ذخیره با .rar", callback_data=f"rar_{message.id}")
        ]]
    )

    await message.reply_text(
        f"📂 فایل دریافت شد: `{sanitized}`\nروش ذخیره را انتخاب کنید:",
        reply_markup=buttons
    )

@app.on_callback_query()
async def handle_callback_query(client, callback_query):
    action, message_id = callback_query.data.split("_", 1)
    user_id = callback_query.from_user.id

    message = await client.get_messages(user_id, int(message_id))

    if message.document:
        file_name = message.document.file_name
    elif message.video:
        file_name = message.video.file_name or f"video_{message.id}.mp4"
    elif message.audio:
        file_name = message.audio.file_name or f"audio_{message.id}.mp3"
    else:
        file_name = f"photo_{message.id}.jpg"

    sanitized = sanitize_file_name(file_name)

    if action == "default":
        path = os.path.join(DOWNLOAD_DIR, sanitized)
    else:
        path = os.path.join(DOWNLOAD_DIR, f"{sanitized}.rar")

    await message.download(file_name=path)

    public_link = PUBLIC_URL + os.path.basename(path)
    await callback_query.edit_message_text(f"✅ فایل ذخیره شد\n🔗 لینک دانلود:\n{public_link}")

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("سلام 👋\nاین ربات خصوصی است و فقط کاربران مجاز دسترسی دارند.")

@app.on_message(filters.command("add_user") & filters.private)
async def add_user(client, message):
    if message.from_user.id != ADMIN_ID:
        await message.reply_text("❌ دسترسی ندارید.")
        return

    user_id = int(message.text.split()[1])
    whitelist = load_whitelist()

    if user_id not in whitelist:
        whitelist.append(user_id)
        save_whitelist(whitelist)
        await message.reply_text("✅ کاربر اضافه شد.")

@app.on_message(filters.command("remove_user") & filters.private)
async def remove_user(client, message):
    if message.from_user.id != ADMIN_ID:
        await message.reply_text("❌ دسترسی ندارید.")
        return

    user_id = int(message.text.split()[1])
    whitelist = load_whitelist()

    if user_id in whitelist:
        whitelist.remove(user_id)
        save_whitelist(whitelist)
        await message.reply_text("✅ کاربر حذف شد.")

print("Bot is running...")
app.run()
