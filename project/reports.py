"""
Main model to call functions and run the projects
"""

import utils

JIRA = utils.JiraConfig()

print("Creating pdf infos...")
utils.create_infos_pdf()
