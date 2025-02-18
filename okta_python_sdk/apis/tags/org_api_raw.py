# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_org_privacy_okta_support_extend.post import ExtendOktaSupportRaw
from okta_python_sdk.paths.api_v1_org_privacy_okta_support_revoke.post import ExtendOktaSupport0Raw
from okta_python_sdk.paths.api_v1_org_contacts_contact_type.get import GetContactUserRaw
from okta_python_sdk.paths.api_v1_org_privacy_okta_communication.get import GetOktaCommunicationSettingsRaw
from okta_python_sdk.paths.api_v1_org_privacy_okta_support.get import GetOktaSupportSettingsRaw
from okta_python_sdk.paths.api_v1_org_preferences.get import GetOrgPreferencesRaw
from okta_python_sdk.paths.api_v1_org.get import GetSettingsRaw
from okta_python_sdk.paths.api_v1_org_privacy_okta_support_grant.post import GrantOktaSupportAccessRaw
from okta_python_sdk.paths.api_v1_org_preferences_hide_end_user_footer.post import HideEndUserFooterRaw
from okta_python_sdk.paths.api_v1_org_contacts.get import ListContactTypesRaw
from okta_python_sdk.paths.api_v1_org_preferences_show_end_user_footer.post import MakeOktaUiFooterVisibleRaw
from okta_python_sdk.paths.api_v1_org_privacy_okta_communication_opt_in.post import OptInOktaCommunicationEmailsRaw
from okta_python_sdk.paths.api_v1_org_privacy_okta_communication_opt_out.post import OptOutOktaCommunicationEmailsRaw
from okta_python_sdk.paths.api_v1_org_contacts_contact_type.put import UpdateContactUserRaw
from okta_python_sdk.paths.api_v1_org_logo.post import UpdateOrganizationLogoRaw
from okta_python_sdk.paths.api_v1_org.put import UpdateSettingRaw
from okta_python_sdk.paths.api_v1_org.post import UpdateSettingsRaw


class OrgApiRaw(
    ExtendOktaSupportRaw,
    ExtendOktaSupport0Raw,
    GetContactUserRaw,
    GetOktaCommunicationSettingsRaw,
    GetOktaSupportSettingsRaw,
    GetOrgPreferencesRaw,
    GetSettingsRaw,
    GrantOktaSupportAccessRaw,
    HideEndUserFooterRaw,
    ListContactTypesRaw,
    MakeOktaUiFooterVisibleRaw,
    OptInOktaCommunicationEmailsRaw,
    OptOutOktaCommunicationEmailsRaw,
    UpdateContactUserRaw,
    UpdateOrganizationLogoRaw,
    UpdateSettingRaw,
    UpdateSettingsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
