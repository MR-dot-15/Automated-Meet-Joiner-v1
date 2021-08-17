# Automated-Meet-Joiner-v1
A simple python program-bundle to automate meet-joining, only for Windows (Linux-ians are too literate to need this, Mac-ians can pay PA-s to login on behalf of 'em)

## Requirements
1. Python 3.x
2. Chrome browser
3. A MP3 player set as system-default

### Installation procedure
1. Download the zip and extract the files anywhere under ```C:``` drive
2. Run ```init.py```
3. Details needed in this step:
- Schedule details (strict time format: HH-M, M = 0 to 59 [e.g. 13-5, 17-45]) 
- Log-in details (Email ID, Password)
5. If any of the initiation steps fails, please perform it manually and/ or report 
6. Drag-drop/ copy-paste ```move.exe``` to the startup folder (usually at ```C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp```)
7. If the Chrome version is anything but 92, install the Chromedriver for the same version (https://chromedriver.chromium.org/downloads) at ```C:\amj\```

### What to expect
- If ```move.exe``` is moved to the start-up folder, ```main.py``` will get initiated every time the machine starts
- Otherwise, ```main.py``` needs to be executed manually (expectedly sits at ```C:\amj\```)
- Once ```main.py``` starts running, the meet log-ins will occur as per the input schedule
- 10 seconds before every log-in a notification audio will be played (refer to Requirements.3)

### Probable updates
- Weekend-events and scope to edit an already-made schedule
- More customizability 
- Manual cancellation of an upcoming event

### Report at 
- Repository\Issues
- bamchikabnaobnao@gmail.com
