# 🔍 Webpage Montitor with Telegram & Gmail Alerts

> **A lightweight Python tool that monitors job listings and sends real-time alerts via Telegram and Gmail.**

---

## 🚀 Features

- ✅ Monitor any custom job listing URL for changes
- ✅ Instant alerts via Telegram bot
- ✅ Optional Gmail email notifications
- ✅ 24/7 operation using Replit + UptimeRobot
- ✅ Easy to set up, fully customizable, open-source

---

## 🔧 Requirements

- Python 3.7+
- The following Python libraries (listed in `requirements.txt`):
  - `requests`
  - `beautifulsoup4`
  - `flask`

---

## 📂 Project Structure

job-monitor/
- ├── main.py # Main monitoring and notification logic
- ├── keep_alive.py # Flask server to keep Replit project running
- ├── requirements.txt # Python dependencies
- ├── README.md # Project description (this file)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/yourusername/job-monitor.git
cd job-monitor
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Configure the Script
Edit main.py and set your values:

- JOB_URL = 'https://example.com/jobs'  # Replace with real job listing URL

- BOT_TOKEN = 'your_telegram_bot_token'

- CHAT_ID = 'your_chat_id'

- EMAIL = 'your_gmail@gmail.com'              # Optional

- APP_PASSWORD = 'your_gmail_app_password'    # Optional

- RECEIVER = 'receiver_email@gmail.com'       # Optional

💡 For Gmail: Enable 2FA and create an App Password from https://myaccount.google.com/apppasswords
https://myaccount.google.com/apppasswords

---

## 🧠 How It Works
- The script fetches the specified job listing page at regular intervals.
- It hashes the relevant section (HTML) to detect changes.
- If the hash changes, it triggers a Telegram message and optionally sends an email.

### 🟢 Running the Script
Locally
```
python main.py
```

---

## 📬 Notification Examples

### 🔔 Telegram

🔔 New job update detected at: https://example.com/jobs
### 📧 Email

- Subject: New Job Alert

- Body: A new job has been posted on: https://example.com/jobs

---

## ✨ Future Improvements

- Keyword-based job filtering

- Save detected job titles to local storage or DB

- Add login/session support for private job boards

---

## 📄 License

- Please feel free to use, modify, and share it as needed.

---

## 🙌 Contributing

- Pull requests are welcome.

- If you find bugs or want to suggest a feature, open an issue or submit a PR!

---

## 👤 Author

- Made by Muhammad Umar Aiba


