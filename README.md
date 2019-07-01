# ansible-role-pca-gophish-composition #

[![Build Status](https://travis-ci.com/cisagov/ansible-role-pca-gophish-composition.svg?branch=develop)](https://travis-ci.com/cisagov/ansible-role-pca-gophish-composition)
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

## Contributing ##

We welcome contributions!  Please see [here](CONTRIBUTING.md) for
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
