#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
from email.policy import default
from fileinput import filename
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_module

short_description: Тестовый модуль для netology.

version_added: "1.0.8"

description: Тестовый модуль для netology, который создаёт файл по пути path, с именем filename и содержимым content.

options:
    path:
        description: Путь до файла.
        required: true
        type: path
    content:
        description: Содержание файла.
        required: true
        type: str
    filename:
        description: Имя файла.
        required: false
        type: str
        default: file

extends_documentation_fragment:
    - netology_collection.lesson_collection.my_module_doc

author:
    - Arkhipov Evgeniy (@arhipovea)
'''

EXAMPLES = r'''
# Create file
- name: Test with a file create
  netology_collection.lesson_collection.my_module:
    path: ./
    content: test content

# Create file with filename new_filename
- name: Test with a file create
  netology_collection.lesson_collection.my_module:
    path: /home/ansible
    content: test
    filename: test_file
'''

RETURN = r'''
# These are examples of possible return values.
msg:
    description: The output message.
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import os


def run_module():
    module_args = dict(
        path=dict(type='path', required=True, aliases=['dest']),
        content=dict(type='str', required=True),
        filename=dict(type='str', required=False, default='file', aliases=['name'])
    )

    result = dict(
        changed=False,
        msg='File created'
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    fullname = os.path.join(module.params['path'], module.params['filename'])

    try:
        if os.path.isfile(fullname) and open(fullname, "r").read() == module.params['content']:
            module.exit_json(changed=False, **result)
        else:
            with open(fullname, "w") as f:
                f.write(module.params['content'])
    except IOError as e:
        module.fail_json(msg="ERROR: {}".format(e.strerror))

    module.exit_json(changed=True, **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
