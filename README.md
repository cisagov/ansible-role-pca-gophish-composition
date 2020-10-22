# ansible-role-pca-gophish-composition #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-pca-gophish-composition/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-pca-gophish-composition/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-pca-gophish-composition.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-pca-gophish-composition/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-pca-gophish-composition.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-pca-gophish-composition/context:python)

An Ansible role for installing [cisagov/pca-gophish-composition](https://github.com/cisagov/pca-gophish-composition)

## Requirements ##

None.

## Role Variables ##

None.

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: phishing
  become: yes
  become_method: sudo
  roles:
    - pca-gophish-composition
```

## New Repositories from a Skeleton ##

Please see our [Project Setup guide](https://github.com/cisagov/development-guide/tree/develop/project_setup)
for step-by-step instructions on how to start a new repository from
a skeleton. This will save you time and effort when configuring a
new repository!

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

David Redmin - <david.redmin@trio.dhs.gov>
