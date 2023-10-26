echo "Everyone can see your creds. docker_flag:{'it_was_here_all_along'}" > /usr/share/nginx/html/docker/hidden_flag.txt

nginx -g "daemon off;"
