from __future__ import absolute_import, print_function

import os

from jinja2 import Environment, PackageLoader


def module(name, **kwargs):
    env = Environment(loader=PackageLoader('elixir', 'templates'))
    
    os.mkdir('modules/{0}'.format(name))
    os.mkdir('modules/{0}/controllers'.format(name))
    os.mkdir('modules/{0}/models'.format(name))
    os.mkdir('modules/{0}/views'.format(name))
    
    bootstrap_template = env.get_template('bootstrap.lxr')
    b_tmp = bootstrap_template.render(name=name)
    
    controller_template = env.get_template('controller.lxr')
    c_tmp = controller_template.render(name=name)
    
    model_template = env.get_template('model.lxr')
    m_tmp = model_template.render(name=name)
    
    view_template = env.get_template('view.lxr')
    v_tmp = view_template.render(name=name)
    
    with open('modules/{0}/{0}.js'.format(name), 'w+') as f:
        f.write(b_tmp)
    
    with open('modules/{0}/controllers/{0}Controller.js'.format(name), 'w+') as f:
        f.write(c_tmp)
    
    with open('modules/{0}/models/{0}Model.js'.format(name), 'w+') as f:
        f.write(m_tmp)
    
    with open('modules/{0}/views/{0}.html'.format(name), 'w+') as f:
        f.write(v_tmp)