#!/bin/bash

####
## CA Generation
####

#Generate Root CSR & Key
openssl req -new \
    -config ./root-ca.conf \
    -passout pass:password \
    -out ca/root-ca.csr \
    -keyout ca/root-ca/private/root-ca.key

#Generate CA Cert
openssl ca -selfsign \
    -batch \
    -config ./root-ca.conf \
    -passin pass:password \
    -in ca/root-ca.csr \
    -out ca/root-ca.crt \
    -extensions root_ca_ext

# Generate Network CSR & Key
openssl req -new \
    -config ./network-ca.conf \
    -passout pass:password \
    -out ca/network-ca.csr \
    -keyout ca/network-ca/private/network-ca.key

# Generate Network CA cert
openssl ca \
    -batch \
    -config ./root-ca.conf \
    -passin pass:password \
    -in ca/network-ca.csr \
    -out ca/network-ca.crt \
    -extensions intermediate_ca_ext \
    -enddate 20301231235959Z

# Create ROOT & NETWORK PEM Bundle
cat ca/network-ca.crt ca/root-ca.crt > \
    ca/network-ca-chain.pem

# Create Identity CA CSR & Key
openssl req -new \
    -config ./identity-ca.conf \
    -passout pass:password \
    -out ca/identity-ca.csr \
    -keyout ca/identity-ca/private/identity-ca.key

# Create Identity CA Cert
openssl ca \
    -batch \
    -config ./network-ca.conf \
    -passin pass:password \
    -in ca/identity-ca.csr \
    -out ca/identity-ca.crt \
    -extensions signing_ca_ext

# Create Network & Identity PEM Bundle
cat ca/identity-ca.crt ca/network-ca-chain.pem > \
    ca/identity-ca-chain.pem



####
## TLS CERTS 
####

#####  Certtrust crt gen
openssl req -new -newkey \
rsa:4096 -days 365 -nodes \
-x509 -keyout cert-scada.key  \
-out cert-scada.crt \
-subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_CERT/CN=cert.scada.local"

######## Authenticator crt gen
openssl req -new -newkey \
rsa:4096 -days 365 -nodes \
-x509 -keyout auth-scada.key  \
-out auth-scada.crt \
-subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_AUTH/CN=auth.scada.local"

######## Data crt gen
openssl req -new -newkey \
rsa:4096 -days 365 -nodes \
-x509 -keyout data-scada.key  \
-out data-scada.crt \
-subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_DATA/CN=data.scada.local"

######## FrontEnd crt gen
openssl req -new -newkey \
rsa:4096 -days 365 -nodes \
-x509 -keyout web-scada.key  \
-out web-scada.crt \
-subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_WEB/CN=web.scada.local"
####
## DIGITAL ID's
####

# Generate USER ID CSR & Key
openssl req -new \
    -config ./identity.conf \
    -passout pass:12345678 \
    -out certs/fred-user.csr \
    -keyout certs/fred-user.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=Users/CN=fred.flintstone"

#Generate USER ID Cert
openssl ca \
    -batch \
    -config ./identity-ca.conf \
    -passin pass:password \
    -in certs/fred-user.csr \
    -out certs/fred-user.crt \
    -extensions identity_ext

# Generate Admin ID CSR & Key
openssl req -new \
    -config ./identity.conf \
    -passout pass:12345678 \
    -out certs/fred-adm.csr \
    -keyout certs/fred-adm.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=Admins/CN=fred.flintstone.adm"

#Generate Admin ID Cert
openssl ca \
    -batch \
    -config ./identity-ca.conf \
    -passin pass:password \
    -in certs/fred-adm.csr \
    -out certs/fred-adm.crt \
    -extensions identity_ext