#!/bin/bash
openssl req -new -newkey \
rsa:4096 -days 365 -nodes \
-x509 -keyout web-scada.key  \
-out web-scada.crt \
-subj "/C=US/ST=NC/L=Raleigh/O=SCADA/OU=SCADA_WEB/CN=web.scada.local"