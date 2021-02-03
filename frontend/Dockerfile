FROM node:12.2.0-alpine as build

# Set working directory
WORKDIR /app

# Copy the react app to the container
COPY . /app/

# Install and build react app
RUN npm install --silent
RUN npm run build --silent

# Nginx
FROM nginx:stable-alpine

WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=build /app/build .
COPY --from=build /app/nginx/nginx.conf /etc/nginx/conf.d/default.conf

# Start Nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
