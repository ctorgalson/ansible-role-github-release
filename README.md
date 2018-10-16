# Ansible Role Github Release

This role can be used to download and install command-line utilities directly from Github releases.

## Role Variables

| Variable name              | Default value    | Description |
|----------------------------|------------------|-------------|
| `ghr_tmp_dir`              | `/tmp`           | The directory to download releases to. Required. |
| `ghr_install_dir`          | `/usr/local/bin` | Default value for installing releases to. Optional. |
| `ghr_releases`             | `[]`             | List of releases to download and their properties (see below). Required. |
| `ghr_releases.url`         | `-`              | Url of downloadable release file. Passed directly to Ansible `get_url` module as `url`. Required. |
| `ghr_releases.checksum`    | `-`              | Checksum or checksum file for release. Passed directly to Ansible `get_url` module as `checksum`. Optional. |
| `ghr_releases.extract_dir` | `-`              | Directory (if any) to extract downloaded archive to. Passed directly to Ansible `unarchive` module as `dest`. Optional.|
| `ghr_releases.copy_src`    | `-`              | Path in temp directory to binary file. Passed directly to Ansible `copy` module as `src`. Required. |
| `ghr_releases.copy_dest`   | `-`              | Path in install directory to binary file. Passed directly to Ansible `copy` module as `dest`. Required. |

## Dependencies

The Ansible [Unarchive module](http://docs.ansible.com/ansible/latest/modules/unarchive_module.html#unarchive-module) (used in this role to extract .zip and .tar.gz release files) "requires gtar/unzip command on target host."

## Example Playbook

See `defaults/main.yml` and `molecule/default/playbook.yml` for more information.

    - hosts: all
      vars:
        ghr_tmp_dir: "/tmp"
        ghr_install_dir: "/usr/local/bin"
        ghr_releases:
          # Install hostess: https://github.com/cbednarski/hostess
          - url: "https://github.com/cbednarski/hostess/releases/download/v0.3.0/hostess_linux_amd64"
            copy_src: "{{ ghr_tmp_dir }}/hostess_linux_amd64"
            copy_dest: "{{ ghr_install_dir }}/hostess"
          # Install drush: https://github.com/drush-ops/drush
          - url: "https://github.com/drush-ops/drush/releases/download/8.1.17/drush.phar"
            copy_src: "{{ ghr_tmp_dir }}/drush.phar"
            copy_dest: "{{ ghr_install_dir }}/drush"
          # Install ddev: https://github.com/drud/ddev
          - url: "https://github.com/drud/ddev/releases/download/v1.3.0/ddev_linux.v1.3.0.tar.gz"
            checksum: "sha256:https://github.com/drud/ddev/releases/download/v1.3.0/ddev_linux.v1.3.0.tar.gz.sha256.txt"
            extract_dir: "ddev_linux.v1.3.0"
            copy_src: "{{ ghr_tmp_dir }}/ddev_linux.v1.3.0/ddev"
            copy_dest: "{{ ghr_install_dir }}/ddev"
      roles:
        - role: ansible-role-github-release

## License

GPLv3
