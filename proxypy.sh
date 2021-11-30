python3 -m proxy \
  --hostname 127.0.0.1 \
  --port 8000 \
  --backlog 65536 \
  --open-file-limit 65536 \
  --enable-web-server \
  --plugin proxy.plugin.WebServerPlugin \
  --disable-http-proxy \
  --local-executor --log-file /dev/null > /dev/null 2>&1 &