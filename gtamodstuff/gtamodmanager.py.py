import os
import shutil
import tkinter as tk
from tkinter import messagebox
import winreg  # To check registry keys for Steam and Rockstar game installs

# Registry paths for GTA V installation
rockstar_registry_path = r"SOFTWARE\WOW6432Node\Rockstar Games\Grand Theft Auto V"
steam_registry_path = r"SOFTWARE\WOW6432Node\Valve\Steam\Apps\271590"  # Steam's GTA V AppID

# Paths for default Rockstar and Steam installations (these are default paths and may differ based on the user)
default_steam_path = r"C:\Program Files (x86)\Steam\steamapps\common\Grand Theft Auto V"
default_rockstar_path = r"C:\Program Files\Rockstar Games\Grand Theft Auto V"

# File tracking
injected_files_path = os.path.join(os.getcwd(), "injected_files.txt")  # File to track injected files

# Check if GTA V is installed through Rockstar or Steam
def get_game_version():
    steam_path = None
    rockstar_path = None

    try:
        # Check for Rockstar version (check the registry)
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, rockstar_registry_path) as key:
            rockstar_path = winreg.QueryValueEx(key, "InstallFolder")[0]
        print("Rockstar version detected!")
        return "Rockstar", rockstar_path
    except FileNotFoundError:
        pass

    try:
        # Check for Steam version (check the registry)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, steam_registry_path) as key:
            steam_path = winreg.QueryValueEx(key, "installdir")[0]
        print("Steam version detected!")
        return "Steam", steam_path
    except FileNotFoundError:
        pass

    print("Neither Rockstar nor Steam version detected.")
    return None, None

# Automatically search for gtamodstuff folder on Desktop
def find_gtamodstuff_folder():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    search_folder = "gtamodstuff"
    for root, dirs, files in os.walk(desktop_path):
        if os.path.basename(root).lower() == search_folder.lower():
            return root
    return None

# Determine the correct GTA V installation path
game_version, gta_install_path = get_game_version()

if game_version:
    print(f"Detected {game_version} version of GTA V at: {gta_install_path}")
else:
    print("GTA V is not installed via Rockstar or Steam.")

# Use this path for the target folder
target_folder = gta_install_path if gta_install_path else r"C:\Program Files\Rockstar Games\Grand Theft Auto V"

# Automatically find the gtamodstuff folder
source_folder = find_gtamodstuff_folder()

if source_folder:
    print(f"Found 'gtamodstuff' folder at: {source_folder}")
else:
    print("No 'gtamodstuff' folder found on the Desktop. Please create one.")

def load_injected_files():
    """Load the list of injected files from the tracking file."""
    if os.path.exists(injected_files_path):
        with open(injected_files_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_injected_files(files):
    """Save the list of injected files and folders to the tracking file."""
    with open(injected_files_path, "w") as file:
        for f in files:
            file.write(f"{f}\n")

def inject_scripts():
    """Copy files and folders from source to target and track them."""
    if not source_folder:
        messagebox.showerror("Error", "No 'gtamodstuff' folder found on the Desktop!")
        return

    injected_files = load_injected_files()  # Load previously injected files
    if not os.path.exists(source_folder):
        messagebox.showerror("Error", f"Source folder '{source_folder}' does not exist!")
        return

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    scripts_injected = 0

    # Inject all files and folders
    for item in os.listdir(source_folder):
        item_path = os.path.join(source_folder, item)
        target_path = os.path.join(target_folder, item)

        try:
            if os.path.isfile(item_path):  # If it's a file
                if target_path not in injected_files:  # Avoid duplicates
                    shutil.copy(item_path, target_path)  # Copy the file
                    injected_files.append(target_path)  # Track the file
                    scripts_injected += 1

            elif os.path.isdir(item_path):  # If it's a folder
                if target_path not in injected_files:  # Avoid duplicates
                    if os.path.exists(target_path):
                        shutil.rmtree(target_path)  # Remove existing folder to prevent duplication
                    shutil.copytree(item_path, target_path)  # Copy the entire folder
                    injected_files.append(target_path)  # Track the folder
                    scripts_injected += 1

        except PermissionError:
            messagebox.showerror("Permission Error", f"Permission denied: Unable to copy '{item}' to the target folder.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while copying '{item}': {str(e)}")

    save_injected_files(injected_files)  # Save the updated list of injected files

    if scripts_injected > 0:
        messagebox.showinfo("Success", f"Injected {scripts_injected} items to the target folder.")
    else:
        messagebox.showinfo("Info", "No new files or folders found in the source folder to inject.")

def disable_scripts():
    """Remove files and folders from target that were previously injected."""
    injected_files = load_injected_files()  # Load the list of injected files
    if not os.path.exists(target_folder):
        messagebox.showerror("Error", f"Target folder '{target_folder}' does not exist!")
        return

    if not injected_files:
        messagebox.showinfo("Info", "No injected files or folders to remove.")
        return

    scripts_removed = 0
    for file_path in injected_files:
        if os.path.exists(file_path):  # Check if the file/folder exists before removing
            try:
                if os.path.isfile(file_path):  # If it's a file
                    os.remove(file_path)  # Remove the file
                elif os.path.isdir(file_path):  # If it's a folder
                    shutil.rmtree(file_path)  # Remove the folder and its contents
                scripts_removed += 1
            except PermissionError:
                messagebox.showerror("Permission Error", f"Permission denied: Unable to delete '{file_path}'.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while deleting '{file_path}': {str(e)}")

    save_injected_files([])  # Clear the tracking file after removal

    if scripts_removed > 0:
        messagebox.showinfo("Success", f"Removed {scripts_removed} injected items from the target folder.")
    else:
        messagebox.showinfo("Info", "No files or folders were removed as none were found.")


# Create GUI
root = tk.Tk()
root.title("GTA Mod Manager")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="GTA Mod Manager", font=("Arial", 16))
label.pack(pady=10)

inject_button = tk.Button(frame, text="Inject Needed Scripts", command=inject_scripts, width=25, height=2)
inject_button.pack(pady=5)

disable_button = tk.Button(frame, text="Disable", command=disable_scripts, width=25, height=2)
disable_button.pack(pady=5)

root.mainloop()
