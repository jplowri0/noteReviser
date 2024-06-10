

# get a list of all files from fleeting , lit, and perm. Create a csv with SR,filename,count
# Where count is the times this program has opened the file. 
#
# It needs to check for newly created files and add to list. 
#
# It will then randomly open a file, once opened it will add a 1 to the count. 
# It cant reopen files until all have been opeened. 
#
# Files should be opened randomly. The file is opened by the SR. 
#
# When a file is opened, I want to see the filepath of the note and also the file contents.
#
# I should get an option to etihter go onto next note, Or follow the links. 


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

