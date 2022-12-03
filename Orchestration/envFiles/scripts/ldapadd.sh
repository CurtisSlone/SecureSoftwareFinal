#!/bin/bash
/usr/bin/ldapadd -x -D "cn=Manager,dc=scada,dc=local" -w secret -f /etc/openldap/init.ldif;