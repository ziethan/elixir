# Elixir

A command line AngularJS app generator written in python. Creates scaffolding for directives, services, modules, controllers, models, and views given the flongular specification. Elixir is part of the cask tool suite that is currently under active development.

## Version
v0.1.0

## Example
Here's a basic example of creating an app
```
elixir app
```
Yep, it's that simple!

## Install
The best option is to pip install it:
```
pip install cask-elixir
```

Or you can clone the repo, put it where ever you like and then run
```
python setup.py install
```
If you want to install globally you'll need to use `sudo`

## Usage

### App
Generates application scaffolding in the form of an app bootstrap and directives, services, and modules directory.
```
elixir app [-n | --name <name>]
```
```
-n --name               Set the application name - default: app
```

### Directive
Creates a directive directory with a directive module.
```
elixir directive <name>
```
```
name                    The name of the directive
```
* must be run from application root directory

### Service
Creates a service directory with a service module.
```
elixir service <name>
```
```
name                    The name of the service
```
* must be run from application root directory

### Module
Creates a module directory with an initial module bootstrap, controller, model, and view with their respective directories.
```
elixir module <name> [-m | --model-name <model-name>] [-v | --view-name <view-name>] [-c | --controller-name <controller-name>]
```
```
name                    The name of the module
-m --model-name         The name of the models (comma separated) - default: module name
-v --view-name          The name of the views (comma separated)- default: module name
-c --controller-name    The name of the controllers (comma separated) - default: module
```
* must be run from application root directory

### Controller
Creates a controller within a module.
```
elixir controller <name>
```
```
name                    The name of the controller
```
* must be run from inside a module's directory


### Model
Creates a model within a module.
```
elixir model <name>
```
```
name                    The name of the model
```
* must be run from inside a module's directory

### View
Creates a view within a module.
```
elixir view <name>
```
```
name                    The name of the view
```
* must be run from inside a module's directory
