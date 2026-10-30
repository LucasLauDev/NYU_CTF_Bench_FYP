FROM nginx:alpine
RUN sed -i 's/index  index.html index.htm;/autoindex on; index index.html index.htm;/' /etc/nginx/conf.d/default.conf
COPY ecxor_handout_100.py rfc8032.py ciphertext /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/index.html
