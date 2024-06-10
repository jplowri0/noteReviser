
def file_opener():
    # Define the path to your Markdown file
    file_path = 'filepath.txt'

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file
        contents = file.read()

    # Print the contents
    print(contents)




def main():
    file_opener()

  #Yadda yadda 


if __name__ == "__main__":
    main()

