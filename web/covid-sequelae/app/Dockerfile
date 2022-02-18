FROM node
WORKDIR /app/
RUN apt-get update -y && apt-get upgrade -y
COPY . /app/
RUN npm install

ENV FLAG=alphaCTF{ar3_s3qu3l_1nj3ct1000n_st1lll_4_b11G_D34L}
EXPOSE 3000
CMD ["node", "server.js"]
