#!/bin/bash
openssl req -new -newkey \
rsa:4096 -days 365 -nodes \
-x509 -keyout auth-scada.key  \
-out auth-scada.crt \
-subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_AUTH/CN=auth.scada.local"