from __future__ import absolute_import, print_function

import os

from jinja2 import Environment, PackageLoader


def service(name, **kwargs):
    os.mkdir('services/{0}'.format(name))
    
    env = Environment(loader=PackageLoader('elixir', 'templates'))
    
    template = env.get_template('service.lxr')
    tmp = template.render(name=name)
    
    with open('services/{0}/{0}.js'.format(name), 'w+') as f:
        f.write(tmp)