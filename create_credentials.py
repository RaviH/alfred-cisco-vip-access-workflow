import os
import base64
import json


def main(query):
    try:
        data_dir = os.getenv('alfred_workflow_data').rstrip('\n')
        if not os.path.exists(data_dir):
	    	os.makedirs(data_dir)
        data_file_name = data_dir + "/config.json"

        data_file = open(data_file_name, 'w+')
        password = base64.b64encode(query)
        config_dict = {'password': password}
        config_json = json.dumps(config_dict, sort_keys=True, indent=4, separators=(',', ': '))
        data_file.write(config_json)
        print "Created password config successfully"
    except Exception as e:
        print "I/O error({0}): {1} {2}".format(e.errno, e.strerror, data_dir)


# if __name__ == '__main__':
#     os.environ['alfred_workflow_data'] = '/Users/rhasija/Google Drive/Alfred/Alfred.alfredpreferences/workflows/user.workflow.B865A65B-5916-46CE-AE15-D413FFB64F64'
#     main('foobar')
