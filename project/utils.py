from pathlib import Path

import os

'''Create a directory in $home/$user//Documents/jira/reports'''
def create_directory():
    path = (str(Path.home()) + "/Documents/jira/reports")

    try:
        os.makedirs(path)
    except FileExistsError:
        print("The directory {} already exists".format(path))
    except OSError:
        print ("Creation of the directory {} failed".format(path))
