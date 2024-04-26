import os
import pyperclip

def grep_search(root_path, search_string):
    for root, _, files in os.walk(root_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    if search_string in file.read():
                        print("\nFile Name:", file_name)
                        print("File Location:", file_path)
                        print("File Contents:")
                        with open(file_path, 'r', encoding='utf-8') as f:
                            print(f.read())
                        
                        while True:
                            choice = input("\nPress 'N' to move to the next file, 'SC' to copy the file name to the clipboard, 'Q' to quit, or any other key to continue: ").strip().upper()
                            
                            if choice == 'N':
                                break
                            elif choice == 'SC':
                                filename = os.path.splitext(file_name)[0] # Remove file extension
                                pyperclip.copy(filename)
                                print(f"File name '{filename}' copied to clipboard.")
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

