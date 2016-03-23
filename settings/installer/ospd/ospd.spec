---
subparsers:
    ospd:
        help: Installs openstack using OSP Director
        groups:
            - title: Firewall
              options:
                firewall-rules:
                    type: YamlFile
                    help: The list of firewall rules
                    default: default.yml

            - title: Product
              options:
                product:
                    type: YamlFile
                    help: The product to install
                    default: "rhos-latest.yml"

            - title: Undercloud
              options:
                undercloud-network:
                    type: YamlFile
                    help: The undercloud network config
                    default: default.yml

            - title: Overcloud
              options:
                overcloud-use_ssl:
                    type: Value
                    help: Specifies whether ths SSL should be used for overcloud
                    default: 'no'
                overcloud-storage:
                    type: YamlFile
                    help: The overcloud storage type
                    default: ceph.yml
                overcloud-images-task:
                    type: Value
                    help: Specifies whether the images should be built or imported
                    required: yes
                    #choices: [import, build]
                overcloud-images-files:
                    type: YamlFile
                    help: The list of images for overcloud nodes
                    required: yes
                overcloud-images-url:
                    type: Value
                    help: The images download url
                    required: yes
                overcloud-network-backend:
                    type: Value
                    help: The overcloud network backend.
                    default: vxlan
                overcloud-network-protocol:
                    type: Value
                    help: The network protocol for overcloud
                    default: ipv4
                overcloud-network-isolation:
                    type: YamlFile
                    help: The overcloud network isolation type
                    required: yes
                overcloud-network-isolation-template:
                    type: YamlFile
                    help: The overcloud network isolation template

            - title: Version
              options:
                version-major:
                    type: Value
                    help: The OSPd major version
                    default: 7
                version-minor:
                    type: Value
                    help: The OSPd minor version
                    default: 3
                build:
                    type: Value
                    help: The OSPd build
                    default: latest

            - title: User
              options:
                user-name:
                    type: Value
                    help: The installation user name
                    default: stack
                user-password:
                    type: Value
                    help: The installation user password
                    default: stack

            - title: common
              options:
                  dry-run:
                      action: store_true
                      help: Only generate settings, skip the playbook execution stage
                  cleanup:
                      action: store_true
                      help: Clean given system instead of provisioning a new one
                  input:
                      action: append
                      type: str
                      short: i
                      help: Input settings file to be loaded before the merging of user args
                  output:
                      type: str
                      short: o
                      help: 'File to dump the generated settings into (default: stdout)'
                  extra-vars:
                      action: append
                      short: e
                      help: Extra variables to be merged last
                      type: str
                  from-file:
                      type: IniFile
                      help: the ini file with the list of arguments
                  generate-conf-file:
                      type: str
                      help: generate configuration file (ini) containing default values and exits. This file is than can be used with the from-file argument
