# fail2ban

An Ansible role to install fail2ban on Ubuntu/Debian.
![Ansible Role](https://img.shields.io/ansible/role/d/walidsa3d/failban)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/walidsa3d/ansible-fail2ban/main.yml)
## Table of Contents

- [Requirements](#requirements)
- [Role Variables](#role-variables)
- [Dependencies](#dependencies)
- [Example Playbook](#example-playbook)
- [Molecule Testing](#molecule-testing)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Ansible >= 2.9
- Supported platforms:
  - Ubuntu

## Role Variables

The variables used in this role are defined in `defaults/main.yml` and can be customized as per your requirements. Here are some of the main variables:

| Variable           | Default Value           | Description                          |
|--------------------|-------------------------|--------------------------------------|
| `logelevel`  | `INFO`      | log level|
| `ban_ignoreip`  | `INFO`      | excluded ips|
| `bantime`  | `600`      | number of seconds an IP address is banned |
| `findtime`  | `600`      | retris must occur within the findtime duration. |
| `maxretry`  | `5`      | max retries before ban|

## Dependencies

This role has no external dependencies.

## Example Playbook

Here is an example of how to use this role in a playbook:

```yaml
---
- name: Install and configure Fail2ban.
  hosts: all
  become: true
  roles:
    - role: walidsa3d.failban
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.