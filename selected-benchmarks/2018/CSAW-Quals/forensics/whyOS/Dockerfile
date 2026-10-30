FROM nginx:alpine
RUN sed -i 's/index  index.html index.htm;/autoindex on; index index.html index.htm;/' /etc/nginx/conf.d/default.conf
COPY com.yourcompany.whyos_4.2.0-28+debug_iphoneos-arm.deb console.log /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/index.html
