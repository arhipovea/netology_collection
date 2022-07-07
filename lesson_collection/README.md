# Ansible Collection - netology_mnt_13.lesson_collection

Module создаваёт текстовый файл на удалённом хосте по пути, определённом в параметре path, с содержимым, определённым в параметре content.

## Requirements

```yml
---
collections:
  - name: git@github.com:arhipovea/netology_collection.git
    type: git
    version: master
```

## Example

Создаёт файл с именем test_file и содержимым hello world

```yml
---
- name: Check module
  hosts: localhost
  tasks:
    - name: Test with a file create
      netology_collection.lesson_collection.my_module:
        path: /
        content: hello world
        filename: test_file
```

