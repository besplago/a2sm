'''Main module for adding th given program to the start menu path.'''

import os
import sys
import win32com.client

def _add_to_start_menu(program_path: str, shortcut_name: str) -> None:
    # Validate if the provided file exists
    if not os.path.exists(program_path):
        print(f"Error: The specified file '{program_path}' does not exist.")
        return

    # Get the user's home directory
    user_home: str = os.path.expanduser("~")

    # Construct the Start Menu Programs path
    start_menu_programs_path: str = os.path.join(
        user_home, "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs"
    )

    # Create a shortcut file in the Start Menu Programs directory
    shortcut_path: str = os.path.join(start_menu_programs_path, f"{shortcut_name}.lnk")

    try:
        _create_shortcut(program_path, shortcut_path)
        print(f"Successfully created shortcut '{shortcut_name}' in the Start Menu.")
    except Exception as e:
        print(f"Error: Failed to create shortcut - {str(e)}")
        return

    # Open the Start Menu Programs directory
    os.startfile(start_menu_programs_path)

def _create_shortcut(program_path: str, shortcut_path: str) -> None:
    # Create a shell object
    shell: win32com.client.Dispatch = win32com.client.Dispatch("WScript.Shell")

    # Create a shortcut object
    shortcut: win32com.client.Dispatch = shell.CreateShortcut(shortcut_path)

    # Set the shortcut's target
    shortcut.TargetPath = program_path

    # Set the shortcut's working directory
    shortcut.WorkingDirectory = os.path.dirname(program_path)

    # Save the shortcut
    shortcut.Save()

def main():
    '''Main function for adding the given program to the start menu path.'''
    if len(sys.argv) != 3:
        print("Usage: a2sm <path_to_program> <shortcut_name>")
    else:
        program_path: str = sys.argv[1]
        shortcut_name: str = sys.argv[2]
        _add_to_start_menu(program_path, shortcut_name)

if __name__ == "__main__":
    main()
