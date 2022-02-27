"""
(c) 2017 DigitalOcean
(c) 2022 Faelix Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import sys

import requests

from pypeering.core.query import Request
from pypeering.core.app import App
from pypeering.core.response import Record


class Api(object):
    """The API object is the point of entry to pypeering.

    After instantiating the Api() with the appropriate named arguments
    you can specify which app and endpoint you wish to interact with.

    Valid attributes currently are:
        * bgp
        * devices
        * extras
        * net
        * peering
        * peeringdb
        * users
        * utils

    Calling any of these attributes will return
    :py:class:`.App` which exposes endpoints as attributes.

    **Additional Attributes**:
        *  **http_session(requests.Session)**:
                Override the default session with your own. This is used to control
                a number of HTTP behaviors such as SSL verification, custom headers,
                retires, and timeouts.
                See `custom sessions <advanced.html#custom-sessions>`__ for more info.

    :param str url: The base URL to the instance of Peering Manager you
        wish to connect to.
    :param str token: Your Peering Manager token.
    :param bool,optional threading: Set to True to use threading in ``.all()``
        and ``.filter()`` requests.
    :raises ValueError: If *private_key* and *private_key_file* are both
        specified.
    :raises AttributeError: If app doesn't exist.
    :Examples:

    >>> import pypeering
    >>> pm = pypeering.api(
    ...     'http://localhost:8000',
    ...     token='d6f4e314a5b5fefd164995169f28ae32d987704f'
    ... )
    >>> list(pm.dcim.devices.all())
    [test1-leaf1, test1-leaf2, test1-leaf3]
    """

    def __init__(
        self,
        url,
        token=None,
        threading=False,
    ):
        base_url = "{}/api".format(url if url[-1] != "/" else url[:-1])
        self.token = token
        self.base_url = base_url
        self.http_session = requests.Session()
        if threading and sys.version_info.major == 2:
            raise NotImplementedError(
                "Threaded pypeering calls not supported                 in Python 2"
            )
        self.threading = threading

        self.bgp = App(self, "bgp")
        self.devices = App(self, "devices")
        self.extras = App(self, "extras")
        self.net = App(self, "net")
        self.peering = App(self, "peering")
        self.peeringdb = App(self, "peeringdb")
        self.users = App(self, "users")
        self.utils = App(self, "utils")

    @property
    def version(self):
        """Gets the API version of Peering Manager.

        Can be used to check the Peering Manager API version if there are
        version-dependent features or syntaxes in the API.

        :Returns: Version number as a string.
        :Example:

        >>> import pypeering
        >>> pm = pypeering.api(
        ...     'http://localhost:8000',
        ...     token='d6f4e314a5b5fefd164995169f28ae32d987704f'
        ... )
        >>> pm.version
        '3.1'
        >>>
        """
        version = Request(
            base=self.base_url,
            http_session=self.http_session,
        ).get_version()
        return version

    def openapi(self):
        """Returns the OpenAPI spec.

        Quick helper function to pull down the entire OpenAPI spec.

        :Returns: dict
        :Example:

        >>> import pypeering
        >>> pm = pypeering.api(
        ...     'http://localhost:8000',
        ...     token='d6f4e314a5b5fefd164995169f28ae32d987704f'
        ... )
        >>> pm.openapi()
        {...}
        >>>
        """
        return Request(
            base=self.base_url,
            http_session=self.http_session,
        ).get_openapi()

    def status(self):
        """Gets the status information from Peering Manager.

        Available in Peering Manager 2.10.0 or newer.

        :Returns: Dictionary as returned by Peering Manager.
        :Raises: :py:class:`.RequestError` if the request is not successful.
        :Example:

        >>> pprint.pprint(pm.status())
        {'django-version': '3.2.10',
         'installed-apps': {'cacheops': '5.0.1',
                            'debug_toolbar': '3.2.2',
                            'django_filters': '21.1',
                            'django_prometheus': '2.1.0',
                            'django_rq': '2.5.1',
                            'django_tables2': '2.4.1',
                            'drf_spectacular': '0.21.0',
                            'rest_framework': '3.12.4',
                            'taggit': '2.0.0'},
         'peering-manager-version': 'v1.5.2',
         'python-version': '3.7.3',
         'rq-workers-running': 1}
        >>>
        """
        status = Request(
            base=self.base_url,
            token=self.token,
            http_session=self.http_session,
        ).get_status()
        return status
