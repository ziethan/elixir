#!/usr/bin/env python
from __future__ import absolute_import, print_function

import argparse

from elixir.app import app
from elixir.directive import directive
from elixir.module import module
from elixir.service import service
from elixir.controller import controller
from elixir.model import model
from elixir.view import view

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='commands',help='Select a command')

#app
parse_app = subparsers.add_parser('app', help='Create application scaffolding')
app_group = parse_app.add_argument_group('app')
app_group.set_defaults(func=app)
app_group.add_argument('-n', '--name', help='Set the application name - default: app', default='app')

#module
parse_module = subparsers.add_parser('module', help='Create module scaffolding')
module_group = parse_module.add_argument_group('module')
module_group.set_defaults(func=module)
module_group.add_argument('name', help='The name of the module')
module_group.add_argument('-m','--model-name', help='The name of the models (comma separated) - default: module name', default='%(name)'+'Model')
module_group.add_argument('-v','--view-name', help='The name of the views (comma separated)- default: module name', default='%(name)'+'View')
module_group.add_argument('-c','--controller-name', help='The name of the controllers (comma separated) - default: module name', default='%(name)'+'Controller')

#directive
parse_directive = subparsers.add_parser('directive', help='Create directive scaffolding')
directive_group = parse_directive.add_argument_group('directive')
directive_group.set_defaults(func=directive)
directive_group.add_argument('name', help="The name of the directive")

#service
parse_service = subparsers.add_parser('service', help='Create service scaffolding')
service_group = parse_service.add_argument_group('service')
service_group.set_defaults(func=service)
service_group.add_argument('name', help="The name of the service")

#controller
parse_controller = subparsers.add_parser('controller', help='Create controller scaffolding')
controller_group = parse_controller.add_argument_group('controller')
controller_group.set_defaults(func=controller)
controller_group.add_argument('name', help="The name of the controller")

#model
parse_model = subparsers.add_parser('model', help='Create model scaffolding')
model_group = parse_model.add_argument_group('model')
model_group.set_defaults(func=model)
model_group.add_argument('name', help="The name of the model")

#view
parse_view = subparsers.add_parser('view', help='Create view scaffolding')
view_group = parse_view.add_argument_group('view')
view_group.set_defaults(func=view)
view_group.add_argument('name', help="The name of the view")

def main():
    #args
    args=parser.parse_args()
    args.func(**vars(args))