"""
DB operations for Proxy Types
"""

from api.models.base import DBModel


class ProxyTypeDB(DBModel):
    '''DBModel for the proxy_types table'''

    tablename = 'proxy_types'
