# Deadlock Lobby Background Randomizer

I tried to make a script that made the customization of the lobby background as similar to wallpaper engine as possible.

## Contents:
- [How to compile .exe](https://github.com/ShelbyPop/DeadlockBackgroundRandomizer/tree/main?tab=readme-ov-file#how-to-compile-exe)
- [Adding Additional Backgrounds](https://github.com/ShelbyPop/DeadlockBackgroundRandomizer/tree/main?tab=readme-ov-file#adding-additional-backgrounds)
- [Automating Script like Wallpaper Engine](https://github.com/ShelbyPop/DeadlockBackgroundRandomizer/tree/main?tab=readme-ov-file#automating-script-like-wallpaper-engine)
  - [Open Task Scheduler](https://github.com/ShelbyPop/DeadlockBackgroundRandomizer/tree/main?tab=readme-ov-file#open-task-scheduler)



## How to compile .exe

Install Latest version of python at https://www.python.org/downloads/

Open terminal (Powershell in windows) and type the following:
```bash
pip install pyinstaller
```

After installing pyinstaller, find the location of the folder where BackgroundRandomizer.py is located, and type:
```bash
pyinstaller --onefile BackgroundRandomizer.py
```

The BackgroundRandomizer.exe file will be found in the /dist/ folder, and can be moved out of the folder.

Launching this .exe will open terminal for a brief second before exiting immediately after, and you should see the Deadlock lobby background change to one of the 3 presets I included in the /Backgrounds/ folder.

---

## Adding Additional Backgrounds

Locate the /Backgrounds/ Folder.

You should see three included folders, 'GogetaBlue', 'KITABOCCHIPANIC', 'MikuShrek'.
![image](https://github.com/user-attachments/assets/906869f9-430c-49f6-a08a-2ce1a85ecce7)


You may add any folders of videos you wish, even .mp4s, just know that there won't be any sound, until me or someone else figures out how to do this on a file-per-file basis, or to work with the script.

NOTE: Do not delete the 'ORIGINAL, DO NOT DELETE', it includes the base deadlock lobby file and is used as a backup should something fail.

When putting your videos, name the folder whatever, but make sure that the file within the folder has the filename 'menu_streets_loop2.webm' or else the game will *not* use the file.

## Automating Script like Wallpaper Engine

First, install the pythonw package. This package allows running of pythonscripts without opening terminal, so it doesn't alt-tab you from the middle of a game.

```bash
pip install pythonw
```

Next, locate where the pythonw.exe file is located, this can be done by typing the following:

```bash
python -c "import sys; print(sys.executable)"
```
This should print the location of python.exe, please navigate to the folder (remove the python.exe bit from the file path), and verify that pythonw.exe is installed there.

Next, right click on pythonw.exe, and select 'copy as path'. Keep this to your clipboard as it is needed for the next step.

### Open Task Scheduler

Click on 'Create Task...'
![image](https://github.com/user-attachments/assets/92d30e57-5c9b-4bed-a215-44a731330d7a)

Type whatever you want for the name and description, I have mostly everything as default. "Run with highest privileges" shouldn't be necessary, but may vary on the system.

![image](https://github.com/user-attachments/assets/0a61ebaf-1199-4a0f-9b3d-a7ba42a63098)


Go to the 'Triggers' tab, and click "New...", and use the settings as follows.
NOTE: Your start date and time will differ, this is fine, set the time for whenever you want the program to run for the first time. Since we're not done setting up, set it for something like 5 minutes in the future.
Also, don't forget to check 'enabled'.

![image](https://github.com/user-attachments/assets/dd28472e-c629-41e5-8361-5e92462e8c41)

Go to the 'Actions' Tab, click "New...", and copy and paste the pythonw.exe file path from before into the 'program/script' option as shown:

![image](https://github.com/user-attachments/assets/8dfd8bb5-6a81-400d-a11b-21e0625460c1)

- For 'Add arguments' just add "BackgroundRandomizer.py" 
- For 'Start in', add the file path for the DeadlockBackgroundRandomizer-main folder location.


--- 

And you're done! Please DM me on discord @shelby.uwu or in the channel https://discord.com/channels/1231286446472691825/1284190624563724411 where @HappyAnton3 made the initial tutorial. 

I should note, the program will not run if you're in lobby, but if you want to quick shuffle it, just go into sandbox, launch the .exe, and return back to lobby. It may pick the same background as you previously had, so just repeat if you want a different one.

Happy Shuffling!



