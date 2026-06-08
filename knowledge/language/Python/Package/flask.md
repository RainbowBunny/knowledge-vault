[https://flask.palletsprojects.com/en/stable/api/](https://flask.palletsprojects.com/en/stable/api/)
# Application Object

## Flask

Signature: `class flask.Flask(import_name, static_url_path=None, static_folder='static', static_host=None, host_matching=False, subdomain_matching=False, template_folder='templates', instance_path=None, instance_relative_config=False, root_path=None)`
Parameters:
- `import_name` (`str`) – the name of the application package

### add_url_rule

Signature: `def add_url_rule(rule, endpoint=None, view_func=None, provide_automatic_options=None, **options)`
Parameters:
- `rule` (`str`) – The URL rule string.
- `endpoint` (`str` | `None`) – The endpoint name to associate with the rule and view function. Used when routing and building URLs. Defaults to `view_func.__name__`.
- `view_func` (`ft.RouteCallable` | `None`) – The view function to associate with the endpoint name.
- `provide_automatic_options` (`bool` | `None`) – Add the `OPTIONS` method and respond to `OPTIONS` requests automatically.
Register a rule for routing incoming requests and building URLs. [[#route]] decorator is a shortcut to call this with the `view_func` argument:
```python
@app.route('/')
def index():
```
Equivalent to: 
```python
def index():
app.add_url_rule("/", view_func=index)
```
Default method: `["GET"]`. `HEAD` is always added automatically, and `OPTIONS` is added automatically by default.

### route

Signature: `def route(rule, **options)`
Parameters:
- `rule` (`str`) – The URL rule string
- `options` (`Any`) – Extra options passed to the [`Rule`](https://werkzeug.palletsprojects.com/en/stable/routing/#werkzeug.routing.Rule "(in Werkzeug v3.1.x)") object.
Decorate a view function to register it with the given URL rule and options. Calls [[#add_url_rule]], which has more details about the implementation.


# Blueprint Objects

# Incoming Request Data

## Request

Signature: 

# Response Objects

# Session

# Session Interface


