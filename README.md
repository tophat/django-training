# Django Training

## Purpose

All web apps need persist and retrieve data to be useful. You can use django-orm as an interface to access and update your persisted application data. The business of retrieving and storing data can be done in multiple ways, some better than others. Inefficient implementations can cause a single user to use up 60% of the database on a single request. We don't like that. This is a training module to help you avoid common pitfalls.

## How to run

- Run `. script/bootstrap` to initialize dependencies and virtualenv
- Run fix the implementation in `exercises/exercise_*/use_cases.py`
- Run `make exercise_*` to verify that the fix was made
