# Changelog

## [2.1.1] - 2026-05-18

### Security
- **CRITICAL**: Fixed credential leak where `password` and `api_key` were sent in API request bodies via raw `module.params` passthrough (all modules)
- Added `_filter_params()` to `ApiClient` to strip connection/auth keys before API calls
- Added HTTP request timeout (30s) to all API client methods to prevent indefinite hangs
- Expanded `.gitignore` to exclude `.env`, `*.pem`, `*.key`, vault files, and other sensitive patterns

## [2.0.0] - 2026-05-17

### Added
- Idempotency: get-before-write with state comparison in 26 modules
- Pagination support (limit/offset) for all _info modules
- Pre-commit and linting configuration

### Fixed
- Role README files added for Galaxy compliance
- Galaxy import validation issues resolved

### Security
- Bumped requests>=2.32.5 to fix CVE-2023-32681, CVE-2024-35195

## [1.2.0] - 2026-05-15

### Added
- 52 modules covering full WekaIO distributed storage platform API
- 10 Day-2 operation roles
- Dynamic inventory plugin
- EDA source plugins for event-driven automation

## [1.0.1] - 2026-05-15

### Fixed
- Module documentation rendering on Galaxy
- Module DOCUMENTATION: added all argument_spec params

## [1.0.0] - 2026-05-15

### Added
- Initial release with filesystem, snapshot, quota, NFS, S3, and interface group modules
- EDA source plugins (webhook, events)
- Inventory plugin
- Unit tests and CI pipeline
