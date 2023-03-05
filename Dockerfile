FROM nginx:1.21-alpine
COPY . /usr/share/nginx/html
EXPOSE s 80
CMD ["nginx", "-g", "daemon off;"]
