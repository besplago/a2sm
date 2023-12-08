'''Main module for adding th given program to the start menu path.'''

import os
import sys
import win32com.client

def add_to_start_menu(program_path):
    '''Adds the given program to the start menu path.'''
    # Validate if the provided file exists
    if not os.path.exists(program_path):
        print(f"Error: The specified file '{program_path}' does not exist.")
        return

    # Get the user's home directory
    user_home = os.path.expanduser("~")

    # Construct the Start Menu Programs path
    start_menu_programs_path = os.path.join(user_home, "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs")

    # Create a shortcut file in the Start Menu Programs directory
    program_name = os.path.basename(program_path)
    shortcut_path = os.path.join(start_menu_programs_path, f"{program_name}.lnk")

    try:
        # Use win32com.client to create a shortcut
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.TargetPath = program_path
        shortcut.save()
        print(f"Success: '{program_name}' added to Start Menu/Programs.")
    except Exception as e:
        print(f"Error: Failed to create shortcut - {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_to_start_menu.py <path_to_exe>")
    else:
        exe_path = sys.argv[1]
        add_to_start_menu(exe_path)
