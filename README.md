pep8-autochecker
================

Automated PEP8 review of Python projects

# Installation

Run the following commands :

    virtualenv env # If you don't want to use a virtualenv, go directly to the `pip install` command
    source bin/env/activate
    pip install -r requirements

To enable social accounts authentification, you should open the admin page (http://localhost:8000/admin/socialaccount/socialapp/) and add a social application (for example GitHub). You will need details (public and API keys) from the selected platform.

# Screenshots

**Landing page**:

![landing page](./screenshots/landing.png)

---

**Example of scan results**:

![scan results](./screenshots/scan-results.png)

**Details of a project**:

---

![project details](./screenshots/project-details.png)

# Status

[ ![Codeship Status for MickaelBergem/pep8-autochecker](https://www.codeship.io/projects/14046180-0bae-0132-97d8-062262e0aab7/status)](https://www.codeship.io/projects/32046)

[![Coverage Status](https://coveralls.io/repos/MickaelBergem/pep8-autochecker/badge.png?branch=HEAD)](https://coveralls.io/r/MickaelBergem/pep8-autochecker?branch=HEAD)

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/MickaelBergem/pep8-autochecker/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/MickaelBergem/pep8-autochecker/?branch=master)
