#!/bin/bash
certbot certonly --standalone --http-01-port 8088 -d $1

/etc/letsencrypt/renewal-hooks/post/fix-le-archive-right