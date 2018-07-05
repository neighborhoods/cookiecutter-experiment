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
password_alert = 'Please select a Jupyter Notebook password.'


def assemble_output_contents(password_hash):
    output_dict = {
        "NotebookApp": {
            "password": password_hash
        }
    }
    return output_dict


def alert_user_if_setting_password(password):
    if password is None:
        print(password_alert)


def main():
    password = os.environ.get(password_env_var)
    alert_user_if_setting_password(password)
    password_hash = passwd(password)
    output_dict = assemble_output_contents(password_hash)
    with open(output_file_name, 'w') as f:
        json.dump(output_dict, f)


if __name__ == "__main__":
    main()

