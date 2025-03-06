"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "directory", [{"path": "/var/pca/pca-gophish-composition", "mode": "0o755"}]
)
def test_directories(host, directory):
    """Test that the appropriate directories were created."""
    assert host.file(directory["path"]).exists
    assert host.file(directory["path"]).is_directory
    assert oct(host.file(directory["path"]).mode) == directory["mode"]


@pytest.mark.parametrize("f", ["/var/pca/pca-gophish-composition/docker-compose.yml"])
def test_command(host, f):
    """Test that appropriate files exist."""
    assert host.file(f).exists
    assert host.file(f).is_file


def test_packages(host):
    """Test that appropriate packages were installed."""
    pkgs = ["at", "jq", "python3-virtualenv"]

    for pkg in pkgs:
        assert host.package(pkg).is_installed


def test_pip_packages(host):
    """Test that the pip packages were installed."""
    pkgs = ["gophish-init"]

    for pkg in pkgs:
        # Note that we are using the version of pip in the Python
        # virtual environment that has been created.
        assert pkg in host.pip.get_packages(
            pip_path="/var/pca/pca-gophish-composition/.venv/bin/pip"
        )
