"""
Generic functions model
"""

from pathlib import Path

import os
import sys
import datetime
import pdfkit

def create_directory(date):
    """
    Function to create a directory in:
    $home/$user/Documents/jira/reports/year/month/day
    """

    path = (str(Path.home()) + "/Documents/jira/reports")

    for i in range(0, 3):
        path = (path + "/" + date[i])

        if not os.path.exists(path):
            os.makedirs(path)

    return path

def create_infos_pdf():
    """
    Function to create a pdf
    To consult: https://github.com/JazzCore/python-pdfkit
    """

    date = str(datetime.datetime.now())
    
    # The datetime, example: 2020-03-31 11:54:10.883115 and
    # is replace two times, firstly on ' ' to '-' and then ':' to '-', afeter
    # is splited on '-', result: ['2020'],['03'],['31'],['11'],['54'],['10.883115']
    sub_date = date.replace(" ", "-").replace(":", "-").split("-")
    doc = (f"report_{sub_date[3]}h{sub_date[4]}min.pdf")
    doc_path = Path(create_directory(sub_date) + "/" + doc)

    try:
        if doc_path.exists():
            os.remove(doc_path)
        pdfkit.from_string('Pandas lib results here, but using other function', doc_path)
    except IOError:
        print("No wkhtmltopdf executable found")
        sys.exit()
