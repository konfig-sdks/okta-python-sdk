# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_idps_idp_id_lifecycle_activate.post import ActivateIdpLifecycle
from okta_python_sdk.paths.api_v1_idps.post import AddNewIdp
from okta_python_sdk.paths.api_v1_idps_credentials_keys.post import AddX509CertificatePublicKey
from okta_python_sdk.paths.api_v1_idps_idp_id_credentials_keys_key_id_clone.post import CloneSigningKeyCredential
from okta_python_sdk.paths.api_v1_idps_idp_id_lifecycle_deactivate.post import DeactivateIdp
from okta_python_sdk.paths.api_v1_idps_credentials_keys_key_id.delete import DeleteKeyCredential
from okta_python_sdk.paths.api_v1_idps_credentials_keys.get import EnumerateIdpKeys
from okta_python_sdk.paths.api_v1_idps_idp_id_credentials_csrs.post import GenerateCsr
from okta_python_sdk.paths.api_v1_idps_idp_id_credentials_keys_generate.post import GenerateNewSigningKeyCredential
from okta_python_sdk.paths.api_v1_idps_idp_id.get import GetByIdp
from okta_python_sdk.paths.api_v1_idps_idp_id_credentials_csrs_csr_id.get import GetCsrByIdp
from okta_python_sdk.paths.api_v1_idps_credentials_keys_key_id.get import GetKeyCredentialByIdp
from okta_python_sdk.paths.api_v1_idps_idp_id_users_user_id.get import GetLinkedUserById
from okta_python_sdk.paths.api_v1_idps_idp_id_credentials_keys_key_id.get import GetSigningKeyCredentialByIdp
from okta_python_sdk.paths.api_v1_idps_idp_id_users_user_id_credentials_tokens.get import GetSocialAuthTokens
from okta_python_sdk.paths.api_v1_idps_idp_id_users.get import GetUser
from okta_python_sdk.paths.api_v1_idps_idp_id_users_user_id.post import LinkUserToIdpWithoutTransaction
from okta_python_sdk.paths.api_v1_idps.get import List
from okta_python_sdk.paths.api_v1_idps_idp_id_credentials_csrs.get import ListCsrsForCertificateSigningRequests
from okta_python_sdk.paths.api_v1_idps_idp_id_credentials_keys.get import ListSigningKeyCredentials
from okta_python_sdk.paths.api_v1_idps_idp_id.delete import RemoveIdp
from okta_python_sdk.paths.api_v1_idps_idp_id_credentials_csrs_csr_id.delete import RevokeCsrForIdentityProvider
from okta_python_sdk.paths.api_v1_idps_idp_id_users_user_id.delete import UnlinkUser
from okta_python_sdk.paths.api_v1_idps_idp_id.put import UpdateConfiguration
from okta_python_sdk.paths.api_v1_idps_idp_id_credentials_csrs_csr_id_lifecycle_publish.post import UpdateCsrLifecyclePublish
from okta_python_sdk.apis.tags.identity_provider_api_raw import IdentityProviderApiRaw


class IdentityProviderApi(
    ActivateIdpLifecycle,
    AddNewIdp,
    AddX509CertificatePublicKey,
    CloneSigningKeyCredential,
    DeactivateIdp,
    DeleteKeyCredential,
    EnumerateIdpKeys,
    GenerateCsr,
    GenerateNewSigningKeyCredential,
    GetByIdp,
    GetCsrByIdp,
    GetKeyCredentialByIdp,
    GetLinkedUserById,
    GetSigningKeyCredentialByIdp,
    GetSocialAuthTokens,
    GetUser,
    LinkUserToIdpWithoutTransaction,
    List,
    ListCsrsForCertificateSigningRequests,
    ListSigningKeyCredentials,
    RemoveIdp,
    RevokeCsrForIdentityProvider,
    UnlinkUser,
    UpdateConfiguration,
    UpdateCsrLifecyclePublish,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: IdentityProviderApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = IdentityProviderApiRaw(api_client)
