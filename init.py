import pickle, os, shutil

# blah blah blah: welcome message + instructions
print("Kindly refer to the readme\n")
print("Step 1: Here you set the schedule")
print("After \"Start time\", press Enter to exit")
print("Time format: hh-mm, 0-0 to 23-59")

# dict that would store the schedule input
schedule = dict()
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

# taking schedule input
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

# the schedule will be saved as a pickle file named 'schedule' inside 'amj'
with open(os.getcwd() + "\\amj\\schedule", "wb") as f:
    pickle.dump(schedule, f)

# installation of selenium
print("Step 2: The following module will be installed on your system")
print("Selenium")
os.system("pip install selenium")

# taking login details input
print("Step 3: email ID, password")
email = input("Email ID: ").strip()
pwd = input("Password: ").strip()
data = {"email": email, "pwd": pwd}
# saved as amj\accessories
with open(os.getcwd() + "\\amj\\accessories", 'wb') as f:
    pickle.dump(data, f)

# copying the amj folder to C:\
print("Step 5: The folder to C:")
source = os.getcwd() + "\\amj"; destination = r"C:\amj"
os.system("xcopy/E /I " + source + " " + destination)

print("Set up done, close the shell window", end = ' ')
print("if installation is complete. If not, do on your own.")
input()