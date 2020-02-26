import os
import pkg_resources


X = "foo"
SCRIPT_PATH = os.path.abspath(pkg_resources.resource_filename(__name__, 'run-blocks'))
