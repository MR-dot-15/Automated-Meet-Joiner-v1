"""
    fetched by move.exe everytime the machine starts
    loads the schedule for that day and uses meet_joiner.py to join meets
    as per the schedule input
"""

import pickle, os, datetime, time, meet_joiner, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from termcolor import colored

# access to mic, camera, permission to show notifications granted
# access to location denied
# chrome window will start with its maximum geometry
opt = Options()
opt.add_argument('--start-maximized')
opt.add_argument('log-level=3')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})

# just something fancy; self-explanatory
def convert_to_am_pm(hour, minute): 
    if len(minute) == 1:
        minute = '0' + minute
    if int(hour) < 12:
        return hour + ':' + minute + ' am'
    else:
        return str(int(hour) - 12) + ':' + minute + ' pm'

# welcome note
welcome = colored("Have a great day, pal!", 'blue', \
    attrs = ['bold'])
print(welcome)

# loading login details
with open("accessories", 'rb') as f:
    accessories = pickle.load(f)

# date-time,right now 
td = datetime.datetime.now()
today = td.strftime("%a")

# loads the schedule for that day
# executes Except block if none found
try:
    with open('schedule', 'rb') as f:
        today_schedule = pickle.load(f)[today]
except:
    text = colored("No event found today", 'red')
    print(text)
    print("Press ENTER to exit")
    input(); sys.exit()

# main body, accesses the events in the schedule one by one
for event in today_schedule:
    [hr_part, min_part] = event[0].split('-')
    # no event from past, this is no time machine
    if int(hr_part) - int(datetime.datetime.now().strftime("%H")) < 0:
        continue

    # next event at ...
    event_display = colored("Next event at " + \
        convert_to_am_pm(hr_part, min_part), 'cyan')
    print(event_display)

# sets the pause timer 
    time_now = datetime.datetime.now()
    # determining time left, till 5 min before the event
    time_hr, time_min = int(time_now.strftime("%H")), \
        int(time_now.strftime("%M"))
    pause_in_min = int(hr_part) * 60 + int(min_part)\
        - (time_hr * 60 + time_min) - 5
    # if time left < 5 mins, the joining time is set to 1 min before
    if pause_in_min <= 0:
        pause_in_min = int(hr_part) * 60 + int(min_part)\
        - (time_hr * 60 + time_min) - 1
    pause_display = colored("Paused for " + str(pause_in_min) + \
        ' Min(s)', 'cyan')
    print(pause_display)
    time.sleep(pause_in_min * 60)

    # plays the notification: error if no default MP3 player is found
    os.system('C:\\amj\\notif.mp3')

    # sme text etc etc
    event_start = colored("-----------------Event at " + \
        event[0] + "-----------------", 'green')
    print(event_start)
    time.sleep(10)

    # initiates a driver instance and uses meet_joiner.py
    driver = webdriver.Chrome(r"C:\amj\chromedriver.exe", options = opt)
    meet_joiner.join_meet(accessories["email"], \
        accessories["pwd"], event[1], driver)

    # some formality lol
    if today_schedule[-1] == event:
        end_display = colored("Done for the day, bravo!", 'red')
        print(end_display)