from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from supabase import create_client, Client
import time
import csv
import string
import random
from multiprocessing import Pool

# Konfigurasi Supabase
SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "gaslagi"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def random_string(count):
    return "".join(random.choice(string.ascii_letters) for _ in range(count))


def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver


def process_keyword(kw):
    driver = web_driver()
    driver.maximize_window()
    try:
        slug = f"fs-{kw.replace(' ', '-')}-x{random_string(6)}"
        gmail = f"{kw.replace(' ', '_')}-{random_string(6)}@gmail.com"
        judul = f"*# {kw} - Telegram Catalog"
        link = f"https://clipsfans.com/bento/?title={kw}"

        # Akses halaman dan isi form
        driver.get("https://bento.me/signup?ref=techcrunch&app=wetransferflow&atb=true")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='your-name']").send_keys(slug)
        time.sleep(20)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Isi email dan password
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email address']").send_keys(gmail)
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("YourSecurePassword123")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(5)

        # Isi konten
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true']").send_keys(judul)
        driver.switch_to.default_content()
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
        time.sleep(5)

        # Simpan hasil ke Supabase
        supabase.table(SUPABASE_TABLE_NAME).insert({"keyword": kw, "result": driver.current_url}).execute()
        print(f"Sukses: {kw}")
    except Exception as e:
        print(f"Error pada {kw}: {str(e)}")
    finally:
        driver.quit()


if __name__ == "__main__":
    with open("x.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        keywords = [line[0] for line in csv_reader]

    # Jalankan secara paralel
    with Pool(processes=4) as pool:  # Ubah 4 sesuai jumlah core CPU Anda
        pool.map(process_keyword, keywords)
