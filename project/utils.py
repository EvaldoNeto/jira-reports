"""
Generic functions model
"""

from pathlib import Path

import os
import sys
import datetime
import pdfkit

def create_directory():
    """
    Function to create a directory in:
    $home/$user/Documents/jira/reports/year/month/day
    """

    path = (str(Path.home()) + "/Documents/jira/reports")

    # In this loop, geted datetime in isoformat, example: 2020-03-31T11:54:10.883115 and
    # is splited two times, firstly on '-' to get year/month/day and then to remove all after 'T'
    # on each iterate, incremented path with the new sub-date
    for i in range(0, 3):
        sub_date = str(datetime.datetime.now().isoformat().split("-")[i].split("T")[0])
        path = path + str("/" + sub_date)

        if not os.path.exists(path):
            os.makedirs(path)

    return path

def create_infos_pdf():
    """
    Function to create a pdf
    To consult: https://github.com/JazzCore/python-pdfkit
    """

    date_info = datetime.datetime.now().isoformat().split("T")[1].split(":")
    doc = str("report_" + date_info[0] + "h" + date_info[1] + "min.pdf")
    doc_path = Path(create_directory() + "/" + doc)

    try:
        if doc_path.exists():
            os.remove(doc_path)
        pdfkit.from_string('Pandas lib results here, but using other function', doc_path)
    except IOError:
        print("No wkhtmltopdf executable found")
        sys.exit()
