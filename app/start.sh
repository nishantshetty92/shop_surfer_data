#!/bin/sh

gunicorn shop_surfer_data.wsgi:application -b 0.0.0.0:80