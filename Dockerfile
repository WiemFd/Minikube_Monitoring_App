#STEP 1 BUILD VUE PROJECT
FROM node:20.3.0-alpine AS build-stage
WORKDIR /app
COPY package.json ./
RUN npm install 
COPY . .
RUN npm run build


#STEP 2 CREATE NGINX SERVER
FROM nginx:1.18.0-alpine AS prod-stage
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx","-g","daemon off;"]

