# PoPi
433mhz Raspberry Pi Python Light Webinterface.
Needs linux. Development under Linux Mint Debian Edition.

## Installation

Install WiringPi:
```
https://projects.drogon.net/raspberry-pi/wiringpi/download-and-install/
```

Install python-dev and python-setuptools:
```
sudo apt-get install python-dev python-setuptools
```

Install libev-dev:
```
sudo apt-get install libev-dev
```

Install python requirements:
```
sudo pip install -r requirements.txt
```

Install WiringPi-Python
```
sudo git clone https://github.com/WiringPi/WiringPi-Python.git
cd WiringPi-Python
sudo python setup.py install
```

Export Pin 17 for non root usage on boot:
```
sudo nano /etc/rc.local
Before line "exit 0". Replace "user" with your user. In my case "pi"
sudo -u user /usr/local/bin/gpio export 17 out
```

Restart your Pi:
```
sudo reboot
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

Serve with gunicorn:
```
gunicorn popi:app
```

Check out:

```
http://yourip
```

