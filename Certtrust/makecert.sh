#!/bin/bash
openssl req -new -newkey \
rsa:4096 -days 365 -nodes \
-x509 -keyout cert-scada.key  \
-out cert-scada.crt \
-subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_CERT/CN=cert.scada.local"