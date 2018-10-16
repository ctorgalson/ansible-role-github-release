import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("version", [
    "v1.3.0",
])
def test_release(host, version):
    s = host.check_output('ddev version')

    assert version in s
