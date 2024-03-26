# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_domains_domain_id_certificate.put import CreateCertificate
from okta_python_sdk.paths.api_v1_domains.post import CreateNewDomain
from okta_python_sdk.paths.api_v1_domains_domain_id.get import GetById
from okta_python_sdk.paths.api_v1_domains.get import ListVerifiedCustom
from okta_python_sdk.paths.api_v1_domains_domain_id.delete import RemoveById
from okta_python_sdk.paths.api_v1_domains_domain_id_verify.post import VerifyById
from okta_python_sdk.apis.tags.domain_api_raw import DomainApiRaw


class DomainApi(
    CreateCertificate,
    CreateNewDomain,
    GetById,
    ListVerifiedCustom,
    RemoveById,
    VerifyById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DomainApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DomainApiRaw(api_client)
