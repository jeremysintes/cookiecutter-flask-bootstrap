from flask import Flask, request


app = Flask(__name__)


from {{cookiecutter.project_slug}} import views


__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'


# [N!]N(.N)*[{a|b|rc}N][.postN][.devN]
# For more information : https://www.python.org/dev/peps/pep-0440/