FROM node:21

WORKDIR /app
COPY package.json .
RUN npm install --only=production

ARG NODE_ENV
RUN if [ "$NODE_ENV" = "development" ]; \
        then npm install -g nodemon; \
        else npm install --only=production; \
        fi

COPY . ./
ENV PORT 3000
EXPOSE $PORT
CMD [ "node", "index.js" ]