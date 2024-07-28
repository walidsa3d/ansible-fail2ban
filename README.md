# fail2ban

Install Fail2ban

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
| `docker_data_dir`  | `/mnt/docker_data`      | Directory for Docker data            |
| `molecule_driver`  | `vagrant`               | Molecule driver (vagrant, docker, podman) |
| `molecule_verifier`| `ansible`               | Molecule verifier (ansible, testinfra) |

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
      docker_data_dir: /mnt/docker_data
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.