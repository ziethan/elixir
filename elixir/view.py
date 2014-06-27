from __future__ import absolute_import, print_function

import os

from jinja2 import Environment, PackageLoader


def view(name, **kwargs):
    env = Environment(loader=PackageLoader('elixir', 'templates'))
    
    template = env.get_template('view.lxr')
    tmp = template.render(name=name)
    
    with open('views/{0}.js'.format(name), 'w+') as f:
        f.write(tmp)