import os
import shutil
import sys
import random
# Note, This is for Windows Machines only, unknown if works on others
# Created by Shelby.uwu on discord, aka ShelbyPop (Sept/16/2024)

# Also, make sure to rename the video files you wish to add to the "menu_streets_loop2.webm" base name.
# Add an escape \ to every '\' that already exists, or it won't work.

# In game

# NOTE: THE BELOW DESTINATION PATH MAY NOT BE ACCURATE, PLEASE CHECK FOR YOURSELF AND REPLACE IF DIFFERENT FOR YOUR SYSTEM
DESTINATION_PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Deadlock\\game\\citadel\\panorama\\videos\\main_menu\\menu_streets_loop2.webm"

# This folder should contain a "ORIGINAL, DO NOT DELETE" folder containing a copy of the original background, put that file path below.
BG_Default = "<Original background file path>"

# If you increase to BG_6 or further, please increase this value. (If have up to BG_8, change to an 8 below)
NUM_BACKGROUNDS = 5
# Chosen Background File Locations.
BG_1 = "<Background 1 location file path>"
BG_2 = "<Background 2 location file path>"
BG_3 = "<Background 3 location file path>"
BG_4 = "<Background 4 location file path>"
BG_5 = "<Background 5 location file path>"
def main():
    # randint range includes final num
    num = random.randint(1,NUM_BACKGROUNDS)
    
    if os.path.exists(DESTINATION_PATH):
        os.remove(DESTINATION_PATH)
    else:
        sys.exit("Error 1: File not found in destination. Please place original Deadlock Lobby Background in file location.")
    
    match num:
        case 1:
            if os.path.exists(BG_1):
                shutil.copy(BG_1, DESTINATION_PATH)
            else:
                sys.exit("BG_1 could not be copied")
        case 2:
            if os.path.exists(BG_2):
                shutil.copy(BG_2, DESTINATION_PATH)
            else:
                sys.exit("BG_2 could not be copied")
        case 3:
            if os.path.exists(BG_3):
                shutil.copy(BG_3, DESTINATION_PATH)
            else:
                sys.exit("BG_3 could not be copied")
        case 4:
            if os.path.exists(BG_4):
                shutil.copy(BG_4, DESTINATION_PATH)
            else:
                sys.exit("BG_4 could not be copied")                
        case 5:
            if os.path.exists(BG_5):
                shutil.copy(BG_5, DESTINATION_PATH)
            else:
                sys.exit("BG_5 could not be copied")        
    


if __name__=="__main__":
    main()