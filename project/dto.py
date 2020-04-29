"""
Data transfer functions, connecting with Jira and sending data to other modules
"""
import jira_connection
import args_validate

JIRA = jira_connection.open_connection()

def get_project_data(project):
    """
    Function to open connection with jira and calls function to get all data from any project
    """
    jira = jira_connection.open_connection()
    data = jira.search_issues('project=' + project + ' ORDER BY key ASC',
                              startAt=0, maxResults=None)
    return data

def main(args):
    """
    Call the correct functions
    """
    args_validate.main(args)
    data = get_project_data('CLIEN')
