from __future__ import absolute_import, print_function

import os

from jinja2 import Environment, PackageLoader


def controller(name, **kwargs):
    env = Environment(loader=PackageLoader('elixir', 'templates'))
    
    template = env.get_template('controller.lxr')
    tmp = template.render(name=name)
    
    with open('controllers/{0}Controller.js'.format(name), 'w+') as f:
        f.write(tmp)