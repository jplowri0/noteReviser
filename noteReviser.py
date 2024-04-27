import os
import pyperclip

def remove_not_reviewed(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace("NOT_REVIEWED", "")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def grep_search(root_path, search_string):
    for root, _, files in os.walk(root_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if search_string in content:
                        print("\nFile Name:", file_name)
                        print("File Location:", file_path)
                        print("File Contents:")
                        print(content)
                        
                        while True:
                            choice = input("\nPress 'N' to move to the next file, 'SC' to copy the file name to the clipboard, 'S' to remove 'NOT_REVIEWED' from the file, 'Q' to quit, or any other key to continue: ").strip().upper()
                            
                            if choice == 'N':
                                break
                            elif choice == 'SC':
                                filename = os.path.splitext(file_name)[0] # Remove file extension
                                pyperclip.copy(filename)
                                print(f"File name '{filename}' copied to clipboard.")
                            elif choice == 'S':
                                if "NOT_REVIEWED" in content:
                                    remove_not_reviewed(file_path)
                                    print("Removed 'NOT_REVIEWED' from the file.")
                                else:
                                    print("'NOT_REVIEWED' not found in the file.")
                            elif choice == 'Q':
                                return
                            else:
                                return
            except UnicodeDecodeError:
                print("\nUnable to read:", file_path, "- File is not encoded in UTF-8")

def main():
    root_path = input("Enter the root directory path to start searching: ")
    search_string = input("Enter the string to search: ")
    grep_search(root_path, search_string)

if __name__ == "__main__":
    main()

