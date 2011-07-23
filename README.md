Django-Communes
===============

List of all the French cities with name, population, insee_code, postal code, latitude and longitude as a PointField

Installation
------------

    pip install git+git://github.com/platypus-creation/django-communes.git

or:

    git clone git://github.com/platypus-creation/django-communes.git
    cd django-communes
    python setup.py install


Add `communes` to your INSTALLED_APPS

    INSTALLED_APPS = (
        ...
        'communes',
    )

Create the database table
    
    python manage.py syncdb

or if you are using South (you should)

    python manage.py migrate communes

Then load the datas

    python manage loaddata communes.json

You are done


Usage
-----

You should find your best way to use those datas. At least it should provide an easy way to suggest city from a postal code.


Greetings
---------

All the datas were taken from http://www.galichon.com/codesgeo/
We wanted to thanks Jerome Galichon for creating those files.
