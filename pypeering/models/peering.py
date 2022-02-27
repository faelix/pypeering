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
from pypeering.core.response import Record
from pypeering.core.endpoint import DetailEndpoint
from pypeering.models.bgp import Relationships
from pypeering.models.net import Connections
from pypeering.models.devices import Platforms


class AutonomousSystems(Record):
    pass


class Communities(Record):
    pass


class RoutingPolicies(Record):
    pass


class InternetExchanges(Record):
    local_autonomous_system = AutonomousSystems
    import_routing_policies = [RoutingPolicies]
    export_routing_policies = [RoutingPolicies]
    communities = [Communities]


class BgpGroups(Record):
    local_autonomous_system = AutonomousSystems
    import_routing_policies = [RoutingPolicies]
    export_routing_policies = [RoutingPolicies]
    communities = [Communities]


class Emails(Record):
    pass


class InternetExchangePeeringSessions(Record):
    autonomous_system = AutonomousSystems
    ixp_connection = Connections


class Routers(Record):
    platform = Platforms
    local_autonomous_system = AutonomousSystems


class DirectPeeringSessions(Record):
    local_autonomous_system = AutonomousSystems
    autonomous_system = AutonomousSystems
    bgp_group = BgpGroups
    relationship = Relationships
    router = Routers
    import_routing_policies = [RoutingPolicies]
    export_routing_policies = [RoutingPolicies]
