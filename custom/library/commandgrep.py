#!/usr/bin/python
DOCUMENTATION = '''
---
module: commandgrep
short_description: Execute a shell command and filter the output
'''
EXAMPLES = '''
- hosts: localhost
  tasks:
    - name: Test commandgrep module
      commandgrep:
        command: "df"
        matchstring: "nv"
      register: result

    - debug: var=result

'''
from ansible.module_utils.basic import *

import subprocess
import re

def process_command_filter(comm, filt):
    print "process_command()"
    results = []
    raw_op=subprocess.check_output(comm, shell=True)
    op_in_list=raw_op.split('\n')
    for line in op_in_list:
	#print line
        match = re.search(filt, line)
        if match:
           print line
           results.append(line)
    return results

def main():
    fields = {
        "command": {"required": True, "type": "str"},
        "matchstring": {"required": True, "type": "str"},
    }

    module = AnsibleModule(argument_spec=fields)
    result = process_command_filter(module.params['command'], module.params['matchstring'])
    module.exit_json(changed=False, meta=result)

if __name__=='__main__':
   main()
