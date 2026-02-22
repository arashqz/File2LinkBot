# FileGateBot

A restricted Telegram bot for downloading files and generating public download links.  
ربات تلگرامی با دسترسی محدود برای دانلود فایل و ساخت لینک دانلود عمومی.

---

## 📌 معرفی | Introduction

### 🇮🇷 فارسی
**FileGateBot** یک ربات تلگرامی حرفه‌ای است که به کاربران مجاز اجازه می‌دهد فایل‌های خود را ارسال کرده و لینک دانلود عمومی دریافت کنند.  
دسترسی کاربران از طریق **Whitelist** مدیریت می‌شود و فقط ادمین امکان اضافه یا حذف کاربران را دارد.

این پروژه با رعایت کامل اصول امنیتی طراحی شده و تمامی اطلاعات حساس از طریق **Environment Variables** مدیریت می‌شوند.

### 🇬🇧 English
**FileGateBot** is a professional Telegram bot that allows authorized users to upload files and receive public download links.  
Access is controlled using a **whitelist**, and only the admin can manage allowed users.

The project follows security best practices by using **environment variables** for all sensitive data.

---

## ✨ ویژگی‌ها | Features

- 🔐 دسترسی محدود با Whitelist  
- 📥 دانلود فایل‌های ارسالی (Document, Video, Audio, Photo)  
- 🔗 تولید لینک دانلود عمومی  
- 🧾 مدیریت کاربران توسط ادمین  
- ⚙️ استفاده از Environment Variables  
- 🚀 مناسب برای GitHub و Open Source  

---

## 👤 سازنده | Author

**arashqz**  
Telegram: [@arashqz](https://t.me/arashqz)

---

## ⚙️ نصب و اجرا | Installation & Run

### 1️⃣ کلون کردن پروژه | Clone repository
```bash
git clone https://github.com/arashqz/File2LinkBot.git
cd file-gate-bot
```

### 2️⃣ نصب وابستگی‌ها | Install requirements
```bash
pip install -r requirements.txt
```

### 3️⃣ ساخت فایل `.env`
بر اساس `.env.example` یک فایل `.env` بسازید:

```env
API_ID=12345678
API_HASH=your_api_hash_here
BOT_TOKEN=your_bot_token_here
ADMIN_ID=123456789
DOWNLOAD_DIR=/path/to/downloads
PUBLIC_URL=https://example.com/downloads/
```

### 4️⃣ اجرای ربات | Run the bot
```bash
python bot.py
```

---

## 📝 دستورات ربات | Bot Commands

| Command | Description |
|-------|------------|
| `/start` | شروع ربات |
| `/add_user <id>` | افزودن کاربر به whitelist (ادمین) |
| `/remove_user <id>` | حذف کاربر از whitelist (ادمین) |

---

## 📂 ساختار پروژه | Project Structure

```
file-gate-bot/
│
├─ bot.py             # کد اصلی ربات
├─ whitelist.json     # لیست کاربران مجاز (ignored)
├─ downloads/         # فایل‌های دانلود شده (ignored)
├─ .env.example       # نمونه تنظیمات محیطی
├─ requirements.txt   # وابستگی‌ها
├─ .gitignore         # فایل ignore
└─ README.md
```

---

## 🔒 نکات امنیتی | Security Notes

- هرگز فایل `.env` را در GitHub قرار ندهید  
- `whitelist.json` و `downloads/` در `.gitignore` قرار دارند  
- از توکن‌ها و API واقعی فقط روی سرور استفاده کنید  

---

## 📜 لایسنس | License

This project is released under the **MIT License**.  
You are free to use, modify, and distribute this project.

---

**FileGateBot**  
Secure • Private • Professional  
Author: `arashqz` | Telegram: @arashqz
