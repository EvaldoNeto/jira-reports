"""
Model to define the dotenv location and credencials to connect with Jira
"""

from pathlib import Path

import os
import sys

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

    try:
        jira = JIRA(server=WORKSPACE, basic_auth=(EMAIL, TOKEN))
        print("Connecting to Jira...")
        return jira
    except Exception:
        print("Could not connect to Jira, incorrect credencials!")
        sys.exit()
