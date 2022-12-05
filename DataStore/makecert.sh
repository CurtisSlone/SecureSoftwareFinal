#!/bin/bash
openssl req -new -newkey \
rsa:4096 -days 365 -nodes \
-x509 -keyout data-scada.key  \
-out data-scada.crt \
-subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_DATA/CN=data.scada.local"