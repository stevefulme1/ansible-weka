# Contributing to stevefulme1.weka

Thank you for considering contributing to the Weka Ansible collection.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/ansible-weka.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Install development dependencies: `pip install -r requirements.txt`

## Development Guidelines

### Code Style

- Follow [Ansible module conventions](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html)
- Use PEP 8 for Python code
- Maximum line length: 120 characters
- Use meaningful variable and function names

### Module Development

When adding a new module:

1. Create the module in `plugins/modules/`
2. Include complete DOCUMENTATION, EXAMPLES, and RETURN sections
3. Use the `weka_api` module_utils for API calls
4. Support `check_mode` for dry-run operations
5. Return changed status accurately
6. Handle errors gracefully with meaningful messages

### Testing

All contributions must include tests:

```bash
# Run unit tests
ansible-test units --python 3.11

# Run sanity tests
ansible-test sanity --python 3.11

# Run linting
ansible-lint
flake8
```

### Unit Test Requirements

- Place tests in `tests/unit/plugins/modules/test_<module_name>.py`
- Mock all API calls using `unittest.mock`
- Test both success and failure scenarios
- Test parameter validation
- Test check_mode behavior
- Aim for >80% code coverage

### Documentation

- Update README.md with new modules
- Add examples to module documentation
- Update CHANGELOG.md following [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
- Document any new authentication parameters in doc fragments

### Commit Messages

Follow conventional commits:

```
feat: add weka_volume module
fix: handle API timeout in weka_filesystem
docs: update installation instructions
test: add unit tests for weka_snapshot
```

### Pull Request Process

1. Update documentation for any changed functionality
2. Add tests for new features
3. Ensure all tests pass locally
4. Update CHANGELOG.md with your changes
5. Submit PR with clear description of changes
6. Link to any related issues

### PR Checklist

- [ ] Tests pass (`ansible-test units` and `ansible-test sanity`)
- [ ] Linting passes (`ansible-lint` and `flake8`)
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Commit messages follow conventions
- [ ] Code follows style guidelines

## Review Process

1. Maintainers will review within 5 business days
2. Address any requested changes
3. Once approved, maintainer will merge

## Questions?

Open an issue or contact the maintainer at sfulmer@redhat.com

## Code of Conduct

This project follows the Contributor Covenant Code of Conduct. See CODE_OF_CONDUCT.md.

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.
