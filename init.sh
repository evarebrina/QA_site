sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf ~/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -sf ~/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
sudo /etc/init.d/nginx restart
#gunicorn -c /etc/gunicorn.d/test hello:wsgi_application
gunicorn -c /etc/gunicorn.d/test-django ask.wsgi:application
