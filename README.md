# fail2ban

An Ansible role to install fail2ban on Ubuntu/Debian.

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
| `bantime`  | `600`      | banned 600 seconds|
| `maxretry`  | `5`      | max retries before ban|

## Dependencies

This role has no external dependencies.

## Example Playbook

Here is an example of how to use this role in a playbook:

```yaml
---
- name: Install and configure Docker
  hosts: all
  become: yes
  roles:
    - role: fail2ban
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.