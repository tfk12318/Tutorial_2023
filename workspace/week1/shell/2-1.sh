#!/bin/bash
mkdir /tmp/scripts
cd /tmp/scripts
cp  -r /etc/pam.d /tmp/scripts | mv pam.d test
useradd "redhat"
chown -R "redhat" test
chmod -R g=---,o=--- test
