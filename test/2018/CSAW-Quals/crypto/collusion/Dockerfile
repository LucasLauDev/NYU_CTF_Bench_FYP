FROM nginx:alpine
RUN sed -i 's/index  index.html index.htm;/autoindex on; index index.html index.htm;/' /etc/nginx/conf.d/default.conf
COPY bobs-key.json carols-key.json encrypter.json message.json common.go /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/index.html
