FROM node
RUN apt-get update && rm -rf /var/lib/apt/lists/*

COPY ./app /app
WORKDIR /app
EXPOSE 8080

ENV FLAG=alphaCTF{j4v4scr1pt_w4rr10r_d3s3rv3s_pr3m1um_fl4g}
CMD ["node", "server.js"]