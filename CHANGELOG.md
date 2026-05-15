# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-05-15

### Added

- Initial release of stevefulme1.weka collection
- Filesystem management modules:
  - `weka_filesystem` - Create, update, and delete filesystems
  - `weka_filesystem_info` - Retrieve filesystem information
- Snapshot management modules:
  - `weka_snapshot` - Create, update, and delete snapshots
  - `weka_snapshot_info` - Retrieve snapshot information
- Quota management modules:
  - `weka_quota` - Manage user and group quotas
  - `weka_quota_info` - Retrieve quota information
- NFS permission modules:
  - `weka_nfs_permission` - Configure NFS export permissions
  - `weka_nfs_permission_info` - Retrieve NFS permission configuration
- S3 bucket modules:
  - `weka_s3_bucket` - Manage S3 buckets
  - `weka_s3_bucket_info` - Retrieve S3 bucket information
- Interface group modules:
  - `weka_interface_group` - Manage network interface groups
  - `weka_interface_group_info` - Retrieve interface group information
- Cluster information module:
  - `weka_cluster_info` - Retrieve cluster status and configuration
- Event-Driven Ansible plugins:
  - `webhook` event source - Receive Weka alerts via webhook
  - `events` event source - Poll Weka events API
- Dynamic inventory plugin:
  - `weka_inventory` - Generate inventory from Weka cluster
- Module utilities:
  - `weka_api` - REST API client with token authentication
- Documentation fragments:
  - `weka_auth` - Common authentication parameters
- Comprehensive test suite with unit tests
- CI/CD pipeline with GitHub Actions
- Full documentation and examples
