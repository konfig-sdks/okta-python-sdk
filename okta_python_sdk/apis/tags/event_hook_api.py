# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_event_hooks_event_hook_id_lifecycle_activate.post import ActivateLifecycleSuccess
from okta_python_sdk.paths.api_v1_event_hooks.post import CreateSuccess
from okta_python_sdk.paths.api_v1_event_hooks_event_hook_id_lifecycle_deactivate.post import DeactivateLifecycleEvent
from okta_python_sdk.paths.api_v1_event_hooks_event_hook_id.get import GetSuccessEvent
from okta_python_sdk.paths.api_v1_event_hooks.get import ListSuccessEvents
from okta_python_sdk.paths.api_v1_event_hooks_event_hook_id.delete import RemoveSuccessEvent
from okta_python_sdk.paths.api_v1_event_hooks_event_hook_id.put import UpdateSuccessEvent
from okta_python_sdk.paths.api_v1_event_hooks_event_hook_id_lifecycle_verify.post import VerifyLifecycleSuccess
from okta_python_sdk.apis.tags.event_hook_api_raw import EventHookApiRaw


class EventHookApi(
    ActivateLifecycleSuccess,
    CreateSuccess,
    DeactivateLifecycleEvent,
    GetSuccessEvent,
    ListSuccessEvents,
    RemoveSuccessEvent,
    UpdateSuccessEvent,
    VerifyLifecycleSuccess,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EventHookApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EventHookApiRaw(api_client)
