from pathlib import Path

import pdfkit
import os
import datetime
import sys
import shutil

#Create a directory in $home/$user//Documents/jira/reports
def create_main_directory():
    path = (str(Path.home()) + "/Documents/jira/reports")

    try:
        os.makedirs(path)
    except FileExistsError:
        print("The directory {} already exists".format(path))
    except OSError:
        print ("Creation of the directory {} failed".format(path))

def create_date_directory():
    path = (str(Path.home()) + "/Documents/jira/reports")

# Create a pdf, to consult: https://github.com/JazzCore/python-pdfkit
def create__infos_pdf()
    iso_date = datetime.datetime.now().isoformat()
    doc = str("report-" + iso_date.replace("T", "_").replace("-", "_").split(":")[0] + ".pdf")

    try:
        pdfkit.from_string('Pandas lib results here, but using other function', doc)
        shutil.move(doc, path)
    except IOError:
        print("No wkhtmltopdf executable found")
        sys.exit()
