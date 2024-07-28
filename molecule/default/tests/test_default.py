import os

import testinfra.utils.ansible_runner as runner

testinfra_hosts = runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_fail2ban_installed(host):
    pkg = host.package("fail2ban")
    assert pkg.is_installed

def test_fail2ban_service_is_running(host):
     with host.sudo():
        svc = host.service('fail2ban')
        assert svc.is_running

def test_fail2ban_service_is_enabled(host):
    service = host.service("fail2ban")
    assert service.is_enabled


def test_jail_local_file(host):
    f = host.file("/etc/fail2ban/jail.local")
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
