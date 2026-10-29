FROM nginx:alpine
RUN sed -i 's/index  index.html index.htm;/autoindex on; index index.html index.htm;/' /etc/nginx/conf.d/default.conf
COPY Tax_Ret_Form_Nov_2021.zip Tax_Ret_Form_Blank.pdf SPBlock_Email.pdf /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/index.html
