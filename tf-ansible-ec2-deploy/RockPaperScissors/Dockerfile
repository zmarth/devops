FROM nginx:alpine
RUN rm /usr/share/nginx/html/index.html
COPY ./www/html/* /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]