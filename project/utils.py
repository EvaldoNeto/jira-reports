from pathlib import Path

import os

class GenericFunctions:
    def __init__(self):
        pass

    def create_directory(self):
        path = (str(Path.home()) + "/Documents/jira/reports")

        try:
            os.makedirs(path)
        except FileExistsError:
            print("The directory {} already exists".format(path))
        except OSError:
            print ("Creation of the directory {} failed".format(path))