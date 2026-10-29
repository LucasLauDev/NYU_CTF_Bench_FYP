FROM nginx:alpine
RUN sed -i 's/index  index.html index.htm;/autoindex on; index index.html index.htm;/' /etc/nginx/conf.d/default.conf
COPY hypokrinesthai.txt /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/index.html
