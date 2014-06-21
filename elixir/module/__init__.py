from __future__ import absolute_import, print_function

import os

from jinja2 import Environment, PackageLoader


def module(name, **kwargs):
    env = Environment(loader=PackageLoader('app', '../templates'))

    os.mkdir('modules/{0}'.format(name))
    os.mkdir('modules/{0}/controllers'.format(name))
    os.mkdir('modules/{0}/models'.format(name))
    os.mkdir('modules/{0}/views'.format(name))

    bootstrap_template = env.get_template('module/bootstrap.lxr')
    b_tmp = bootstrap_template.render(name=name)

    controller_template = env.get_template('module/controller.lxr')
    c_tmp = controller_template.render(name=name)
    
    model_template = env.get_template('module/model.lxr')
    m_tmp = model_template.render(name=name)
    
    view_template = env.get_template('module/view.lxr')
    v_tmp = view_template.render(name=name)
    
    with open('modules/{0}/{0}.js'.format(name), 'w+') as f:
        f.write(b_tmp)
        
    with open('modules/{0}/controllers/{0}Controller.js'.format(name), 'w+') as f:
        f.write(c_tmp)
    
    with open('modules/{0}/models/{0}Model.js'.format(name), 'w+') as f:
        f.write(m_tmp)
    
    with open('modules/{0}/views/{0}View.html'.format(name), 'w+') as f:
        f.write(v_tmp)