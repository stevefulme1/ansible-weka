#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Steve Fulmer
# Apache-2.0 (see LICENSE)

"""Ansible module: weka_s3_bucket."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: weka_s3_bucket
short_description: Manage Weka S3 buckets
description:
    - Manage Weka S3 buckets in Weka.
    - Supports create, update, and delete operations.
version_added: "1.0.0"
author:
    - Steve Fulmer (@stevefulme1)
options:
    state:
        description: Desired state of the resource.
        type: str
        default: present
        choices: [present, absent]
    bucket_name:
        description: Unique identifier of the s3 bucket.
        type: str
    name:
        description: Display name of the s3 bucket.
        type: str
"""

EXAMPLES = r"""
- name: Create a s3 bucket
  stevefulme1.weka.weka_s3_bucket:
    name: my-s3-bucket
    state: present

- name: Delete a s3 bucket
  stevefulme1.weka.weka_s3_bucket:
    bucket_name: "example-id"
    state: absent
"""

RETURN = r"""
s3_bucket:
    description: Resource details.
    returned: on success
    type: dict
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
            state=dict(type="str", default="present", choices=["present", "absent"]),
            bucket_name=dict(type="str"),
            name=dict(type="str"),
            host=dict(type="str", required=True),
            username=dict(type="str"),
            password=dict(type="str", no_log=True),
            api_key=dict(type="str", no_log=True),
            validate_certs=dict(type="bool", default=True),
        ),
        supports_check_mode=True,
        required_if=[
            ("state", "absent", ("bucket_name",)),
        ],
    )

    if not HAS_CLIENT:
        module.fail_json(msg="Required Python libraries not found.")

    client = ApiClient(module)
    state = module.params["state"]
    resource_id = module.params.get("bucket_name")

    if state == "present":
        if resource_id:
            result = client.update("s3_bucket", resource_id, module.params)
        else:
            if module.check_mode:
                module.exit_json(changed=True)
            result = client.create("s3_bucket", module.params)
        module.exit_json(changed=True, s3_bucket=result)
    else:
        if module.check_mode:
            module.exit_json(changed=True)
        client.delete("s3_bucket", resource_id)
        module.exit_json(changed=True)


if __name__ == "__main__":
    main()
