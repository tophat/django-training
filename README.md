# Django Training

Master the Django ORM for fun and profit, by actually writing code.

All web apps need to persist and retrieve data to be useful. You can use
Django-[ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) to access
and update your persisted data. The business of retrieving and storing data can
be done in multiple ways; some better than others.

To get familiar with the Django ORM, start by reading through
https://docs.djangoproject.com/en/2.2/topics/db/optimization/. This project is
a training module containing exercises that help solidify the learnings.

## What is Django?

Django is a popular Python framework for building web applications. You can
learn more about Django on its [website](https://www.djangoproject.com/).
Django comes with baked-in support for things like handling API requests and
persisting Python model objects to the database. Django provides a
full-featured [ORM (Object Relational
Mapper)](https://en.wikipedia.org/wiki/Object-relational_mapping) to facilitate
persistence to relational databases via a Python API -- that's right, no SQL
required.

The Django ORM has its pros and cons. Whether or not you like it is one
question, but if you find yourself having to work with it, it's very important
to understand _how_ it works:

- How do I minimize the number of database queries I make?
- When do my querysets get evaluated?
- What does the generated SQL look like?

These are just some of the questions that are important to answer to work
effectively with Django.

## What is django-training?

This project aims to get you familiar with the Django ORM by going through a
set of exercises. Each exercise gets you to try and minimize the number of
queries made in each scenario.

To go through the exercises:

- Clone this repo: `git clone git@github.com:tophat/django-training.git`
- Run `. script/bootstrap` to initialize dependencies and virtualenv (see more https://github.com/github/scripts-to-rule-them-all)
- Go to one of the exercises, e.g. `cd exercise/exercise_1`
- Run the test to see what was expected, e.g. `inv test --exercise=1` or `inv test 1`
- Fix the implementation, e.g. `goto exercise/exercise_1/use_cases.py`
- For a reference to documentation that will help you solve the question use `inv test 1 --hint`
- Run the test to verify your solution, e.g. `inv test 1`

## Contributing

The following invoke commands are available when contributing to this project:

|Command|Description|
|---|---|
|`lint`|Lint checks everything, does not reformat files|
|`format`|Fixes formatting for all python files|

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/sjoanes"><img src="https://avatars3.githubusercontent.com/u/5768264?v=4" width="100px;" alt="sjoanes"/><br /><sub><b>sjoanes</b></sub></a><br /><a href="https://github.com/tophat/django-training/commits?author=sjoanes" title="Code">💻</a> <a href="#ideas-sjoanes" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/tophat/django-training/commits?author=sjoanes" title="Documentation">📖</a></td>
    <td align="center"><a href="https://mcataford.github.io"><img src="https://avatars2.githubusercontent.com/u/6210361?v=4" width="100px;" alt="Marc Cataford"/><br /><sub><b>Marc Cataford</b></sub></a><br /><a href="#infra-mcataford" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/tophat/django-training/commits?author=mcataford" title="Documentation">📖</a></td>
    <td align="center"><a href="http://msrose.github.io"><img src="https://avatars3.githubusercontent.com/u/3495264?v=4" width="100px;" alt="Michael Rose"/><br /><sub><b>Michael Rose</b></sub></a><br /><a href="https://github.com/tophat/django-training/commits?author=msrose" title="Code">💻</a> <a href="https://github.com/tophat/django-training/commits?author=msrose" title="Documentation">📖</a> <a href="#infra-msrose" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
