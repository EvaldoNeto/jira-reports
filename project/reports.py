"""
Main model to call functions and run the projects
"""

import utils
import dto

print("Getting CLIEN project data...")
dto.get_project_data('CLIEN')
print("Creating pdf infos...")
utils.create_infos_pdf('no data')
