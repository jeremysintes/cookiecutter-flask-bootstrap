{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Quickstart
----------
-  Create a developpement environment (recommended):
   ``conda env create -n NAME_OF_THE_PROJECT``

-  Activate the developpement environment :
   ``activate NAME_OF_THE_PROJECT``

-  Install the required librairies : (platform\_demo)$
   ``pip install -r requirements``

 -  Activate the developpement environment :
   ``activate NAME_OF_THE_PROJECT``

-  Run the application : (platform\_demo)$ ``python run.py``

Credits
---------

This package was created with Cookiecutter_ and the `jeremysintes/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`jeremysintes/cookiecutter-pypackage`: https://github.com/jeremysintes/cookiecutter-pypackage

