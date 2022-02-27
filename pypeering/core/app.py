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
from pypeering.core.endpoint import Endpoint
from pypeering.core.query import Request
from pypeering.models import (
    bgp,
    devices,
    extras,
    net,
    peering,
    peeringdb,
    users,
    utils,
)


class App(object):
    """Represents apps in Peering Manager.

    Calls to attributes are returned as Endpoint objects.

    :returns: :py:class:`.Endpoint` matching requested attribute.
    :raises: :py:class:`.RequestError`
        if requested endpoint doesn't exist.
    """

    def __init__(self, api, name):
        self.api = api
        self.name = name
        self._choices = None
        self._setmodel()

    models = {
        "bgp": bgp,
        "devices": devices,
        "extras": extras,
        "net": net,
        "peering": peering,
        "peeringdb": peeringdb,
        "users": users,
        "utils": utils,
    }

    def _setmodel(self):
        self.model = App.models[self.name] if self.name in App.models else None

    def __getstate__(self):
        return {"api": self.api, "name": self.name}

    def __setstate__(self, d):
        self.__dict__.update(d)
        self._setmodel()

    def __getattr__(self, name):
        return Endpoint(self.api, self, name, model=self.model)
