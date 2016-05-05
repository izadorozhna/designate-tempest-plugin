# Copyright 2016 Hewlett Packard Enterprise Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from tempest import clients
from tempest import config

from designate_tempest_plugin.services.dns.v2.json.zones_client import \
    ZonesClient
from designate_tempest_plugin.services.dns.v2.json.zone_imports_client import \
    ZoneImportsClient
from designate_tempest_plugin.services.dns.v2.json.blacklists_client import \
    BlacklistsClient
from designate_tempest_plugin.services.dns.admin.json.quotas_client import \
    QuotasClient
from designate_tempest_plugin.services.dns.v2.json.zone_exports_client import \
    ZoneExportsClient
from designate_tempest_plugin.services.dns.v2.json.recordset_client import \
    RecordsetClient
from designate_tempest_plugin.services.dns.v2.json.pool_client import \
    PoolClient
from designate_tempest_plugin.services.dns.v2.json.tld_client import \
    TldClient

CONF = config.CONF


class Manager(clients.Manager):
    def __init__(self, credentials=None, service=None):
        super(Manager, self).__init__(credentials, service)

        params = {
            'service': CONF.dns.catalog_type,
            'region': CONF.identity.region,
            'endpoint_type': CONF.dns.endpoint_type,
            'build_interval': CONF.dns.build_interval,
            'build_timeout': CONF.dns.build_timeout
        }
        params.update(self.default_params)

        self.zones_client = ZonesClient(self.auth_provider, **params)
        self.zone_imports_client = ZoneImportsClient(self.auth_provider,
                                                     **params)
        self.blacklists_client = BlacklistsClient(self.auth_provider, **params)
        self.quotas_client = QuotasClient(self.auth_provider, **params)
        self.zone_exports_client = ZoneExportsClient(self.auth_provider,
                                                     **params)
        self.recordset_client = RecordsetClient(self.auth_provider,
                                                **params)
        self.pool_client = PoolClient(self.auth_provider,
                                      **params)
        self.tld_client = TldClient(self.auth_provider,
                                    **params)
