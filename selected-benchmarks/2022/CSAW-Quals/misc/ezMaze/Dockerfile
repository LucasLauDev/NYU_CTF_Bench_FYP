FROM nginx:alpine
RUN sed -i 's/index  index.html index.htm;/autoindex on; index index.html index.htm;/' /etc/nginx/conf.d/default.conf
COPY attachment/ /usr/share/nginx/html/attachment/
COPY attachment/maze.pt /usr/share/nginx/html/
COPY description/challenge.txt /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/index.html
