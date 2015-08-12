# polis-heroku
Miscellaneous scripts hosted on Heroku

https://paralelnipolis.herokuapp.com

Prerequisites
* Installed Python and Virtualenv, see http://docs.python-guide.org/en/latest/starting/install/linux/

Install
* clone repo and cd `cd paralelnipolis`
* build local environment `virtualenv venv --distribute`
* use app context `source venv/bin/activate`
* install dependencies `pip install -r requirements.txt`
* create db tables and superuser`python manage.py syncdb`
* start server `python manage.py runserver`

Database migration [South]
* see [The Basics](http://south.readthedocs.org/en/0.7.6/tutorial/part1.html) and [Converting An App](http://south.readthedocs.org/en/0.7.6/convertinganapp.html)

Dev satabase data
* open and login at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
* insert master public keys and products
* dev product image: [http://www.freegreatpicture.com/files/104/20309-christmas-food.jpg](http://www.freegreatpicture.com/files/104/20309-christmas-food.jpg)

Restore DB dump on localhost
* dropdb -h localhost -U postgres paralelnipolis
* createdb -h localhost -U postgres paralelnipolis
* pg_restore --verbose --clean --no-acl --no-owner -h localhost -U postgres -d paralelnipolis latest.dump

