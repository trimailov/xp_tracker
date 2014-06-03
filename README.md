Extreme Programming user stories and tasks tracker
=========

App is written with Python 3.4, database - PostgreSQL 9.3. 
Dependencies are in requirements.txt

Instructions
---------
1. Create python3 virtualenv
1. Clone repository
1. Run `pip install -r requirements.txt`
1. Run postgres (`psql`)
1. Create database `CREATE DATABASE xp_tracker_app`
1. In project repository run `python manage.py shell`
1. In shell prompt enter: `from xp_tracker_app import populate_db as popdb`
1. `popdb.create_stories()`
1. `popdb.create_tasks()`
1. In project repository run `python manage.py runserver`


Features:
-   Stories and tasks are estimated separately;
-   Work time is registered only for tasks;
-   Multiple task finishing/improving times could be registered;
-   Work time on story is calculated from associated task work times;
-   Tasks have fields for iteration and developer;
-   Web-app calculates all estimated work time and all spent work time;
-   Developers are selected from a dropdown.

For production in settings.py `DEBUG` option must be set to `False`

