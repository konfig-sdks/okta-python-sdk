# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_domains_domain_id_certificate.put import CreateCertificateRaw
from okta_python_sdk.paths.api_v1_domains.post import CreateNewDomainRaw
from okta_python_sdk.paths.api_v1_domains_domain_id.get import GetByIdRaw
from okta_python_sdk.paths.api_v1_domains.get import ListVerifiedCustomRaw
from okta_python_sdk.paths.api_v1_domains_domain_id.delete import RemoveByIdRaw
from okta_python_sdk.paths.api_v1_domains_domain_id_verify.post import VerifyByIdRaw


class DomainApiRaw(
    CreateCertificateRaw,
    CreateNewDomainRaw,
    GetByIdRaw,
    ListVerifiedCustomRaw,
    RemoveByIdRaw,
    VerifyByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
