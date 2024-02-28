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


@pytest.mark.parametrize("pkg", ["at", "jq", "python3-virtualenv"])
def test_packages(host, pkg):
    """Test that appropriate packages were installed."""
    assert host.package(pkg).is_installed


# Even though the module name is gophish_init (with an underscore) in setup.py
# (in the pca-gophish-composition repo), as far as pip is concerned, the
# package name is gophish-init (with a hyphen).
# https://stackoverflow.com/questions/19097057/pip-e-no-magic-underscore-to-dash-replacement
@pytest.mark.parametrize("pkg", ["gophish-init"])
def test_pip_packages(host, pkg):
    """Test that the pip packages were installed."""
    # Note that we are using the version of pip in the Python virtual
    # environment that has been created.
    assert pkg in host.pip.get_packages(
        pip_path="/var/pca/pca-gophish-composition/.venv/bin/pip"
    )
