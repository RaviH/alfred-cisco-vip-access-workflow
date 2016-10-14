# encoding: utf-8

import os
import json
import base64

from find_credentials import get_password

os.environ['alfred_workflow_data'] = '/Users/rhasija/Google Drive/Alfred/Alfred.alfredpreferences/workflows/user.workflow.B865A65B-5916-46CE-AE15-D413FFB64F64'


def main():
    password = get_password('org.javawithravi.alfred.workflow.cisco.anytimeconnect.vip')

    if password is not None:
        print password
    else:
        data_dir = os.getenv('alfred_workflow_data')
        data_file_name = data_dir + "/config.json"

        if os.path.isfile(data_file_name):
            data_file = open(data_file_name, 'r')
            data = data_file.read()
            config = json.loads(data)
            password = config['password']
            print base64.b64decode(password)
        else:
            print "Please provide a config.json in " + os.getenv('alfred_workflow_data') + " dir."


if __name__ == '__main__':
    os.environ['alfred_workflow_data'] = '/Users/rhasija/Library/Application Support/Alfred 3/Workflow Data/org.javawithravi.alfred.workflow.cisco.anytimeconnect.vip'
    main()
