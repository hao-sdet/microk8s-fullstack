FROM node:15.8.0-alpine as build

# Set working directory
WORKDIR /usr/src/app

# Install and build React app using yarn (--network-timeout 1000000 fixes the slow network error)
COPY package.json yarn.lock ./
RUN yarn install --network-timeout 1000000
COPY . ./
RUN yarn build

# Nginx
FROM nginx:stable-alpine

WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=build /app/build .
COPY --from=build /app/nginx/nginx.conf /etc/nginx/conf.d/default.conf

# Start Nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]