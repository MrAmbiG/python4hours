#!/usr/bin/python
from ansible.module_utils.basic import *

'''
make host file entries
'''

def hoster(file,data):
    with open(file, 'a+') as f:
        f.write(data)

def main():
    fields = {
        "file": {"required": True, "type": "str"},
        "data": {"required": True, "type": "str"},
    }
    module = AnsibleModule(argument_spec=fields)
    response = hoster(module.params['file'], module.params['data'])
    module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()
