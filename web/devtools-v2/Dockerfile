FROM node
RUN apt-get update -y && apt-get upgrade -y

ENV NODE_ENV production
ENV PORT 3002

EXPOSE 3002

WORKDIR /app

COPY ./app/package.json .

RUN yarn
RUN npx next telemetry disable

COPY ./app/ .

RUN pwd && ls
RUN yarn build

CMD [ "yarn", "start", "-p", "3002"]