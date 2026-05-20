# Ansible Collection - stevefulme1.weka

Ansible collection for managing WekaIO storage systems via the Weka REST API.

## Description

This collection provides modules for managing Weka storage infrastructure, including filesystems, snapshots, quotas, NFS permissions, S3 buckets, and interface groups. It also includes Event-Driven Ansible (EDA) plugins for responding to Weka alerts and events.

## Requirements

- Ansible >= 2.16.0
- Python >= 3.11
- `requests` library (>= 2.25.0)
- Weka cluster with REST API access

## Installation

```bash
ansible-galaxy collection install stevefulme1.weka
```

## Modules

| Module | Description |
|--------|-------------|
| `weka_filesystem` | Manage Weka filesystems |
| `weka_filesystem_info` | Retrieve information about Weka filesystems |
| `weka_snapshot` | Manage Weka filesystem snapshots |
| `weka_snapshot_info` | Retrieve information about snapshots |
| `weka_quota` | Manage quotas on Weka filesystems |
| `weka_quota_info` | Retrieve quota information |
| `weka_nfs_permission` | Manage NFS export permissions |
| `weka_nfs_permission_info` | Retrieve NFS permission information |
| `weka_s3_bucket` | Manage S3 buckets on Weka |
| `weka_s3_bucket_info` | Retrieve S3 bucket information |
| `weka_interface_group` | Manage network interface groups |
| `weka_interface_group_info` | Retrieve interface group information |
| `weka_cluster_info` | Retrieve Weka cluster status and configuration |

## EDA Plugins

- `webhook` - Receive Weka alerts via webhook
- `events` - Poll Weka events API for new events

## Inventory Plugin

- `weka_inventory` - Dynamic inventory from Weka cluster

## Usage Examples

### Creating a Filesystem

```yaml
- name: Create a Weka filesystem
  stevefulme1.weka.weka_filesystem:
    weka_host: weka.example.com
    username: admin
    password: secret
    name: my_filesystem
    capacity: 1TB
    thin_provisioning: true
    state: present
```

### Managing Snapshots

```yaml
- name: Create a snapshot
  stevefulme1.weka.weka_snapshot:
    weka_host: weka.example.com
    username: admin
    password: secret
    filesystem: my_filesystem
    name: snapshot_2026_05_15
    state: present

- name: List all snapshots
  stevefulme1.weka.weka_snapshot_info:
    weka_host: weka.example.com
    username: admin
    password: secret
    filesystem: my_filesystem
  register: snapshots
```

### Setting Quotas

```yaml
- name: Set user quota
  stevefulme1.weka.weka_quota:
    weka_host: weka.example.com
    username: admin
    password: secret
    filesystem: my_filesystem
    entity_type: user
    entity_id: user123
    hard_limit: 500GB
    soft_limit: 450GB
    state: present
```

### Managing NFS Permissions

```yaml
- name: Configure NFS export
  stevefulme1.weka.weka_nfs_permission:
    weka_host: weka.example.com
    username: admin
    password: secret
    filesystem: my_filesystem
    client_rules:
      - client: "192.168.1.0/24"
        access: rw
        root_squash: false
    state: present
```

### Managing S3 Buckets

```yaml
- name: Create S3 bucket
  stevefulme1.weka.weka_s3_bucket:
    weka_host: weka.example.com
    username: admin
    password: secret
    name: my-bucket
    filesystem: my_filesystem
    state: present
```

### Event-Driven Ansible

```yaml
# rulebooks/alert_remediation.yml
- name: Respond to Weka alerts
  hosts: localhost
  sources:
    - stevefulme1.weka.webhook:
        port: 5000
  rules:
    - name: Handle filesystem full alert
      condition: event.alert_type == "FILESYSTEM_FULL"
      action:
        run_playbook:
          name: remediate_full_filesystem.yml
```

## Authentication

All modules support these authentication parameters:

- `weka_host` - Weka cluster hostname or IP
- `weka_port` - API port (default: 14000)
- `username` - API username
- `password` - API password
- `validate_certs` - Validate SSL certificates (default: true)

These can be set via environment variables:
- `WEKA_HOST`
- `WEKA_PORT`
- `WEKA_USERNAME`
- `WEKA_PASSWORD`
- `WEKA_VALIDATE_CERTS`

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
ansible-test units --python 3.11
ansible-test sanity --python 3.11

# Lint
ansible-lint
flake8
```

## License

Apache-2.0

## Author

Steve Fulmer (sfulmer@redhat.com)

## Community

- [Contributing](CONTRIBUTING.md) - How to contribute to this project
- [Code of Conduct](CODE_OF_CONDUCT.md) - Ansible Community Code of Conduct
- [Security Policy](SECURITY.md) - How to report security vulnerabilities
- [License](COPYING) - GPL-3.0

