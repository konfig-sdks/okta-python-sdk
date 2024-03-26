# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_templates_sms.post import AddNewCustomSms
from okta_python_sdk.paths.api_v1_templates_sms.get import EnumerateSmsTemplates
from okta_python_sdk.paths.api_v1_templates_sms_template_id.get import GetById
from okta_python_sdk.paths.api_v1_templates_sms_template_id.post import PartialSmsUpdate
from okta_python_sdk.paths.api_v1_templates_sms_template_id.delete import RemoveSms
from okta_python_sdk.paths.api_v1_templates_sms_template_id.put import UpdateSmsTemplate
from okta_python_sdk.apis.tags.template_api_raw import TemplateApiRaw


class TemplateApi(
    AddNewCustomSms,
    EnumerateSmsTemplates,
    GetById,
    PartialSmsUpdate,
    RemoveSms,
    UpdateSmsTemplate,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TemplateApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TemplateApiRaw(api_client)
