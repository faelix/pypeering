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
from six.moves.urllib.parse import urlsplit

from pypeering.core.query import Request
from pypeering.core.response import Record, JsonField
from pypeering.models.peering import InternetExchanges, Routers


class Connections(Record):
    """Connections Object

    Represents a connection response from peering manager.

    Attributes:
        primary_ip, ip4, ip6 (list): Tells __init__ in Record() to
            take the `primary_ip` field's value from the API
            response and return an initialized list of IpAddress
            objects
        device_type (obj): Tells __init__ in Record() to take the
            `device_type` field's value from the API response and
            return an initialized DeviceType object
    """

    # XXX has_details = True
    internet_exchange_point = InternetExchanges
    router = Routers
    config_context = JsonField
    # XXX tags = [Tags]
