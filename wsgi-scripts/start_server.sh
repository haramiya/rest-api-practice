#!/usr/bin/bash
sudo systemctl stop uwsgi
sudo systemctl stop nginx
sudo systemctl start nginx
sudo systemctl start uwsgi
sudo systemctl status nginx
sudo systemctl status uwsgi
