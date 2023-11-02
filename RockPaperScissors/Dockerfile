FROM nginx:1.25.2-alpine
COPY ./www/html/* /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]