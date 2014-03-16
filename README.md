# PoPi
433mhz Raspberry Pi Python Light Webinterface
Needs linux. Development under Linux Mint Debian Edition.

## Installation

Install python-dev:
```
sudo apt-get install python-dev
```

Install libev-dev:
```
sudo apt-get install libev-dev
```

Install python requirements:
```
sudo pip install -r requirements.txt
```

Serve with gunicorn:
```
gunicorn popi:app
```

Nginx as proxy between external and the web server. It also servers the static file:
```
apt-get install nginx
```

If you are using nginx only for PoPi:

```
rm /etc/nginx/sites-enabled/default
nano /etc/nginx/sites-enabled/default
```

and paste:

```
server {
    listen 80;
    server_name localhost;

    root /path/to/PoPi;

    access_log /path/to/PoPi/logs/access.log;
    error_log /path/to/PoPi/logs/error.log;

    location / {
        proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        if (!-f $request_filename) {
            proxy_pass http://127.0.0.1:8000;
            break;
        }
    }
}
```

Reload nginx:

```
sudo service nginx reload
```

Reload nginx:

```
http://yourip
```

