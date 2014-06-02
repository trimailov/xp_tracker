Extreme Programming user stories and tasks tracker
=========

App is written with Python 3.4. Dependencies are in requirements.txt

App file tree:
---------
'''
.
|-- README.md
|-- manage.py
|-- requirements.txt
|-- tracker
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- ...
|   |-- settings.py
|   |-- templates
|   |   `-- base.html
|   |-- urls.py
|   `-- wsgi.py
`-- xp_tracker_app
    |-- __init__.py
    |-- __pycache__
    |   |-- ...
    |-- admin.py
    |-- forms.py
    |-- helper.py
    |-- migrations
    |   |-- 0001_initial.py
    |   |-- ...
    |-- models.py
    |-- populate_db.py
    |-- templates
    |   |-- index.html
    |   |-- new_story.html
    |   `-- new_task.html
    |-- test_func.py
    |-- test_unit.py
    |-- urls.py
    `-- views.py
'''

Features:
-   Stories and tasks are estimated separately;
-   Work time is registered only for tasks;
-   Multiple task finishing/improving times could be registered;
-   Work time on story is calculated from associated task work times;
-   Tasks have fields for iteration and developer;
-   Web-app calculates all estimated work time and all spent work time;
-   Developers are selected from a dropdown.
