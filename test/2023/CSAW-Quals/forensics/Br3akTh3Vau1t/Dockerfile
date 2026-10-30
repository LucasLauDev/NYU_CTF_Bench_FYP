FROM nginx:alpine
RUN sed -i 's/index  index.html index.htm;/autoindex on; index index.html index.htm;/' /etc/nginx/conf.d/default.conf
COPY runme.yml ansible.cfg /usr/share/nginx/html/
COPY vars /usr/share/nginx/html/vars/
COPY index.html /usr/share/nginx/html/index.html
