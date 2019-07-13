sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf ~/web/etc/gunicorn-django.py /etc/gunicorn.d/test-django
sudo /etc/init.d/mysql start
sudo /etc/init.d/nginx restart
gunicorn --config /etc/gunicorn.d/test-django --pid ~/web/gunicorn.pid --daemon ask.wsgi:application
