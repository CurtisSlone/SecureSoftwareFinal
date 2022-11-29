FROM alpine
LABEL maintainer="curtisdslone@gmail.com"
LABEL updated="29NOV2022"
WORKDIR /
COPY envFiles/conf/ldap/* ./etc
RUN apk update; apk add openldap openldap-back-mdb openldap-clients;
