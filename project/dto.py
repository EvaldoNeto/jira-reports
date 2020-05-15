"""
Data transfer functions, connecting with Jira and sending data to other modules
"""

import sys

import jira_connector as connector

JIRA = connector.open_connection()

def get_project_data(project):
    """
    Function to open connection with jira and calls function to get all data from any project
    """

    data = JIRA.search_issues('project=' + project + ' ORDER BY key ASC',
                              startAt=0, maxResults=None)
    return data

def main(args):
    """
    Call the correct functions
    """

    projects = {
        '1': 'TI',
        '2': 'CLIEN'
    }

    if str(args) in projects:
        proj = projects[args]
    else:
        print("The number of this argument does not correspond to any project!")
        sys.exit()

    data = get_project_data(proj)
