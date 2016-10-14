# encoding: utf-8

import os
import json
import base64
import sys


from find_credentials import get_password


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
            sys.stdout.write("Network password not configured")


if __name__ == '__main__':
	# for debugging the app
    os.environ['alfred_workflow_data'] = '/Users/rhasija/Library/Application Support/Alfred 3/Workflow Data/org.javawithravi.alfred.workflow.cisco.anytimeconnect.vip'
    main()
