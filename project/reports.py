"""
Main model to call functions and run the projects
"""

import sys
import utils
import dto

print("Getting (any) project data...")
dto.main(sys.argv)
print("Creating pdf infos...")
utils.create_infos_pdf('no data')
