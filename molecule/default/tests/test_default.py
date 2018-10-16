import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('command,version', [
    ('ddev version', 'v1.3.0'),
    ('drush --version', '8.1.17'),
    ('hostess --version', '0.3.0'),
])
def test_release(host, command, version):
    s = host.check_output(command)

    assert version in s
