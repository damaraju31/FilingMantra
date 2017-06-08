# FillingMantra
web application using Flask framework

Flask framework installation:<br>
$ sudo pip install Flask<br>

Install python-pymongo:<br>
$ sudo apt-get update<br>
$ sudo apt-get install python-pymongo<br>

Install MongoDB:<br>
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927<br>
$ echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list<br>
$ sudo apt-get update<br>
$ sudo apt-get install -y mongodb-org<br>

For configuration of mongodb follow<br>
https://www.howtoforge.com/tutorial/install-mongodb-on-ubuntu-16.04/<br>

To access the database, use mongodb restore on prodList in database folder:<br>
$ sudo mongorestore --db prodList --drop /location/of/prodList<br>

Finally to run the code:<br>
$ python Assignment.py<br>

Now server is set up and open browser to access the webpage(address at terminal)
