FROM alpine
LABEL maintainer="curtisdslone@gmail.com"
LABEL updated="25NOV2022"
WORKDIR /opt
COPY envFiles/scripts/gencerts.sh .
COPY envFiles/conf/ca/* .
#ENTRYPOINT ["tail", "-f", "/dev/null"]
RUN apk update; apk add openssl; apk add base64;\
    # Root CA
    mkdir -p ca/root-ca/private ca/root-ca/db crl certs; \
    chmod 700 ca/root-ca/private; \
    cp /dev/null ca/root-ca/db/root-ca.db; \
    cp /dev/null ca/root-ca/db/root-ca.db.attr; \
    echo 01 > ca/root-ca/db/root-ca.crt.srl; \
    echo 01 > ca/root-ca/db/root-ca.crl.srl; \
    # Network CA
    mkdir -p ca/network-ca/private ca/network-ca/db crl certs; \
    chmod 700 ca/network-ca/private; \
    cp /dev/null ca/network-ca/db/network-ca.db; \
    cp /dev/null ca/network-ca/db/network-ca.db.attr; \
    echo 01 > ca/network-ca/db/network-ca.crt.srl; \
    echo 01 > ca/network-ca/db/network-ca.crl.srl; \
    # Identity CA
    mkdir -p ca/identity-ca/private ca/identity-ca/db crl certs; \
    chmod 700 ca/identity-ca/private; \
    cp /dev/null ca/identity-ca/db/identity-ca.db; \
    cp /dev/null ca/identity-ca/db/identity-ca.db.attr; \
    echo 01 > ca/identity-ca/db/identity-ca.crt.srl; \
    echo 01 > ca/identity-ca/db/identity-ca.crl.srl; \
    # Component CA
    mkdir -p ca/component-ca/private ca/component-ca/db crl certs; \
    chmod 700 ca/component-ca/private; \
    cp /dev/null ca/component-ca/db/component-ca.db; \
    cp /dev/null ca/component-ca/db/component-ca.db.attr; \
    echo 01 > ca/component-ca/db/component-ca.crt.srl; \
    echo 01 > ca/component-ca/db/component-ca.crl.srl; \
    # Run Certificate Generating script
    . ./gencerts.sh; \
    # Move certs to shared cert Vol
    mkdir CERT; \
    mkdir AUTH; \
    mkdir DATA; \
    mkdir WEB; \
    mkdir USER; \
    cp certs/fred-user.crt CERT/; \ 
    cp certs/fred-adm.crt CERT/; \
    cp certs/cert-scada.key CERT/; \ 
    cp certs/cert-scada.crt CERT/; \
    cp certs/auth-scada.key AUTH/; \ 
    cp certs/auth-scada.crt AUTH/; \
    cp certs/data-scada.key DATA/; \ 
    cp certs/data-scada.crt DATA/; \
    cp certs/web-scada.crt WEB/; \ 
    cp certs/web-scada.key WEB/; \
    cp certs/fred-user.crt USER/; \ 
    cp certs/fred-adm.crt USER/; \
    cp certs/fred-user.key USER/; \ 
    cp certs/fred-adm.key USER/; \
    echo "finished"