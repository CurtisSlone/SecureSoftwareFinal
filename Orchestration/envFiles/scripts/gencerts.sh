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

# Create Component CA CSR & Key
openssl req -new \
    -config ./component-ca.conf \
    -passout pass:password \
    -out ca/component-ca.csr \
    -keyout ca/component-ca/private/component-ca.key

#Create Component CA Cert
openssl ca \
    -batch \
    -config ./network-ca.conf \
    -passin pass:password \
    -in ca/component-ca.csr \
    -out ca/component-ca.crt \
    -extensions signing_ca_ext

# Create Network & Component PEM Bundle
cat ca/component-ca.crt ca/network-ca-chain.pem > \
    ca/component-ca-chain.pem


####
## TLS CERTS via Component CA
####

# Generate TLS CSR & Key for WEB
SAN=DNS:web.scada.local \
openssl req -new \
    -config ./server.conf \
    -out certs/web-scada.csr \
    -keyout certs/web-scada.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_WEB/CN=web.scada.local"
######
## WEB TLS SRV
#####
# Generate WEB TLS CERT 
openssl ca \
    -batch \
    -config ./component-ca.conf \
    -passin pass:password \
    -in certs/web-scada.csr \
    -out certs/web-scada.crt \
    -extensions server_ext


## Gen: Auth Client TLS CSR & Key
openssl req -new \
    -config etc/client.conf \
    -out certs/web-auth.csr \
    -keyout certs/web-auth.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_WEB/CN=web.scada.local"

# Auth Client CRT
openssl ca \
    -batch \
    -config etc/component-ca.conf \
    -passin pass:password \
    -in certs/web-auth.csr \
    -out certs/web-auth.crt \
    -extensions client_ext

## Gen: Data Client TLS CSR & Key
openssl req -new \
    -config etc/client.conf \
    -out certs/web-data.csr \
    -keyout certs/web-data.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_WEB/CN=web.scada.local"

# Data Client CRT
openssl ca \
    -batch \
    -config etc/component-ca.conf \
    -passin pass:password \
    -in certs/web-data.csr \
    -out certs/web-data.crt \
    -extensions client_ext

######
## CERT TLS SRV
#####
# Generate TLS CSR & Key for CERT
SAN=DNS:cert.scada.local \
openssl req -new \
    -config ./server.conf \
    -out certs/cert-scada.csr \
    -keyout certs/cert-scada.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_CERT/CN=cert.scada.local"

# Generate Certtrust TLS CERT
openssl ca \
    -batch \
    -config ./component-ca.conf \
    -passin pass:password \
    -in certs/cert-scada.csr \
    -out certs/cert-scada.crt \
    -extensions server_ext


## Gen: Auth Client TLS CSR & Key
openssl req -new \
    -config etc/client.conf \
    -out certs/cert-auth.csr \
    -keyout certs/cert-auth.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_CERT/CN=cert.scada.local"

# Auth Client CRT
openssl ca \
    -batch \
    -config etc/component-ca.conf \
    -passin pass:password \
    -in certs/cert-auth.csr \
    -out certs/cert-auth.crt \
    -extensions client_ext


######
## AUTH TLS SRV
#####
# Generate TLS CSR & Key for AUTH
SAN=DNS:auth.scada.local \
openssl req -new \
    -config ./server.conf \
    -out certs/auth-scada.csr \
    -keyout certs/auth-scada.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_AUTH/CN=auth.scada.local"

# Generate AUTH TLS CERT
openssl ca \
    -batch \
    -config ./component-ca.conf \
    -passin pass:password \
    -in certs/auth-scada.csr \
    -out certs/auth-scada.crt \
    -extensions server_ext

## Gen: Web Client TLS CSR & Key
openssl req -new \
    -config etc/client.conf \
    -out certs/auth-web.csr \
    -keyout certs/auth-web.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_AUTH/CN=auth.scada.local"

# Web Client CRT
openssl ca \
    -batch \
    -config etc/component-ca.conf \
    -passin pass:password \
    -in certs/auth-web.csr \
    -out certs/auth-web.crt \
    -extensions client_ext

## Gen: Cert Client TLS CSR & Key
openssl req -new \
    -config etc/client.conf \
    -out certs/auth-cert.csr \
    -keyout certs/auth-cert.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_AUTH/CN=auth.scada.local"

# Cert Client CRT
openssl ca \
    -batch \
    -config etc/component-ca.conf \
    -passin pass:password \
    -in certs/auth-cert.csr \
    -out certs/auth-cert.crt \
    -extensions client_ext

## Gen: Data Client TLS CSR & Key
openssl req -new \
    -config etc/client.conf \
    -out certs/auth-data.csr \
    -keyout certs/auth-data.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_AUTH/CN=auth.scada.local"

# DataClient CRT
openssl ca \
    -batch \
    -config etc/component-ca.conf \
    -passin pass:password \
    -in certs/auth-data.csr \
    -out certs/auth-data.crt \
    -extensions client_ext

######
## DATA TLS SRV
#####
# Generate TLS CSR & Key for DATA
SAN=DNS:data.scada.local \
openssl req -new \
    -config ./server.conf \
    -out certs/data-scada.csr \
    -keyout certs/data-scada.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_DATA/CN=data.scada.local"

# Generate DATA TLS CERT
openssl ca \
    -batch \
    -config ./component-ca.conf \
    -passin pass:password \
    -in certs/data-scada.csr \
    -out certs/data-scada.crt \
    -extensions server_ext

## Gen: Data Client TLS CSR & Key
openssl req -new \
    -config etc/client.conf \
    -out certs/data-auth.csr \
    -keyout certs/data-auth.key \
    -subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_DATA/CN=data.scada.local"

# DataClient CRT
openssl ca \
    -batch \
    -config etc/component-ca.conf \
    -passin pass:password \
    -in certs/data-auth.csr \
    -out certs/data-auth.crt \
    -extensions client_ext


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