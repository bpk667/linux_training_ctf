FROM nginx

ENV dockerfile_var="docker_flag={'your_secret_is_showing'}"

COPY creds /root/

COPY ./run.sh /run.sh
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
RUN chmod 750 /run.sh

EXPOSE 80

CMD ["./run.sh"]

