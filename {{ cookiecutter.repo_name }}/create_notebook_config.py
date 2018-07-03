#!/usr/bin/python3

"""
Read the env var JUPYTER_PASSWORD and create jupyter_notebook_config.json
with a hash of the password.
"""

import json
import os
from notebook.auth import passwd

output_file_name = 'jupyter_notebook_config.json'
password_env_var = 'JUPYTER_PASSWORD'


def assemble_output_contents(password_hash):
    output_dict = {
        "NotebookApp": {
            "password": password_hash
        }
    }
    return output_dict


def main():
    password = os.environ.get(password_env_var)
    password_hash = passwd(password)
    output_dict = assemble_output_contents(password_hash)
    with open(output_file_name, 'w') as f:
        json.dump(output_dict, f)


if __name__ == "__main__":
    main()

