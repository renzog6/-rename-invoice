import os

#old_name = r"E:\demos\files\reports\details.txt"
#new_name = r"E:\demos\files\reports\new_details.txt"


def rename(old_name, new_name):
    if os.path.isfile(new_name):
        print("The file already exists")
    else:
        # Rename the file
        os.rename(old_name, new_name)
        print("OK!")
