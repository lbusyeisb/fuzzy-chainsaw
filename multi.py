from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from supabase import create_client, Client
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import string
import random

SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "gaslagi"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))

    # return random.choice(string.ascii_letters)


with open("x.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        kw = line[0]

        def web_driver():
            options = webdriver.ChromeOptions()
            options.add_argument("--verbose")
            # options.add_argument('--no-sandbox')
            # options.add_argument('--headless')
            options.add_argument("--disable-gpu")
            # options.add_argument("--window-size=1920, 1200")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=options)
            return driver

        driver = web_driver()
        driver.maximize_window()

        try:

            nama_modif = kw.replace(" ", "-")
            gmail = f"{nama_modif}-onlyfans-yvi{random_string(6)}@gmail.com"
            slug = f"fs-{nama_modif}-telegram-chanel-x{random_string(6)}"

          
            
            judul = f"*# {kw} -Telegram Catalog"
            
            link = f"https://clipsfans.com/bento/?title= CLICK HERE >> {kw} "


            driver.get(
                    "https://bento.me/signup?ref=techcrunch&app=wetransferflow&atb=true"
                )
            time.sleep(3)

                # Isi form dengan slug
            driver.find_element(By.CSS_SELECTOR, "input[placeholder='your-name']").send_keys(slug)
            time.sleep(15)         


            def inputslug():

                driver.get(
                    "https://bento.me/signup?ref=techcrunch&app=wetransferflow&atb=true"
                )
                time.sleep(3)

                # Isi form dengan slug
                driver.find_element(By.CSS_SELECTOR, "input[placeholder='your-name']").send_keys(slug)
                time.sleep(25)         


            try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "colored")))
                driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
                time.sleep(2)
            except TimeoutException:
                print("Elemen tidak muncul dalam 10 detik, reload halaman.")
                inputslug()


            time.sleep(2)
            driver.find_element(
                By.CSS_SELECTOR, "input[placeholder='Email address']"
            ).send_keys(gmail)
            driver.find_element(
                By.CSS_SELECTOR, "input[placeholder='Password']"
            ).send_keys("@@Kamudia12sPos")
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            time.sleep(15)

            driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

            driver.find_element(
                By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div[2]/button[1]"
            ).click()

            time.sleep(3)

            driver.find_element(
                By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div[3]/button[1]/div[1]"
            ).click()

            time.sleep(3)

            driver.find_element(
                By.XPATH, "/html/body/div[2]/div[1]/div/div/div/button"
            ).click()
            time.sleep(5)

            # Ketik judul pada editor
            driver.find_element(
                By.CSS_SELECTOR, "div[contenteditable='true'].ProseMirror.rt-editor"
            ).send_keys(judul)
            time.sleep(1)

            konten = f"{kw} Leaked Video Original Video Viral Video Leaked on X Twitter Telegram \n [-FULL-]— {kw} ʟᴇᴀᴋᴇᴅ Video ᴠɪʀᴀʟ On Social Media Twitter \n Leaked Video {kw} Original Video Viral Video Leaked on X Twitter.. \n"
            driver.find_element(
                By.XPATH, "/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div"
            ).send_keys(konten)
            time.sleep(7)

            driver.switch_to.default_content()
            # Klik tombol untuk submit
            driver.find_element(
                By.XPATH,
                "/html[1]/body[1]/div[1]/main[1]/div[3]/div[2]/button[1]/div[1]",
            ).click()
            time.sleep(5)

            # Isi link dan simpan hasil
            driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[2]/form[1]/input[1]"
            ).send_keys(link)
            time.sleep(2)

            driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[2]/div[1]/button[1]"
            ).click()
            time.sleep(5)

            # with open("result.txt", "a") as f:
            #     f.write(driver.current_url + "\n")

            response = (
                supabase.table(SUPABASE_TABLE_NAME)
                .insert({"result": driver.current_url})
                .execute()
            )

            print(f"SUKSES CREATE: {kw}")

            time.sleep(5)
            driver.close()
        except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")
            driver.close()
