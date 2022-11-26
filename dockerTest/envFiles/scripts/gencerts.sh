#!/bin/bash

#Generate Root CSR & Key
openssl req -new \
    -config etc/root-ca.conf \
    -passout pass:password \
    -out ca/root-ca.csr \
    -keyout ca/root-ca/private/root-ca.key

#Generate CA Cert
openssl ca -selfsign \
    -batch \
    -config etc/root-ca.conf \
    -passin pass:password \
    -in ca/root-ca.csr \
    -out ca/root-ca.crt \
    -extensions root_ca_ext

# Generate Network CSR & Key
openssl req -new \
    -config etc/network-ca.conf \
    -passout pass:password \
    -out ca/network-ca.csr \
    -keyout ca/network-ca/private/network-ca.key

# Generate Network CA cert
openssl ca \
    -batch \
    -config etc/root-ca.conf \
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
    -config etc/identity-ca.conf \
    -passout pass:password \
    -out ca/identity-ca.csr \
    -keyout ca/identity-ca/private/identity-ca.key

# Create Identity CA Cert
openssl ca \
    -batch \
    -config etc/network-ca.conf \
    -passin pass:password \
    -in ca/identity-ca.csr \
    -out ca/identity-ca.crt \
    -extensions signing_ca_ext

# Create Network & Identity PEM Bundle
cat ca/identity-ca.crt ca/network-ca-chain.pem > \
    ca/identity-ca-chain.pem

# Create Component CA CSR & Key
openssl req -new \
    -config etc/component-ca.conf \
    -passout pass:password \
    -out ca/component-ca.csr \
    -keyout ca/component-ca/private/component-ca.key

#Create Component CA Cert
openssl ca \
    -batch \
    -config etc/network-ca.conf \
    -passin pass:password \
    -in ca/component-ca.csr \
    -out ca/component-ca.crt \
    -extensions signing_ca_ext

# Create Network & Component PEM Bundle
cat ca/component-ca.crt ca/network-ca-chain.pem > \
    ca/component-ca-chain.pem

# Generate TLS CSR & Key for Web-app
SAN=DNS:webapp.scada.local \
openssl req -new \
    -config etc/server.conf \
    -out certs/webapp.scada.local.csr \
    -keyout certs/webapp.scada.local.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_WEB/CN=web.scada.local"

# Generate TLS CERT
openssl ca \
    -batch \
    -config etc/component-ca.conf \
    -passin pass:password \
    -in certs/webapp.scada.local.csr \
    -out certs/webapp.scada.local.crt \
    -extensions server_ext

# Generate USER ID CSR & Key
openssl req -new \
    -config etc/identity.conf \
    -passout pass:12345678 \
    -out certs/fred-user-id.csr \
    -keyout certs/fred-user-id.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=User/CN=fred.flintstone"

#Generate USER ID Cert
openssl ca \
    -batch \
    -config etc/identity-ca.conf \
    -passin pass:password \
    -in certs/fred-user-id.csr \
    -out certs/fred-user-id.crt \
    -extensions identity_ext

# Generate PKCS#12 for User ID
openssl pkcs12 -export \
    -name "fred.flintstone" \
    -caname "Identity CA" \
    -caname "Network CA" \
    -caname "Root CA" \
    -passin pass:12345678 \
    -passout pass:password \
    -inkey certs/fred-user-id.key \
    -in certs/fred-user-id.crt \
    -certfile ca/identity-ca-chain.pem \
    -out certs/fred-user-id.p12

# Generate Admin ID CSR & Key
openssl req -new \
    -config etc/identity.conf \
    -passout pass:12345678 \
    -out certs/fred-adm-id.csr \
    -keyout certs/fred-adm-id.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=Admin/CN=fred.flintstone"

#Generate Admin ID Cert
openssl ca \
    -batch \
    -config etc/identity-ca.conf \
    -passin pass:password \
    -in certs/fred-adm-id.csr \
    -out certs/fred-adm-id.crt \
    -extensions identity_ext

# Generate PKCS#12 for Admin ID
openssl pkcs12 -export \
    -name "fred.flintstone.admin" \
    -caname "Identity CA" \
    -caname "Network CA" \
    -caname "Root CA" \
    -passin pass:12345678 \
    -passout pass:password \
    -inkey certs/fred-adm-id.key \
    -in certs/fred-adm-id.crt \
    -certfile ca/identity-ca-chain.pem \
    -out certs/fred-adm-id.p12 

# Generate SCADA Device TLS Client CSR & Key
openssl req -new \
    -config etc/client.conf \
    -passout pass:password \
    -out certs/net-mon.csr \
    -keyout certs/net-mon.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=Devices/CN=device1"

# Generate SCADA Device TLS CERT
openssl ca \
    -batch \
    -config etc/component-ca.conf \
    -passin pass:password \
    -in certs/net-mon.csr \
    -out certs/net-mon.crt \
    -extensions client_ext 

# Publish Identity certs to x509 der format
## Admin cert
openssl x509 \
    -in certs/fred-adm-id.crt \
    -out certs/fred-adm-id.cer \
    -outform der
## User cert
openssl x509 \
    -in certs/fred-user-id.crt \
    -out certs/fred-user-id.cer \
    -outform der
## Device
openssl x509 \
    -in certs/net-mon.crt \
    -out certs/net-mon.cer \
    -outform der
