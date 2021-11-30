# How I ran these.

They're run exactly as they are in the file with [oha](https://github.com/hatoo/oha)
however, proxy.py was run with the following CLI args because the script didn't work
(which was copied from the benchmark repo :/)

```
python3 -m proxy --hostname 127.0.0.1 --port 8000 --backlog 65536 --open-file-limit 65536 --enable-web-server --plugin proxy.plugin.WebServerPlugin --disable-http-proxy --log-file /dev/null
```

Some reasons why there is such a difference compared to the claim:

- We actually use multiple workers here making it a fair comparison
- Uvicorn and HTTPTools improve Uvicorn's performance several times over.

NOTE: proxy.py had accessed to the exact same system e.g. it has uvloop available
and httptools if the system supported it.

Extra Note: Proxy.py used 16 workers, the others used 10. So I'd like to empathise just how much
faster uvicorn is.

# Results
TL;DR no, proxy.py is not faster.

Starlette
```
chillfish8@JACKAL:~/projects/personal/benchmark-proxypy$ oha --no-tui --latency-correction --insecure -c 100 -n 1000000 http://127.0.0.1:8000/http-route-example
Summary:
  Success rate: 1.0000
  Total:        11.5783 secs
  Slowest:      0.0205 secs
  Fastest:      0.0001 secs
  Average:      0.0012 secs
  Requests/sec: 86368.5823

  Total data:   12.40 MiB
  Size/request: 13 B
  Size/sec:     1.07 MiB

Response time histogram:
  0.000 [153146] |■■■■■■■■■■■■■■■■■■■■■■■■
  0.001 [163275] |■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.001 [105835] |■■■■■■■■■■■■■■■■■
  0.001 [135535] |■■■■■■■■■■■■■■■■■■■■■■
  0.002 [196099] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.002 [142069] |■■■■■■■■■■■■■■■■■■■■■■■
  0.002 [68043]  |■■■■■■■■■■■
  0.002 [26161]  |■■■■
  0.003 [6303]   |■
  0.003 [1998]   |
  0.003 [1536]   |

Latency distribution:
  10% in 0.0003 secs
  25% in 0.0006 secs
  50% in 0.0012 secs
  75% in 0.0016 secs
  90% in 0.0019 secs
  95% in 0.0022 secs
  99% in 0.0025 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0003 secs, 0.0001 secs, 0.0007 secs
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs

Status code distribution:
  [200] 1000000 responses
```

Blacksheep
```
chillfish8@JACKAL:~/projects/personal/benchmark-proxypy$ oha --no-tui --latency-correction --insecure -c 100 -n 1000000 http://127.0.0.1:8000/http-route-example
Summary:
  Success rate: 1.0000
  Total:        11.1912 secs
  Slowest:      0.0205 secs
  Fastest:      0.0001 secs
  Average:      0.0011 secs
  Requests/sec: 89356.1285

  Total data:   18.12 MiB
  Size/request: 19 B
  Size/sec:     1.62 MiB

Response time histogram:
  0.000 [152990] |■■■■■■■■■■■■■■■■■■
  0.001 [174269] |■■■■■■■■■■■■■■■■■■■■
  0.001 [34454]  |■■■■
  0.001 [153187] |■■■■■■■■■■■■■■■■■■
  0.001 [270771] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.002 [141670] |■■■■■■■■■■■■■■■■
  0.002 [51767]  |■■■■■■
  0.002 [13697]  |■
  0.003 [4182]   |
  0.003 [1494]   |
  0.003 [1519]   |

Latency distribution:
  10% in 0.0003 secs
  25% in 0.0005 secs
  50% in 0.0013 secs
  75% in 0.0015 secs
  90% in 0.0018 secs
  95% in 0.0020 secs
  99% in 0.0024 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0007 secs, 0.0001 secs, 0.0028 secs
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0004 secs

Status code distribution:
  [200] 1000000 responses
```

Proxy.py
```
chillfish8@JACKAL:~/projects/personal/benchmark-proxypy$ oha --no-tui --latency-correction --insecure -c 100 -n 1000000 http://127.0.0.1:8000/http-route-example
Summary:
  Success rate: 1.0000
  Total:        27.3925 secs
  Slowest:      0.1770 secs
  Fastest:      0.0001 secs
  Average:      0.0027 secs
  Requests/sec: 36506.3870

  Total data:   18.12 MiB
  Size/request: 19 B
  Size/sec:     677.36 KiB

Response time histogram:
  0.001 [235031] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.001 [209800] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.002 [149930] |■■■■■■■■■■■■■■■■■■■■
  0.003 [104897] |■■■■■■■■■■■■■■
  0.004 [74442]  |■■■■■■■■■■
  0.004 [53129]  |■■■■■■■
  0.005 [39441]  |■■■■■
  0.006 [29939]  |■■■■
  0.007 [22934]  |■■■
  0.007 [17483]  |■■
  0.008 [62974]  |■■■■■■■■

Latency distribution:
  10% in 0.0005 secs
  25% in 0.0009 secs
  50% in 0.0018 secs
  75% in 0.0035 secs
  90% in 0.0061 secs
  95% in 0.0082 secs
  99% in 0.0133 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0003 secs, 0.0001 secs, 0.0004 secs
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs

Status code distribution:
  [200] 1000000 responses
```