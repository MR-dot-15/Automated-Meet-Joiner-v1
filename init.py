import pickle, os, shutil

print("Kindly refer to the readme\n")
print("Step 1: Here you set the schedule")
print("After \"Start time\", press Enter to exit")
print("Time format: hh, 0 to 23")

schedule = dict()
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

for day in days:
    time_link = []
    print("Day: ", day, end = '\n')
    while True:
        start_time = input("Start time: ").strip()
        if start_time == '':
            break
        link = input("Meet link: ")
        time_link.append((start_time, link))

    schedule[day] = time_link

with open(os.getcwd() + "\\amj\\schedule", "wb") as f:
    pickle.dump(schedule, f)

print("Step 2: The following module will be installed on your system")
print("Selenium")
os.system("pip install selenium")

print("Step 3: email ID, password")
email = input("Email ID: ").strip()
pwd = input("Password: ").strip()
data = {"email": email, "pwd": pwd}
with open(os.getcwd() + "\\amj\\accessories", 'wb') as f:
    pickle.dump(data, f)

print("Step 5: The folder to C:")
source = os.getcwd() + "\\amj"; destination = r"C:\amj"
os.system("xcopy/E /I " + source + " " + destination)

print("Set up done, close the shell window", end = ' ')
print("if installation is complete. If not, do on your own.")
input()