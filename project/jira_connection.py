"""
Some class to Jira hooks
"""

from pathlib import Path

import os

from dotenv import load_dotenv
from jira import JIRA

ENV_PATH = Path.home()/'.env'
load_dotenv(dotenv_path=ENV_PATH)

WORKSPACE = os.getenv("WORKSPACE")
EMAIL = os.getenv("EMAIL")
TOKEN = os.getenv("TOKEN")

class TIProj:
    """
    Class to get datas from TI Project
    """
    def __init__(self):
        self.jira = open_connection()

    def get_ti_data(self):
        """
        Function to get all issues and priority of TI project
        """
        infos = ''
        ti_data = self.jira.search_issues('project=TI ORDER BY key ASC', startAt=0, maxResults=None)
        for issue in ti_data:
            infos = infos + structure_response(str(issue), str(issue.fields.priority))
        return infos

    def future_function(self):
        """
        Mold method to pass in pylint
        """

def open_connection():
    """
    Function to establish connection with Jira
    """
    jira = JIRA(server=WORKSPACE, basic_auth=(EMAIL, TOKEN))
    return jira

def structure_response(issue, data):
    """
    Function to return the structure response
    """
    line_info = str(issue + ', ' + data + '\n')
    return line_info
