# Automated-Meet-Joiner-v1
A simple python program-bundle to automate meet-joining, only for Windows (Linux-ians are too literate to need this, Mac-ians can pay PA-s to login on behalf of 'em)

### Installation procedure
1. Download the zip and extract the files anywhere under ```C:``` drive
2. Run ```init.py```
3. Details needed in this step:
- Schedule details 
- Log-in details
5. If any of the initiation steps fails, please perform it manually
6. Move/ copy-paste ```move.exe``` to the startup folder (usually at ```C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp```)

### Supposed to do
- If ```move.exe``` is moved to the start-up folder, it will get initiated every time the machine starts
- Otherwise, the ```main.py``` needs to be executed manually (expectedly sits at ```C:\amj\```)
- Once ```main.py``` starts running, the meet log-ins will occur as per the input schedule

### Probable updates
- Weekend-events and permission to edit an already-made schedule
- More customizability 
