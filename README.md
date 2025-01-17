# gtamodstuff

Step-by-Step Guide: Installing Python, Using the Script, and Troubleshooting
Step 1: Install Python
Download Python:

Go to the official Python website: https://www.python.org/downloads/
Download the latest version for your operating system (Windows, macOS, or Linux).
Install Python:

Run the installer once it’s downloaded.
Important: During installation, check the box that says "Add Python to PATH" to make it easier to run Python scripts from anywhere.
Click Install Now and follow the prompts.
Verify Python Installation:

Open Command Prompt or Terminal.
Type the following command and press Enter:
bash
Copy
Edit
python --version
You should see the Python version printed, like Python 3.x.x.
Step 2: Using the Script’s UI
Download the Script:

Clone or download the repository from GitHub.
You should have the gtamodmanager.py script saved on your Desktop or a folder you prefer.
Locate gtamodstuff Folder:

Create a folder called gtamodstuff on your Desktop.
Inside this folder, place your GTA V mod files (and any subfolders like MENYOO STUFF, MODS, etc.).
Running the Script:

Double-click the gtamodmanager.py script file to open it.
This will automatically launch the GUI for the GTA Mod Manager.
The UI will have two buttons:
Inject Needed Scripts: This will copy all files and folders from gtamodstuff into your GTA V directory (Rockstar or Steam version).
Disable: This will remove all injected files from the GTA V directory.
UI Usage:
Click Inject Needed Scripts to copy the mods into your GTA V installation directory.
Click Disable to remove all injected files and folders.
Step 3: Running the Script by Double-Clicking
Locate the Script: Find the script (gtamodmanager.py) on your Desktop or where you placed it.

Double-Click to Run: Simply double-click the gtamodmanager.py file. Python will execute it, and the UI will appear.

If the script fails to launch, it may be due to missing permissions or Python not being installed correctly. Follow the troubleshooting steps below.

Step 4: Troubleshooting Common Errors
Here are some common errors you may encounter and how to resolve them:

Error: "Permission Denied":

Cause: The script doesn't have the necessary permissions to access or modify files in protected directories (like C:\Program Files).
Solution: Run the script as Administrator:
Right-click on gtamodmanager.py and select Run as Administrator.
Alternatively, open Command Prompt as Administrator and run the script using the command:
bash
Copy
Edit
python C:\path\to\gtamodmanager.py
Error: "Source Folder Not Found":

Cause: The gtamodstuff folder is not found on your desktop, or it's named incorrectly.
Solution: Ensure the gtamodstuff folder exists on your Desktop and contains the mod files and subfolders (like MENYOO STUFF, MODS).
If it's missing, create a folder called gtamodstuff and put your mod files in it.
Error: "Registry Key Not Found" (for Rockstar or Steam detection):

Cause: The script is trying to detect the game version (Steam or Rockstar) via the Windows registry but couldn't find the correct registry key.
Solution: Make sure your GTA V is installed through either Rockstar Games Launcher or Steam.
If it’s installed via Steam, verify that the correct Steam AppID is set.
For Rockstar, ensure that it’s correctly installed via the Rockstar Launcher.
Error: "Python Not Found":

Cause: Python isn’t installed or not added to the system path.
Solution: Reinstall Python and check "Add Python to PATH" during installation.
Step 5: Installing Notepad++ for Editing (Optional)
If you want to edit the Python script or fix issues in the code, you can use Notepad++, which is a lightweight code editor.

Download and Install Notepad++:
Go to the official Notepad++ website: [https://notepad-plus-plus
