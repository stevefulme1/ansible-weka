#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Steve Fulmer
# Apache-2.0 (see LICENSE)
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module: weka_nfs_permission_info."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: weka_nfs_permission_info
short_description: Retrieve nfs permission information
description:
    - Retrieve details about nfs permissions.
    - This is a read-only module.
version_added: "1.0.0"
author:
    - Steve Fulmer (@stevefulme1)
options:
    host:
        description: API host address.
        type: str
        required: true
    username:
        description: Authentication username.
        type: str
    password:
        description: Authentication password.
        type: str
    api_key:
        description: API key for authentication.
        type: str
    name:
        description:
            - The name identifier.
        type: str
    validate_certs:
        description: Whether to validate SSL certificates.
        type: bool
        default: true

    permission_id:
        description: The permission id.
        type: str
    limit:
        description:
          - Maximum number of results to return.
        type: int
        default: 100
    offset:
        description:
          - Number of results to skip for pagination.
        type: int
        default: 0
"""

EXAMPLES = r"""
- name: List all nfs permissions
  stevefulme1.weka.weka_nfs_permission_info:
  register: result

- name: Get a specific nfs permission
  stevefulme1.weka.weka_nfs_permission_info:
    permission_id: "example-id"
  register: result
"""

RETURN = r"""
nfs_permissions:
    description: List of nfs permission details.
    returned: always
    type: list
    elements: dict
"""

from ansible.module_utils.basic import AnsibleModule

try:
    from ansible_collections.stevefulme1.weka.plugins.module_utils.api_client import ApiClient
    HAS_CLIENT = True
except ImportError:
    HAS_CLIENT = False


def main():
    module = AnsibleModule(
        argument_spec=dict(
            limit=dict(type='int', default=100),
            offset=dict(type='int', default=0),
            permission_id=dict(type="str"),
            name=dict(type="str"),
            host=dict(type="str", required=True),
            username=dict(type="str"),
            password=dict(type="str", no_log=True),
            api_key=dict(type="str", no_log=True),
            validate_certs=dict(type="bool", default=True),
        ),
        supports_check_mode=True,
    )

    if not HAS_CLIENT:
        module.fail_json(msg="Required Python libraries not found.")

    client = ApiClient(module)
    resource_id = module.params.get("permission_id")

    if resource_id:
        result = client.get("nfs_permission", resource_id)
        resources = [result] if result else []
    else:
        resources = client.list("nfs_permission", module.params)

    module.exit_json(changed=False, nfs_permissions=resources)


if __name__ == "__main__":
    main()
