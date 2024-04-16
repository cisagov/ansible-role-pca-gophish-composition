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
    pkgs = None
    if (
        host.system_info.distribution == "debian"
        and host.system_info.codename == "buster"
    ):
        pkgs = ["at", "jq", "python3-virtualenv", "virtualenv"]
    else:
        pkgs = ["at", "jq", "python3-virtualenv"]

    for pkg in pkgs:
        assert host.package(pkg).is_installed


def test_pip_packages(host):
    """Test that the pip packages were installed."""
    if host.system_info.distribution in ["fedora"] and host.system_info.release in [
        "39"
    ]:
        # Right now the version of pip that ships with Fedora 39 _does
        # not_ insist on normalizing the package name.  I think this
        # may be new behavior as of pip version 23.2, which was the
        # first version to include the changes in pypa/pip#12044.
        # (This PR was a fix to address pypa/pip#12038.)
        #
        # https://pip.pypa.io/en/stable/news/#v23-2
        pkgs = ["gophish_init"]
    else:
        # Even though the module name is gophish_init (with an
        # underscore) in setup.py (in the pca-gophish-composition
        # repo), as far as older versions of pip are concerned the
        # package name is gophish-init (with a hyphen).
        # https://stackoverflow.com/questions/19097057/pip-e-no-magic-underscore-to-dash-replacement
        pkgs = ["gophish-init"]

    for pkg in pkgs:
        # Note that we are using the version of pip in the Python
        # virtual environment that has been created.
        assert pkg in host.pip.get_packages(
            pip_path="/var/pca/pca-gophish-composition/.venv/bin/pip"
        )
