from pkg_resources import get_distribution, DistributionNotFound

from pypeering.core.query import RequestError, AllocationError, ContentError
from pypeering.core.api import Api as api

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    pass
