import requests
from bs4 import BeautifulSoup
import hashlib
import time
from keep_alive import keep_alive
import smtplib
from email.mime.text import MIMEText

# === CONFIG ===
JOB_URL = 'https://example.com/jobs'  # Replace with actual job page URL
CHECK_INTERVAL = 600  # in seconds (10 minutes)

# === TELEGRAM CONFIG ===
BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'

# === EMAIL CONFIG (Optional) ===
EMAIL = 'youremail@gmail.com'
APP_PASSWORD = 'your_app_password'  # Gmail app password
RECEIVER = 'youremail@gmail.com'  # Where to send alert

# === Notifier Functions ===
def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=payload)

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = RECEIVER

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

def notify_all(message):
    send_telegram(message)
    try:
        send_email("New Job Alert", message)
    except Exception as e:
        print("Email error:", e)

# === Monitoring Logic ===
def fetch_and_hash():
    response = requests.get(JOB_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    # TODO: Customize this selector to match your job listing section
    job_section = soup.select_one('div.job-list') or soup.body
    return hashlib.md5(str(job_section).encode()).hexdigest()

# === Main Loop ===
def monitor():
    print("🔄 Starting Job Monitor...")
    last_hash = ""
    while True:
        try:
            current_hash = fetch_and_hash()
            if current_hash != last_hash:
                if last_hash:
                    notify_all("🔔 New job update detected at:\n" + JOB_URL)
                    print("📢 Notified!")
                last_hash = current_hash
            else:
                print("✅ No change.")
        except Exception as e:
            print("❌ Error:", e)
        time.sleep(CHECK_INTERVAL)

# === Run Everything ===
keep_alive()
monitor()
