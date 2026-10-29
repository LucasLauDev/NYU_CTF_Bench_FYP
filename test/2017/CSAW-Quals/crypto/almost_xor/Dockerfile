FROM nginx:alpine
RUN sed -i 's/index  index.html index.htm;/autoindex on; index index.html index.htm;/' /etc/nginx/conf.d/default.conf
COPY almostxor.py ciphertext /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/index.html
