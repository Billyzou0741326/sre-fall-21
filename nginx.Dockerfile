FROM zguanhan/sre-f21-base:latest AS static_1
WORKDIR /app/
COPY . /app/
RUN python3 manage.py collectstatic --no-input

FROM node:16-alpine3.14 AS static_builder_2
COPY ./package*.json /app/
COPY ./*.config.js /app/
WORKDIR /app/
RUN npm install


FROM static_builder_2 AS static_2
WORKDIR /app/
COPY ./css /app/css
COPY ./public /app/public
COPY ./templates /app/templates/
RUN NODE_ENV=production npx postcss css/tailwind.css -o public/static/css/tailwind-output.css


FROM nginx:1.21.3-alpine
COPY --from=static_2 /app/public/ /app/public/
COPY --from=static_1 /app/static/ /app/public/static/
COPY ./nginx/* /etc/nginx/templates/
