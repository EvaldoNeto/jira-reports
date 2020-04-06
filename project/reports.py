"""
Main model to call functions and run the projects
"""

import utils
import jira_connection

TI = jira_connection.TIProj()

print("Creating pdf infos...")
utils.create_infos_pdf(TI.get_ti_data())
