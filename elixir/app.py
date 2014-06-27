from __future__ import absolute_import, print_function

import os

from jinja2 import Environment, PackageLoader


def app(name, **kwargs):
    env = Environment(loader=PackageLoader('elixir', 'templates'))
    
    os.mkdir('directives')
    os.mkdir('services')
    os.mkdir('modules')
    
    template = env.get_template('app.lxr')
    tmp = template.render(name=name)
    
    with open(name+'.js', 'w+') as f:
        f.write(tmp)