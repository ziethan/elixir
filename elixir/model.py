from __future__ import absolute_import, print_function

import os

from jinja2 import Environment, PackageLoader


def model(name, **kwargs):
    env = Environment(loader=PackageLoader('elixir', 'templates'))
    
    template = env.get_template('model.lxr')
    tmp = template.render(name=name)
    
    with open('models/{0}Model.js'.format(name), 'w+') as f:
        f.write(tmp)