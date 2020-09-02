"""
Main model to call functions and run the projects
"""

import sys
import utils
import dto

import args_validate as val

val.validate_args(sys.argv)

print("Getting (any) project data...")
dto.main(sys.argv[1])
print("Creating pdf infos...")
utils.create_infos_pdf('no data')
