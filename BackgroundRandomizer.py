import os
import shutil
import sys
import random
# Note, This is for Windows Machines only, unknown if works on others
# Created by Shelby.uwu on discord, aka ShelbyPop (Sept/16/2024)

def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller 
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



# NOTE: THE BELOW DESTINATION PATH MAY NOT BE ACCURATE, PLEASE CHECK FOR YOURSELF AND REPLACE IF DIFFERENT FOR YOUR SYSTEM
DESTINATION_PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Deadlock\\game\\citadel\\panorama\\videos\\main_menu\\menu_streets_loop2.webm"

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the "Backgrounds" folder
BACKGROUNDS_DIR = os.path.join(SCRIPT_DIR, "Backgrounds")

# Name of the folder to exclude
EXCLUDE_FOLDER = "ORIGINAL, DO NOT DELETE"



def get_background_folders():
    # Get all background folders in the Backgrounds directory, excluding the original folder.
    if not os.path.exists(BACKGROUNDS_DIR):
        sys.exit(f"Error: Backgrounds folder not found at {BACKGROUNDS_DIR}")
    
    folders = [f for f in os.listdir(BACKGROUNDS_DIR) 
               if os.path.isdir(os.path.join(BACKGROUNDS_DIR, f)) and f != EXCLUDE_FOLDER]
    return folders

def get_random_background(folders):
    # Choose a random background folder and return the path to the video file.
    if not folders:
        sys.exit("Error: No background folders found (excluding the original folder).")
    
    chosen_folder = random.choice(folders)
    video_path = os.path.join(BACKGROUNDS_DIR, chosen_folder, "menu_streets_loop2.webm")
    
    if not os.path.exists(video_path):
        sys.exit(f"Error: menu_streets_loop2.webm not found in {chosen_folder}")
    
    return video_path

def main():
    

    # Get all background folders (excluding the original)
    bg_folders = get_background_folders()
    # Choose a random background
    chosen_bg = get_random_background(bg_folders)
    # Remove existing file at destination if it exists
    if os.path.exists(DESTINATION_PATH):
        os.remove(DESTINATION_PATH)
    
    # Copy the chosen background to the destination
    try:
        shutil.copy(chosen_bg, DESTINATION_PATH)
        print(f"Successfully copied {chosen_bg} to {DESTINATION_PATH}")
    except FileNotFoundError:
        print(f"Error: The destination path {DESTINATION_PATH} does not exist.")
        print("The game files may have moved or been updated.")
        print("Please update the DESTINATION_PATH in the script.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()