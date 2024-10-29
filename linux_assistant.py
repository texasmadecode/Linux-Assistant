import os
import shutil
from datetime import datetime
import webbrowser

# Command Explanations for Quick Help
command_help = {
    "ls": "Lists directory contents.",
    "cat": "Displays the contents of a file.",
    "cp": "Copies files or directories.",
    "mv": "Moves files or directories.",
    "rm": "Deletes files or directories.",
    "mkdir": "Creates a new directory.",
    "chmod": "Changes file permissions.",
}

def list_files():
    """List all files in the current directory."""
    print("\nFiles in the current directory:")
    for file in os.listdir('.'):
        print(file)
    print()

def delete_file():
    """Delete a specified file."""
    filename = input("Enter the name of the file to delete: ")
    if os.path.isfile(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    else:
        print(f"File '{filename}' does not exist.")

def view_file():
    """View the contents of a specified file."""
    filename = input("Enter the name of the file to view: ")
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            content = file.read()
        print(f"\nContents of '{filename}':\n{content}\n")
    else:
        print(f"File '{filename}' does not exist.")

def search_in_file():
    """Search for a term in a specified file."""
    filename = input("Enter the name of the file to search in: ")
    if os.path.isfile(filename):
        search_term = input("Enter the term to search for: ")
        with open(filename, 'r') as file:
            content = file.readlines()
        found = any(search_term in line for line in content)
        if found:
            print(f"The term '{search_term}' was found in '{filename}'.")
        else:
            print(f"The term '{search_term}' was NOT found in '{filename}'.")
    else:
        print(f"File '{filename}' does not exist.")

def create_directory():
    """Create a new directory."""
    dirname = input("Enter the name of the directory to create: ")
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        print(f"Directory '{dirname}' created successfully.")
    else:
        print(f"Directory '{dirname}' already exists.")

def copy_file():
    """Copy a specified file."""
    src_filename = input("Enter the name of the file to copy: ")
    if os.path.isfile(src_filename):
        dest_filename = input("Enter the name of the new file: ")
        shutil.copy(src_filename, dest_filename)
        print(f"File '{src_filename}' copied to '{dest_filename}' successfully.")
    else:
        print(f"File '{src_filename}' does not exist.")

def move_file():
    """Move a specified file."""
    src_filename = input("Enter the name of the file to move: ")
    if os.path.isfile(src_filename):
        dest_directory = input("Enter the destination directory: ")
        if os.path.exists(dest_directory):
            shutil.move(src_filename, os.path.join(dest_directory, src_filename))
            print(f"File '{src_filename}' moved to '{dest_directory}' successfully.")
        else:
            print(f"Destination directory '{dest_directory}' does not exist.")
    else:
        print(f"File '{src_filename}' does not exist.")

def rename_file():
    """Rename a specified file."""
    old_filename = input("Enter the current name of the file: ")
    if os.path.isfile(old_filename):
        new_filename = input("Enter the new name of the file: ")
        os.rename(old_filename, new_filename)
        print(f"File '{old_filename}' renamed to '{new_filename}' successfully.")
    else:
        print(f"File '{old_filename}' does not exist.")

def show_help(command):
    """Show help for a specific command."""
    if command in command_help:
        print(f"{command}: {command_help[command]}")
    else:
        print(f"No help available for '{command}'.")

def check_permissions():
    """Check permissions of a specified file."""
    filename = input("Enter the name of the file to check permissions: ")
    if os.path.isfile(filename):
        permissions = oct(os.stat(filename).st_mode)[-3:]
        print(f"Permissions for '{filename}': {permissions}")
    else:
        print(f"File '{filename}' does not exist.")

def open_web():
    """Open a URL in the default web browser."""
    url = input("Enter the URL you want to open: ")
    webbrowser.open(url)
    print(f"Opening {url} in your web browser.")

def display_commands_summary(used_commands):
    """Display summary of frequently used commands."""
    print("\nSummary of commands used in this session:")
    for command, count in used_commands.items():
        print(f"{command}: used {count} time(s)")
    print("Thanks for using computer_Terminal!")

# Main program starts here
current_time_local = datetime.now()
print("computer_Terminal")
print("Version 1.0")
print("Bytesec Inc.")
print()
print("Current Time:", current_time_local.strftime("%Y-%m-%d %I:%M %p"))

used_commands = {}

while True:
    answer = input(
        "\nWhat do you want to do today?\n"
        " a. Make file\n"
        " b. Add to file\n"
        " c. List files\n"
        " d. Delete file\n"
        " e. View file\n"
        " f. Search in file\n"
        " g. Create directory\n"
        " h. Copy file\n"
        " i. Move file\n"
        " j. Rename file\n"
        " k. Check permissions\n"
        " l. Open Web\n"
        " m. Help\n"
        " n. Exit\n"
    ).strip().lower()

    # Increment command usage for summary
    used_commands[answer] = used_commands.get(answer, 0) + 1

    if answer == 'a':
        filename = input("Enter the name of the file to create: ")
        with open(filename, 'w') as file:
            file.write("This is a new file.\n")
        print(f"File '{filename}' created successfully.")

    elif answer == 'b':
        filename = input("Enter the name of the file to add to: ")
        if os.path.isfile(filename):
            content = input("Enter content to add to the file: ")
            with open(filename, 'a') as file:
                file.write(content + '\n')
            print(f"Content added to '{filename}' successfully.")
        else:
            print(f"File '{filename}' does not exist. Please create it first.")

    elif answer == 'c':
        list_files()

    elif answer == 'd':
        delete_file()

    elif answer == 'e':
        view_file()

    elif answer == 'f':
        search_in_file()

    elif answer == 'g':
        create_directory()

    elif answer == 'h':
        copy_file()

    elif answer == 'i':
        move_file()

    elif answer == 'j':
        rename_file()

    elif answer == 'k':
        check_permissions()

    elif answer == 'l':
        open_web()

    elif answer == 'm':
        command = input("Enter the command you need help with: ")
        show_help(command)

    elif answer == 'n':
        display_commands_summary(used_commands)
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please choose a valid option.")
