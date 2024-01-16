FROM alpine:3.18.4
RUN apk add --no-cache nginx
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./www/html/* /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]