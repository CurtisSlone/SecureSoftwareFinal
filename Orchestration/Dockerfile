FROM alpine
LABEL maintainer="curtisdslone@gmail.com"
LABEL updated="04DEC2022"
WORKDIR /
COPY envFiles/scripts/ldapadd.sh .
COPY envFiles/conf/ldap/init.ldif /opt
ENTRYPOINT ["tail", "-f", "/dev/null"]
#ENTRYPOINT [".", "./ldapadd.sh"]
RUN apk update; apk add openldap openldap-back-mdb openldap-clients; \
    install -m 755 -o ldap -g ldap -d /etc/openldap/slapd.d; \
    sed -r -i 's/dc=my-domain,dc=com/dc=scada,dc=local/g' /etc/openldap/slapd.ldif; \
    /usr/sbin/slapadd -n 0 -F /etc/openldap/slapd.d -l /etc/openldap/slapd.ldif; \
    /usr/sbin/slapd -F /etc/openldap/slapd.d; \
    mv /opt/init.ldif /etc/openldap; \
    /usr/bin/ldapadd -x -D "cn=Manager,dc=scada,dc=local" -w secret -f /etc/openldap/init.ldif; \