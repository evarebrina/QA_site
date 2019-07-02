sudo apt-get update
sudo apt-get install python3.5
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
sudo pip3 install django
sudo pip3 install gunicorn
sudo pip3 instal mysqlclient

mysql -uroot -e "CREATE USER 'vadim'@'localhost'"
mysql -uroot -e "CREATE DATABASE qa"
mysql -uroot -e "GRANT ALL ON qa.* TO 'vadim'@'localhost'"