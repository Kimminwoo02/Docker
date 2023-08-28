FROM node:14

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

VOLUME [ "/app/feedback" ] // 컨테이너 내부 경로

CMD [ "node","executable"]