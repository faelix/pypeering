# Pypeering
Python API client library for [Peering Manager](https://github.com/peering-manager/peering-manager).


## Installation

To install run `pip install pypeering`.

Alternatively, you can clone the repo and run `python setup.py install`.


## Quick Start

The full pypeering API is documented on [Read the Docs](https://peering-manager.readthedocs.io/en/stable/), but the following should be enough to get started using it.

To begin, import pypeering and instantiate the API.

```
import pypeering
nb = pypeering.api(
    'http://localhost:8000',
    token='d6f4e314a5b5fefd164995169f28ae32d987704f'
)
```

The first argument the .api() method takes is the Peering Manager URL. The `token` argument should to be provided, and will grant
read-only or read-write access as configured in Peering Manager.


## Queries

The pypeering API is setup so that Peering Manager's apps are attributes of the `.api()` object, and in turn those apps have attribute representing each endpoint. Each endpoint has a handful of methods available to carry out actions on the endpoint. For example, in order to query all the objects in the `devices` endpoint you would do the following:

```
>>> devices = nb.dcim.devices.all()
>>> for device in devices:
...     print(device.name)
...
test1-leaf1
test1-leaf2
test1-leaf3
>>>
```

### Threading

pypypeering supports multithreaded calls (in Python 3 only) for `.filter()` and `.all()` queries. It is **highly recommended** you have `MAX_PAGE_SIZE` in your Netbox install set to anything *except* `0` or `None`. The default value of `1000` is usually a good value to use. To enable threading, add `threading=True` parameter to the `.api`:

```python
nb = pypeering.api(
    'http://localhost:8000',
    threading=True,
)
```
