import os
import re
import logging


def find_acct(entry, word):
    found = word in entry
    return found


def get_account(bundle_id):
    output = os.popen('security find-internet-password -j ' + bundle_id + ' -g').read()
    output_list = output.split("\n")
    account_strings = [x for x in output_list if find_acct(x, 'acct')]
    account_string = account_strings[0]
    m = re.search('.*\"(\w*)\"', account_string)
    return m.group(1)


def get_password(bundle_id):
    output = os.popen('security 2>&1 >/dev/null find-internet-password -j "' + bundle_id + '" -g').read()
    if output.rstrip('\n').endswith('The specified item could not be found in the keychain.'):
        logging.info("Could not find password for bundle id: %s", bundle_id)
        return None
    else:
        m = re.search('.*: \"(.*)\".*', output)
        return m.group(1)


if __name__ == '__main__':
    print get_account('org.javawithravi.stash.workflow')
    print get_password('org.javawithravi.stash.workflow')
    print get_password('org.javawithravi.alfred.workflow.cisco.anytimeconnect.vip')
