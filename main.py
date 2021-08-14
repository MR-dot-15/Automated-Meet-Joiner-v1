import pickle, os, datetime, time, meet_joiner, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})

print("Have a great day, dear!")

with open("accessories", 'rb') as f:
    accessories = pickle.load(f)

td = datetime.datetime.now()
today = td.strftime("%a")

try:
    with open('schedule', 'rb') as f:
        today_schedule = pickle.load(f)[today]
except:
    print("No event found today")
    input(); sys.exit()

for event in today_schedule:
    if int(event[0]) - int(datetime.datetime.now().strftime("%H")) < 0:
        continue
    while True:
        hour = int(datetime.datetime.now().strftime("%H"))
        if hour == int(event[0]) - 1:
            minute = int(datetime.datetime.now().strftime("%M"))
            pause_for = 55 - int(minute)
            time.sleep(pause_for * 60)
            os.system('C:\\amj\\notif.mp3')
            print("----------------Event at " + event[0] + "----------------")
            time.sleep(10)
            driver = webdriver.Chrome(r"D:\chromedriver.exe", options = opt)
            meet_joiner.join_meet(accessories["email"], \
                accessories["pwd"], event[1], driver)
            break
        pause_for = 45
        time.sleep(pause_for * 60)   