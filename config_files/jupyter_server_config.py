# Configuration file for jupyter-server.

## Allow password to be changed at login for the Jupyter server.
#
#                      While logging in with a token, the Jupyter server UI will give the opportunity to
#                      the user to enter a new password at the same time that will replace
#                      the token login mechanism.
#
#                      This can be set to false to prevent changing password from
#  the UI/API.
#  Default: True
#c.ServerApp.allow_password_change = True

## Allow requests where the Host header doesn't point to a local server
#
#         By default, requests get a 403 forbidden response if the 'Host' header
#         shows that the browser thinks it's on a non-local domain.
#         Setting this option to True disables this check.
#
#         This protects against 'DNS rebinding' attacks, where a remote web server
#         serves you a page and then changes its DNS to send later requests to a
#         local IP, bypassing same-origin checks.
#
#         Local IP addresses (such as 127.0.0.1 and ::1) are allowed as local,
#         along with hostnames configured in local_hostnames.
#  Default: False
#c.ServerApp.allow_remote_access = True

## Set the Access-Control-Allow-Origin header
#
#          Use '*' to allow any origin to access your server.
#
#          Takes precedence over allow_origin_pat.
#  Default: ''
#c.ServerApp.allow_origin = '*'


## Whether to allow the user to run the server as root.
#  Default: False
c.ServerApp.allow_root = True

## Timeout (in seconds) after which a kernel is considered idle and ready to be culled.
#          Values of 0 or lower disable culling. Very short timeouts may result in kernels being culled
#          for users with poor network connections.
#  Default: 0
c.MappingKernelManager.cull_idle_timeout = 0


## Hashed password to use for web authentication.
#
#                        To generate, type in a python/IPython shell:
#
#                          from jupyter_server.auth import passwd; passwd()
#
#                        The string should be of the form type:salt:hashed-
#  password.
#  Default: ''
#c.ServerApp.password = ''

## Token used for authenticating first-time connections to the server.
#
#          The token can be read from the file referenced by JUPYTER_TOKEN_FILE or set directly
#          with the JUPYTER_TOKEN environment variable.
#
#          When no password is enabled,
#          the default is to generate a new, random token.
#
#          Setting to an empty string disables authentication altogether, which
#  is NOT RECOMMENDED.
#  Default: '<generated>'
c.ServerApp.token = ''


## Forces users to use a password for the Jupyter server.
#                        This is useful in a multi user environment, for instance when
#                        everybody in the LAN can access each other's machine through ssh.
#
#                        In such a case, serving on localhost is not secure since
#                        any user can connect to the Jupyter server via ssh.
#  Default: False
#c.ServerApp.password_required = False

## Preferred starting directory to use for notebooks and kernels.
#  Default: ''
c.ServerApp.preferred_dir = '/home/jupyter/project'

## The directory to use for notebooks and kernels.
#  Default: ''
c.ServerApp.root_dir = '/home/jupyter/project'

#
## The UNIX socket the Jupyter server will listen on.
#  Default: ''
#c.ServerApp.sock = '8888'


## Set the kernel's IP address [default localhost].
#          If the IP address is s