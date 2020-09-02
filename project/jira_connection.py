"""
Model to define the dotenv location and credencials to connect with Jira
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

def open_connection():
    """
    Function to establish connection with Jira
    """
    jira = JIRA(server=WORKSPACE, basic_auth=(EMAIL, TOKEN))
    return jira
