<div align="center">

[![Visit Okta](./header.png)](https://okta.com)

# Okta<a id="okta"></a>

Allows customers to easily access the Okta API


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`okta.application.activate_client_secret`](#oktaapplicationactivate_client_secret)
  * [`okta.application.activate_default_provisioning_connection`](#oktaapplicationactivate_default_provisioning_connection)
  * [`okta.application.activate_inactive`](#oktaapplicationactivate_inactive)
  * [`okta.application.add_client_secret`](#oktaapplicationadd_client_secret)
  * [`okta.application.assign_group_to`](#oktaapplicationassign_group_to)
  * [`okta.application.assign_policy_to_application`](#oktaapplicationassign_policy_to_application)
  * [`okta.application.assign_user_to_application`](#oktaapplicationassign_user_to_application)
  * [`okta.application.clone_application_key_credential`](#oktaapplicationclone_application_key_credential)
  * [`okta.application.create_new`](#oktaapplicationcreate_new)
  * [`okta.application.deactivate_client_secret_by_id`](#oktaapplicationdeactivate_client_secret_by_id)
  * [`okta.application.deactivate_default_provisioning_connection`](#oktaapplicationdeactivate_default_provisioning_connection)
  * [`okta.application.deactivate_lifecycle`](#oktaapplicationdeactivate_lifecycle)
  * [`okta.application.delete_csr_by_id`](#oktaapplicationdelete_csr_by_id)
  * [`okta.application.generate_csr_for_application`](#oktaapplicationgenerate_csr_for_application)
  * [`okta.application.generate_x509_certificate`](#oktaapplicationgenerate_x509_certificate)
  * [`okta.application.get_by_id`](#oktaapplicationget_by_id)
  * [`okta.application.get_client_secret`](#oktaapplicationget_client_secret)
  * [`okta.application.get_credentials_csrs`](#oktaapplicationget_credentials_csrs)
  * [`okta.application.get_default_provisioning_connection`](#oktaapplicationget_default_provisioning_connection)
  * [`okta.application.get_feature`](#oktaapplicationget_feature)
  * [`okta.application.get_group_assignment`](#oktaapplicationget_group_assignment)
  * [`okta.application.get_key_credential`](#oktaapplicationget_key_credential)
  * [`okta.application.get_single_scope_consent_grant`](#oktaapplicationget_single_scope_consent_grant)
  * [`okta.application.get_specific_user_assignment`](#oktaapplicationget_specific_user_assignment)
  * [`okta.application.get_token`](#oktaapplicationget_token)
  * [`okta.application.grant_consent_to_scope`](#oktaapplicationgrant_consent_to_scope)
  * [`okta.application.list_apps`](#oktaapplicationlist_apps)
  * [`okta.application.list_assigned_users`](#oktaapplicationlist_assigned_users)
  * [`okta.application.list_client_secrets`](#oktaapplicationlist_client_secrets)
  * [`okta.application.list_csrs_for_application`](#oktaapplicationlist_csrs_for_application)
  * [`okta.application.list_features`](#oktaapplicationlist_features)
  * [`okta.application.list_groups_assigned`](#oktaapplicationlist_groups_assigned)
  * [`okta.application.list_key_credentials`](#oktaapplicationlist_key_credentials)
  * [`okta.application.list_scope_consent_grants`](#oktaapplicationlist_scope_consent_grants)
  * [`okta.application.list_tokens`](#oktaapplicationlist_tokens)
  * [`okta.application.preview_saml_app_metadata`](#oktaapplicationpreview_saml_app_metadata)
  * [`okta.application.publish_csr_lifecycle`](#oktaapplicationpublish_csr_lifecycle)
  * [`okta.application.remove_group_assignment`](#oktaapplicationremove_group_assignment)
  * [`okta.application.remove_inactive`](#oktaapplicationremove_inactive)
  * [`okta.application.remove_secret`](#oktaapplicationremove_secret)
  * [`okta.application.remove_user_from`](#oktaapplicationremove_user_from)
  * [`okta.application.revoke_all_tokens`](#oktaapplicationrevoke_all_tokens)
  * [`okta.application.revoke_permission`](#oktaapplicationrevoke_permission)
  * [`okta.application.revoke_token`](#oktaapplicationrevoke_token)
  * [`okta.application.set_default_provisioning_connection`](#oktaapplicationset_default_provisioning_connection)
  * [`okta.application.update_application_in_org`](#oktaapplicationupdate_application_in_org)
  * [`okta.application.update_feature`](#oktaapplicationupdate_feature)
  * [`okta.application.update_logo`](#oktaapplicationupdate_logo)
  * [`okta.application.update_profile_for_user`](#oktaapplicationupdate_profile_for_user)
  * [`okta.authenticator.activate_lifecycle_success`](#oktaauthenticatoractivate_lifecycle_success)
  * [`okta.authenticator.create_new`](#oktaauthenticatorcreate_new)
  * [`okta.authenticator.deactivate_lifecycle_success`](#oktaauthenticatordeactivate_lifecycle_success)
  * [`okta.authenticator.get_success`](#oktaauthenticatorget_success)
  * [`okta.authenticator.list_all_available`](#oktaauthenticatorlist_all_available)
  * [`okta.authenticator.update_authenticator`](#oktaauthenticatorupdate_authenticator)
  * [`okta.authorization_server.activate_lifecycle_success`](#oktaauthorization_serveractivate_lifecycle_success)
  * [`okta.authorization_server.activate_policy_lifecycle`](#oktaauthorization_serveractivate_policy_lifecycle)
  * [`okta.authorization_server.activate_policy_rule`](#oktaauthorization_serveractivate_policy_rule)
  * [`okta.authorization_server.create_claims`](#oktaauthorization_servercreate_claims)
  * [`okta.authorization_server.create_new_server`](#oktaauthorization_servercreate_new_server)
  * [`okta.authorization_server.create_policy`](#oktaauthorization_servercreate_policy)
  * [`okta.authorization_server.create_policy_rule`](#oktaauthorization_servercreate_policy_rule)
  * [`okta.authorization_server.create_scope`](#oktaauthorization_servercreate_scope)
  * [`okta.authorization_server.deactivate_lifecycle`](#oktaauthorization_serverdeactivate_lifecycle)
  * [`okta.authorization_server.deactivate_policy_lifecycle`](#oktaauthorization_serverdeactivate_policy_lifecycle)
  * [`okta.authorization_server.deactivate_policy_rule`](#oktaauthorization_serverdeactivate_policy_rule)
  * [`okta.authorization_server.delete_auth_token`](#oktaauthorization_serverdelete_auth_token)
  * [`okta.authorization_server.delete_claim`](#oktaauthorization_serverdelete_claim)
  * [`okta.authorization_server.delete_client_token`](#oktaauthorization_serverdelete_client_token)
  * [`okta.authorization_server.delete_policy_by_id`](#oktaauthorization_serverdelete_policy_by_id)
  * [`okta.authorization_server.delete_policy_rule`](#oktaauthorization_serverdelete_policy_rule)
  * [`okta.authorization_server.delete_scope`](#oktaauthorization_serverdelete_scope)
  * [`okta.authorization_server.delete_success`](#oktaauthorization_serverdelete_success)
  * [`okta.authorization_server.enumerate_policy_rules`](#oktaauthorization_serverenumerate_policy_rules)
  * [`okta.authorization_server.get_by_id`](#oktaauthorization_serverget_by_id)
  * [`okta.authorization_server.get_claims`](#oktaauthorization_serverget_claims)
  * [`okta.authorization_server.get_claims_0`](#oktaauthorization_serverget_claims_0)
  * [`okta.authorization_server.get_client_auth_token`](#oktaauthorization_serverget_client_auth_token)
  * [`okta.authorization_server.get_client_tokens`](#oktaauthorization_serverget_client_tokens)
  * [`okta.authorization_server.get_policies`](#oktaauthorization_serverget_policies)
  * [`okta.authorization_server.get_policies_success`](#oktaauthorization_serverget_policies_success)
  * [`okta.authorization_server.get_policy_rule_by_id`](#oktaauthorization_serverget_policy_rule_by_id)
  * [`okta.authorization_server.get_scopes`](#oktaauthorization_serverget_scopes)
  * [`okta.authorization_server.get_scopes_0`](#oktaauthorization_serverget_scopes_0)
  * [`okta.authorization_server.list_clients`](#oktaauthorization_serverlist_clients)
  * [`okta.authorization_server.list_credentials_keys`](#oktaauthorization_serverlist_credentials_keys)
  * [`okta.authorization_server.list_servers`](#oktaauthorization_serverlist_servers)
  * [`okta.authorization_server.rotate_key_lifecycle`](#oktaauthorization_serverrotate_key_lifecycle)
  * [`okta.authorization_server.update_by_id`](#oktaauthorization_serverupdate_by_id)
  * [`okta.authorization_server.update_claim_success`](#oktaauthorization_serverupdate_claim_success)
  * [`okta.authorization_server.update_policy_rule_configuration`](#oktaauthorization_serverupdate_policy_rule_configuration)
  * [`okta.authorization_server.update_policy_success`](#oktaauthorization_serverupdate_policy_success)
  * [`okta.authorization_server.update_scope_success`](#oktaauthorization_serverupdate_scope_success)
  * [`okta.brand.create_email_template_customization`](#oktabrandcreate_email_template_customization)
  * [`okta.brand.delete_email_customization`](#oktabranddelete_email_customization)
  * [`okta.brand.delete_email_template_customizations`](#oktabranddelete_email_template_customizations)
  * [`okta.brand.delete_theme_background_image`](#oktabranddelete_theme_background_image)
  * [`okta.brand.delete_theme_favicon`](#oktabranddelete_theme_favicon)
  * [`okta.brand.delete_theme_logo`](#oktabranddelete_theme_logo)
  * [`okta.brand.get_all_brands`](#oktabrandget_all_brands)
  * [`okta.brand.get_by_id`](#oktabrandget_by_id)
  * [`okta.brand.get_email_customization_preview`](#oktabrandget_email_customization_preview)
  * [`okta.brand.get_email_template`](#oktabrandget_email_template)
  * [`okta.brand.get_email_template_customization_by_id`](#oktabrandget_email_template_customization_by_id)
  * [`okta.brand.get_email_template_default_content`](#oktabrandget_email_template_default_content)
  * [`okta.brand.get_email_template_default_content_preview`](#oktabrandget_email_template_default_content_preview)
  * [`okta.brand.get_email_template_default_content_preview_0`](#oktabrandget_email_template_default_content_preview_0)
  * [`okta.brand.get_theme_by_id`](#oktabrandget_theme_by_id)
  * [`okta.brand.get_themes`](#oktabrandget_themes)
  * [`okta.brand.list_email_template_customizations`](#oktabrandlist_email_template_customizations)
  * [`okta.brand.list_email_templates`](#oktabrandlist_email_templates)
  * [`okta.brand.update_by_brand_id`](#oktabrandupdate_by_brand_id)
  * [`okta.brand.update_email_customization`](#oktabrandupdate_email_customization)
  * [`okta.brand.update_theme`](#oktabrandupdate_theme)
  * [`okta.brand.update_theme_background_image`](#oktabrandupdate_theme_background_image)
  * [`okta.brand.update_theme_favicon`](#oktabrandupdate_theme_favicon)
  * [`okta.brand.update_theme_logo`](#oktabrandupdate_theme_logo)
  * [`okta.domain.create_certificate`](#oktadomaincreate_certificate)
  * [`okta.domain.create_new_domain`](#oktadomaincreate_new_domain)
  * [`okta.domain.get_by_id`](#oktadomainget_by_id)
  * [`okta.domain.list_verified_custom`](#oktadomainlist_verified_custom)
  * [`okta.domain.remove_by_id`](#oktadomainremove_by_id)
  * [`okta.domain.verify_by_id`](#oktadomainverify_by_id)
  * [`okta.event_hook.activate_lifecycle_success`](#oktaevent_hookactivate_lifecycle_success)
  * [`okta.event_hook.create_success`](#oktaevent_hookcreate_success)
  * [`okta.event_hook.deactivate_lifecycle_event`](#oktaevent_hookdeactivate_lifecycle_event)
  * [`okta.event_hook.get_success_event`](#oktaevent_hookget_success_event)
  * [`okta.event_hook.list_success_events`](#oktaevent_hooklist_success_events)
  * [`okta.event_hook.remove_success_event`](#oktaevent_hookremove_success_event)
  * [`okta.event_hook.update_success_event`](#oktaevent_hookupdate_success_event)
  * [`okta.event_hook.verify_lifecycle_success`](#oktaevent_hookverify_lifecycle_success)
  * [`okta.feature.create_lifecycle_success`](#oktafeaturecreate_lifecycle_success)
  * [`okta.feature.get_success`](#oktafeatureget_success)
  * [`okta.feature.get_success_by_id`](#oktafeatureget_success_by_id)
  * [`okta.feature.list_dependencies`](#oktafeaturelist_dependencies)
  * [`okta.feature.list_dependents`](#oktafeaturelist_dependents)
  * [`okta.group.activate_rule_lifecycle`](#oktagroupactivate_rule_lifecycle)
  * [`okta.group.add_app_instance_target_to_app_admin_role_given_to_group`](#oktagroupadd_app_instance_target_to_app_admin_role_given_to_group)
  * [`okta.group.add_rule`](#oktagroupadd_rule)
  * [`okta.group.add_user_to_group`](#oktagroupadd_user_to_group)
  * [`okta.group.assign_role_to_group`](#oktagroupassign_role_to_group)
  * [`okta.group.create_new_group`](#oktagroupcreate_new_group)
  * [`okta.group.deactivate_rule_lifecycle`](#oktagroupdeactivate_rule_lifecycle)
  * [`okta.group.delete_target_group_roles_catalog_apps`](#oktagroupdelete_target_group_roles_catalog_apps)
  * [`okta.group.enumerate_group_members`](#oktagroupenumerate_group_members)
  * [`okta.group.get_all_rules`](#oktagroupget_all_rules)
  * [`okta.group.get_group_rule_by_id`](#oktagroupget_group_rule_by_id)
  * [`okta.group.get_role_list`](#oktagroupget_role_list)
  * [`okta.group.get_role_success`](#oktagroupget_role_success)
  * [`okta.group.get_role_targets_catalog_apps`](#oktagroupget_role_targets_catalog_apps)
  * [`okta.group.get_rules`](#oktagroupget_rules)
  * [`okta.group.list`](#oktagrouplist)
  * [`okta.group.list_assigned_apps`](#oktagrouplist_assigned_apps)
  * [`okta.group.list_role_targets_groups`](#oktagrouplist_role_targets_groups)
  * [`okta.group.remove_app_instance_target_to_app_admin_role_given_to_group`](#oktagroupremove_app_instance_target_to_app_admin_role_given_to_group)
  * [`okta.group.remove_operation`](#oktagroupremove_operation)
  * [`okta.group.remove_rule_by_id`](#oktagroupremove_rule_by_id)
  * [`okta.group.remove_target_group`](#oktagroupremove_target_group)
  * [`okta.group.remove_user_from`](#oktagroupremove_user_from)
  * [`okta.group.unassign_role`](#oktagroupunassign_role)
  * [`okta.group.update_profile`](#oktagroupupdate_profile)
  * [`okta.group.update_roles_catalog_apps`](#oktagroupupdate_roles_catalog_apps)
  * [`okta.group.update_rule`](#oktagroupupdate_rule)
  * [`okta.group.update_target_groups_role`](#oktagroupupdate_target_groups_role)
  * [`okta.group_schema.get`](#oktagroup_schemaget)
  * [`okta.group_schema.update_custom_properties`](#oktagroup_schemaupdate_custom_properties)
  * [`okta.identity_provider.activate_idp_lifecycle`](#oktaidentity_provideractivate_idp_lifecycle)
  * [`okta.identity_provider.add_new_idp`](#oktaidentity_provideradd_new_idp)
  * [`okta.identity_provider.add_x509_certificate_public_key`](#oktaidentity_provideradd_x509_certificate_public_key)
  * [`okta.identity_provider.clone_signing_key_credential`](#oktaidentity_providerclone_signing_key_credential)
  * [`okta.identity_provider.deactivate_idp`](#oktaidentity_providerdeactivate_idp)
  * [`okta.identity_provider.delete_key_credential`](#oktaidentity_providerdelete_key_credential)
  * [`okta.identity_provider.enumerate_idp_keys`](#oktaidentity_providerenumerate_idp_keys)
  * [`okta.identity_provider.generate_csr`](#oktaidentity_providergenerate_csr)
  * [`okta.identity_provider.generate_new_signing_key_credential`](#oktaidentity_providergenerate_new_signing_key_credential)
  * [`okta.identity_provider.get_by_idp`](#oktaidentity_providerget_by_idp)
  * [`okta.identity_provider.get_csr_by_idp`](#oktaidentity_providerget_csr_by_idp)
  * [`okta.identity_provider.get_key_credential_by_idp`](#oktaidentity_providerget_key_credential_by_idp)
  * [`okta.identity_provider.get_linked_user_by_id`](#oktaidentity_providerget_linked_user_by_id)
  * [`okta.identity_provider.get_signing_key_credential_by_idp`](#oktaidentity_providerget_signing_key_credential_by_idp)
  * [`okta.identity_provider.get_social_auth_tokens`](#oktaidentity_providerget_social_auth_tokens)
  * [`okta.identity_provider.get_user`](#oktaidentity_providerget_user)
  * [`okta.identity_provider.link_user_to_idp_without_transaction`](#oktaidentity_providerlink_user_to_idp_without_transaction)
  * [`okta.identity_provider.list`](#oktaidentity_providerlist)
  * [`okta.identity_provider.list_csrs_for_certificate_signing_requests`](#oktaidentity_providerlist_csrs_for_certificate_signing_requests)
  * [`okta.identity_provider.list_signing_key_credentials`](#oktaidentity_providerlist_signing_key_credentials)
  * [`okta.identity_provider.remove_idp`](#oktaidentity_providerremove_idp)
  * [`okta.identity_provider.revoke_csr_for_identity_provider`](#oktaidentity_providerrevoke_csr_for_identity_provider)
  * [`okta.identity_provider.unlink_user`](#oktaidentity_providerunlink_user)
  * [`okta.identity_provider.update_configuration`](#oktaidentity_providerupdate_configuration)
  * [`okta.identity_provider.update_csr_lifecycle_publish`](#oktaidentity_providerupdate_csr_lifecycle_publish)
  * [`okta.inline_hook.activate_lifecycle`](#oktainline_hookactivate_lifecycle)
  * [`okta.inline_hook.create_success`](#oktainline_hookcreate_success)
  * [`okta.inline_hook.deactivate_lifecycle`](#oktainline_hookdeactivate_lifecycle)
  * [`okta.inline_hook.delete_matching_by_id`](#oktainline_hookdelete_matching_by_id)
  * [`okta.inline_hook.execute_with_input`](#oktainline_hookexecute_with_input)
  * [`okta.inline_hook.get_by_id`](#oktainline_hookget_by_id)
  * [`okta.inline_hook.get_success`](#oktainline_hookget_success)
  * [`okta.inline_hook.update_by_id`](#oktainline_hookupdate_by_id)
  * [`okta.linked_object.create_linked_object`](#oktalinked_objectcreate_linked_object)
  * [`okta.linked_object.delete_user_linked_object`](#oktalinked_objectdelete_user_linked_object)
  * [`okta.linked_object.get_user_linked_objects`](#oktalinked_objectget_user_linked_objects)
  * [`okta.linked_object.get_user_linked_objects_0`](#oktalinked_objectget_user_linked_objects_0)
  * [`okta.log.get_list_events`](#oktalogget_list_events)
  * [`okta.network_zone.activate_lifecycle`](#oktanetwork_zoneactivate_lifecycle)
  * [`okta.network_zone.create_new`](#oktanetwork_zonecreate_new)
  * [`okta.network_zone.deactivate_zone_lifecycle`](#oktanetwork_zonedeactivate_zone_lifecycle)
  * [`okta.network_zone.get_by_id`](#oktanetwork_zoneget_by_id)
  * [`okta.network_zone.list_zones`](#oktanetwork_zonelist_zones)
  * [`okta.network_zone.remove_zone`](#oktanetwork_zoneremove_zone)
  * [`okta.network_zone.update_zone`](#oktanetwork_zoneupdate_zone)
  * [`okta.org.extend_okta_support`](#oktaorgextend_okta_support)
  * [`okta.org.extend_okta_support_0`](#oktaorgextend_okta_support_0)
  * [`okta.org.get_contact_user`](#oktaorgget_contact_user)
  * [`okta.org.get_okta_communication_settings`](#oktaorgget_okta_communication_settings)
  * [`okta.org.get_okta_support_settings`](#oktaorgget_okta_support_settings)
  * [`okta.org.get_org_preferences`](#oktaorgget_org_preferences)
  * [`okta.org.get_settings`](#oktaorgget_settings)
  * [`okta.org.grant_okta_support_access`](#oktaorggrant_okta_support_access)
  * [`okta.org.hide_end_user_footer`](#oktaorghide_end_user_footer)
  * [`okta.org.list_contact_types`](#oktaorglist_contact_types)
  * [`okta.org.make_okta_ui_footer_visible`](#oktaorgmake_okta_ui_footer_visible)
  * [`okta.org.opt_in_okta_communication_emails`](#oktaorgopt_in_okta_communication_emails)
  * [`okta.org.opt_out_okta_communication_emails`](#oktaorgopt_out_okta_communication_emails)
  * [`okta.org.update_contact_user`](#oktaorgupdate_contact_user)
  * [`okta.org.update_organization_logo`](#oktaorgupdate_organization_logo)
  * [`okta.org.update_setting`](#oktaorgupdate_setting)
  * [`okta.org.update_settings`](#oktaorgupdate_settings)
  * [`okta.policy.activate_lifecycle`](#oktapolicyactivate_lifecycle)
  * [`okta.policy.activate_rule_lifecycle`](#oktapolicyactivate_rule_lifecycle)
  * [`okta.policy.create_new_policy`](#oktapolicycreate_new_policy)
  * [`okta.policy.create_rule`](#oktapolicycreate_rule)
  * [`okta.policy.deactivate_lifecycle`](#oktapolicydeactivate_lifecycle)
  * [`okta.policy.deactivate_rule_lifecycle`](#oktapolicydeactivate_rule_lifecycle)
  * [`okta.policy.enumerate_rules`](#oktapolicyenumerate_rules)
  * [`okta.policy.get_all_with_type`](#oktapolicyget_all_with_type)
  * [`okta.policy.get_policy`](#oktapolicyget_policy)
  * [`okta.policy.get_policy_rule`](#oktapolicyget_policy_rule)
  * [`okta.policy.remove_policy_operation`](#oktapolicyremove_policy_operation)
  * [`okta.policy.remove_rule`](#oktapolicyremove_rule)
  * [`okta.policy.update_operation`](#oktapolicyupdate_operation)
  * [`okta.policy.update_rule`](#oktapolicyupdate_rule)
  * [`okta.profile_mapping.get_by_id`](#oktaprofile_mappingget_by_id)
  * [`okta.profile_mapping.list_with_pagination`](#oktaprofile_mappinglist_with_pagination)
  * [`okta.profile_mapping.update_property_mappings`](#oktaprofile_mappingupdate_property_mappings)
  * [`okta.session.close`](#oktasessionclose)
  * [`okta.session.create_session_with_token`](#oktasessioncreate_session_with_token)
  * [`okta.session.get_details`](#oktasessionget_details)
  * [`okta.session.refresh_lifecycle`](#oktasessionrefresh_lifecycle)
  * [`okta.subscription.custom_role_notification_unsubscribe`](#oktasubscriptioncustom_role_notification_unsubscribe)
  * [`okta.subscription.get_role_subscriptions_by_notification_type`](#oktasubscriptionget_role_subscriptions_by_notification_type)
  * [`okta.subscription.list_role_subscriptions`](#oktasubscriptionlist_role_subscriptions)
  * [`okta.subscription.role_notification_subscribe`](#oktasubscriptionrole_notification_subscribe)
  * [`okta.subscription.unsubscribe_user_subscription_by_notification_type`](#oktasubscriptionunsubscribe_user_subscription_by_notification_type)
  * [`okta.subscription.user_notification_subscribe`](#oktasubscriptionuser_notification_subscribe)
  * [`okta.template.add_new_custom_sms`](#oktatemplateadd_new_custom_sms)
  * [`okta.template.enumerate_sms_templates`](#oktatemplateenumerate_sms_templates)
  * [`okta.template.get_by_id`](#oktatemplateget_by_id)
  * [`okta.template.partial_sms_update`](#oktatemplatepartial_sms_update)
  * [`okta.template.remove_sms`](#oktatemplateremove_sms)
  * [`okta.template.update_sms_template`](#oktatemplateupdate_sms_template)
  * [`okta.threat_insight.get_current_configuration`](#oktathreat_insightget_current_configuration)
  * [`okta.threat_insight.update_configuration`](#oktathreat_insightupdate_configuration)
  * [`okta.trusted_origin.activate_lifecycle_success`](#oktatrusted_originactivate_lifecycle_success)
  * [`okta.trusted_origin.create_success`](#oktatrusted_origincreate_success)
  * [`okta.trusted_origin.deactivate_lifecycle_success`](#oktatrusted_origindeactivate_lifecycle_success)
  * [`okta.trusted_origin.delete_success`](#oktatrusted_origindelete_success)
  * [`okta.trusted_origin.get_list`](#oktatrusted_originget_list)
  * [`okta.trusted_origin.get_success_by_id`](#oktatrusted_originget_success_by_id)
  * [`okta.trusted_origin.update_success`](#oktatrusted_originupdate_success)
  * [`okta.user.activate_lifecycle`](#oktauseractivate_lifecycle)
  * [`okta.user.add_app_instance_target_to_app_administrator_role_given_to_user`](#oktauseradd_app_instance_target_to_app_administrator_role_given_to_user)
  * [`okta.user.assign_role`](#oktauserassign_role)
  * [`okta.user.change_password_validation`](#oktauserchange_password_validation)
  * [`okta.user.create_new_user`](#oktausercreate_new_user)
  * [`okta.user.deactivate_lifecycle`](#oktauserdeactivate_lifecycle)
  * [`okta.user.delete_linked_objects`](#oktauserdelete_linked_objects)
  * [`okta.user.delete_permanently`](#oktauserdelete_permanently)
  * [`okta.user.delete_target_app`](#oktauserdelete_target_app)
  * [`okta.user.expire_password_and_get_temporary_password`](#oktauserexpire_password_and_get_temporary_password)
  * [`okta.user.expire_password_and_temporary_password`](#oktauserexpire_password_and_temporary_password)
  * [`okta.user.forgot_password`](#oktauserforgot_password)
  * [`okta.user.generate_password_reset_token`](#oktausergenerate_password_reset_token)
  * [`okta.user.get_assigned_role`](#oktauserget_assigned_role)
  * [`okta.user.get_client_refresh_token`](#oktauserget_client_refresh_token)
  * [`okta.user.get_grant_by_id`](#oktauserget_grant_by_id)
  * [`okta.user.get_linked_objects`](#oktauserget_linked_objects)
  * [`okta.user.get_member_groups`](#oktauserget_member_groups)
  * [`okta.user.get_okta_user`](#oktauserget_okta_user)
  * [`okta.user.get_subscription_by_notification`](#oktauserget_subscription_by_notification)
  * [`okta.user.list_active_users`](#oktauserlist_active_users)
  * [`okta.user.list_app_targets_for_role`](#oktauserlist_app_targets_for_role)
  * [`okta.user.list_assigned_app_links`](#oktauserlist_assigned_app_links)
  * [`okta.user.list_assigned_roles`](#oktauserlist_assigned_roles)
  * [`okta.user.list_clients`](#oktauserlist_clients)
  * [`okta.user.list_grants`](#oktauserlist_grants)
  * [`okta.user.list_grants_for_client`](#oktauserlist_grants_for_client)
  * [`okta.user.list_idps_for_user`](#oktauserlist_idps_for_user)
  * [`okta.user.list_refresh_tokens_for_user_and_client`](#oktauserlist_refresh_tokens_for_user_and_client)
  * [`okta.user.list_role_targets_groups`](#oktauserlist_role_targets_groups)
  * [`okta.user.list_subscriptions`](#oktauserlist_subscriptions)
  * [`okta.user.reactivate_user`](#oktauserreactivate_user)
  * [`okta.user.remove_app_instance_target_to_app_administrator_role_given_to`](#oktauserremove_app_instance_target_to_app_administrator_role_given_to)
  * [`okta.user.remove_target_group`](#oktauserremove_target_group)
  * [`okta.user.reset_factors_operation`](#oktauserreset_factors_operation)
  * [`okta.user.revoke_all_sessions`](#oktauserrevoke_all_sessions)
  * [`okta.user.revoke_all_tokens`](#oktauserrevoke_all_tokens)
  * [`okta.user.revoke_grant`](#oktauserrevoke_grant)
  * [`okta.user.revoke_grants`](#oktauserrevoke_grants)
  * [`okta.user.revoke_grants_for_user_and_client`](#oktauserrevoke_grants_for_user_and_client)
  * [`okta.user.revoke_token_for_client`](#oktauserrevoke_token_for_client)
  * [`okta.user.suspend_lifecycle`](#oktausersuspend_lifecycle)
  * [`okta.user.unassign_role`](#oktauserunassign_role)
  * [`okta.user.unlock_user_status`](#oktauserunlock_user_status)
  * [`okta.user.unsuspend_lifecycle`](#oktauserunsuspend_lifecycle)
  * [`okta.user.update_linked_object`](#oktauserupdate_linked_object)
  * [`okta.user.update_profile`](#oktauserupdate_profile)
  * [`okta.user.update_profile_0`](#oktauserupdate_profile_0)
  * [`okta.user.update_recovery_question`](#oktauserupdate_recovery_question)
  * [`okta.user.update_roles_catalog_apps`](#oktauserupdate_roles_catalog_apps)
  * [`okta.user.update_roles_catalog_apps_0`](#oktauserupdate_roles_catalog_apps_0)
  * [`okta.user.update_roles_catalog_apps_1`](#oktauserupdate_roles_catalog_apps_1)
  * [`okta.user_factor.activate_factor_lifecycle`](#oktauser_factoractivate_factor_lifecycle)
  * [`okta.user_factor.enroll_supported_factor`](#oktauser_factorenroll_supported_factor)
  * [`okta.user_factor.enumerate_enrolled`](#oktauser_factorenumerate_enrolled)
  * [`okta.user_factor.enumerate_security_questions`](#oktauser_factorenumerate_security_questions)
  * [`okta.user_factor.enumerate_supported_factors`](#oktauser_factorenumerate_supported_factors)
  * [`okta.user_factor.get_factor`](#oktauser_factorget_factor)
  * [`okta.user_factor.poll_factor_transaction_status`](#oktauser_factorpoll_factor_transaction_status)
  * [`okta.user_factor.unenroll_factor`](#oktauser_factorunenroll_factor)
  * [`okta.user_factor.verify_otp`](#oktauser_factorverify_otp)
  * [`okta.user_schema.get_schema_by_id`](#oktauser_schemaget_schema_by_id)
  * [`okta.user_schema.get_user_schema`](#oktauser_schemaget_user_schema)
  * [`okta.user_schema.partial_update_user_profile`](#oktauser_schemapartial_update_user_profile)
  * [`okta.user_schema.partial_update_user_profile_0`](#oktauser_schemapartial_update_user_profile_0)
  * [`okta.user_type.create_new_user_type`](#oktauser_typecreate_new_user_type)
  * [`okta.user_type.delete_permanently`](#oktauser_typedelete_permanently)
  * [`okta.user_type.get_all_user_types`](#oktauser_typeget_all_user_types)
  * [`okta.user_type.get_by_id`](#oktauser_typeget_by_id)
  * [`okta.user_type.replace_existing_type`](#oktauser_typereplace_existing_type)
  * [`okta.user_type.update_existing_type`](#oktauser_typeupdate_existing_type)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Okta&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from okta_python_sdk import Okta, ApiException

okta = Okta(

        api_token = 'YOUR_API_KEY',
)

try:
    # Activate a client secret
    activate_client_secret_response = okta.application.activate_client_secret(
        app_id="appId_example",
        secret_id="secretId_example",
    )
    print(activate_client_secret_response)
except ApiException as e:
    print("Exception when calling ApplicationApi.activate_client_secret: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from okta_python_sdk import Okta, ApiException

okta = Okta(

        api_token = 'YOUR_API_KEY',
)

async def main():
    try:
        # Activate a client secret
        activate_client_secret_response = await okta.application.aactivate_client_secret(
            app_id="appId_example",
            secret_id="secretId_example",
        )
        print(activate_client_secret_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi.activate_client_secret: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from okta_python_sdk import Okta, ApiException

okta = Okta(

        api_token = 'YOUR_API_KEY',
)

try:
    # Activate a client secret
    activate_client_secret_response = okta.application.raw.activate_client_secret(
        app_id="appId_example",
        secret_id="secretId_example",
    )
    pprint(activate_client_secret_response.body)
    pprint(activate_client_secret_response.body["links"])
    pprint(activate_client_secret_response.body["client_secret"])
    pprint(activate_client_secret_response.body["created"])
    pprint(activate_client_secret_response.body["id"])
    pprint(activate_client_secret_response.body["last_updated"])
    pprint(activate_client_secret_response.body["secret_hash"])
    pprint(activate_client_secret_response.body["status"])
    pprint(activate_client_secret_response.headers)
    pprint(activate_client_secret_response.status)
    pprint(activate_client_secret_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ApplicationApi.activate_client_secret: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `okta.application.activate_client_secret`<a id="oktaapplicationactivate_client_secret"></a>

Activates a specific client secret by secretId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_client_secret_response = okta.application.activate_client_secret(
    app_id="appId_example",
    secret_id="secretId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### secret_id: `str`<a id="secret_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ClientSecret`](./okta_python_sdk/pydantic/client_secret.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/secrets/{secretId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.activate_default_provisioning_connection`<a id="oktaapplicationactivate_default_provisioning_connection"></a>

Activates the default Provisioning Connection for an application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.activate_default_provisioning_connection(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/connections/default/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.activate_inactive`<a id="oktaapplicationactivate_inactive"></a>

Activates an inactive application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.activate_inactive(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.add_client_secret`<a id="oktaapplicationadd_client_secret"></a>

Adds a new secret to the client's collection of secrets.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_client_secret_response = okta.application.add_client_secret(
    body=None,
    app_id="appId_example",
    client_secret="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### client_secret: `str`<a id="client_secret-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ClientSecretMetadata`](./okta_python_sdk/type/client_secret_metadata.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ClientSecret`](./okta_python_sdk/pydantic/client_secret.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/secrets` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.assign_group_to`<a id="oktaapplicationassign_group_to"></a>

Assigns a group to an application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_group_to_response = okta.application.assign_group_to(
    app_id="appId_example",
    group_id="groupId_example",
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    priority=1,
    profile={
        "key": {},
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### embedded: [`ApplicationGroupAssignmentEmbedded`](./okta_python_sdk/type/application_group_assignment_embedded.py)<a id="embedded-applicationgroupassignmentembeddedokta_python_sdktypeapplication_group_assignment_embeddedpy"></a>

##### links: [`ApplicationGroupAssignmentLinks`](./okta_python_sdk/type/application_group_assignment_links.py)<a id="links-applicationgroupassignmentlinksokta_python_sdktypeapplication_group_assignment_linkspy"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### priority: `int`<a id="priority-int"></a>

##### profile: [`ApplicationGroupAssignmentProfile`](./okta_python_sdk/type/application_group_assignment_profile.py)<a id="profile-applicationgroupassignmentprofileokta_python_sdktypeapplication_group_assignment_profilepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicationGroupAssignment`](./okta_python_sdk/type/application_group_assignment.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationGroupAssignment`](./okta_python_sdk/pydantic/application_group_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/groups/{groupId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.assign_policy_to_application`<a id="oktaapplicationassign_policy_to_application"></a>

Assign an application to a specific policy. This unassigns the application from its currently assigned policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.assign_policy_to_application(
    app_id="appId_example",
    policy_id="policyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/policies/{policyId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.assign_user_to_application`<a id="oktaapplicationassign_user_to_application"></a>

Assigns an user to an application with [credentials](https://raw.githubusercontent.com) and an app-specific [profile](https://raw.githubusercontent.com). Profile mappings defined for the application are first applied before applying any profile properties specified in the request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_user_to_application_response = okta.application.assign_user_to_application(
    app_id="appId_example",
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    credentials={
    },
    external_id="string_example",
    id="string_example",
    last_sync="1970-01-01T00:00:00.00Z",
    last_updated="1970-01-01T00:00:00.00Z",
    password_changed="1970-01-01T00:00:00.00Z",
    profile={
        "key": {},
    },
    scope="string_example",
    status="string_example",
    status_changed="1970-01-01T00:00:00.00Z",
    sync_state="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### embedded: [`AppUserEmbedded`](./okta_python_sdk/type/app_user_embedded.py)<a id="embedded-appuserembeddedokta_python_sdktypeapp_user_embeddedpy"></a>

##### links: [`AppUserLinks`](./okta_python_sdk/type/app_user_links.py)<a id="links-appuserlinksokta_python_sdktypeapp_user_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### credentials: [`AppUserCredentials`](./okta_python_sdk/type/app_user_credentials.py)<a id="credentials-appusercredentialsokta_python_sdktypeapp_user_credentialspy"></a>


##### external_id: `str`<a id="external_id-str"></a>

##### id: `str`<a id="id-str"></a>

##### last_sync: `datetime`<a id="last_sync-datetime"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### password_changed: `datetime`<a id="password_changed-datetime"></a>

##### profile: [`AppUserProfile`](./okta_python_sdk/type/app_user_profile.py)<a id="profile-appuserprofileokta_python_sdktypeapp_user_profilepy"></a>

##### scope: `str`<a id="scope-str"></a>

##### status: `str`<a id="status-str"></a>

##### status_changed: `datetime`<a id="status_changed-datetime"></a>

##### sync_state: `str`<a id="sync_state-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppUser`](./okta_python_sdk/type/app_user.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AppUser`](./okta_python_sdk/pydantic/app_user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.clone_application_key_credential`<a id="oktaapplicationclone_application_key_credential"></a>

Clones a X.509 certificate for an application key credential from a source application to target application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
clone_application_key_credential_response = okta.application.clone_application_key_credential(
    app_id="appId_example",
    key_id="keyId_example",
    target_aid="targetAid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### key_id: `str`<a id="key_id-str"></a>

##### target_aid: `str`<a id="target_aid-str"></a>

Unique key of the target Application

#### 🔄 Return<a id="🔄-return"></a>

[`JsonWebKey`](./okta_python_sdk/pydantic/json_web_key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/keys/{keyId}/clone` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.create_new`<a id="oktaapplicationcreate_new"></a>

Adds a new application to your Okta organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = okta.application.create_new(
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    accessibility={
    },
    created="1970-01-01T00:00:00.00Z",
    credentials={
    },
    features=[
        "string_example"
    ],
    id="string_example",
    label="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    licensing={
    },
    name="string_example",
    profile={
        "key": {},
    },
    settings={
    },
    sign_on_mode="BOOKMARK",
    status="ACTIVE",
    visibility={
    },
    activate=True,
    okta_access_gateway_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### embedded: [`ApplicationEmbedded`](./okta_python_sdk/type/application_embedded.py)<a id="embedded-applicationembeddedokta_python_sdktypeapplication_embeddedpy"></a>

##### links: [`ApplicationLinks`](./okta_python_sdk/type/application_links.py)<a id="links-applicationlinksokta_python_sdktypeapplication_linkspy"></a>

##### accessibility: [`ApplicationAccessibility`](./okta_python_sdk/type/application_accessibility.py)<a id="accessibility-applicationaccessibilityokta_python_sdktypeapplication_accessibilitypy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### credentials: [`ApplicationCredentials`](./okta_python_sdk/type/application_credentials.py)<a id="credentials-applicationcredentialsokta_python_sdktypeapplication_credentialspy"></a>


##### features: [`ApplicationFeatures`](./okta_python_sdk/type/application_features.py)<a id="features-applicationfeaturesokta_python_sdktypeapplication_featurespy"></a>

##### id: `str`<a id="id-str"></a>

##### label: `str`<a id="label-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### licensing: [`ApplicationLicensing`](./okta_python_sdk/type/application_licensing.py)<a id="licensing-applicationlicensingokta_python_sdktypeapplication_licensingpy"></a>


##### name: `str`<a id="name-str"></a>

##### profile: [`ApplicationProfile`](./okta_python_sdk/type/application_profile.py)<a id="profile-applicationprofileokta_python_sdktypeapplication_profilepy"></a>

##### settings: [`ApplicationSettings`](./okta_python_sdk/type/application_settings.py)<a id="settings-applicationsettingsokta_python_sdktypeapplication_settingspy"></a>


##### sign_on_mode: [`ApplicationSignOnMode`](./okta_python_sdk/type/application_sign_on_mode.py)<a id="sign_on_mode-applicationsignonmodeokta_python_sdktypeapplication_sign_on_modepy"></a>

##### status: `str`<a id="status-str"></a>

##### visibility: [`ApplicationVisibility`](./okta_python_sdk/type/application_visibility.py)<a id="visibility-applicationvisibilityokta_python_sdktypeapplication_visibilitypy"></a>


##### activate: `bool`<a id="activate-bool"></a>

Executes activation lifecycle operation when creating the app

##### okta_access_gateway_agent: `str`<a id="okta_access_gateway_agent-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Application`](./okta_python_sdk/type/application.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Application`](./okta_python_sdk/pydantic/application.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.deactivate_client_secret_by_id`<a id="oktaapplicationdeactivate_client_secret_by_id"></a>

Deactivates a specific client secret by secretId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deactivate_client_secret_by_id_response = okta.application.deactivate_client_secret_by_id(
    app_id="appId_example",
    secret_id="secretId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### secret_id: `str`<a id="secret_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ClientSecret`](./okta_python_sdk/pydantic/client_secret.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/secrets/{secretId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.deactivate_default_provisioning_connection`<a id="oktaapplicationdeactivate_default_provisioning_connection"></a>

Deactivates the default Provisioning Connection for an application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.deactivate_default_provisioning_connection(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/connections/default/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.deactivate_lifecycle`<a id="oktaapplicationdeactivate_lifecycle"></a>

Deactivates an active application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.deactivate_lifecycle(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.delete_csr_by_id`<a id="oktaapplicationdelete_csr_by_id"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.delete_csr_by_id(
    app_id="appId_example",
    csr_id="csrId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### csr_id: `str`<a id="csr_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/csrs/{csrId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.generate_csr_for_application`<a id="oktaapplicationgenerate_csr_for_application"></a>

Generates a new key pair and returns the Certificate Signing Request for it.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_csr_for_application_response = okta.application.generate_csr_for_application(
    body=None,
    app_id="appId_example",
    subject=None,
    subject_alt_names=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### subject: [`CsrMetadataSubject`](./okta_python_sdk/type/csr_metadata_subject.py)<a id="subject-csrmetadatasubjectokta_python_sdktypecsr_metadata_subjectpy"></a>


##### subject_alt_names: [`CsrMetadataSubjectAltNames`](./okta_python_sdk/type/csr_metadata_subject_alt_names.py)<a id="subject_alt_names-csrmetadatasubjectaltnamesokta_python_sdktypecsr_metadata_subject_alt_namespy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CsrMetadata`](./okta_python_sdk/type/csr_metadata.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Csr`](./okta_python_sdk/pydantic/csr.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/csrs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.generate_x509_certificate`<a id="oktaapplicationgenerate_x509_certificate"></a>

Generates a new X.509 certificate for an application key credential

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_x509_certificate_response = okta.application.generate_x509_certificate(
    app_id="appId_example",
    validity_years=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### validity_years: `int`<a id="validity_years-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`JsonWebKey`](./okta_python_sdk/pydantic/json_web_key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/keys/generate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.get_by_id`<a id="oktaapplicationget_by_id"></a>

Fetches an application from your Okta organization by `id`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = okta.application.get_by_id(
    app_id="appId_example",
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Application`](./okta_python_sdk/pydantic/application.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.get_client_secret`<a id="oktaapplicationget_client_secret"></a>

Gets a specific client secret by secretId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_client_secret_response = okta.application.get_client_secret(
    app_id="appId_example",
    secret_id="secretId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### secret_id: `str`<a id="secret_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ClientSecret`](./okta_python_sdk/pydantic/client_secret.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/secrets/{secretId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.get_credentials_csrs`<a id="oktaapplicationget_credentials_csrs"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_credentials_csrs_response = okta.application.get_credentials_csrs(
    app_id="appId_example",
    csr_id="csrId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### csr_id: `str`<a id="csr_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Csr`](./okta_python_sdk/pydantic/csr.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/csrs/{csrId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.get_default_provisioning_connection`<a id="oktaapplicationget_default_provisioning_connection"></a>

Get default Provisioning Connection for application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_default_provisioning_connection_response = okta.application.get_default_provisioning_connection(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ProvisioningConnection`](./okta_python_sdk/pydantic/provisioning_connection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/connections/default` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.get_feature`<a id="oktaapplicationget_feature"></a>

Fetches a Feature object for an application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_feature_response = okta.application.get_feature(
    app_id="appId_example",
    name="name_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### name: `str`<a id="name-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationFeature`](./okta_python_sdk/pydantic/application_feature.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/features/{name}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.get_group_assignment`<a id="oktaapplicationget_group_assignment"></a>

Fetches an application group assignment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_group_assignment_response = okta.application.get_group_assignment(
    app_id="appId_example",
    group_id="groupId_example",
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationGroupAssignment`](./okta_python_sdk/pydantic/application_group_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/groups/{groupId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.get_key_credential`<a id="oktaapplicationget_key_credential"></a>

Gets a specific application key credential by kid

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_key_credential_response = okta.application.get_key_credential(
    app_id="appId_example",
    key_id="keyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### key_id: `str`<a id="key_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`JsonWebKey`](./okta_python_sdk/pydantic/json_web_key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/keys/{keyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.get_single_scope_consent_grant`<a id="oktaapplicationget_single_scope_consent_grant"></a>

Fetches a single scope consent grant for the application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_scope_consent_grant_response = okta.application.get_single_scope_consent_grant(
    app_id="appId_example",
    grant_id="grantId_example",
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### grant_id: `str`<a id="grant_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OAuth2ScopeConsentGrant`](./okta_python_sdk/pydantic/o_auth2_scope_consent_grant.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/grants/{grantId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.get_specific_user_assignment`<a id="oktaapplicationget_specific_user_assignment"></a>

Fetches a specific user assignment for application by `id`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_user_assignment_response = okta.application.get_specific_user_assignment(
    app_id="appId_example",
    user_id="userId_example",
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AppUser`](./okta_python_sdk/pydantic/app_user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/users/{userId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.get_token`<a id="oktaapplicationget_token"></a>

Gets a token for the specified application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_token_response = okta.application.get_token(
    app_id="appId_example",
    token_id="tokenId_example",
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### token_id: `str`<a id="token_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OAuth2Token`](./okta_python_sdk/pydantic/o_auth2_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/tokens/{tokenId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.grant_consent_to_scope`<a id="oktaapplicationgrant_consent_to_scope"></a>

Grants consent for the application to request an OAuth 2.0 Okta scope

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
grant_consent_to_scope_response = okta.application.grant_consent_to_scope(
    app_id="appId_example",
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    client_id="string_example",
    created="1970-01-01T00:00:00.00Z",
    created_by={
    },
    id="string_example",
    issuer="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    scope_id="string_example",
    source="END_USER",
    status="ACTIVE",
    user_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### embedded: [`OAuth2ScopeConsentGrantEmbedded`](./okta_python_sdk/type/o_auth2_scope_consent_grant_embedded.py)<a id="embedded-oauth2scopeconsentgrantembeddedokta_python_sdktypeo_auth2_scope_consent_grant_embeddedpy"></a>

##### links: [`OAuth2ScopeConsentGrantLinks`](./okta_python_sdk/type/o_auth2_scope_consent_grant_links.py)<a id="links-oauth2scopeconsentgrantlinksokta_python_sdktypeo_auth2_scope_consent_grant_linkspy"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### created_by: [`OAuth2Actor`](./okta_python_sdk/type/o_auth2_actor.py)<a id="created_by-oauth2actorokta_python_sdktypeo_auth2_actorpy"></a>


##### id: `str`<a id="id-str"></a>

##### issuer: `str`<a id="issuer-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### scope_id: `str`<a id="scope_id-str"></a>

##### source: [`OAuth2ScopeConsentGrantSource`](./okta_python_sdk/type/o_auth2_scope_consent_grant_source.py)<a id="source-oauth2scopeconsentgrantsourceokta_python_sdktypeo_auth2_scope_consent_grant_sourcepy"></a>

##### status: [`OAuth2ScopeConsentGrantStatus`](./okta_python_sdk/type/o_auth2_scope_consent_grant_status.py)<a id="status-oauth2scopeconsentgrantstatusokta_python_sdktypeo_auth2_scope_consent_grant_statuspy"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OAuth2ScopeConsentGrant`](./okta_python_sdk/type/o_auth2_scope_consent_grant.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OAuth2ScopeConsentGrant`](./okta_python_sdk/pydantic/o_auth2_scope_consent_grant.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/grants` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.list_apps`<a id="oktaapplicationlist_apps"></a>

Enumerates apps added to your organization with pagination. A subset of apps can be returned that match a supported filter expression or query.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_apps_response = okta.application.list_apps(
    q="string_example",
    after="string_example",
    limit=-1,
    filter="string_example",
    expand="string_example",
    include_non_deleted=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

##### after: `str`<a id="after-str"></a>

Specifies the pagination cursor for the next page of apps

##### limit: `int`<a id="limit-int"></a>

Specifies the number of results for a page

##### filter: `str`<a id="filter-str"></a>

Filters apps by status, user.id, group.id or credentials.signing.kid expression

##### expand: `str`<a id="expand-str"></a>

Traverses users link relationship and optionally embeds Application User resource

##### include_non_deleted: `bool`<a id="include_non_deleted-bool"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationListAppsResponse`](./okta_python_sdk/pydantic/application_list_apps_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.list_assigned_users`<a id="oktaapplicationlist_assigned_users"></a>

Enumerates all assigned [application users](https://raw.githubusercontent.com) for an application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_assigned_users_response = okta.application.list_assigned_users(
    app_id="appId_example",
    q="string_example",
    query_scope="string_example",
    after="string_example",
    limit=-1,
    filter="string_example",
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### q: `str`<a id="q-str"></a>

##### query_scope: `str`<a id="query_scope-str"></a>

##### after: `str`<a id="after-str"></a>

specifies the pagination cursor for the next page of assignments

##### limit: `int`<a id="limit-int"></a>

specifies the number of results for a page

##### filter: `str`<a id="filter-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationListAssignedUsersResponse`](./okta_python_sdk/pydantic/application_list_assigned_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.list_client_secrets`<a id="oktaapplicationlist_client_secrets"></a>

Enumerates the client's collection of secrets

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_client_secrets_response = okta.application.list_client_secrets(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationListClientSecretsResponse`](./okta_python_sdk/pydantic/application_list_client_secrets_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/secrets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.list_csrs_for_application`<a id="oktaapplicationlist_csrs_for_application"></a>

Enumerates Certificate Signing Requests for an application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_csrs_for_application_response = okta.application.list_csrs_for_application(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationListCsrsForApplicationResponse`](./okta_python_sdk/pydantic/application_list_csrs_for_application_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/csrs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.list_features`<a id="oktaapplicationlist_features"></a>

List Features for application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_features_response = okta.application.list_features(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationListFeaturesResponse`](./okta_python_sdk/pydantic/application_list_features_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/features` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.list_groups_assigned`<a id="oktaapplicationlist_groups_assigned"></a>

Enumerates group assignments for an application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_groups_assigned_response = okta.application.list_groups_assigned(
    app_id="appId_example",
    q="string_example",
    after="string_example",
    limit=-1,
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### q: `str`<a id="q-str"></a>

##### after: `str`<a id="after-str"></a>

Specifies the pagination cursor for the next page of assignments

##### limit: `int`<a id="limit-int"></a>

Specifies the number of results for a page

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationListGroupsAssignedResponse`](./okta_python_sdk/pydantic/application_list_groups_assigned_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.list_key_credentials`<a id="oktaapplicationlist_key_credentials"></a>

Enumerates key credentials for an application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_key_credentials_response = okta.application.list_key_credentials(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationListKeyCredentialsResponse`](./okta_python_sdk/pydantic/application_list_key_credentials_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/keys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.list_scope_consent_grants`<a id="oktaapplicationlist_scope_consent_grants"></a>

Lists all scope consent grants for the application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_scope_consent_grants_response = okta.application.list_scope_consent_grants(
    app_id="appId_example",
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationListScopeConsentGrantsResponse`](./okta_python_sdk/pydantic/application_list_scope_consent_grants_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/grants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.list_tokens`<a id="oktaapplicationlist_tokens"></a>

Lists all tokens for the application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_tokens_response = okta.application.list_tokens(
    app_id="appId_example",
    expand="string_example",
    after="string_example",
    limit=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationListTokensResponse`](./okta_python_sdk/pydantic/application_list_tokens_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/tokens` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.preview_saml_app_metadata`<a id="oktaapplicationpreview_saml_app_metadata"></a>

Previews SAML metadata based on a specific key credential for an application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
preview_saml_app_metadata_response = okta.application.preview_saml_app_metadata(
    app_id="appId_example",
    kid="kid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### kid: `str`<a id="kid-str"></a>

unique key identifier of an Application Key Credential

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationPreviewSamlAppMetadataResponse`](./okta_python_sdk/pydantic/application_preview_saml_app_metadata_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/sso/saml/metadata` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.publish_csr_lifecycle`<a id="oktaapplicationpublish_csr_lifecycle"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
publish_csr_lifecycle_response = okta.application.publish_csr_lifecycle(
    app_id="appId_example",
    csr_id="csrId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### csr_id: `str`<a id="csr_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`JsonWebKey`](./okta_python_sdk/pydantic/json_web_key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/csrs/{csrId}/lifecycle/publish` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.remove_group_assignment`<a id="oktaapplicationremove_group_assignment"></a>

Removes a group assignment from an application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.remove_group_assignment(
    app_id="appId_example",
    group_id="groupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/groups/{groupId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.remove_inactive`<a id="oktaapplicationremove_inactive"></a>

Removes an inactive application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.remove_inactive(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.remove_secret`<a id="oktaapplicationremove_secret"></a>

Removes a secret from the client's collection of secrets.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.remove_secret(
    app_id="appId_example",
    secret_id="secretId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### secret_id: `str`<a id="secret_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/credentials/secrets/{secretId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.remove_user_from`<a id="oktaapplicationremove_user_from"></a>

Removes an assignment for a user from an application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.remove_user_from(
    app_id="appId_example",
    user_id="userId_example",
    send_email=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### send_email: `bool`<a id="send_email-bool"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/users/{userId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.revoke_all_tokens`<a id="oktaapplicationrevoke_all_tokens"></a>

Revokes all tokens for the specified application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.revoke_all_tokens(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/tokens` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.revoke_permission`<a id="oktaapplicationrevoke_permission"></a>

Revokes permission for the application to request the given scope

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.revoke_permission(
    app_id="appId_example",
    grant_id="grantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### grant_id: `str`<a id="grant_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/grants/{grantId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.revoke_token`<a id="oktaapplicationrevoke_token"></a>

Revokes the specified token for the specified application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.revoke_token(
    app_id="appId_example",
    token_id="tokenId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### token_id: `str`<a id="token_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/tokens/{tokenId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.set_default_provisioning_connection`<a id="oktaapplicationset_default_provisioning_connection"></a>

Set default Provisioning Connection for application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_default_provisioning_connection_response = okta.application.set_default_provisioning_connection(
    app_id="appId_example",
    profile={
        "auth_scheme": "TOKEN",
    },
    activate=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### profile: [`ProvisioningConnectionProfile`](./okta_python_sdk/type/provisioning_connection_profile.py)<a id="profile-provisioningconnectionprofileokta_python_sdktypeprovisioning_connection_profilepy"></a>


##### activate: `bool`<a id="activate-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProvisioningConnectionRequest`](./okta_python_sdk/type/provisioning_connection_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProvisioningConnection`](./okta_python_sdk/pydantic/provisioning_connection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/connections/default` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.update_application_in_org`<a id="oktaapplicationupdate_application_in_org"></a>

Updates an application in your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_application_in_org_response = okta.application.update_application_in_org(
    app_id="appId_example",
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    accessibility={
    },
    created="1970-01-01T00:00:00.00Z",
    credentials={
    },
    features=[
        "string_example"
    ],
    id="string_example",
    label="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    licensing={
    },
    name="string_example",
    profile={
        "key": {},
    },
    settings={
    },
    sign_on_mode="BOOKMARK",
    status="ACTIVE",
    visibility={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### embedded: [`ApplicationEmbedded`](./okta_python_sdk/type/application_embedded.py)<a id="embedded-applicationembeddedokta_python_sdktypeapplication_embeddedpy"></a>

##### links: [`ApplicationLinks`](./okta_python_sdk/type/application_links.py)<a id="links-applicationlinksokta_python_sdktypeapplication_linkspy"></a>

##### accessibility: [`ApplicationAccessibility`](./okta_python_sdk/type/application_accessibility.py)<a id="accessibility-applicationaccessibilityokta_python_sdktypeapplication_accessibilitypy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### credentials: [`ApplicationCredentials`](./okta_python_sdk/type/application_credentials.py)<a id="credentials-applicationcredentialsokta_python_sdktypeapplication_credentialspy"></a>


##### features: [`ApplicationFeatures`](./okta_python_sdk/type/application_features.py)<a id="features-applicationfeaturesokta_python_sdktypeapplication_featurespy"></a>

##### id: `str`<a id="id-str"></a>

##### label: `str`<a id="label-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### licensing: [`ApplicationLicensing`](./okta_python_sdk/type/application_licensing.py)<a id="licensing-applicationlicensingokta_python_sdktypeapplication_licensingpy"></a>


##### name: `str`<a id="name-str"></a>

##### profile: [`ApplicationProfile`](./okta_python_sdk/type/application_profile.py)<a id="profile-applicationprofileokta_python_sdktypeapplication_profilepy"></a>

##### settings: [`ApplicationSettings`](./okta_python_sdk/type/application_settings.py)<a id="settings-applicationsettingsokta_python_sdktypeapplication_settingspy"></a>


##### sign_on_mode: [`ApplicationSignOnMode`](./okta_python_sdk/type/application_sign_on_mode.py)<a id="sign_on_mode-applicationsignonmodeokta_python_sdktypeapplication_sign_on_modepy"></a>

##### status: `str`<a id="status-str"></a>

##### visibility: [`ApplicationVisibility`](./okta_python_sdk/type/application_visibility.py)<a id="visibility-applicationvisibilityokta_python_sdktypeapplication_visibilitypy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Application`](./okta_python_sdk/type/application.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Application`](./okta_python_sdk/pydantic/application.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.update_feature`<a id="oktaapplicationupdate_feature"></a>

Updates a Feature object for an application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_feature_response = okta.application.update_feature(
    app_id="appId_example",
    name="name_example",
    create={
    },
    update={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### name: `str`<a id="name-str"></a>

##### create: [`CapabilitiesCreateObject`](./okta_python_sdk/type/capabilities_create_object.py)<a id="create-capabilitiescreateobjectokta_python_sdktypecapabilities_create_objectpy"></a>


##### update: [`CapabilitiesUpdateObject`](./okta_python_sdk/type/capabilities_update_object.py)<a id="update-capabilitiesupdateobjectokta_python_sdktypecapabilities_update_objectpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CapabilitiesObject`](./okta_python_sdk/type/capabilities_object.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationFeature`](./okta_python_sdk/pydantic/application_feature.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/features/{name}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.update_logo`<a id="oktaapplicationupdate_logo"></a>

Update the logo for an application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.application.update_logo(
    file=open('/path/to/file', 'rb'),
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file: `IO`<a id="file-io"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicationUpdateLogoRequest`](./okta_python_sdk/type/application_update_logo_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/logo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.application.update_profile_for_user`<a id="oktaapplicationupdate_profile_for_user"></a>

Updates a user's profile for an application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_profile_for_user_response = okta.application.update_profile_for_user(
    app_id="appId_example",
    user_id="userId_example",
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    credentials={
    },
    external_id="string_example",
    id="string_example",
    last_sync="1970-01-01T00:00:00.00Z",
    last_updated="1970-01-01T00:00:00.00Z",
    password_changed="1970-01-01T00:00:00.00Z",
    profile={
        "key": {},
    },
    scope="string_example",
    status="string_example",
    status_changed="1970-01-01T00:00:00.00Z",
    sync_state="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### embedded: [`AppUserEmbedded`](./okta_python_sdk/type/app_user_embedded.py)<a id="embedded-appuserembeddedokta_python_sdktypeapp_user_embeddedpy"></a>

##### links: [`AppUserLinks`](./okta_python_sdk/type/app_user_links.py)<a id="links-appuserlinksokta_python_sdktypeapp_user_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### credentials: [`AppUserCredentials`](./okta_python_sdk/type/app_user_credentials.py)<a id="credentials-appusercredentialsokta_python_sdktypeapp_user_credentialspy"></a>


##### external_id: `str`<a id="external_id-str"></a>

##### id: `str`<a id="id-str"></a>

##### last_sync: `datetime`<a id="last_sync-datetime"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### password_changed: `datetime`<a id="password_changed-datetime"></a>

##### profile: [`AppUserProfile`](./okta_python_sdk/type/app_user_profile.py)<a id="profile-appuserprofileokta_python_sdktypeapp_user_profilepy"></a>

##### scope: `str`<a id="scope-str"></a>

##### status: `str`<a id="status-str"></a>

##### status_changed: `datetime`<a id="status_changed-datetime"></a>

##### sync_state: `str`<a id="sync_state-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppUser`](./okta_python_sdk/type/app_user.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AppUser`](./okta_python_sdk/pydantic/app_user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/apps/{appId}/users/{userId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authenticator.activate_lifecycle_success`<a id="oktaauthenticatoractivate_lifecycle_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_lifecycle_success_response = okta.authenticator.activate_lifecycle_success(
    authenticator_id="authenticatorId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authenticator_id: `str`<a id="authenticator_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Authenticator`](./okta_python_sdk/pydantic/authenticator.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authenticators/{authenticatorId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authenticator.create_new`<a id="oktaauthenticatorcreate_new"></a>

Create Authenticator

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = okta.authenticator.create_new(
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    key="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    provider=None,
    settings={
        "allowed_for": "recovery",
        "user_verification": "REQUIRED",
    },
    status="ACTIVE",
    type="app",
    activate=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### links: [`AuthenticatorLinks`](./okta_python_sdk/type/authenticator_links.py)<a id="links-authenticatorlinksokta_python_sdktypeauthenticator_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### key: `str`<a id="key-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### provider: [`AuthenticatorProvider`](./okta_python_sdk/type/authenticator_provider.py)<a id="provider-authenticatorproviderokta_python_sdktypeauthenticator_providerpy"></a>


##### settings: [`AuthenticatorSettings`](./okta_python_sdk/type/authenticator_settings.py)<a id="settings-authenticatorsettingsokta_python_sdktypeauthenticator_settingspy"></a>


##### status: [`AuthenticatorStatus`](./okta_python_sdk/type/authenticator_status.py)<a id="status-authenticatorstatusokta_python_sdktypeauthenticator_statuspy"></a>

##### type: [`AuthenticatorType`](./okta_python_sdk/type/authenticator_type.py)<a id="type-authenticatortypeokta_python_sdktypeauthenticator_typepy"></a>

##### activate: `bool`<a id="activate-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Authenticator`](./okta_python_sdk/type/authenticator.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Authenticator`](./okta_python_sdk/pydantic/authenticator.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authenticators` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authenticator.deactivate_lifecycle_success`<a id="oktaauthenticatordeactivate_lifecycle_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deactivate_lifecycle_success_response = okta.authenticator.deactivate_lifecycle_success(
    authenticator_id="authenticatorId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authenticator_id: `str`<a id="authenticator_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Authenticator`](./okta_python_sdk/pydantic/authenticator.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authenticators/{authenticatorId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authenticator.get_success`<a id="oktaauthenticatorget_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_success_response = okta.authenticator.get_success(
    authenticator_id="authenticatorId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authenticator_id: `str`<a id="authenticator_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Authenticator`](./okta_python_sdk/pydantic/authenticator.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authenticators/{authenticatorId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authenticator.list_all_available`<a id="oktaauthenticatorlist_all_available"></a>

List Authenticators

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_available_response = okta.authenticator.list_all_available()
```

#### 🔄 Return<a id="🔄-return"></a>

[`AuthenticatorListAllAvailableResponse`](./okta_python_sdk/pydantic/authenticator_list_all_available_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authenticators` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authenticator.update_authenticator`<a id="oktaauthenticatorupdate_authenticator"></a>

Updates an authenticator

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_authenticator_response = okta.authenticator.update_authenticator(
    authenticator_id="authenticatorId_example",
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    key="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    provider=None,
    settings={
        "allowed_for": "recovery",
        "user_verification": "REQUIRED",
    },
    status="ACTIVE",
    type="app",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authenticator_id: `str`<a id="authenticator_id-str"></a>

##### links: [`AuthenticatorLinks`](./okta_python_sdk/type/authenticator_links.py)<a id="links-authenticatorlinksokta_python_sdktypeauthenticator_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### key: `str`<a id="key-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### provider: [`AuthenticatorProvider`](./okta_python_sdk/type/authenticator_provider.py)<a id="provider-authenticatorproviderokta_python_sdktypeauthenticator_providerpy"></a>


##### settings: [`AuthenticatorSettings`](./okta_python_sdk/type/authenticator_settings.py)<a id="settings-authenticatorsettingsokta_python_sdktypeauthenticator_settingspy"></a>


##### status: [`AuthenticatorStatus`](./okta_python_sdk/type/authenticator_status.py)<a id="status-authenticatorstatusokta_python_sdktypeauthenticator_statuspy"></a>

##### type: [`AuthenticatorType`](./okta_python_sdk/type/authenticator_type.py)<a id="type-authenticatortypeokta_python_sdktypeauthenticator_typepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Authenticator`](./okta_python_sdk/type/authenticator.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Authenticator`](./okta_python_sdk/pydantic/authenticator.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authenticators/{authenticatorId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.activate_lifecycle_success`<a id="oktaauthorization_serveractivate_lifecycle_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.authorization_server.activate_lifecycle_success(
    auth_server_id="authServerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.activate_policy_lifecycle`<a id="oktaauthorization_serveractivate_policy_lifecycle"></a>

Activate Authorization Server Policy

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.authorization_server.activate_policy_lifecycle(
    auth_server_id="authServerId_example",
    policy_id="policyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies/{policyId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.activate_policy_rule`<a id="oktaauthorization_serveractivate_policy_rule"></a>

Activate Authorization Server Policy Rule

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.authorization_server.activate_policy_rule(
    auth_server_id="authServerId_example",
    policy_id="policyId_example",
    rule_id="ruleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.create_claims`<a id="oktaauthorization_servercreate_claims"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_claims_response = okta.authorization_server.create_claims(
    auth_server_id="authServerId_example",
    links={
        "key": {},
    },
    always_include_in_token=True,
    claim_type="IDENTITY",
    conditions={
    },
    group_filter_type="STARTS_WITH",
    id="string_example",
    name="string_example",
    status="ACTIVE",
    system=True,
    value="string_example",
    value_type="EXPRESSION",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### links: [`OAuth2ClaimLinks`](./okta_python_sdk/type/o_auth2_claim_links.py)<a id="links-oauth2claimlinksokta_python_sdktypeo_auth2_claim_linkspy"></a>

##### always_include_in_token: `bool`<a id="always_include_in_token-bool"></a>

##### claim_type: `str`<a id="claim_type-str"></a>

##### conditions: [`OAuth2ClaimConditions`](./okta_python_sdk/type/o_auth2_claim_conditions.py)<a id="conditions-oauth2claimconditionsokta_python_sdktypeo_auth2_claim_conditionspy"></a>


##### group_filter_type: `str`<a id="group_filter_type-str"></a>

##### id: `str`<a id="id-str"></a>

##### name: `str`<a id="name-str"></a>

##### status: `str`<a id="status-str"></a>

##### system: `bool`<a id="system-bool"></a>

##### value: `str`<a id="value-str"></a>

##### value_type: `str`<a id="value_type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OAuth2Claim`](./okta_python_sdk/type/o_auth2_claim.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OAuth2Claim`](./okta_python_sdk/pydantic/o_auth2_claim.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/claims` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.create_new_server`<a id="oktaauthorization_servercreate_new_server"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_server_response = okta.authorization_server.create_new_server(
    description="string_example",
    links={
        "key": {},
    },
    audiences=[
        "string_example"
    ],
    created="1970-01-01T00:00:00.00Z",
    credentials=None,
    default=True,
    id="string_example",
    issuer="string_example",
    issuer_mode="ORG_URL",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    status="ACTIVE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

##### links: [`AuthorizationServerLinks`](./okta_python_sdk/type/authorization_server_links.py)<a id="links-authorizationserverlinksokta_python_sdktypeauthorization_server_linkspy"></a>

##### audiences: [`AuthorizationServerAudiences`](./okta_python_sdk/type/authorization_server_audiences.py)<a id="audiences-authorizationserveraudiencesokta_python_sdktypeauthorization_server_audiencespy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### credentials: [`AuthorizationServerCredentials`](./okta_python_sdk/type/authorization_server_credentials.py)<a id="credentials-authorizationservercredentialsokta_python_sdktypeauthorization_server_credentialspy"></a>


##### default: `bool`<a id="default-bool"></a>

##### id: `str`<a id="id-str"></a>

##### issuer: `str`<a id="issuer-str"></a>

##### issuer_mode: `str`<a id="issuer_mode-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### status: `str`<a id="status-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthorizationServer`](./okta_python_sdk/type/authorization_server.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServer`](./okta_python_sdk/pydantic/authorization_server.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.create_policy`<a id="oktaauthorization_servercreate_policy"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_policy_response = okta.authorization_server.create_policy(
    auth_server_id="authServerId_example",
    description="string_example",
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    conditions={
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    priority=1,
    status="ACTIVE",
    system=True,
    type="OAUTH_AUTHORIZATION_POLICY",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### description: `str`<a id="description-str"></a>

##### embedded: [`AuthorizationServerPolicyEmbedded`](./okta_python_sdk/type/authorization_server_policy_embedded.py)<a id="embedded-authorizationserverpolicyembeddedokta_python_sdktypeauthorization_server_policy_embeddedpy"></a>

##### links: [`AuthorizationServerPolicyLinks`](./okta_python_sdk/type/authorization_server_policy_links.py)<a id="links-authorizationserverpolicylinksokta_python_sdktypeauthorization_server_policy_linkspy"></a>

##### conditions: [`PolicyRuleConditions`](./okta_python_sdk/type/policy_rule_conditions.py)<a id="conditions-policyruleconditionsokta_python_sdktypepolicy_rule_conditionspy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### priority: `int`<a id="priority-int"></a>

##### status: `str`<a id="status-str"></a>

##### system: `bool`<a id="system-bool"></a>

##### type: [`PolicyType`](./okta_python_sdk/type/policy_type.py)<a id="type-policytypeokta_python_sdktypepolicy_typepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthorizationServerPolicy`](./okta_python_sdk/type/authorization_server_policy.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerPolicy`](./okta_python_sdk/pydantic/authorization_server_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.create_policy_rule`<a id="oktaauthorization_servercreate_policy_rule"></a>

Creates a policy rule for the specified Custom Authorization Server and Policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_policy_rule_response = okta.authorization_server.create_policy_rule(
    auth_server_id="authServerId_example",
    policy_id="policyId_example",
    actions={
    },
    conditions={
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    priority=1,
    status="ACTIVE",
    system=False,
    type="RESOURCE_ACCESS",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### actions: [`AuthorizationServerPolicyRuleActions`](./okta_python_sdk/type/authorization_server_policy_rule_actions.py)<a id="actions-authorizationserverpolicyruleactionsokta_python_sdktypeauthorization_server_policy_rule_actionspy"></a>


##### conditions: [`AuthorizationServerPolicyRuleConditions`](./okta_python_sdk/type/authorization_server_policy_rule_conditions.py)<a id="conditions-authorizationserverpolicyruleconditionsokta_python_sdktypeauthorization_server_policy_rule_conditionspy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### priority: `int`<a id="priority-int"></a>

##### status: `str`<a id="status-str"></a>

##### system: `bool`<a id="system-bool"></a>

##### type: `str`<a id="type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthorizationServerPolicyRule`](./okta_python_sdk/type/authorization_server_policy_rule.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerPolicyRule`](./okta_python_sdk/pydantic/authorization_server_policy_rule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.create_scope`<a id="oktaauthorization_servercreate_scope"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_scope_response = okta.authorization_server.create_scope(
    auth_server_id="authServerId_example",
    description="string_example",
    consent="REQUIRED",
    default=True,
    display_name="string_example",
    id="string_example",
    metadata_publish="ALL_CLIENTS",
    name="string_example",
    system=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### description: `str`<a id="description-str"></a>

##### consent: `str`<a id="consent-str"></a>

##### default: `bool`<a id="default-bool"></a>

##### display_name: `str`<a id="display_name-str"></a>

##### id: `str`<a id="id-str"></a>

##### metadata_publish: `str`<a id="metadata_publish-str"></a>

##### name: `str`<a id="name-str"></a>

##### system: `bool`<a id="system-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OAuth2Scope`](./okta_python_sdk/type/o_auth2_scope.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OAuth2Scope`](./okta_python_sdk/pydantic/o_auth2_scope.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/scopes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.deactivate_lifecycle`<a id="oktaauthorization_serverdeactivate_lifecycle"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.authorization_server.deactivate_lifecycle(
    auth_server_id="authServerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.deactivate_policy_lifecycle`<a id="oktaauthorization_serverdeactivate_policy_lifecycle"></a>

Deactivate Authorization Server Policy

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.authorization_server.deactivate_policy_lifecycle(
    auth_server_id="authServerId_example",
    policy_id="policyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies/{policyId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.deactivate_policy_rule`<a id="oktaauthorization_serverdeactivate_policy_rule"></a>

Deactivate Authorization Server Policy Rule

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.authorization_server.deactivate_policy_rule(
    auth_server_id="authServerId_example",
    policy_id="policyId_example",
    rule_id="ruleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.delete_auth_token`<a id="oktaauthorization_serverdelete_auth_token"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.authorization_server.delete_auth_token(
    auth_server_id="authServerId_example",
    client_id="clientId_example",
    token_id="tokenId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### token_id: `str`<a id="token_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens/{tokenId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.delete_claim`<a id="oktaauthorization_serverdelete_claim"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.authorization_server.delete_claim(
    auth_server_id="authServerId_example",
    claim_id="claimId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### claim_id: `str`<a id="claim_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/claims/{claimId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.delete_client_token`<a id="oktaauthorization_serverdelete_client_token"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.authorization_server.delete_client_token(
    auth_server_id="authServerId_example",
    client_id="clientId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### client_id: `str`<a id="client_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.delete_policy_by_id`<a id="oktaauthorization_serverdelete_policy_by_id"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.authorization_server.delete_policy_by_id(
    auth_server_id="authServerId_example",
    policy_id="policyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies/{policyId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.delete_policy_rule`<a id="oktaauthorization_serverdelete_policy_rule"></a>

Deletes a Policy Rule defined in the specified Custom Authorization Server and Policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.authorization_server.delete_policy_rule(
    auth_server_id="authServerId_example",
    policy_id="policyId_example",
    rule_id="ruleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.delete_scope`<a id="oktaauthorization_serverdelete_scope"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.authorization_server.delete_scope(
    auth_server_id="authServerId_example",
    scope_id="scopeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### scope_id: `str`<a id="scope_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/scopes/{scopeId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.delete_success`<a id="oktaauthorization_serverdelete_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.authorization_server.delete_success(
    auth_server_id="authServerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.enumerate_policy_rules`<a id="oktaauthorization_serverenumerate_policy_rules"></a>

Enumerates all policy rules for the specified Custom Authorization Server and Policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enumerate_policy_rules_response = okta.authorization_server.enumerate_policy_rules(
    auth_server_id="authServerId_example",
    policy_id="policyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerEnumeratePolicyRulesResponse`](./okta_python_sdk/pydantic/authorization_server_enumerate_policy_rules_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.get_by_id`<a id="oktaauthorization_serverget_by_id"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = okta.authorization_server.get_by_id(
    auth_server_id="authServerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServer`](./okta_python_sdk/pydantic/authorization_server.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.get_claims`<a id="oktaauthorization_serverget_claims"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_claims_response = okta.authorization_server.get_claims(
    auth_server_id="authServerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerGetClaimsResponse`](./okta_python_sdk/pydantic/authorization_server_get_claims_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/claims` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.get_claims_0`<a id="oktaauthorization_serverget_claims_0"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_claims_0_response = okta.authorization_server.get_claims_0(
    auth_server_id="authServerId_example",
    claim_id="claimId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### claim_id: `str`<a id="claim_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OAuth2Claim`](./okta_python_sdk/pydantic/o_auth2_claim.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/claims/{claimId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.get_client_auth_token`<a id="oktaauthorization_serverget_client_auth_token"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_client_auth_token_response = okta.authorization_server.get_client_auth_token(
    auth_server_id="authServerId_example",
    client_id="clientId_example",
    token_id="tokenId_example",
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### token_id: `str`<a id="token_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OAuth2RefreshToken`](./okta_python_sdk/pydantic/o_auth2_refresh_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens/{tokenId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.get_client_tokens`<a id="oktaauthorization_serverget_client_tokens"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_client_tokens_response = okta.authorization_server.get_client_tokens(
    auth_server_id="authServerId_example",
    client_id="clientId_example",
    expand="string_example",
    after="string_example",
    limit=-1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerGetClientTokensResponse`](./okta_python_sdk/pydantic/authorization_server_get_client_tokens_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.get_policies`<a id="oktaauthorization_serverget_policies"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policies_response = okta.authorization_server.get_policies(
    auth_server_id="authServerId_example",
    policy_id="policyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerPolicy`](./okta_python_sdk/pydantic/authorization_server_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies/{policyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.get_policies_success`<a id="oktaauthorization_serverget_policies_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policies_success_response = okta.authorization_server.get_policies_success(
    auth_server_id="authServerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerGetPoliciesSuccessResponse`](./okta_python_sdk/pydantic/authorization_server_get_policies_success_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.get_policy_rule_by_id`<a id="oktaauthorization_serverget_policy_rule_by_id"></a>

Returns a Policy Rule by ID that is defined in the specified Custom Authorization Server and Policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policy_rule_by_id_response = okta.authorization_server.get_policy_rule_by_id(
    auth_server_id="authServerId_example",
    policy_id="policyId_example",
    rule_id="ruleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerPolicyRule`](./okta_python_sdk/pydantic/authorization_server_policy_rule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.get_scopes`<a id="oktaauthorization_serverget_scopes"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_scopes_response = okta.authorization_server.get_scopes(
    auth_server_id="authServerId_example",
    q="string_example",
    filter="string_example",
    cursor="string_example",
    limit=-1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### q: `str`<a id="q-str"></a>

##### filter: `str`<a id="filter-str"></a>

##### cursor: `str`<a id="cursor-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerGetScopesResponse`](./okta_python_sdk/pydantic/authorization_server_get_scopes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/scopes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.get_scopes_0`<a id="oktaauthorization_serverget_scopes_0"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_scopes_0_response = okta.authorization_server.get_scopes_0(
    auth_server_id="authServerId_example",
    scope_id="scopeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### scope_id: `str`<a id="scope_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OAuth2Scope`](./okta_python_sdk/pydantic/o_auth2_scope.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/scopes/{scopeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.list_clients`<a id="oktaauthorization_serverlist_clients"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_clients_response = okta.authorization_server.list_clients(
    auth_server_id="authServerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerListClientsResponse`](./okta_python_sdk/pydantic/authorization_server_list_clients_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/clients` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.list_credentials_keys`<a id="oktaauthorization_serverlist_credentials_keys"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_credentials_keys_response = okta.authorization_server.list_credentials_keys(
    auth_server_id="authServerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerListCredentialsKeysResponse`](./okta_python_sdk/pydantic/authorization_server_list_credentials_keys_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/credentials/keys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.list_servers`<a id="oktaauthorization_serverlist_servers"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_servers_response = okta.authorization_server.list_servers(
    q="string_example",
    limit="string_example",
    after="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

##### limit: `str`<a id="limit-str"></a>

##### after: `str`<a id="after-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerListServersResponse`](./okta_python_sdk/pydantic/authorization_server_list_servers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.rotate_key_lifecycle`<a id="oktaauthorization_serverrotate_key_lifecycle"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rotate_key_lifecycle_response = okta.authorization_server.rotate_key_lifecycle(
    body=None,
    auth_server_id="authServerId_example",
    use="sig",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### use: `str`<a id="use-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JwkUse`](./okta_python_sdk/type/jwk_use.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerRotateKeyLifecycleResponse`](./okta_python_sdk/pydantic/authorization_server_rotate_key_lifecycle_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/credentials/lifecycle/keyRotate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.update_by_id`<a id="oktaauthorization_serverupdate_by_id"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = okta.authorization_server.update_by_id(
    auth_server_id="authServerId_example",
    description="string_example",
    links={
        "key": {},
    },
    audiences=[
        "string_example"
    ],
    created="1970-01-01T00:00:00.00Z",
    credentials=None,
    default=True,
    id="string_example",
    issuer="string_example",
    issuer_mode="ORG_URL",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    status="ACTIVE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### description: `str`<a id="description-str"></a>

##### links: [`AuthorizationServerLinks`](./okta_python_sdk/type/authorization_server_links.py)<a id="links-authorizationserverlinksokta_python_sdktypeauthorization_server_linkspy"></a>

##### audiences: [`AuthorizationServerAudiences`](./okta_python_sdk/type/authorization_server_audiences.py)<a id="audiences-authorizationserveraudiencesokta_python_sdktypeauthorization_server_audiencespy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### credentials: [`AuthorizationServerCredentials`](./okta_python_sdk/type/authorization_server_credentials.py)<a id="credentials-authorizationservercredentialsokta_python_sdktypeauthorization_server_credentialspy"></a>


##### default: `bool`<a id="default-bool"></a>

##### id: `str`<a id="id-str"></a>

##### issuer: `str`<a id="issuer-str"></a>

##### issuer_mode: `str`<a id="issuer_mode-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### status: `str`<a id="status-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthorizationServer`](./okta_python_sdk/type/authorization_server.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServer`](./okta_python_sdk/pydantic/authorization_server.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.update_claim_success`<a id="oktaauthorization_serverupdate_claim_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_claim_success_response = okta.authorization_server.update_claim_success(
    auth_server_id="authServerId_example",
    claim_id="claimId_example",
    links={
        "key": {},
    },
    always_include_in_token=True,
    claim_type="IDENTITY",
    conditions={
    },
    group_filter_type="STARTS_WITH",
    id="string_example",
    name="string_example",
    status="ACTIVE",
    system=True,
    value="string_example",
    value_type="EXPRESSION",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### claim_id: `str`<a id="claim_id-str"></a>

##### links: [`OAuth2ClaimLinks`](./okta_python_sdk/type/o_auth2_claim_links.py)<a id="links-oauth2claimlinksokta_python_sdktypeo_auth2_claim_linkspy"></a>

##### always_include_in_token: `bool`<a id="always_include_in_token-bool"></a>

##### claim_type: `str`<a id="claim_type-str"></a>

##### conditions: [`OAuth2ClaimConditions`](./okta_python_sdk/type/o_auth2_claim_conditions.py)<a id="conditions-oauth2claimconditionsokta_python_sdktypeo_auth2_claim_conditionspy"></a>


##### group_filter_type: `str`<a id="group_filter_type-str"></a>

##### id: `str`<a id="id-str"></a>

##### name: `str`<a id="name-str"></a>

##### status: `str`<a id="status-str"></a>

##### system: `bool`<a id="system-bool"></a>

##### value: `str`<a id="value-str"></a>

##### value_type: `str`<a id="value_type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OAuth2Claim`](./okta_python_sdk/type/o_auth2_claim.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OAuth2Claim`](./okta_python_sdk/pydantic/o_auth2_claim.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/claims/{claimId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.update_policy_rule_configuration`<a id="oktaauthorization_serverupdate_policy_rule_configuration"></a>

Updates the configuration of the Policy Rule defined in the specified Custom Authorization Server and Policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_policy_rule_configuration_response = okta.authorization_server.update_policy_rule_configuration(
    auth_server_id="authServerId_example",
    policy_id="policyId_example",
    rule_id="ruleId_example",
    actions={
    },
    conditions={
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    priority=1,
    status="ACTIVE",
    system=False,
    type="RESOURCE_ACCESS",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

##### actions: [`AuthorizationServerPolicyRuleActions`](./okta_python_sdk/type/authorization_server_policy_rule_actions.py)<a id="actions-authorizationserverpolicyruleactionsokta_python_sdktypeauthorization_server_policy_rule_actionspy"></a>


##### conditions: [`AuthorizationServerPolicyRuleConditions`](./okta_python_sdk/type/authorization_server_policy_rule_conditions.py)<a id="conditions-authorizationserverpolicyruleconditionsokta_python_sdktypeauthorization_server_policy_rule_conditionspy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### priority: `int`<a id="priority-int"></a>

##### status: `str`<a id="status-str"></a>

##### system: `bool`<a id="system-bool"></a>

##### type: `str`<a id="type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthorizationServerPolicyRule`](./okta_python_sdk/type/authorization_server_policy_rule.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerPolicyRule`](./okta_python_sdk/pydantic/authorization_server_policy_rule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.update_policy_success`<a id="oktaauthorization_serverupdate_policy_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_policy_success_response = okta.authorization_server.update_policy_success(
    auth_server_id="authServerId_example",
    policy_id="policyId_example",
    description="string_example",
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    conditions={
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    priority=1,
    status="ACTIVE",
    system=True,
    type="OAUTH_AUTHORIZATION_POLICY",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### description: `str`<a id="description-str"></a>

##### embedded: [`AuthorizationServerPolicyEmbedded`](./okta_python_sdk/type/authorization_server_policy_embedded.py)<a id="embedded-authorizationserverpolicyembeddedokta_python_sdktypeauthorization_server_policy_embeddedpy"></a>

##### links: [`AuthorizationServerPolicyLinks`](./okta_python_sdk/type/authorization_server_policy_links.py)<a id="links-authorizationserverpolicylinksokta_python_sdktypeauthorization_server_policy_linkspy"></a>

##### conditions: [`PolicyRuleConditions`](./okta_python_sdk/type/policy_rule_conditions.py)<a id="conditions-policyruleconditionsokta_python_sdktypepolicy_rule_conditionspy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### priority: `int`<a id="priority-int"></a>

##### status: `str`<a id="status-str"></a>

##### system: `bool`<a id="system-bool"></a>

##### type: [`PolicyType`](./okta_python_sdk/type/policy_type.py)<a id="type-policytypeokta_python_sdktypepolicy_typepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthorizationServerPolicy`](./okta_python_sdk/type/authorization_server_policy.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizationServerPolicy`](./okta_python_sdk/pydantic/authorization_server_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/policies/{policyId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.authorization_server.update_scope_success`<a id="oktaauthorization_serverupdate_scope_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_scope_success_response = okta.authorization_server.update_scope_success(
    auth_server_id="authServerId_example",
    scope_id="scopeId_example",
    description="string_example",
    consent="REQUIRED",
    default=True,
    display_name="string_example",
    id="string_example",
    metadata_publish="ALL_CLIENTS",
    name="string_example",
    system=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_server_id: `str`<a id="auth_server_id-str"></a>

##### scope_id: `str`<a id="scope_id-str"></a>

##### description: `str`<a id="description-str"></a>

##### consent: `str`<a id="consent-str"></a>

##### default: `bool`<a id="default-bool"></a>

##### display_name: `str`<a id="display_name-str"></a>

##### id: `str`<a id="id-str"></a>

##### metadata_publish: `str`<a id="metadata_publish-str"></a>

##### name: `str`<a id="name-str"></a>

##### system: `bool`<a id="system-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OAuth2Scope`](./okta_python_sdk/type/o_auth2_scope.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OAuth2Scope`](./okta_python_sdk/pydantic/o_auth2_scope.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authorizationServers/{authServerId}/scopes/{scopeId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.create_email_template_customization`<a id="oktabrandcreate_email_template_customization"></a>

Create an email customization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_template_customization_response = okta.brand.create_email_template_customization(
    body=None,
    brand_id="brandId_example",
    template_name="templateName_example",
    body="string_example",
    is_default=True,
    language="string_example",
    subject="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### template_name: `str`<a id="template_name-str"></a>

##### body: `str`<a id="body-str"></a>

##### is_default: `bool`<a id="is_default-bool"></a>

##### language: `str`<a id="language-str"></a>

unique under each email template

##### subject: `str`<a id="subject-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmailTemplateCustomizationRequest`](./okta_python_sdk/type/email_template_customization_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmailTemplateCustomization`](./okta_python_sdk/pydantic/email_template_customization.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/templates/email/{templateName}/customizations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.delete_email_customization`<a id="oktabranddelete_email_customization"></a>

Delete an email customization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.brand.delete_email_customization(
    brand_id="brandId_example",
    template_name="templateName_example",
    customization_id="customizationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### template_name: `str`<a id="template_name-str"></a>

##### customization_id: `str`<a id="customization_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.delete_email_template_customizations`<a id="oktabranddelete_email_template_customizations"></a>

Delete all customizations for an email template. Also known as “Reset to Default”.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.brand.delete_email_template_customizations(
    brand_id="brandId_example",
    template_name="templateName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### template_name: `str`<a id="template_name-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/templates/email/{templateName}/customizations` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.delete_theme_background_image`<a id="oktabranddelete_theme_background_image"></a>

Deletes a Theme background image

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.brand.delete_theme_background_image(
    brand_id="brandId_example",
    theme_id="themeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### theme_id: `str`<a id="theme_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/themes/{themeId}/background-image` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.delete_theme_favicon`<a id="oktabranddelete_theme_favicon"></a>

Deletes a Theme favicon. The org then uses the Okta default favicon.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.brand.delete_theme_favicon(
    brand_id="brandId_example",
    theme_id="themeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### theme_id: `str`<a id="theme_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/themes/{themeId}/favicon` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.delete_theme_logo`<a id="oktabranddelete_theme_logo"></a>

Deletes a Theme logo. The org then uses the Okta default logo.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.brand.delete_theme_logo(
    brand_id="brandId_example",
    theme_id="themeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### theme_id: `str`<a id="theme_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/themes/{themeId}/logo` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.get_all_brands`<a id="oktabrandget_all_brands"></a>

List all the brands in your org.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_brands_response = okta.brand.get_all_brands()
```

#### 🔄 Return<a id="🔄-return"></a>

[`BrandGetAllBrandsResponse`](./okta_python_sdk/pydantic/brand_get_all_brands_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.get_by_id`<a id="oktabrandget_by_id"></a>

Fetches a brand by `brandId`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = okta.brand.get_by_id(
    brand_id="brandId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Brand`](./okta_python_sdk/pydantic/brand.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.get_email_customization_preview`<a id="oktabrandget_email_customization_preview"></a>

Get a preview of an email template customization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_email_customization_preview_response = okta.brand.get_email_customization_preview(
    brand_id="brandId_example",
    template_name="templateName_example",
    customization_id="customizationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### template_name: `str`<a id="template_name-str"></a>

##### customization_id: `str`<a id="customization_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmailTemplateContent`](./okta_python_sdk/pydantic/email_template_content.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId}/preview` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.get_email_template`<a id="oktabrandget_email_template"></a>

Fetch an email template by templateName

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_email_template_response = okta.brand.get_email_template(
    brand_id="brandId_example",
    template_name="templateName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### template_name: `str`<a id="template_name-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmailTemplate`](./okta_python_sdk/pydantic/email_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/templates/email/{templateName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.get_email_template_customization_by_id`<a id="oktabrandget_email_template_customization_by_id"></a>

Fetch an email customization by id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_email_template_customization_by_id_response = okta.brand.get_email_template_customization_by_id(
    brand_id="brandId_example",
    template_name="templateName_example",
    customization_id="customizationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### template_name: `str`<a id="template_name-str"></a>

##### customization_id: `str`<a id="customization_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmailTemplateCustomization`](./okta_python_sdk/pydantic/email_template_customization.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.get_email_template_default_content`<a id="oktabrandget_email_template_default_content"></a>

Fetch the default content for an email template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_email_template_default_content_response = okta.brand.get_email_template_default_content(
    brand_id="brandId_example",
    template_name="templateName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### template_name: `str`<a id="template_name-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmailTemplateContent`](./okta_python_sdk/pydantic/email_template_content.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/templates/email/{templateName}/default-content` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.get_email_template_default_content_preview`<a id="oktabrandget_email_template_default_content_preview"></a>

Fetch a preview of an email template's default content by populating velocity references with the current user's environment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_email_template_default_content_preview_response = okta.brand.get_email_template_default_content_preview(
    brand_id="brandId_example",
    template_name="templateName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### template_name: `str`<a id="template_name-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmailTemplateContent`](./okta_python_sdk/pydantic/email_template_content.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/templates/email/{templateName}/default-content/preview` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.get_email_template_default_content_preview_0`<a id="oktabrandget_email_template_default_content_preview_0"></a>

Send a test email to the current users primary and secondary email addresses. The email content is selected based on the following priority: An email customization specifically for the users locale. The default language of email customizations. The email templates default content.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.brand.get_email_template_default_content_preview_0(
    body=None,
    brand_id="brandId_example",
    template_name="templateName_example",
    customization_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### template_name: `str`<a id="template_name-str"></a>

##### customization_id: `str`<a id="customization_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmailTemplateTestRequest`](./okta_python_sdk/type/email_template_test_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/templates/email/{templateName}/test` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.get_theme_by_id`<a id="oktabrandget_theme_by_id"></a>

Fetches a theme for a brand

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_theme_by_id_response = okta.brand.get_theme_by_id(
    brand_id="brandId_example",
    theme_id="themeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### theme_id: `str`<a id="theme_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ThemeResponse`](./okta_python_sdk/pydantic/theme_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/themes/{themeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.get_themes`<a id="oktabrandget_themes"></a>

List all the themes in your brand

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_themes_response = okta.brand.get_themes(
    brand_id="brandId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BrandGetThemesResponse`](./okta_python_sdk/pydantic/brand_get_themes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/themes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.list_email_template_customizations`<a id="oktabrandlist_email_template_customizations"></a>

List all email customizations for an email template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_email_template_customizations_response = okta.brand.list_email_template_customizations(
    brand_id="brandId_example",
    template_name="templateName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### template_name: `str`<a id="template_name-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BrandListEmailTemplateCustomizationsResponse`](./okta_python_sdk/pydantic/brand_list_email_template_customizations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/templates/email/{templateName}/customizations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.list_email_templates`<a id="oktabrandlist_email_templates"></a>

List email templates in your organization with pagination.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_email_templates_response = okta.brand.list_email_templates(
    brand_id="brandId_example",
    after="string_example",
    limit=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### after: `str`<a id="after-str"></a>

Specifies the pagination cursor for the next page of email templates.

##### limit: `int`<a id="limit-int"></a>

Specifies the number of results returned (maximum 200)

#### 🔄 Return<a id="🔄-return"></a>

[`BrandListEmailTemplatesResponse`](./okta_python_sdk/pydantic/brand_list_email_templates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/templates/email` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.update_by_brand_id`<a id="oktabrandupdate_by_brand_id"></a>

Updates a brand by `brandId`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_brand_id_response = okta.brand.update_by_brand_id(
    body=None,
    brand_id="brandId_example",
    links={
        "key": {},
    },
    agree_to_custom_privacy_policy=True,
    custom_privacy_policy_url="string_example",
    id="string_example",
    remove_powered_by_okta=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### links: `Dict[str, Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`<a id="links-dictstr-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### agree_to_custom_privacy_policy: `bool`<a id="agree_to_custom_privacy_policy-bool"></a>

##### custom_privacy_policy_url: `str`<a id="custom_privacy_policy_url-str"></a>

##### id: `str`<a id="id-str"></a>

##### remove_powered_by_okta: `bool`<a id="remove_powered_by_okta-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Brand`](./okta_python_sdk/type/brand.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Brand`](./okta_python_sdk/pydantic/brand.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.update_email_customization`<a id="oktabrandupdate_email_customization"></a>

Update an email customization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_email_customization_response = okta.brand.update_email_customization(
    body=None,
    brand_id="brandId_example",
    template_name="templateName_example",
    customization_id="customizationId_example",
    body="string_example",
    is_default=True,
    language="string_example",
    subject="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### template_name: `str`<a id="template_name-str"></a>

##### customization_id: `str`<a id="customization_id-str"></a>

##### body: `str`<a id="body-str"></a>

##### is_default: `bool`<a id="is_default-bool"></a>

##### language: `str`<a id="language-str"></a>

unique under each email template

##### subject: `str`<a id="subject-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmailTemplateCustomizationRequest`](./okta_python_sdk/type/email_template_customization_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmailTemplateCustomization`](./okta_python_sdk/pydantic/email_template_customization.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.update_theme`<a id="oktabrandupdate_theme"></a>

Updates a theme for a brand

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_theme_response = okta.brand.update_theme(
    body=None,
    brand_id="brandId_example",
    theme_id="themeId_example",
    links={
        "key": {},
    },
    background_image="string_example",
    email_template_touch_point_variant="OKTA_DEFAULT",
    end_user_dashboard_touch_point_variant="OKTA_DEFAULT",
    error_page_touch_point_variant="OKTA_DEFAULT",
    primary_color_contrast_hex="string_example",
    primary_color_hex="string_example",
    secondary_color_contrast_hex="string_example",
    secondary_color_hex="string_example",
    sign_in_page_touch_point_variant="OKTA_DEFAULT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### theme_id: `str`<a id="theme_id-str"></a>

##### links: `Dict[str, Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`<a id="links-dictstr-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### background_image: `str`<a id="background_image-str"></a>

##### email_template_touch_point_variant: [`EmailTemplateTouchPointVariant`](./okta_python_sdk/type/email_template_touch_point_variant.py)<a id="email_template_touch_point_variant-emailtemplatetouchpointvariantokta_python_sdktypeemail_template_touch_point_variantpy"></a>

##### end_user_dashboard_touch_point_variant: [`EndUserDashboardTouchPointVariant`](./okta_python_sdk/type/end_user_dashboard_touch_point_variant.py)<a id="end_user_dashboard_touch_point_variant-enduserdashboardtouchpointvariantokta_python_sdktypeend_user_dashboard_touch_point_variantpy"></a>

##### error_page_touch_point_variant: [`ErrorPageTouchPointVariant`](./okta_python_sdk/type/error_page_touch_point_variant.py)<a id="error_page_touch_point_variant-errorpagetouchpointvariantokta_python_sdktypeerror_page_touch_point_variantpy"></a>

##### primary_color_contrast_hex: `str`<a id="primary_color_contrast_hex-str"></a>

##### primary_color_hex: `str`<a id="primary_color_hex-str"></a>

##### secondary_color_contrast_hex: `str`<a id="secondary_color_contrast_hex-str"></a>

##### secondary_color_hex: `str`<a id="secondary_color_hex-str"></a>

##### sign_in_page_touch_point_variant: [`SignInPageTouchPointVariant`](./okta_python_sdk/type/sign_in_page_touch_point_variant.py)<a id="sign_in_page_touch_point_variant-signinpagetouchpointvariantokta_python_sdktypesign_in_page_touch_point_variantpy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Theme`](./okta_python_sdk/type/theme.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ThemeResponse`](./okta_python_sdk/pydantic/theme_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/themes/{themeId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.update_theme_background_image`<a id="oktabrandupdate_theme_background_image"></a>

Updates the background image for your Theme

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_theme_background_image_response = okta.brand.update_theme_background_image(
    file=open('/path/to/file', 'rb'),
    brand_id="brandId_example",
    theme_id="themeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file: `IO`<a id="file-io"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### theme_id: `str`<a id="theme_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicationUpdateLogoRequest`](./okta_python_sdk/type/application_update_logo_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ImageUploadResponse`](./okta_python_sdk/pydantic/image_upload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/themes/{themeId}/background-image` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.update_theme_favicon`<a id="oktabrandupdate_theme_favicon"></a>

Updates the favicon for your theme

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_theme_favicon_response = okta.brand.update_theme_favicon(
    file=open('/path/to/file', 'rb'),
    brand_id="brandId_example",
    theme_id="themeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file: `IO`<a id="file-io"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### theme_id: `str`<a id="theme_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicationUpdateLogoRequest`](./okta_python_sdk/type/application_update_logo_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ImageUploadResponse`](./okta_python_sdk/pydantic/image_upload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/themes/{themeId}/favicon` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.brand.update_theme_logo`<a id="oktabrandupdate_theme_logo"></a>

Updates the logo for your Theme

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_theme_logo_response = okta.brand.update_theme_logo(
    file=open('/path/to/file', 'rb'),
    brand_id="brandId_example",
    theme_id="themeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file: `IO`<a id="file-io"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

##### theme_id: `str`<a id="theme_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicationUpdateLogoRequest`](./okta_python_sdk/type/application_update_logo_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ImageUploadResponse`](./okta_python_sdk/pydantic/image_upload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/brands/{brandId}/themes/{themeId}/logo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.domain.create_certificate`<a id="oktadomaincreate_certificate"></a>

Creates the Certificate for the Domain.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.domain.create_certificate(
    body=None,
    domain_id="domainId_example",
    certificate="string_example",
    certificate_chain="string_example",
    private_key="string_example",
    type="PEM",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain_id: `str`<a id="domain_id-str"></a>

##### certificate: `str`<a id="certificate-str"></a>

##### certificate_chain: `str`<a id="certificate_chain-str"></a>

##### private_key: `str`<a id="private_key-str"></a>

##### type: [`DomainCertificateType`](./okta_python_sdk/type/domain_certificate_type.py)<a id="type-domaincertificatetypeokta_python_sdktypedomain_certificate_typepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainCertificate`](./okta_python_sdk/type/domain_certificate.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/domains/{domainId}/certificate` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.domain.create_new_domain`<a id="oktadomaincreate_new_domain"></a>

Creates your domain.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_domain_response = okta.domain.create_new_domain(
    certificate_source_type="MANUAL",
    dns_records=[
        None
    ],
    domain="string_example",
    id="string_example",
    public_certificate=None,
    validation_status="NOT_STARTED",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### certificate_source_type: [`DomainCertificateSourceType`](./okta_python_sdk/type/domain_certificate_source_type.py)<a id="certificate_source_type-domaincertificatesourcetypeokta_python_sdktypedomain_certificate_source_typepy"></a>

##### dns_records: List[`DNSRecord`]<a id="dns_records-listdnsrecord"></a>

##### domain: `str`<a id="domain-str"></a>

##### id: `str`<a id="id-str"></a>

##### public_certificate: [`DomainCertificateMetadata`](./okta_python_sdk/type/domain_certificate_metadata.py)<a id="public_certificate-domaincertificatemetadataokta_python_sdktypedomain_certificate_metadatapy"></a>


##### validation_status: [`DomainValidationStatus`](./okta_python_sdk/type/domain_validation_status.py)<a id="validation_status-domainvalidationstatusokta_python_sdktypedomain_validation_statuspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Domain`](./okta_python_sdk/type/domain.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Domain`](./okta_python_sdk/pydantic/domain.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/domains` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.domain.get_by_id`<a id="oktadomainget_by_id"></a>

Fetches a Domain by `id`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = okta.domain.get_by_id(
    domain_id="domainId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain_id: `str`<a id="domain_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Domain`](./okta_python_sdk/pydantic/domain.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/domains/{domainId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.domain.list_verified_custom`<a id="oktadomainlist_verified_custom"></a>

List all verified custom Domains for the org.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_verified_custom_response = okta.domain.list_verified_custom()
```

#### 🔄 Return<a id="🔄-return"></a>

[`DomainListResponse`](./okta_python_sdk/pydantic/domain_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/domains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.domain.remove_by_id`<a id="oktadomainremove_by_id"></a>

Deletes a Domain by `id`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.domain.remove_by_id(
    domain_id="domainId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain_id: `str`<a id="domain_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/domains/{domainId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.domain.verify_by_id`<a id="oktadomainverify_by_id"></a>

Verifies the Domain by `id`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_by_id_response = okta.domain.verify_by_id(
    domain_id="domainId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain_id: `str`<a id="domain_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Domain`](./okta_python_sdk/pydantic/domain.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/domains/{domainId}/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.event_hook.activate_lifecycle_success`<a id="oktaevent_hookactivate_lifecycle_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_lifecycle_success_response = okta.event_hook.activate_lifecycle_success(
    event_hook_id="eventHookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_hook_id: `str`<a id="event_hook_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EventHook`](./okta_python_sdk/pydantic/event_hook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/eventHooks/{eventHookId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.event_hook.create_success`<a id="oktaevent_hookcreate_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_success_response = okta.event_hook.create_success(
    links={
        "key": {},
    },
    channel={
        "type": "HTTP",
    },
    created="1970-01-01T00:00:00.00Z",
    created_by="string_example",
    events={},
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    status="ACTIVE",
    verification_status="UNVERIFIED",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### links: [`EventHookLinks`](./okta_python_sdk/type/event_hook_links.py)<a id="links-eventhooklinksokta_python_sdktypeevent_hook_linkspy"></a>

##### channel: [`EventHookChannel`](./okta_python_sdk/type/event_hook_channel.py)<a id="channel-eventhookchannelokta_python_sdktypeevent_hook_channelpy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### created_by: `str`<a id="created_by-str"></a>

##### events: [`EventSubscriptions`](./okta_python_sdk/type/event_subscriptions.py)<a id="events-eventsubscriptionsokta_python_sdktypeevent_subscriptionspy"></a>


##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### status: `str`<a id="status-str"></a>

##### verification_status: `str`<a id="verification_status-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EventHook`](./okta_python_sdk/type/event_hook.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EventHook`](./okta_python_sdk/pydantic/event_hook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/eventHooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.event_hook.deactivate_lifecycle_event`<a id="oktaevent_hookdeactivate_lifecycle_event"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deactivate_lifecycle_event_response = okta.event_hook.deactivate_lifecycle_event(
    event_hook_id="eventHookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_hook_id: `str`<a id="event_hook_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EventHook`](./okta_python_sdk/pydantic/event_hook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/eventHooks/{eventHookId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.event_hook.get_success_event`<a id="oktaevent_hookget_success_event"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_success_event_response = okta.event_hook.get_success_event(
    event_hook_id="eventHookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_hook_id: `str`<a id="event_hook_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EventHook`](./okta_python_sdk/pydantic/event_hook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/eventHooks/{eventHookId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.event_hook.list_success_events`<a id="oktaevent_hooklist_success_events"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_success_events_response = okta.event_hook.list_success_events()
```

#### 🔄 Return<a id="🔄-return"></a>

[`EventHookListSuccessEventsResponse`](./okta_python_sdk/pydantic/event_hook_list_success_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/eventHooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.event_hook.remove_success_event`<a id="oktaevent_hookremove_success_event"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.event_hook.remove_success_event(
    event_hook_id="eventHookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_hook_id: `str`<a id="event_hook_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/eventHooks/{eventHookId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.event_hook.update_success_event`<a id="oktaevent_hookupdate_success_event"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_success_event_response = okta.event_hook.update_success_event(
    event_hook_id="eventHookId_example",
    links={
        "key": {},
    },
    channel={
        "type": "HTTP",
    },
    created="1970-01-01T00:00:00.00Z",
    created_by="string_example",
    events={},
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    status="ACTIVE",
    verification_status="UNVERIFIED",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_hook_id: `str`<a id="event_hook_id-str"></a>

##### links: [`EventHookLinks`](./okta_python_sdk/type/event_hook_links.py)<a id="links-eventhooklinksokta_python_sdktypeevent_hook_linkspy"></a>

##### channel: [`EventHookChannel`](./okta_python_sdk/type/event_hook_channel.py)<a id="channel-eventhookchannelokta_python_sdktypeevent_hook_channelpy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### created_by: `str`<a id="created_by-str"></a>

##### events: [`EventSubscriptions`](./okta_python_sdk/type/event_subscriptions.py)<a id="events-eventsubscriptionsokta_python_sdktypeevent_subscriptionspy"></a>


##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### status: `str`<a id="status-str"></a>

##### verification_status: `str`<a id="verification_status-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EventHook`](./okta_python_sdk/type/event_hook.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EventHook`](./okta_python_sdk/pydantic/event_hook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/eventHooks/{eventHookId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.event_hook.verify_lifecycle_success`<a id="oktaevent_hookverify_lifecycle_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_lifecycle_success_response = okta.event_hook.verify_lifecycle_success(
    event_hook_id="eventHookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_hook_id: `str`<a id="event_hook_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EventHook`](./okta_python_sdk/pydantic/event_hook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/eventHooks/{eventHookId}/lifecycle/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.feature.create_lifecycle_success`<a id="oktafeaturecreate_lifecycle_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_lifecycle_success_response = okta.feature.create_lifecycle_success(
    feature_id="featureId_example",
    lifecycle="lifecycle_example",
    mode="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### feature_id: `str`<a id="feature_id-str"></a>

##### lifecycle: `str`<a id="lifecycle-str"></a>

##### mode: `str`<a id="mode-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Feature`](./okta_python_sdk/pydantic/feature.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/features/{featureId}/{lifecycle}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.feature.get_success`<a id="oktafeatureget_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_success_response = okta.feature.get_success()
```

#### 🔄 Return<a id="🔄-return"></a>

[`FeatureGetSuccessResponse`](./okta_python_sdk/pydantic/feature_get_success_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/features` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.feature.get_success_by_id`<a id="oktafeatureget_success_by_id"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_success_by_id_response = okta.feature.get_success_by_id(
    feature_id="featureId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### feature_id: `str`<a id="feature_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Feature`](./okta_python_sdk/pydantic/feature.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/features/{featureId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.feature.list_dependencies`<a id="oktafeaturelist_dependencies"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_dependencies_response = okta.feature.list_dependencies(
    feature_id="featureId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### feature_id: `str`<a id="feature_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`FeatureListDependenciesResponse`](./okta_python_sdk/pydantic/feature_list_dependencies_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/features/{featureId}/dependencies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.feature.list_dependents`<a id="oktafeaturelist_dependents"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_dependents_response = okta.feature.list_dependents(
    feature_id="featureId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### feature_id: `str`<a id="feature_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`FeatureListDependentsResponse`](./okta_python_sdk/pydantic/feature_list_dependents_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/features/{featureId}/dependents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.activate_rule_lifecycle`<a id="oktagroupactivate_rule_lifecycle"></a>

Activates a specific group rule by id from your organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.group.activate_rule_lifecycle(
    rule_id="ruleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/rules/{ruleId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.add_app_instance_target_to_app_admin_role_given_to_group`<a id="oktagroupadd_app_instance_target_to_app_admin_role_given_to_group"></a>

Add App Instance Target to App Administrator Role given to a Group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.group.add_app_instance_target_to_app_admin_role_given_to_group(
    group_id="groupId_example",
    role_id="roleId_example",
    app_name="appName_example",
    application_id="applicationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### app_name: `str`<a id="app_name-str"></a>

##### application_id: `str`<a id="application_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.add_rule`<a id="oktagroupadd_rule"></a>

Creates a group rule to dynamically add users to the specified group if they match the condition

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_rule_response = okta.group.add_rule(
    actions={
    },
    conditions={
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    status="ACTIVE",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### actions: [`GroupRuleAction`](./okta_python_sdk/type/group_rule_action.py)<a id="actions-groupruleactionokta_python_sdktypegroup_rule_actionpy"></a>


##### conditions: [`GroupRuleConditions`](./okta_python_sdk/type/group_rule_conditions.py)<a id="conditions-groupruleconditionsokta_python_sdktypegroup_rule_conditionspy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### status: [`GroupRuleStatus`](./okta_python_sdk/type/group_rule_status.py)<a id="status-grouprulestatusokta_python_sdktypegroup_rule_statuspy"></a>

##### type: `str`<a id="type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupRule`](./okta_python_sdk/type/group_rule.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupRule`](./okta_python_sdk/pydantic/group_rule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/rules` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.add_user_to_group`<a id="oktagroupadd_user_to_group"></a>

Adds a user to a group with 'OKTA_GROUP' type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.group.add_user_to_group(
    group_id="groupId_example",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/users/{userId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.assign_role_to_group`<a id="oktagroupassign_role_to_group"></a>

Assigns a Role to a Group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_role_to_group_response = okta.group.assign_role_to_group(
    body=None,
    group_id="groupId_example",
    type="SUPER_ADMIN",
    disable_notifications=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### type: [`RoleType`](./okta_python_sdk/type/role_type.py)<a id="type-roletypeokta_python_sdktyperole_typepy"></a>

##### disable_notifications: `bool`<a id="disable_notifications-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AssignRoleRequest`](./okta_python_sdk/type/assign_role_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Role`](./okta_python_sdk/pydantic/role.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/roles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.create_new_group`<a id="oktagroupcreate_new_group"></a>

Adds a new group with `OKTA_GROUP` type to your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_group_response = okta.group.create_new_group(
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_membership_updated="1970-01-01T00:00:00.00Z",
    last_updated="1970-01-01T00:00:00.00Z",
    object_class=[
        "string_example"
    ],
    profile={
    },
    type="OKTA_GROUP",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### embedded: [`GroupEmbedded`](./okta_python_sdk/type/group_embedded.py)<a id="embedded-groupembeddedokta_python_sdktypegroup_embeddedpy"></a>

##### links: [`GroupLinks`](./okta_python_sdk/type/group_links.py)<a id="links-grouplinksokta_python_sdktypegroup_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_membership_updated: `datetime`<a id="last_membership_updated-datetime"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### object_class: [`GroupObjectClass`](./okta_python_sdk/type/group_object_class.py)<a id="object_class-groupobjectclassokta_python_sdktypegroup_object_classpy"></a>

##### profile: [`GroupProfile`](./okta_python_sdk/type/group_profile.py)<a id="profile-groupprofileokta_python_sdktypegroup_profilepy"></a>


##### type: [`GroupType`](./okta_python_sdk/type/group_type.py)<a id="type-grouptypeokta_python_sdktypegroup_typepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Group`](./okta_python_sdk/type/group.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Group`](./okta_python_sdk/pydantic/group.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.deactivate_rule_lifecycle`<a id="oktagroupdeactivate_rule_lifecycle"></a>

Deactivates a specific group rule by id from your organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.group.deactivate_rule_lifecycle(
    rule_id="ruleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/rules/{ruleId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.delete_target_group_roles_catalog_apps`<a id="oktagroupdelete_target_group_roles_catalog_apps"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.group.delete_target_group_roles_catalog_apps(
    group_id="groupId_example",
    role_id="roleId_example",
    app_name="appName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### app_name: `str`<a id="app_name-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.enumerate_group_members`<a id="oktagroupenumerate_group_members"></a>

Enumerates all users that are a member of a group.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enumerate_group_members_response = okta.group.enumerate_group_members(
    group_id="groupId_example",
    after="string_example",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### after: `str`<a id="after-str"></a>

Specifies the pagination cursor for the next page of users

##### limit: `int`<a id="limit-int"></a>

Specifies the number of user results in a page

#### 🔄 Return<a id="🔄-return"></a>

[`GroupEnumerateGroupMembersResponse`](./okta_python_sdk/pydantic/group_enumerate_group_members_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.get_all_rules`<a id="oktagroupget_all_rules"></a>

Lists all group rules for your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_rules_response = okta.group.get_all_rules(
    limit=50,
    after="string_example",
    search="string_example",
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Specifies the number of rule results in a page

##### after: `str`<a id="after-str"></a>

Specifies the pagination cursor for the next page of rules

##### search: `str`<a id="search-str"></a>

Specifies the keyword to search fules for

##### expand: `str`<a id="expand-str"></a>

If specified as `groupIdToGroupNameMap`, then show group names

#### 🔄 Return<a id="🔄-return"></a>

[`GroupGetAllRulesResponse`](./okta_python_sdk/pydantic/group_get_all_rules_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/rules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.get_group_rule_by_id`<a id="oktagroupget_group_rule_by_id"></a>

Fetches a specific group rule by id from your organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_group_rule_by_id_response = okta.group.get_group_rule_by_id(
    rule_id="ruleId_example",
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GroupRule`](./okta_python_sdk/pydantic/group_rule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/rules/{ruleId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.get_role_list`<a id="oktagroupget_role_list"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_role_list_response = okta.group.get_role_list(
    group_id="groupId_example",
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GroupGetRoleListResponse`](./okta_python_sdk/pydantic/group_get_role_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/roles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.get_role_success`<a id="oktagroupget_role_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_role_success_response = okta.group.get_role_success(
    group_id="groupId_example",
    role_id="roleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Role`](./okta_python_sdk/pydantic/role.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/roles/{roleId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.get_role_targets_catalog_apps`<a id="oktagroupget_role_targets_catalog_apps"></a>

Lists all App targets for an `APP_ADMIN` Role assigned to a Group. This methods return list may include full Applications or Instances. The response for an instance will have an `ID` value, while Application will not have an ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_role_targets_catalog_apps_response = okta.group.get_role_targets_catalog_apps(
    group_id="groupId_example",
    role_id="roleId_example",
    after="string_example",
    limit=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GroupGetRoleTargetsCatalogAppsResponse`](./okta_python_sdk/pydantic/group_get_role_targets_catalog_apps_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.get_rules`<a id="oktagroupget_rules"></a>

Fetches a group from your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_rules_response = okta.group.get_rules(
    group_id="groupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Group`](./okta_python_sdk/pydantic/group.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.list`<a id="oktagrouplist"></a>

Enumerates groups in your organization with pagination. A subset of groups can be returned that match a supported filter expression or query.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = okta.group.list(
    q="string_example",
    filter="string_example",
    after="string_example",
    limit=10000,
    expand="string_example",
    search="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

Searches the name property of groups for matching value

##### filter: `str`<a id="filter-str"></a>

Filter expression for groups

##### after: `str`<a id="after-str"></a>

Specifies the pagination cursor for the next page of groups

##### limit: `int`<a id="limit-int"></a>

Specifies the number of group results in a page

##### expand: `str`<a id="expand-str"></a>

If specified, it causes additional metadata to be included in the response.

##### search: `str`<a id="search-str"></a>

Searches for groups with a supported filtering expression for all attributes except for _embedded, _links, and objectClass

#### 🔄 Return<a id="🔄-return"></a>

[`GroupListResponse`](./okta_python_sdk/pydantic/group_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.list_assigned_apps`<a id="oktagrouplist_assigned_apps"></a>

Enumerates all applications that are assigned to a group.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_assigned_apps_response = okta.group.list_assigned_apps(
    group_id="groupId_example",
    after="string_example",
    limit=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### after: `str`<a id="after-str"></a>

Specifies the pagination cursor for the next page of apps

##### limit: `int`<a id="limit-int"></a>

Specifies the number of app results for a page

#### 🔄 Return<a id="🔄-return"></a>

[`GroupListAssignedAppsResponse`](./okta_python_sdk/pydantic/group_list_assigned_apps_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/apps` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.list_role_targets_groups`<a id="oktagrouplist_role_targets_groups"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_role_targets_groups_response = okta.group.list_role_targets_groups(
    group_id="groupId_example",
    role_id="roleId_example",
    after="string_example",
    limit=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GroupListRoleTargetsGroupsResponse`](./okta_python_sdk/pydantic/group_list_role_targets_groups_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/roles/{roleId}/targets/groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.remove_app_instance_target_to_app_admin_role_given_to_group`<a id="oktagroupremove_app_instance_target_to_app_admin_role_given_to_group"></a>

Remove App Instance Target to App Administrator Role given to a Group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.group.remove_app_instance_target_to_app_admin_role_given_to_group(
    group_id="groupId_example",
    role_id="roleId_example",
    app_name="appName_example",
    application_id="applicationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### app_name: `str`<a id="app_name-str"></a>

##### application_id: `str`<a id="application_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.remove_operation`<a id="oktagroupremove_operation"></a>

Removes a group with `OKTA_GROUP` type from your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.group.remove_operation(
    group_id="groupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.remove_rule_by_id`<a id="oktagroupremove_rule_by_id"></a>

Removes a specific group rule by id from your organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.group.remove_rule_by_id(
    rule_id="ruleId_example",
    remove_users=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

##### remove_users: `bool`<a id="remove_users-bool"></a>

Indicates whether to keep or remove users from groups assigned by this rule.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/rules/{ruleId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.remove_target_group`<a id="oktagroupremove_target_group"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.group.remove_target_group(
    group_id="groupId_example",
    role_id="roleId_example",
    target_group_id="targetGroupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### target_group_id: `str`<a id="target_group_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/roles/{roleId}/targets/groups/{targetGroupId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.remove_user_from`<a id="oktagroupremove_user_from"></a>

Removes a user from a group with 'OKTA_GROUP' type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.group.remove_user_from(
    group_id="groupId_example",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/users/{userId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.unassign_role`<a id="oktagroupunassign_role"></a>

Unassigns a Role from a Group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.group.unassign_role(
    group_id="groupId_example",
    role_id="roleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/roles/{roleId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.update_profile`<a id="oktagroupupdate_profile"></a>

Updates the profile for a group with `OKTA_GROUP` type from your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_profile_response = okta.group.update_profile(
    group_id="groupId_example",
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_membership_updated="1970-01-01T00:00:00.00Z",
    last_updated="1970-01-01T00:00:00.00Z",
    object_class=[
        "string_example"
    ],
    profile={
    },
    type="OKTA_GROUP",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### embedded: [`GroupEmbedded`](./okta_python_sdk/type/group_embedded.py)<a id="embedded-groupembeddedokta_python_sdktypegroup_embeddedpy"></a>

##### links: [`GroupLinks`](./okta_python_sdk/type/group_links.py)<a id="links-grouplinksokta_python_sdktypegroup_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_membership_updated: `datetime`<a id="last_membership_updated-datetime"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### object_class: [`GroupObjectClass`](./okta_python_sdk/type/group_object_class.py)<a id="object_class-groupobjectclassokta_python_sdktypegroup_object_classpy"></a>

##### profile: [`GroupProfile`](./okta_python_sdk/type/group_profile.py)<a id="profile-groupprofileokta_python_sdktypegroup_profilepy"></a>


##### type: [`GroupType`](./okta_python_sdk/type/group_type.py)<a id="type-grouptypeokta_python_sdktypegroup_typepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Group`](./okta_python_sdk/type/group.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Group`](./okta_python_sdk/pydantic/group.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.update_roles_catalog_apps`<a id="oktagroupupdate_roles_catalog_apps"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.group.update_roles_catalog_apps(
    group_id="groupId_example",
    role_id="roleId_example",
    app_name="appName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### app_name: `str`<a id="app_name-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.update_rule`<a id="oktagroupupdate_rule"></a>

Updates a group rule. Only `INACTIVE` rules can be updated.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_rule_response = okta.group.update_rule(
    rule_id="ruleId_example",
    actions={
    },
    conditions={
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    status="ACTIVE",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

##### actions: [`GroupRuleAction`](./okta_python_sdk/type/group_rule_action.py)<a id="actions-groupruleactionokta_python_sdktypegroup_rule_actionpy"></a>


##### conditions: [`GroupRuleConditions`](./okta_python_sdk/type/group_rule_conditions.py)<a id="conditions-groupruleconditionsokta_python_sdktypegroup_rule_conditionspy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### status: [`GroupRuleStatus`](./okta_python_sdk/type/group_rule_status.py)<a id="status-grouprulestatusokta_python_sdktypegroup_rule_statuspy"></a>

##### type: `str`<a id="type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupRule`](./okta_python_sdk/type/group_rule.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupRule`](./okta_python_sdk/pydantic/group_rule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/rules/{ruleId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group.update_target_groups_role`<a id="oktagroupupdate_target_groups_role"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.group.update_target_groups_role(
    group_id="groupId_example",
    role_id="roleId_example",
    target_group_id="targetGroupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### target_group_id: `str`<a id="target_group_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/groups/{groupId}/roles/{roleId}/targets/groups/{targetGroupId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group_schema.get`<a id="oktagroup_schemaget"></a>

Fetches the group schema

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = okta.group_schema.get()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GroupSchema`](./okta_python_sdk/pydantic/group_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/schemas/group/default` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.group_schema.update_custom_properties`<a id="oktagroup_schemaupdate_custom_properties"></a>

Updates, adds ore removes one or more custom Group Profile properties in the schema

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_custom_properties_response = okta.group_schema.update_custom_properties(
    title="string_example",
    description="string_example",
    schema="string_example",
    links={
        "key": {},
    },
    created="string_example",
    definitions={
    },
    id="string_example",
    last_updated="string_example",
    name="string_example",
    properties={
    },
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

##### description: `str`<a id="description-str"></a>

##### schema: `str`<a id="schema-str"></a>

##### links: [`GroupSchemaLinks`](./okta_python_sdk/type/group_schema_links.py)<a id="links-groupschemalinksokta_python_sdktypegroup_schema_linkspy"></a>

##### created: `str`<a id="created-str"></a>

##### definitions: [`GroupSchemaDefinitions`](./okta_python_sdk/type/group_schema_definitions.py)<a id="definitions-groupschemadefinitionsokta_python_sdktypegroup_schema_definitionspy"></a>


##### id: `str`<a id="id-str"></a>

##### last_updated: `str`<a id="last_updated-str"></a>

##### name: `str`<a id="name-str"></a>

##### properties: [`UserSchemaProperties`](./okta_python_sdk/type/user_schema_properties.py)<a id="properties-userschemapropertiesokta_python_sdktypeuser_schema_propertiespy"></a>


##### type: `str`<a id="type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupSchema`](./okta_python_sdk/type/group_schema.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupSchema`](./okta_python_sdk/pydantic/group_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/schemas/group/default` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.activate_idp_lifecycle`<a id="oktaidentity_provideractivate_idp_lifecycle"></a>

Activates an inactive IdP.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_idp_lifecycle_response = okta.identity_provider.activate_idp_lifecycle(
    idp_id="idpId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityProvider`](./okta_python_sdk/pydantic/identity_provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.add_new_idp`<a id="oktaidentity_provideradd_new_idp"></a>

Adds a new IdP to your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_idp_response = okta.identity_provider.add_new_idp(
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    issuer_mode="ORG_URL",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    policy={
    },
    protocol={
        "type": "SAML2",
    },
    status="ACTIVE",
    type="SAML2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### links: [`IdentityProviderLinks`](./okta_python_sdk/type/identity_provider_links.py)<a id="links-identityproviderlinksokta_python_sdktypeidentity_provider_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### issuer_mode: `str`<a id="issuer_mode-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### policy: [`IdentityProviderPolicy`](./okta_python_sdk/type/identity_provider_policy.py)<a id="policy-identityproviderpolicyokta_python_sdktypeidentity_provider_policypy"></a>


##### protocol: [`Protocol`](./okta_python_sdk/type/protocol.py)<a id="protocol-protocolokta_python_sdktypeprotocolpy"></a>


##### status: `str`<a id="status-str"></a>

##### type: `str`<a id="type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IdentityProvider`](./okta_python_sdk/type/identity_provider.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IdentityProvider`](./okta_python_sdk/pydantic/identity_provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.add_x509_certificate_public_key`<a id="oktaidentity_provideradd_x509_certificate_public_key"></a>

Adds a new X.509 certificate credential to the IdP key store.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_x509_certificate_public_key_response = okta.identity_provider.add_x509_certificate_public_key(
    links={
        "key": {},
    },
    alg="string_example",
    created="1970-01-01T00:00:00.00Z",
    e="string_example",
    expires_at="1970-01-01T00:00:00.00Z",
    key_ops=[
        "string_example"
    ],
    kid="string_example",
    kty="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    n="string_example",
    status="string_example",
    use="string_example",
    x5c=[
        "string_example"
    ],
    x5t="string_example",
    x5t_s256="string_example",
    x5u="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### links: [`JsonWebKeyLinks`](./okta_python_sdk/type/json_web_key_links.py)<a id="links-jsonwebkeylinksokta_python_sdktypejson_web_key_linkspy"></a>

##### alg: `str`<a id="alg-str"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### e: `str`<a id="e-str"></a>

##### expires_at: `datetime`<a id="expires_at-datetime"></a>

##### key_ops: [`JsonWebKeyKeyOps`](./okta_python_sdk/type/json_web_key_key_ops.py)<a id="key_ops-jsonwebkeykeyopsokta_python_sdktypejson_web_key_key_opspy"></a>

##### kid: `str`<a id="kid-str"></a>

##### kty: `str`<a id="kty-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### n: `str`<a id="n-str"></a>

##### status: `str`<a id="status-str"></a>

##### use: `str`<a id="use-str"></a>

##### x5c: [`JsonWebKeyX5C`](./okta_python_sdk/type/json_web_key_x5_c.py)<a id="x5c-jsonwebkeyx5cokta_python_sdktypejson_web_key_x5_cpy"></a>

##### x5t: `str`<a id="x5t-str"></a>

##### x5t_s256: `str`<a id="x5t_s256-str"></a>

##### x5u: `str`<a id="x5u-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JsonWebKey`](./okta_python_sdk/type/json_web_key.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JsonWebKey`](./okta_python_sdk/pydantic/json_web_key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/credentials/keys` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.clone_signing_key_credential`<a id="oktaidentity_providerclone_signing_key_credential"></a>

Clones a X.509 certificate for an IdP signing key credential from a source IdP to target IdP

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
clone_signing_key_credential_response = okta.identity_provider.clone_signing_key_credential(
    idp_id="idpId_example",
    key_id="keyId_example",
    target_idp_id="targetIdpId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

##### key_id: `str`<a id="key_id-str"></a>

##### target_idp_id: `str`<a id="target_idp_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`JsonWebKey`](./okta_python_sdk/pydantic/json_web_key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/credentials/keys/{keyId}/clone` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.deactivate_idp`<a id="oktaidentity_providerdeactivate_idp"></a>

Deactivates an active IdP.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deactivate_idp_response = okta.identity_provider.deactivate_idp(
    idp_id="idpId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityProvider`](./okta_python_sdk/pydantic/identity_provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.delete_key_credential`<a id="oktaidentity_providerdelete_key_credential"></a>

Deletes a specific IdP Key Credential by `kid` if it is not currently being used by an Active or Inactive IdP.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.identity_provider.delete_key_credential(
    key_id="keyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key_id: `str`<a id="key_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/credentials/keys/{keyId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.enumerate_idp_keys`<a id="oktaidentity_providerenumerate_idp_keys"></a>

Enumerates IdP key credentials.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enumerate_idp_keys_response = okta.identity_provider.enumerate_idp_keys(
    after="string_example",
    limit=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### after: `str`<a id="after-str"></a>

Specifies the pagination cursor for the next page of keys

##### limit: `int`<a id="limit-int"></a>

Specifies the number of key results in a page

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityProviderEnumerateIdpKeysResponse`](./okta_python_sdk/pydantic/identity_provider_enumerate_idp_keys_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/credentials/keys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.generate_csr`<a id="oktaidentity_providergenerate_csr"></a>

Generates a new key pair and returns a Certificate Signing Request for it.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_csr_response = okta.identity_provider.generate_csr(
    body=None,
    idp_id="idpId_example",
    subject=None,
    subject_alt_names=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

##### subject: [`CsrMetadataSubject`](./okta_python_sdk/type/csr_metadata_subject.py)<a id="subject-csrmetadatasubjectokta_python_sdktypecsr_metadata_subjectpy"></a>


##### subject_alt_names: [`CsrMetadataSubjectAltNames`](./okta_python_sdk/type/csr_metadata_subject_alt_names.py)<a id="subject_alt_names-csrmetadatasubjectaltnamesokta_python_sdktypecsr_metadata_subject_alt_namespy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CsrMetadata`](./okta_python_sdk/type/csr_metadata.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Csr`](./okta_python_sdk/pydantic/csr.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/credentials/csrs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.generate_new_signing_key_credential`<a id="oktaidentity_providergenerate_new_signing_key_credential"></a>

Generates a new X.509 certificate for an IdP signing key credential to be used for signing assertions sent to the IdP

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_new_signing_key_credential_response = okta.identity_provider.generate_new_signing_key_credential(
    idp_id="idpId_example",
    validity_years=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

##### validity_years: `int`<a id="validity_years-int"></a>

expiry of the IdP Key Credential

#### 🔄 Return<a id="🔄-return"></a>

[`JsonWebKey`](./okta_python_sdk/pydantic/json_web_key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/credentials/keys/generate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.get_by_idp`<a id="oktaidentity_providerget_by_idp"></a>

Fetches an IdP by `id`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_idp_response = okta.identity_provider.get_by_idp(
    idp_id="idpId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityProvider`](./okta_python_sdk/pydantic/identity_provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.get_csr_by_idp`<a id="oktaidentity_providerget_csr_by_idp"></a>

Gets a specific Certificate Signing Request model by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_csr_by_idp_response = okta.identity_provider.get_csr_by_idp(
    idp_id="idpId_example",
    csr_id="csrId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

##### csr_id: `str`<a id="csr_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Csr`](./okta_python_sdk/pydantic/csr.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/credentials/csrs/{csrId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.get_key_credential_by_idp`<a id="oktaidentity_providerget_key_credential_by_idp"></a>

Gets a specific IdP Key Credential by `kid`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_key_credential_by_idp_response = okta.identity_provider.get_key_credential_by_idp(
    key_id="keyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key_id: `str`<a id="key_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`JsonWebKey`](./okta_python_sdk/pydantic/json_web_key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/credentials/keys/{keyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.get_linked_user_by_id`<a id="oktaidentity_providerget_linked_user_by_id"></a>

Fetches a linked IdP user by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_linked_user_by_id_response = okta.identity_provider.get_linked_user_by_id(
    idp_id="idpId_example",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityProviderApplicationUser`](./okta_python_sdk/pydantic/identity_provider_application_user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/users/{userId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.get_signing_key_credential_by_idp`<a id="oktaidentity_providerget_signing_key_credential_by_idp"></a>

Gets a specific IdP Key Credential by `kid`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_signing_key_credential_by_idp_response = okta.identity_provider.get_signing_key_credential_by_idp(
    idp_id="idpId_example",
    key_id="keyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

##### key_id: `str`<a id="key_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`JsonWebKey`](./okta_python_sdk/pydantic/json_web_key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/credentials/keys/{keyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.get_social_auth_tokens`<a id="oktaidentity_providerget_social_auth_tokens"></a>

Fetches the tokens minted by the Social Authentication Provider when the user authenticates with Okta via Social Auth.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_social_auth_tokens_response = okta.identity_provider.get_social_auth_tokens(
    idp_id="idpId_example",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityProviderGetSocialAuthTokensResponse`](./okta_python_sdk/pydantic/identity_provider_get_social_auth_tokens_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/users/{userId}/credentials/tokens` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.get_user`<a id="oktaidentity_providerget_user"></a>

Find all the users linked to an identity provider

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_response = okta.identity_provider.get_user(
    idp_id="idpId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityProviderGetUserResponse`](./okta_python_sdk/pydantic/identity_provider_get_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.link_user_to_idp_without_transaction`<a id="oktaidentity_providerlink_user_to_idp_without_transaction"></a>

Links an Okta user to an existing Social Identity Provider. This does not support the SAML2 Identity Provider Type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
link_user_to_idp_without_transaction_response = okta.identity_provider.link_user_to_idp_without_transaction(
    idp_id="idpId_example",
    user_id="userId_example",
    external_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### external_id: `str`<a id="external_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserIdentityProviderLinkRequest`](./okta_python_sdk/type/user_identity_provider_link_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IdentityProviderApplicationUser`](./okta_python_sdk/pydantic/identity_provider_application_user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/users/{userId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.list`<a id="oktaidentity_providerlist"></a>

Enumerates IdPs in your organization with pagination. A subset of IdPs can be returned that match a supported filter expression or query.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = okta.identity_provider.list(
    q="string_example",
    after="string_example",
    limit=20,
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

Searches the name property of IdPs for matching value

##### after: `str`<a id="after-str"></a>

Specifies the pagination cursor for the next page of IdPs

##### limit: `int`<a id="limit-int"></a>

Specifies the number of IdP results in a page

##### type: `str`<a id="type-str"></a>

Filters IdPs by type

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityProviderListResponse`](./okta_python_sdk/pydantic/identity_provider_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.list_csrs_for_certificate_signing_requests`<a id="oktaidentity_providerlist_csrs_for_certificate_signing_requests"></a>

Enumerates Certificate Signing Requests for an IdP

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_csrs_for_certificate_signing_requests_response = okta.identity_provider.list_csrs_for_certificate_signing_requests(
    idp_id="idpId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityProviderListCsrsForCertificateSigningRequestsResponse`](./okta_python_sdk/pydantic/identity_provider_list_csrs_for_certificate_signing_requests_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/credentials/csrs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.list_signing_key_credentials`<a id="oktaidentity_providerlist_signing_key_credentials"></a>

Enumerates signing key credentials for an IdP

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_signing_key_credentials_response = okta.identity_provider.list_signing_key_credentials(
    idp_id="idpId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityProviderListSigningKeyCredentialsResponse`](./okta_python_sdk/pydantic/identity_provider_list_signing_key_credentials_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/credentials/keys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.remove_idp`<a id="oktaidentity_providerremove_idp"></a>

Removes an IdP from your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.identity_provider.remove_idp(
    idp_id="idpId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.revoke_csr_for_identity_provider`<a id="oktaidentity_providerrevoke_csr_for_identity_provider"></a>

Revoke a Certificate Signing Request and delete the key pair from the IdP

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.identity_provider.revoke_csr_for_identity_provider(
    idp_id="idpId_example",
    csr_id="csrId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

##### csr_id: `str`<a id="csr_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/credentials/csrs/{csrId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.unlink_user`<a id="oktaidentity_providerunlink_user"></a>

Removes the link between the Okta user and the IdP user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.identity_provider.unlink_user(
    idp_id="idpId_example",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/users/{userId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.update_configuration`<a id="oktaidentity_providerupdate_configuration"></a>

Updates the configuration for an IdP.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_configuration_response = okta.identity_provider.update_configuration(
    idp_id="idpId_example",
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    issuer_mode="ORG_URL",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    policy={
    },
    protocol={
        "type": "SAML2",
    },
    status="ACTIVE",
    type="SAML2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

##### links: [`IdentityProviderLinks`](./okta_python_sdk/type/identity_provider_links.py)<a id="links-identityproviderlinksokta_python_sdktypeidentity_provider_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### issuer_mode: `str`<a id="issuer_mode-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### policy: [`IdentityProviderPolicy`](./okta_python_sdk/type/identity_provider_policy.py)<a id="policy-identityproviderpolicyokta_python_sdktypeidentity_provider_policypy"></a>


##### protocol: [`Protocol`](./okta_python_sdk/type/protocol.py)<a id="protocol-protocolokta_python_sdktypeprotocolpy"></a>


##### status: `str`<a id="status-str"></a>

##### type: `str`<a id="type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IdentityProvider`](./okta_python_sdk/type/identity_provider.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IdentityProvider`](./okta_python_sdk/pydantic/identity_provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.identity_provider.update_csr_lifecycle_publish`<a id="oktaidentity_providerupdate_csr_lifecycle_publish"></a>

Update the Certificate Signing Request with a signed X.509 certificate and add it into the signing key credentials for the IdP.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_csr_lifecycle_publish_response = okta.identity_provider.update_csr_lifecycle_publish(
    idp_id="idpId_example",
    csr_id="csrId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idp_id: `str`<a id="idp_id-str"></a>

##### csr_id: `str`<a id="csr_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`JsonWebKey`](./okta_python_sdk/pydantic/json_web_key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/idps/{idpId}/credentials/csrs/{csrId}/lifecycle/publish` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.inline_hook.activate_lifecycle`<a id="oktainline_hookactivate_lifecycle"></a>

Activates the Inline Hook matching the provided id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_lifecycle_response = okta.inline_hook.activate_lifecycle(
    inline_hook_id="inlineHookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inline_hook_id: `str`<a id="inline_hook_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`InlineHook`](./okta_python_sdk/pydantic/inline_hook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/inlineHooks/{inlineHookId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.inline_hook.create_success`<a id="oktainline_hookcreate_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_success_response = okta.inline_hook.create_success(
    version="string_example",
    links={
        "key": {},
    },
    channel={
        "type": "HTTP",
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    status="ACTIVE",
    type="com.okta.oauth2.tokens.transform",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

##### links: [`InlineHookLinks`](./okta_python_sdk/type/inline_hook_links.py)<a id="links-inlinehooklinksokta_python_sdktypeinline_hook_linkspy"></a>

##### channel: [`InlineHookChannel`](./okta_python_sdk/type/inline_hook_channel.py)<a id="channel-inlinehookchannelokta_python_sdktypeinline_hook_channelpy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### status: [`InlineHookStatus`](./okta_python_sdk/type/inline_hook_status.py)<a id="status-inlinehookstatusokta_python_sdktypeinline_hook_statuspy"></a>

##### type: [`InlineHookType`](./okta_python_sdk/type/inline_hook_type.py)<a id="type-inlinehooktypeokta_python_sdktypeinline_hook_typepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InlineHook`](./okta_python_sdk/type/inline_hook.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InlineHook`](./okta_python_sdk/pydantic/inline_hook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/inlineHooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.inline_hook.deactivate_lifecycle`<a id="oktainline_hookdeactivate_lifecycle"></a>

Deactivates the Inline Hook matching the provided id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deactivate_lifecycle_response = okta.inline_hook.deactivate_lifecycle(
    inline_hook_id="inlineHookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inline_hook_id: `str`<a id="inline_hook_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`InlineHook`](./okta_python_sdk/pydantic/inline_hook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/inlineHooks/{inlineHookId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.inline_hook.delete_matching_by_id`<a id="oktainline_hookdelete_matching_by_id"></a>

Deletes the Inline Hook matching the provided id. Once deleted, the Inline Hook is unrecoverable. As a safety precaution, only Inline Hooks with a status of INACTIVE are eligible for deletion.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.inline_hook.delete_matching_by_id(
    inline_hook_id="inlineHookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inline_hook_id: `str`<a id="inline_hook_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/inlineHooks/{inlineHookId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.inline_hook.execute_with_input`<a id="oktainline_hookexecute_with_input"></a>

Executes the Inline Hook matching the provided inlineHookId using the request body as the input. This will send the provided data through the Channel and return a response if it matches the correct data contract. This execution endpoint should only be used for testing purposes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
execute_with_input_response = okta.inline_hook.execute_with_input(
    inline_hook_id="inlineHookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inline_hook_id: `str`<a id="inline_hook_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🔄 Return<a id="🔄-return"></a>

[`InlineHookResponse`](./okta_python_sdk/pydantic/inline_hook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/inlineHooks/{inlineHookId}/execute` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.inline_hook.get_by_id`<a id="oktainline_hookget_by_id"></a>

Gets an inline hook by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = okta.inline_hook.get_by_id(
    inline_hook_id="inlineHookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inline_hook_id: `str`<a id="inline_hook_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`InlineHook`](./okta_python_sdk/pydantic/inline_hook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/inlineHooks/{inlineHookId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.inline_hook.get_success`<a id="oktainline_hookget_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_success_response = okta.inline_hook.get_success(
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`InlineHookGetSuccessResponse`](./okta_python_sdk/pydantic/inline_hook_get_success_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/inlineHooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.inline_hook.update_by_id`<a id="oktainline_hookupdate_by_id"></a>

Updates an inline hook by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = okta.inline_hook.update_by_id(
    inline_hook_id="inlineHookId_example",
    version="string_example",
    links={
        "key": {},
    },
    channel={
        "type": "HTTP",
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    status="ACTIVE",
    type="com.okta.oauth2.tokens.transform",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inline_hook_id: `str`<a id="inline_hook_id-str"></a>

##### version: `str`<a id="version-str"></a>

##### links: [`InlineHookLinks`](./okta_python_sdk/type/inline_hook_links.py)<a id="links-inlinehooklinksokta_python_sdktypeinline_hook_linkspy"></a>

##### channel: [`InlineHookChannel`](./okta_python_sdk/type/inline_hook_channel.py)<a id="channel-inlinehookchannelokta_python_sdktypeinline_hook_channelpy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### status: [`InlineHookStatus`](./okta_python_sdk/type/inline_hook_status.py)<a id="status-inlinehookstatusokta_python_sdktypeinline_hook_statuspy"></a>

##### type: [`InlineHookType`](./okta_python_sdk/type/inline_hook_type.py)<a id="type-inlinehooktypeokta_python_sdktypeinline_hook_typepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InlineHook`](./okta_python_sdk/type/inline_hook.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InlineHook`](./okta_python_sdk/pydantic/inline_hook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/inlineHooks/{inlineHookId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.linked_object.create_linked_object`<a id="oktalinked_objectcreate_linked_object"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_linked_object_response = okta.linked_object.create_linked_object(
    links={
        "key": {},
    },
    associated={
        "type": "USER",
    },
    primary={
        "type": "USER",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### links: [`LinkedObjectLinks`](./okta_python_sdk/type/linked_object_links.py)<a id="links-linkedobjectlinksokta_python_sdktypelinked_object_linkspy"></a>

##### associated: [`LinkedObjectDetails`](./okta_python_sdk/type/linked_object_details.py)<a id="associated-linkedobjectdetailsokta_python_sdktypelinked_object_detailspy"></a>


##### primary: [`LinkedObjectDetails`](./okta_python_sdk/type/linked_object_details.py)<a id="primary-linkedobjectdetailsokta_python_sdktypelinked_object_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LinkedObject`](./okta_python_sdk/type/linked_object.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LinkedObject`](./okta_python_sdk/pydantic/linked_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/schemas/user/linkedObjects` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.linked_object.delete_user_linked_object`<a id="oktalinked_objectdelete_user_linked_object"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.linked_object.delete_user_linked_object(
    linked_object_name="linkedObjectName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### linked_object_name: `str`<a id="linked_object_name-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/schemas/user/linkedObjects/{linkedObjectName}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.linked_object.get_user_linked_objects`<a id="oktalinked_objectget_user_linked_objects"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_linked_objects_response = okta.linked_object.get_user_linked_objects()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LinkedObjectGetUserLinkedObjectsResponse`](./okta_python_sdk/pydantic/linked_object_get_user_linked_objects_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/schemas/user/linkedObjects` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.linked_object.get_user_linked_objects_0`<a id="oktalinked_objectget_user_linked_objects_0"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_linked_objects_0_response = okta.linked_object.get_user_linked_objects_0(
    linked_object_name="linkedObjectName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### linked_object_name: `str`<a id="linked_object_name-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`LinkedObject`](./okta_python_sdk/pydantic/linked_object.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/schemas/user/linkedObjects/{linkedObjectName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.log.get_list_events`<a id="oktalogget_list_events"></a>

The Okta System Log API provides read access to your organization’s system log. This API provides more functionality than the Events API

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_events_response = okta.log.get_list_events(
    since="1970-01-01T00:00:00.00Z",
    until="1970-01-01T00:00:00.00Z",
    filter="string_example",
    q="string_example",
    limit=100,
    sort_order="ASCENDING",
    after="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### since: `datetime`<a id="since-datetime"></a>

##### until: `datetime`<a id="until-datetime"></a>

##### filter: `str`<a id="filter-str"></a>

##### q: `str`<a id="q-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### sort_order: `str`<a id="sort_order-str"></a>

##### after: `str`<a id="after-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`LogGetListEventsResponse`](./okta_python_sdk/pydantic/log_get_list_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.network_zone.activate_lifecycle`<a id="oktanetwork_zoneactivate_lifecycle"></a>

Activate Network Zone

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_lifecycle_response = okta.network_zone.activate_lifecycle(
    zone_id="zoneId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### zone_id: `str`<a id="zone_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`NetworkZone`](./okta_python_sdk/pydantic/network_zone.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/zones/{zoneId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.network_zone.create_new`<a id="oktanetwork_zonecreate_new"></a>

Adds a new network zone to your Okta organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = okta.network_zone.create_new(
    links={
        "key": {},
    },
    asns=[
        "string_example"
    ],
    created="1970-01-01T00:00:00.00Z",
    gateways=[
        {
            "type": "CIDR",
        }
    ],
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    locations=[
        {
        }
    ],
    name="string_example",
    proxies=[
        {
            "type": "CIDR",
        }
    ],
    proxy_type="string_example",
    status="ACTIVE",
    system=True,
    type="IP",
    usage="POLICY",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### links: [`NetworkZoneLinks`](./okta_python_sdk/type/network_zone_links.py)<a id="links-networkzonelinksokta_python_sdktypenetwork_zone_linkspy"></a>

##### asns: [`NetworkZoneAsns`](./okta_python_sdk/type/network_zone_asns.py)<a id="asns-networkzoneasnsokta_python_sdktypenetwork_zone_asnspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### gateways: List[`NetworkZoneAddress`]<a id="gateways-listnetworkzoneaddress"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### locations: List[`NetworkZoneLocation`]<a id="locations-listnetworkzonelocation"></a>

##### name: `str`<a id="name-str"></a>

##### proxies: List[`NetworkZoneAddress`]<a id="proxies-listnetworkzoneaddress"></a>

##### proxy_type: `str`<a id="proxy_type-str"></a>

##### status: [`NetworkZoneStatus`](./okta_python_sdk/type/network_zone_status.py)<a id="status-networkzonestatusokta_python_sdktypenetwork_zone_statuspy"></a>

##### system: `bool`<a id="system-bool"></a>

##### type: [`NetworkZoneType`](./okta_python_sdk/type/network_zone_type.py)<a id="type-networkzonetypeokta_python_sdktypenetwork_zone_typepy"></a>

##### usage: [`NetworkZoneUsage`](./okta_python_sdk/type/network_zone_usage.py)<a id="usage-networkzoneusageokta_python_sdktypenetwork_zone_usagepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NetworkZone`](./okta_python_sdk/type/network_zone.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NetworkZone`](./okta_python_sdk/pydantic/network_zone.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/zones` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.network_zone.deactivate_zone_lifecycle`<a id="oktanetwork_zonedeactivate_zone_lifecycle"></a>

Deactivates a network zone.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deactivate_zone_lifecycle_response = okta.network_zone.deactivate_zone_lifecycle(
    zone_id="zoneId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### zone_id: `str`<a id="zone_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`NetworkZone`](./okta_python_sdk/pydantic/network_zone.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/zones/{zoneId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.network_zone.get_by_id`<a id="oktanetwork_zoneget_by_id"></a>

Fetches a network zone from your Okta organization by `id`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = okta.network_zone.get_by_id(
    zone_id="zoneId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### zone_id: `str`<a id="zone_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`NetworkZone`](./okta_python_sdk/pydantic/network_zone.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/zones/{zoneId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.network_zone.list_zones`<a id="oktanetwork_zonelist_zones"></a>

Enumerates network zones added to your organization with pagination. A subset of zones can be returned that match a supported filter expression or query.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_zones_response = okta.network_zone.list_zones(
    after="string_example",
    limit=-1,
    filter="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### after: `str`<a id="after-str"></a>

Specifies the pagination cursor for the next page of network zones

##### limit: `int`<a id="limit-int"></a>

Specifies the number of results for a page

##### filter: `str`<a id="filter-str"></a>

Filters zones by usage or id expression

#### 🔄 Return<a id="🔄-return"></a>

[`NetworkZoneListZonesResponse`](./okta_python_sdk/pydantic/network_zone_list_zones_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/zones` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.network_zone.remove_zone`<a id="oktanetwork_zoneremove_zone"></a>

Removes network zone.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.network_zone.remove_zone(
    zone_id="zoneId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### zone_id: `str`<a id="zone_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/zones/{zoneId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.network_zone.update_zone`<a id="oktanetwork_zoneupdate_zone"></a>

Updates a network zone in your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_zone_response = okta.network_zone.update_zone(
    zone_id="zoneId_example",
    links={
        "key": {},
    },
    asns=[
        "string_example"
    ],
    created="1970-01-01T00:00:00.00Z",
    gateways=[
        {
            "type": "CIDR",
        }
    ],
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    locations=[
        {
        }
    ],
    name="string_example",
    proxies=[
        {
            "type": "CIDR",
        }
    ],
    proxy_type="string_example",
    status="ACTIVE",
    system=True,
    type="IP",
    usage="POLICY",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### zone_id: `str`<a id="zone_id-str"></a>

##### links: [`NetworkZoneLinks`](./okta_python_sdk/type/network_zone_links.py)<a id="links-networkzonelinksokta_python_sdktypenetwork_zone_linkspy"></a>

##### asns: [`NetworkZoneAsns`](./okta_python_sdk/type/network_zone_asns.py)<a id="asns-networkzoneasnsokta_python_sdktypenetwork_zone_asnspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### gateways: List[`NetworkZoneAddress`]<a id="gateways-listnetworkzoneaddress"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### locations: List[`NetworkZoneLocation`]<a id="locations-listnetworkzonelocation"></a>

##### name: `str`<a id="name-str"></a>

##### proxies: List[`NetworkZoneAddress`]<a id="proxies-listnetworkzoneaddress"></a>

##### proxy_type: `str`<a id="proxy_type-str"></a>

##### status: [`NetworkZoneStatus`](./okta_python_sdk/type/network_zone_status.py)<a id="status-networkzonestatusokta_python_sdktypenetwork_zone_statuspy"></a>

##### system: `bool`<a id="system-bool"></a>

##### type: [`NetworkZoneType`](./okta_python_sdk/type/network_zone_type.py)<a id="type-networkzonetypeokta_python_sdktypenetwork_zone_typepy"></a>

##### usage: [`NetworkZoneUsage`](./okta_python_sdk/type/network_zone_usage.py)<a id="usage-networkzoneusageokta_python_sdktypenetwork_zone_usagepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NetworkZone`](./okta_python_sdk/type/network_zone.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NetworkZone`](./okta_python_sdk/pydantic/network_zone.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/zones/{zoneId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.extend_okta_support`<a id="oktaorgextend_okta_support"></a>

Extends the length of time that Okta Support can access your org by 24 hours. This means that 24 hours are added to the remaining access time.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
extend_okta_support_response = okta.org.extend_okta_support()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrgOktaSupportSettingsObj`](./okta_python_sdk/pydantic/org_okta_support_settings_obj.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/privacy/oktaSupport/extend` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.extend_okta_support_0`<a id="oktaorgextend_okta_support_0"></a>

Revokes Okta Support access to your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
extend_okta_support_0_response = okta.org.extend_okta_support_0()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrgOktaSupportSettingsObj`](./okta_python_sdk/pydantic/org_okta_support_settings_obj.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/privacy/oktaSupport/revoke` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.get_contact_user`<a id="oktaorgget_contact_user"></a>

Retrieves the URL of the User associated with the specified Contact Type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_contact_user_response = okta.org.get_contact_user(
    contact_type="contactType_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_type: `str`<a id="contact_type-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OrgContactUser`](./okta_python_sdk/pydantic/org_contact_user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/contacts/{contactType}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.get_okta_communication_settings`<a id="oktaorgget_okta_communication_settings"></a>

Gets Okta Communication Settings of your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_okta_communication_settings_response = okta.org.get_okta_communication_settings()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrgOktaCommunicationSetting`](./okta_python_sdk/pydantic/org_okta_communication_setting.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/privacy/oktaCommunication` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.get_okta_support_settings`<a id="oktaorgget_okta_support_settings"></a>

Gets Okta Support Settings of your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_okta_support_settings_response = okta.org.get_okta_support_settings()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrgOktaSupportSettingsObj`](./okta_python_sdk/pydantic/org_okta_support_settings_obj.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/privacy/oktaSupport` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.get_org_preferences`<a id="oktaorgget_org_preferences"></a>

Gets preferences of your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_org_preferences_response = okta.org.get_org_preferences()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrgPreferences`](./okta_python_sdk/pydantic/org_preferences.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/preferences` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.get_settings`<a id="oktaorgget_settings"></a>

Get settings of your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_settings_response = okta.org.get_settings()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrgSetting`](./okta_python_sdk/pydantic/org_setting.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.grant_okta_support_access`<a id="oktaorggrant_okta_support_access"></a>

Enables you to temporarily allow Okta Support to access your org as an administrator for eight hours.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
grant_okta_support_access_response = okta.org.grant_okta_support_access()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrgOktaSupportSettingsObj`](./okta_python_sdk/pydantic/org_okta_support_settings_obj.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/privacy/oktaSupport/grant` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.hide_end_user_footer`<a id="oktaorghide_end_user_footer"></a>

Hide the Okta UI footer for all end users of your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hide_end_user_footer_response = okta.org.hide_end_user_footer()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrgPreferences`](./okta_python_sdk/pydantic/org_preferences.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/preferences/hideEndUserFooter` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.list_contact_types`<a id="oktaorglist_contact_types"></a>

Gets Contact Types of your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_contact_types_response = okta.org.list_contact_types()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrgListContactTypesResponse`](./okta_python_sdk/pydantic/org_list_contact_types_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/contacts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.make_okta_ui_footer_visible`<a id="oktaorgmake_okta_ui_footer_visible"></a>

Makes the Okta UI footer visible for all end users of your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
make_okta_ui_footer_visible_response = okta.org.make_okta_ui_footer_visible()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrgPreferences`](./okta_python_sdk/pydantic/org_preferences.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/preferences/showEndUserFooter` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.opt_in_okta_communication_emails`<a id="oktaorgopt_in_okta_communication_emails"></a>

Opts in all users of this org to Okta Communication emails.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
opt_in_okta_communication_emails_response = okta.org.opt_in_okta_communication_emails()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrgOktaCommunicationSetting`](./okta_python_sdk/pydantic/org_okta_communication_setting.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/privacy/oktaCommunication/optIn` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.opt_out_okta_communication_emails`<a id="oktaorgopt_out_okta_communication_emails"></a>

Opts out all users of this org from Okta Communication emails.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
opt_out_okta_communication_emails_response = okta.org.opt_out_okta_communication_emails()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OrgOktaCommunicationSetting`](./okta_python_sdk/pydantic/org_okta_communication_setting.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/privacy/oktaCommunication/optOut` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.update_contact_user`<a id="oktaorgupdate_contact_user"></a>

Updates the User associated with the specified Contact Type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_contact_user_response = okta.org.update_contact_user(
    contact_type="contactType_example",
    user_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_type: `str`<a id="contact_type-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserIdString`](./okta_python_sdk/type/user_id_string.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrgContactUser`](./okta_python_sdk/pydantic/org_contact_user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/contacts/{contactType}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.update_organization_logo`<a id="oktaorgupdate_organization_logo"></a>

Updates the logo for your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.org.update_organization_logo(
    file=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicationUpdateLogoRequest`](./okta_python_sdk/type/application_update_logo_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org/logo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.update_setting`<a id="oktaorgupdate_setting"></a>

Update settings of your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_setting_response = okta.org.update_setting(
    links={
        "key": {},
    },
    address1="string_example",
    address2="string_example",
    city="string_example",
    company_name="string_example",
    country="string_example",
    created="1970-01-01T00:00:00.00Z",
    end_user_support_help_url="string_example",
    expires_at="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    phone_number="string_example",
    postal_code="string_example",
    state="string_example",
    status="string_example",
    subdomain="string_example",
    support_phone_number="string_example",
    website="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### links: `Dict[str, Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`<a id="links-dictstr-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### address1: `str`<a id="address1-str"></a>

##### address2: `str`<a id="address2-str"></a>

##### city: `str`<a id="city-str"></a>

##### company_name: `str`<a id="company_name-str"></a>

##### country: `str`<a id="country-str"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### end_user_support_help_url: `str`<a id="end_user_support_help_url-str"></a>

##### expires_at: `datetime`<a id="expires_at-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### phone_number: `str`<a id="phone_number-str"></a>

##### postal_code: `str`<a id="postal_code-str"></a>

##### state: `str`<a id="state-str"></a>

##### status: `str`<a id="status-str"></a>

##### subdomain: `str`<a id="subdomain-str"></a>

##### support_phone_number: `str`<a id="support_phone_number-str"></a>

##### website: `str`<a id="website-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrgSetting`](./okta_python_sdk/type/org_setting.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrgSetting`](./okta_python_sdk/pydantic/org_setting.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.org.update_settings`<a id="oktaorgupdate_settings"></a>

Partial update settings of your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_settings_response = okta.org.update_settings(
    links={
        "key": {},
    },
    address1="string_example",
    address2="string_example",
    city="string_example",
    company_name="string_example",
    country="string_example",
    created="1970-01-01T00:00:00.00Z",
    end_user_support_help_url="string_example",
    expires_at="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    phone_number="string_example",
    postal_code="string_example",
    state="string_example",
    status="string_example",
    subdomain="string_example",
    support_phone_number="string_example",
    website="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### links: `Dict[str, Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`<a id="links-dictstr-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### address1: `str`<a id="address1-str"></a>

##### address2: `str`<a id="address2-str"></a>

##### city: `str`<a id="city-str"></a>

##### company_name: `str`<a id="company_name-str"></a>

##### country: `str`<a id="country-str"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### end_user_support_help_url: `str`<a id="end_user_support_help_url-str"></a>

##### expires_at: `datetime`<a id="expires_at-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### phone_number: `str`<a id="phone_number-str"></a>

##### postal_code: `str`<a id="postal_code-str"></a>

##### state: `str`<a id="state-str"></a>

##### status: `str`<a id="status-str"></a>

##### subdomain: `str`<a id="subdomain-str"></a>

##### support_phone_number: `str`<a id="support_phone_number-str"></a>

##### website: `str`<a id="website-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrgSetting`](./okta_python_sdk/type/org_setting.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrgSetting`](./okta_python_sdk/pydantic/org_setting.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/org` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.activate_lifecycle`<a id="oktapolicyactivate_lifecycle"></a>

Activates a policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.policy.activate_lifecycle(
    policy_id="policyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies/{policyId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.activate_rule_lifecycle`<a id="oktapolicyactivate_rule_lifecycle"></a>

Activates a policy rule.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.policy.activate_rule_lifecycle(
    policy_id="policyId_example",
    rule_id="ruleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies/{policyId}/rules/{ruleId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.create_new_policy`<a id="oktapolicycreate_new_policy"></a>

Creates a policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_policy_response = okta.policy.create_new_policy(
    description="string_example",
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    conditions={
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    priority=1,
    status="ACTIVE",
    system=True,
    type="OAUTH_AUTHORIZATION_POLICY",
    activate=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

##### embedded: [`PolicyEmbedded`](./okta_python_sdk/type/policy_embedded.py)<a id="embedded-policyembeddedokta_python_sdktypepolicy_embeddedpy"></a>

##### links: [`PolicyLinks`](./okta_python_sdk/type/policy_links.py)<a id="links-policylinksokta_python_sdktypepolicy_linkspy"></a>

##### conditions: [`PolicyRuleConditions`](./okta_python_sdk/type/policy_rule_conditions.py)<a id="conditions-policyruleconditionsokta_python_sdktypepolicy_rule_conditionspy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### priority: `int`<a id="priority-int"></a>

##### status: `str`<a id="status-str"></a>

##### system: `bool`<a id="system-bool"></a>

##### type: [`PolicyType`](./okta_python_sdk/type/policy_type.py)<a id="type-policytypeokta_python_sdktypepolicy_typepy"></a>

##### activate: `bool`<a id="activate-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Policy`](./okta_python_sdk/type/policy.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Policy`](./okta_python_sdk/pydantic/policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.create_rule`<a id="oktapolicycreate_rule"></a>

Creates a policy rule.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_rule_response = okta.policy.create_rule(
    policy_id="policyId_example",
    actions={
    },
    conditions={
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    priority=1,
    status="ACTIVE",
    system=False,
    type="SIGN_ON",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### actions: [`PolicyRuleActions`](./okta_python_sdk/type/policy_rule_actions.py)<a id="actions-policyruleactionsokta_python_sdktypepolicy_rule_actionspy"></a>


##### conditions: [`PolicyRuleConditions`](./okta_python_sdk/type/policy_rule_conditions.py)<a id="conditions-policyruleconditionsokta_python_sdktypepolicy_rule_conditionspy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### priority: `int`<a id="priority-int"></a>

##### status: `str`<a id="status-str"></a>

##### system: `bool`<a id="system-bool"></a>

##### type: `str`<a id="type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PolicyRule`](./okta_python_sdk/type/policy_rule.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PolicyRule`](./okta_python_sdk/pydantic/policy_rule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies/{policyId}/rules` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.deactivate_lifecycle`<a id="oktapolicydeactivate_lifecycle"></a>

Deactivates a policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.policy.deactivate_lifecycle(
    policy_id="policyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies/{policyId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.deactivate_rule_lifecycle`<a id="oktapolicydeactivate_rule_lifecycle"></a>

Deactivates a policy rule.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.policy.deactivate_rule_lifecycle(
    policy_id="policyId_example",
    rule_id="ruleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies/{policyId}/rules/{ruleId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.enumerate_rules`<a id="oktapolicyenumerate_rules"></a>

Enumerates all policy rules.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enumerate_rules_response = okta.policy.enumerate_rules(
    policy_id="policyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PolicyEnumerateRulesResponse`](./okta_python_sdk/pydantic/policy_enumerate_rules_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies/{policyId}/rules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.get_all_with_type`<a id="oktapolicyget_all_with_type"></a>

Gets all policies with the specified type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_with_type_response = okta.policy.get_all_with_type(
    type="type_example",
    status="string_example",
    expand="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### status: `str`<a id="status-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PolicyGetAllWithTypeResponse`](./okta_python_sdk/pydantic/policy_get_all_with_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.get_policy`<a id="oktapolicyget_policy"></a>

Gets a policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policy_response = okta.policy.get_policy(
    policy_id="policyId_example",
    expand="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Policy`](./okta_python_sdk/pydantic/policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies/{policyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.get_policy_rule`<a id="oktapolicyget_policy_rule"></a>

Gets a policy rule.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policy_rule_response = okta.policy.get_policy_rule(
    policy_id="policyId_example",
    rule_id="ruleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PolicyRule`](./okta_python_sdk/pydantic/policy_rule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies/{policyId}/rules/{ruleId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.remove_policy_operation`<a id="oktapolicyremove_policy_operation"></a>

Removes a policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.policy.remove_policy_operation(
    policy_id="policyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies/{policyId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.remove_rule`<a id="oktapolicyremove_rule"></a>

Removes a policy rule.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.policy.remove_rule(
    policy_id="policyId_example",
    rule_id="ruleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies/{policyId}/rules/{ruleId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.update_operation`<a id="oktapolicyupdate_operation"></a>

Updates a policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_operation_response = okta.policy.update_operation(
    policy_id="policyId_example",
    description="string_example",
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    conditions={
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    priority=1,
    status="ACTIVE",
    system=True,
    type="OAUTH_AUTHORIZATION_POLICY",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### description: `str`<a id="description-str"></a>

##### embedded: [`PolicyEmbedded`](./okta_python_sdk/type/policy_embedded.py)<a id="embedded-policyembeddedokta_python_sdktypepolicy_embeddedpy"></a>

##### links: [`PolicyLinks`](./okta_python_sdk/type/policy_links.py)<a id="links-policylinksokta_python_sdktypepolicy_linkspy"></a>

##### conditions: [`PolicyRuleConditions`](./okta_python_sdk/type/policy_rule_conditions.py)<a id="conditions-policyruleconditionsokta_python_sdktypepolicy_rule_conditionspy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### priority: `int`<a id="priority-int"></a>

##### status: `str`<a id="status-str"></a>

##### system: `bool`<a id="system-bool"></a>

##### type: [`PolicyType`](./okta_python_sdk/type/policy_type.py)<a id="type-policytypeokta_python_sdktypepolicy_typepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Policy`](./okta_python_sdk/type/policy.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Policy`](./okta_python_sdk/pydantic/policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies/{policyId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.policy.update_rule`<a id="oktapolicyupdate_rule"></a>

Updates a policy rule.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_rule_response = okta.policy.update_rule(
    policy_id="policyId_example",
    rule_id="ruleId_example",
    actions={
    },
    conditions={
    },
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    priority=1,
    status="ACTIVE",
    system=False,
    type="SIGN_ON",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

##### actions: [`PolicyRuleActions`](./okta_python_sdk/type/policy_rule_actions.py)<a id="actions-policyruleactionsokta_python_sdktypepolicy_rule_actionspy"></a>


##### conditions: [`PolicyRuleConditions`](./okta_python_sdk/type/policy_rule_conditions.py)<a id="conditions-policyruleconditionsokta_python_sdktypepolicy_rule_conditionspy"></a>


##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### priority: `int`<a id="priority-int"></a>

##### status: `str`<a id="status-str"></a>

##### system: `bool`<a id="system-bool"></a>

##### type: `str`<a id="type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PolicyRule`](./okta_python_sdk/type/policy_rule.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PolicyRule`](./okta_python_sdk/pydantic/policy_rule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/policies/{policyId}/rules/{ruleId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.profile_mapping.get_by_id`<a id="oktaprofile_mappingget_by_id"></a>

Fetches a single Profile Mapping referenced by its ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = okta.profile_mapping.get_by_id(
    mapping_id="mappingId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### mapping_id: `str`<a id="mapping_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileMapping`](./okta_python_sdk/pydantic/profile_mapping.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/mappings/{mappingId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.profile_mapping.list_with_pagination`<a id="oktaprofile_mappinglist_with_pagination"></a>

Enumerates Profile Mappings in your organization with pagination.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_with_pagination_response = okta.profile_mapping.list_with_pagination(
    after="string_example",
    limit=-1,
    source_id="string_example",
    target_id="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### source_id: `str`<a id="source_id-str"></a>

##### target_id: `str`<a id="target_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileMappingListWithPaginationResponse`](./okta_python_sdk/pydantic/profile_mapping_list_with_pagination_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/mappings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.profile_mapping.update_property_mappings`<a id="oktaprofile_mappingupdate_property_mappings"></a>

Updates an existing Profile Mapping by adding, updating, or removing one or many Property Mappings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_property_mappings_response = okta.profile_mapping.update_property_mappings(
    mapping_id="mappingId_example",
    links={
        "key": {},
    },
    id="string_example",
    properties={
        "key": {
        },
    },
    source={
    },
    target={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### mapping_id: `str`<a id="mapping_id-str"></a>

##### links: [`ProfileMappingLinks`](./okta_python_sdk/type/profile_mapping_links.py)<a id="links-profilemappinglinksokta_python_sdktypeprofile_mapping_linkspy"></a>

##### id: `str`<a id="id-str"></a>

##### properties: [`ProfileMappingProperties`](./okta_python_sdk/type/profile_mapping_properties.py)<a id="properties-profilemappingpropertiesokta_python_sdktypeprofile_mapping_propertiespy"></a>

##### source: [`ProfileMappingSource`](./okta_python_sdk/type/profile_mapping_source.py)<a id="source-profilemappingsourceokta_python_sdktypeprofile_mapping_sourcepy"></a>


##### target: [`ProfileMappingSource`](./okta_python_sdk/type/profile_mapping_source.py)<a id="target-profilemappingsourceokta_python_sdktypeprofile_mapping_sourcepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProfileMapping`](./okta_python_sdk/type/profile_mapping.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProfileMapping`](./okta_python_sdk/pydantic/profile_mapping.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/mappings/{mappingId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.session.close`<a id="oktasessionclose"></a>

Close Session

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.session.close(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/sessions/{sessionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.session.create_session_with_token`<a id="oktasessioncreate_session_with_token"></a>

Creates a new session for a user with a valid session token. Use this API if, for example, you want to set the session cookie yourself instead of allowing Okta to set it, or want to hold the session ID in order to delete a session via the API instead of visiting the logout URL.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_session_with_token_response = okta.session.create_session_with_token(
    session_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_token: `str`<a id="session_token-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateSessionRequest`](./okta_python_sdk/type/create_session_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./okta_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/sessions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.session.get_details`<a id="oktasessionget_details"></a>

Get details about a session.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = okta.session.get_details(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./okta_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/sessions/{sessionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.session.refresh_lifecycle`<a id="oktasessionrefresh_lifecycle"></a>

Refresh Session

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
refresh_lifecycle_response = okta.session.refresh_lifecycle(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./okta_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/sessions/{sessionId}/lifecycle/refresh` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.subscription.custom_role_notification_unsubscribe`<a id="oktasubscriptioncustom_role_notification_unsubscribe"></a>

When roleType Unsubscribes a Role from a specific notification type. When you change the subscription status of a Role, it overrides the subscription of any individual user of that Role. Else when roleId Unsubscribes a Custom Role from a specific notification type. When you change the subscription status of a Custom Role, it overrides the subscription of any individual user of that Custom Role.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.subscription.custom_role_notification_unsubscribe(
    role_type_or_role_id="roleTypeOrRoleId_example",
    notification_type="notificationType_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### role_type_or_role_id: `str`<a id="role_type_or_role_id-str"></a>

##### notification_type: `str`<a id="notification_type-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/roles/{roleTypeOrRoleId}/subscriptions/{notificationType}/unsubscribe` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.subscription.get_role_subscriptions_by_notification_type`<a id="oktasubscriptionget_role_subscriptions_by_notification_type"></a>

When roleType Get subscriptions of a Role with a specific notification type. Else when roleId Get subscription of a Custom Role with a specific notification type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_role_subscriptions_by_notification_type_response = okta.subscription.get_role_subscriptions_by_notification_type(
    role_type_or_role_id="roleTypeOrRoleId_example",
    notification_type="notificationType_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### role_type_or_role_id: `str`<a id="role_type_or_role_id-str"></a>

##### notification_type: `str`<a id="notification_type-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Subscription`](./okta_python_sdk/pydantic/subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/roles/{roleTypeOrRoleId}/subscriptions/{notificationType}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.subscription.list_role_subscriptions`<a id="oktasubscriptionlist_role_subscriptions"></a>

When roleType List all subscriptions of a Role. Else when roleId List subscriptions of a Custom Role

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_role_subscriptions_response = okta.subscription.list_role_subscriptions(
    role_type_or_role_id="roleTypeOrRoleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### role_type_or_role_id: `str`<a id="role_type_or_role_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SubscriptionListRoleSubscriptionsResponse`](./okta_python_sdk/pydantic/subscription_list_role_subscriptions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/roles/{roleTypeOrRoleId}/subscriptions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.subscription.role_notification_subscribe`<a id="oktasubscriptionrole_notification_subscribe"></a>

When roleType Subscribes a Role to a specific notification type. When you change the subscription status of a Role, it overrides the subscription of any individual user of that Role. Else when roleId Subscribes a Custom Role to a specific notification type. When you change the subscription status of a Custom Role, it overrides the subscription of any individual user of that Custom Role.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.subscription.role_notification_subscribe(
    role_type_or_role_id="roleTypeOrRoleId_example",
    notification_type="notificationType_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### role_type_or_role_id: `str`<a id="role_type_or_role_id-str"></a>

##### notification_type: `str`<a id="notification_type-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/roles/{roleTypeOrRoleId}/subscriptions/{notificationType}/subscribe` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.subscription.unsubscribe_user_subscription_by_notification_type`<a id="oktasubscriptionunsubscribe_user_subscription_by_notification_type"></a>

Unsubscribes a User from a specific notification type. Only the current User can unsubscribe from a specific notification type. An AccessDeniedException message is sent if requests are made from other users.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.subscription.unsubscribe_user_subscription_by_notification_type(
    user_id="userId_example",
    notification_type="notificationType_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### notification_type: `str`<a id="notification_type-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/subscriptions/{notificationType}/unsubscribe` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.subscription.user_notification_subscribe`<a id="oktasubscriptionuser_notification_subscribe"></a>

Subscribes a User to a specific notification type. Only the current User can subscribe to a specific notification type. An AccessDeniedException message is sent if requests are made from other users.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.subscription.user_notification_subscribe(
    user_id="userId_example",
    notification_type="notificationType_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### notification_type: `str`<a id="notification_type-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/subscriptions/{notificationType}/subscribe` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.template.add_new_custom_sms`<a id="oktatemplateadd_new_custom_sms"></a>

Adds a new custom SMS template to your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_custom_sms_response = okta.template.add_new_custom_sms(
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    template="string_example",
    translations={},
    type="SMS_VERIFY_CODE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### template: `str`<a id="template-str"></a>

##### translations: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="translations-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### type: [`SmsTemplateType`](./okta_python_sdk/type/sms_template_type.py)<a id="type-smstemplatetypeokta_python_sdktypesms_template_typepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SmsTemplate`](./okta_python_sdk/type/sms_template.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SmsTemplate`](./okta_python_sdk/pydantic/sms_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/templates/sms` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.template.enumerate_sms_templates`<a id="oktatemplateenumerate_sms_templates"></a>

Enumerates custom SMS templates in your organization. A subset of templates can be returned that match a template type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enumerate_sms_templates_response = okta.template.enumerate_sms_templates(
    template_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_type: `str`<a id="template_type-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TemplateEnumerateSmsTemplatesResponse`](./okta_python_sdk/pydantic/template_enumerate_sms_templates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/templates/sms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.template.get_by_id`<a id="oktatemplateget_by_id"></a>

Fetches a specific template by `id`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = okta.template.get_by_id(
    template_id="templateId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SmsTemplate`](./okta_python_sdk/pydantic/sms_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/templates/sms/{templateId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.template.partial_sms_update`<a id="oktatemplatepartial_sms_update"></a>

Updates only some of the SMS template properties:

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
partial_sms_update_response = okta.template.partial_sms_update(
    template_id="templateId_example",
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    template="string_example",
    translations={},
    type="SMS_VERIFY_CODE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### template: `str`<a id="template-str"></a>

##### translations: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="translations-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### type: [`SmsTemplateType`](./okta_python_sdk/type/sms_template_type.py)<a id="type-smstemplatetypeokta_python_sdktypesms_template_typepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SmsTemplate`](./okta_python_sdk/type/sms_template.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SmsTemplate`](./okta_python_sdk/pydantic/sms_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/templates/sms/{templateId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.template.remove_sms`<a id="oktatemplateremove_sms"></a>

Removes an SMS template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.template.remove_sms(
    template_id="templateId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/templates/sms/{templateId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.template.update_sms_template`<a id="oktatemplateupdate_sms_template"></a>

Updates the SMS template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_sms_template_response = okta.template.update_sms_template(
    template_id="templateId_example",
    created="1970-01-01T00:00:00.00Z",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    name="string_example",
    template="string_example",
    translations={},
    type="SMS_VERIFY_CODE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### name: `str`<a id="name-str"></a>

##### template: `str`<a id="template-str"></a>

##### translations: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="translations-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### type: [`SmsTemplateType`](./okta_python_sdk/type/sms_template_type.py)<a id="type-smstemplatetypeokta_python_sdktypesms_template_typepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SmsTemplate`](./okta_python_sdk/type/sms_template.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SmsTemplate`](./okta_python_sdk/pydantic/sms_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/templates/sms/{templateId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.threat_insight.get_current_configuration`<a id="oktathreat_insightget_current_configuration"></a>

Gets current ThreatInsight configuration

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_configuration_response = okta.threat_insight.get_current_configuration()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ThreatInsightConfiguration`](./okta_python_sdk/pydantic/threat_insight_configuration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/threats/configuration` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.threat_insight.update_configuration`<a id="oktathreat_insightupdate_configuration"></a>

Updates ThreatInsight configuration

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_configuration_response = okta.threat_insight.update_configuration(
    body=None,
    links={
        "key": {},
    },
    action="string_example",
    created="1970-01-01T00:00:00.00Z",
    exclude_zones=[
        "string_example"
    ],
    last_updated="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### links: `Dict[str, Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`<a id="links-dictstr-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### action: `str`<a id="action-str"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### exclude_zones: List[`str`]<a id="exclude_zones-liststr"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ThreatInsightConfiguration`](./okta_python_sdk/type/threat_insight_configuration.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ThreatInsightConfiguration`](./okta_python_sdk/pydantic/threat_insight_configuration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/threats/configuration` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.trusted_origin.activate_lifecycle_success`<a id="oktatrusted_originactivate_lifecycle_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_lifecycle_success_response = okta.trusted_origin.activate_lifecycle_success(
    trusted_origin_id="trustedOriginId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### trusted_origin_id: `str`<a id="trusted_origin_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TrustedOrigin`](./okta_python_sdk/pydantic/trusted_origin.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/trustedOrigins/{trustedOriginId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.trusted_origin.create_success`<a id="oktatrusted_origincreate_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_success_response = okta.trusted_origin.create_success(
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    created_by="string_example",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    last_updated_by="string_example",
    name="string_example",
    origin="string_example",
    scopes=[
        {
            "type": "CORS",
        }
    ],
    status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### links: [`TrustedOriginLinks`](./okta_python_sdk/type/trusted_origin_links.py)<a id="links-trustedoriginlinksokta_python_sdktypetrusted_origin_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### created_by: `str`<a id="created_by-str"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### last_updated_by: `str`<a id="last_updated_by-str"></a>

##### name: `str`<a id="name-str"></a>

##### origin: `str`<a id="origin-str"></a>

##### scopes: List[`Scope`]<a id="scopes-listscope"></a>

##### status: `str`<a id="status-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrustedOrigin`](./okta_python_sdk/type/trusted_origin.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TrustedOrigin`](./okta_python_sdk/pydantic/trusted_origin.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/trustedOrigins` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.trusted_origin.deactivate_lifecycle_success`<a id="oktatrusted_origindeactivate_lifecycle_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deactivate_lifecycle_success_response = okta.trusted_origin.deactivate_lifecycle_success(
    trusted_origin_id="trustedOriginId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### trusted_origin_id: `str`<a id="trusted_origin_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TrustedOrigin`](./okta_python_sdk/pydantic/trusted_origin.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/trustedOrigins/{trustedOriginId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.trusted_origin.delete_success`<a id="oktatrusted_origindelete_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.trusted_origin.delete_success(
    trusted_origin_id="trustedOriginId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### trusted_origin_id: `str`<a id="trusted_origin_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/trustedOrigins/{trustedOriginId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.trusted_origin.get_list`<a id="oktatrusted_originget_list"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = okta.trusted_origin.get_list(
    q="string_example",
    filter="string_example",
    after="string_example",
    limit=-1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

##### filter: `str`<a id="filter-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TrustedOriginGetListResponse`](./okta_python_sdk/pydantic/trusted_origin_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/trustedOrigins` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.trusted_origin.get_success_by_id`<a id="oktatrusted_originget_success_by_id"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_success_by_id_response = okta.trusted_origin.get_success_by_id(
    trusted_origin_id="trustedOriginId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### trusted_origin_id: `str`<a id="trusted_origin_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TrustedOrigin`](./okta_python_sdk/pydantic/trusted_origin.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/trustedOrigins/{trustedOriginId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.trusted_origin.update_success`<a id="oktatrusted_originupdate_success"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_success_response = okta.trusted_origin.update_success(
    trusted_origin_id="trustedOriginId_example",
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    created_by="string_example",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    last_updated_by="string_example",
    name="string_example",
    origin="string_example",
    scopes=[
        {
            "type": "CORS",
        }
    ],
    status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### trusted_origin_id: `str`<a id="trusted_origin_id-str"></a>

##### links: [`TrustedOriginLinks`](./okta_python_sdk/type/trusted_origin_links.py)<a id="links-trustedoriginlinksokta_python_sdktypetrusted_origin_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### created_by: `str`<a id="created_by-str"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### last_updated_by: `str`<a id="last_updated_by-str"></a>

##### name: `str`<a id="name-str"></a>

##### origin: `str`<a id="origin-str"></a>

##### scopes: List[`Scope`]<a id="scopes-listscope"></a>

##### status: `str`<a id="status-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrustedOrigin`](./okta_python_sdk/type/trusted_origin.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TrustedOrigin`](./okta_python_sdk/pydantic/trusted_origin.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/trustedOrigins/{trustedOriginId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.activate_lifecycle`<a id="oktauseractivate_lifecycle"></a>

Activates a user.  This operation can only be performed on users with a `STAGED` status.  Activation of a user is an asynchronous operation. The user will have the `transitioningToStatus` property with a value of `ACTIVE` during activation to indicate that the user hasn't completed the asynchronous operation.  The user will have a status of `ACTIVE` when the activation process is complete.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_lifecycle_response = okta.user.activate_lifecycle(
    user_id="userId_example",
    send_email=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### send_email: `bool`<a id="send_email-bool"></a>

Sends an activation email to the user if true

#### 🔄 Return<a id="🔄-return"></a>

[`UserActivationToken`](./okta_python_sdk/pydantic/user_activation_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.add_app_instance_target_to_app_administrator_role_given_to_user`<a id="oktauseradd_app_instance_target_to_app_administrator_role_given_to_user"></a>

Add App Instance Target to App Administrator Role given to a User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.add_app_instance_target_to_app_administrator_role_given_to_user(
    user_id="userId_example",
    role_id="roleId_example",
    app_name="appName_example",
    application_id="applicationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### app_name: `str`<a id="app_name-str"></a>

##### application_id: `str`<a id="application_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.assign_role`<a id="oktauserassign_role"></a>

Assigns a role to a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_role_response = okta.user.assign_role(
    body=None,
    user_id="userId_example",
    type="SUPER_ADMIN",
    disable_notifications=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### type: [`RoleType`](./okta_python_sdk/type/role_type.py)<a id="type-roletypeokta_python_sdktyperole_typepy"></a>

##### disable_notifications: `bool`<a id="disable_notifications-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AssignRoleRequest`](./okta_python_sdk/type/assign_role_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Role`](./okta_python_sdk/pydantic/role.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/roles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.change_password_validation`<a id="oktauserchange_password_validation"></a>

Changes a user's password by validating the user's current password. This operation can only be performed on users in `STAGED`, `ACTIVE`, `PASSWORD_EXPIRED`, or `RECOVERY` status that have a valid password credential

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
change_password_validation_response = okta.user.change_password_validation(
    user_id="userId_example",
    new_password={
    },
    old_password={
    },
    strict=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### new_password: [`PasswordCredential`](./okta_python_sdk/type/password_credential.py)<a id="new_password-passwordcredentialokta_python_sdktypepassword_credentialpy"></a>


##### old_password: [`PasswordCredential`](./okta_python_sdk/type/password_credential.py)<a id="old_password-passwordcredentialokta_python_sdktypepassword_credentialpy"></a>


##### strict: `bool`<a id="strict-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangePasswordRequest`](./okta_python_sdk/type/change_password_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserCredentials`](./okta_python_sdk/pydantic/user_credentials.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/credentials/change_password` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.create_new_user`<a id="oktausercreate_new_user"></a>

Creates a new user in your Okta organization with or without credentials.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_user_response = okta.user.create_new_user(
    credentials={
    },
    group_ids=[
        "string_example"
    ],
    profile={
    },
    type={
    },
    activate=True,
    provider=False,
    next_login="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### credentials: [`UserCredentials`](./okta_python_sdk/type/user_credentials.py)<a id="credentials-usercredentialsokta_python_sdktypeuser_credentialspy"></a>


##### group_ids: [`CreateUserRequestGroupIds`](./okta_python_sdk/type/create_user_request_group_ids.py)<a id="group_ids-createuserrequestgroupidsokta_python_sdktypecreate_user_request_group_idspy"></a>

##### profile: [`UserProfile`](./okta_python_sdk/type/user_profile.py)<a id="profile-userprofileokta_python_sdktypeuser_profilepy"></a>


##### type: [`UserType`](./okta_python_sdk/type/user_type.py)<a id="type-usertypeokta_python_sdktypeuser_typepy"></a>


##### activate: `bool`<a id="activate-bool"></a>

Executes activation lifecycle operation when creating the user

##### provider: `bool`<a id="provider-bool"></a>

Indicates whether to create a user with a specified authentication provider

##### next_login: `str`<a id="next_login-str"></a>

With activate=true, set nextLogin to \"changePassword\" to have the password be EXPIRED, so user must change it the next time they log in.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateUserRequest`](./okta_python_sdk/type/create_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./okta_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.deactivate_lifecycle`<a id="oktauserdeactivate_lifecycle"></a>

Deactivates a user. This operation can only be performed on users that do not have a `DEPROVISIONED` status. While the asynchronous operation (triggered by HTTP header `Prefer: respond-async`) is proceeding the user's `transitioningToStatus` property is `DEPROVISIONED`. The user's status is `DEPROVISIONED` when the deactivation process is complete.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.deactivate_lifecycle(
    user_id="userId_example",
    send_email=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### send_email: `bool`<a id="send_email-bool"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/lifecycle/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.delete_linked_objects`<a id="oktauserdelete_linked_objects"></a>

Delete linked objects for a user, relationshipName can be ONLY a primary relationship name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.delete_linked_objects(
    user_id="userId_example",
    relationship_name="relationshipName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### relationship_name: `str`<a id="relationship_name-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/linkedObjects/{relationshipName}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.delete_permanently`<a id="oktauserdelete_permanently"></a>

Deletes a user permanently.  This operation can only be performed on users that have a `DEPROVISIONED` status.  **This action cannot be recovered!**

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.delete_permanently(
    user_id="userId_example",
    send_email=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### send_email: `bool`<a id="send_email-bool"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.delete_target_app`<a id="oktauserdelete_target_app"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.delete_target_app(
    user_id="userId_example",
    role_id="roleId_example",
    app_name="appName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### app_name: `str`<a id="app_name-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.expire_password_and_get_temporary_password`<a id="oktauserexpire_password_and_get_temporary_password"></a>

This operation transitions the user to the status of `PASSWORD_EXPIRED` so that the user is required to change their password at their next login.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
expire_password_and_get_temporary_password_response = okta.user.expire_password_and_get_temporary_password(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./okta_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/lifecycle/expire_password?tempPassword&#x3D;false` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.expire_password_and_temporary_password`<a id="oktauserexpire_password_and_temporary_password"></a>

This operation transitions the user to the status of `PASSWORD_EXPIRED` and the user's password is reset to a temporary password that is returned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
expire_password_and_temporary_password_response = okta.user.expire_password_and_temporary_password(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TempPassword`](./okta_python_sdk/pydantic/temp_password.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/lifecycle/expire_password?tempPassword&#x3D;true` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.forgot_password`<a id="oktauserforgot_password"></a>

Forgot Password

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
forgot_password_response = okta.user.forgot_password(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ForgotPasswordResponse`](./okta_python_sdk/pydantic/forgot_password_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/credentials/forgot_password` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.generate_password_reset_token`<a id="oktausergenerate_password_reset_token"></a>

Generates a one-time token (OTT) that can be used to reset a user's password.  The OTT link can be automatically emailed to the user or returned to the API caller and distributed using a custom flow.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_password_reset_token_response = okta.user.generate_password_reset_token(
    user_id="userId_example",
    send_email=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### send_email: `bool`<a id="send_email-bool"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ResetPasswordToken`](./okta_python_sdk/pydantic/reset_password_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/lifecycle/reset_password` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.get_assigned_role`<a id="oktauserget_assigned_role"></a>

Gets role that is assigne to user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_assigned_role_response = okta.user.get_assigned_role(
    user_id="userId_example",
    role_id="roleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Role`](./okta_python_sdk/pydantic/role.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/roles/{roleId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.get_client_refresh_token`<a id="oktauserget_client_refresh_token"></a>

Gets a refresh token issued for the specified User and Client.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_client_refresh_token_response = okta.user.get_client_refresh_token(
    user_id="userId_example",
    client_id="clientId_example",
    token_id="tokenId_example",
    expand="string_example",
    limit=20,
    after="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### token_id: `str`<a id="token_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### after: `str`<a id="after-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OAuth2RefreshToken`](./okta_python_sdk/pydantic/o_auth2_refresh_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/clients/{clientId}/tokens/{tokenId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.get_grant_by_id`<a id="oktauserget_grant_by_id"></a>

Gets a grant for the specified user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_grant_by_id_response = okta.user.get_grant_by_id(
    user_id="userId_example",
    grant_id="grantId_example",
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### grant_id: `str`<a id="grant_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OAuth2ScopeConsentGrant`](./okta_python_sdk/pydantic/o_auth2_scope_consent_grant.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/grants/{grantId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.get_linked_objects`<a id="oktauserget_linked_objects"></a>

Get linked objects for a user, relationshipName can be a primary or associated relationship name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_linked_objects_response = okta.user.get_linked_objects(
    user_id="userId_example",
    relationship_name="relationshipName_example",
    after="string_example",
    limit=-1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### relationship_name: `str`<a id="relationship_name-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserGetLinkedObjectsResponse`](./okta_python_sdk/pydantic/user_get_linked_objects_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/linkedObjects/{relationshipName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.get_member_groups`<a id="oktauserget_member_groups"></a>

Fetches the groups of which the user is a member.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_member_groups_response = okta.user.get_member_groups(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserGetMemberGroupsResponse`](./okta_python_sdk/pydantic/user_get_member_groups_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.get_okta_user`<a id="oktauserget_okta_user"></a>

Fetches a user from your Okta organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_okta_user_response = okta.user.get_okta_user(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./okta_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.get_subscription_by_notification`<a id="oktauserget_subscription_by_notification"></a>

Get the subscriptions of a User with a specific notification type. Only gets subscriptions for current user. An AccessDeniedException message is sent if requests are made from other users.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_subscription_by_notification_response = okta.user.get_subscription_by_notification(
    user_id="userId_example",
    notification_type="notificationType_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### notification_type: `str`<a id="notification_type-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Subscription`](./okta_python_sdk/pydantic/subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/subscriptions/{notificationType}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.list_active_users`<a id="oktauserlist_active_users"></a>

Lists users that do not have a status of 'DEPROVISIONED' (by default), up to the maximum (200 for most orgs), with pagination in most cases. A subset of users can be returned that match a supported filter expression or search criteria.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_active_users_response = okta.user.list_active_users(
    q="string_example",
    after="string_example",
    limit=10,
    filter="string_example",
    search="string_example",
    sort_by="string_example",
    sort_order="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

Finds a user that matches firstName, lastName, and email properties

##### after: `str`<a id="after-str"></a>

Specifies the pagination cursor for the next page of users

##### limit: `int`<a id="limit-int"></a>

Specifies the number of results returned

##### filter: `str`<a id="filter-str"></a>

Filters users with a supported expression for a subset of properties

##### search: `str`<a id="search-str"></a>

Searches for users with a supported filtering  expression for most properties

##### sort_by: `str`<a id="sort_by-str"></a>

##### sort_order: `str`<a id="sort_order-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserListActiveUsersResponse`](./okta_python_sdk/pydantic/user_list_active_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.list_app_targets_for_role`<a id="oktauserlist_app_targets_for_role"></a>

Lists all App targets for an `APP_ADMIN` Role assigned to a User. This methods return list may include full Applications or Instances. The response for an instance will have an `ID` value, while Application will not have an ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_app_targets_for_role_response = okta.user.list_app_targets_for_role(
    user_id="userId_example",
    role_id="roleId_example",
    after="string_example",
    limit=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserListAppTargetsForRoleResponse`](./okta_python_sdk/pydantic/user_list_app_targets_for_role_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.list_assigned_app_links`<a id="oktauserlist_assigned_app_links"></a>

Fetches appLinks for all direct or indirect (via group membership) assigned applications.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_assigned_app_links_response = okta.user.list_assigned_app_links(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserListAssignedAppLinksResponse`](./okta_python_sdk/pydantic/user_list_assigned_app_links_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/appLinks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.list_assigned_roles`<a id="oktauserlist_assigned_roles"></a>

Lists all roles assigned to a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_assigned_roles_response = okta.user.list_assigned_roles(
    user_id="userId_example",
    expand="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserListAssignedRolesResponse`](./okta_python_sdk/pydantic/user_list_assigned_roles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/roles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.list_clients`<a id="oktauserlist_clients"></a>

Lists all client resources for which the specified user has grants or tokens.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_clients_response = okta.user.list_clients(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserListClientsResponse`](./okta_python_sdk/pydantic/user_list_clients_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/clients` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.list_grants`<a id="oktauserlist_grants"></a>

Lists all grants for the specified user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_grants_response = okta.user.list_grants(
    user_id="userId_example",
    scope_id="string_example",
    expand="string_example",
    after="string_example",
    limit=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### scope_id: `str`<a id="scope_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserListGrantsResponse`](./okta_python_sdk/pydantic/user_list_grants_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/grants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.list_grants_for_client`<a id="oktauserlist_grants_for_client"></a>

Lists all grants for a specified user and client

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_grants_for_client_response = okta.user.list_grants_for_client(
    user_id="userId_example",
    client_id="clientId_example",
    expand="string_example",
    after="string_example",
    limit=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserListGrantsForClientResponse`](./okta_python_sdk/pydantic/user_list_grants_for_client_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/clients/{clientId}/grants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.list_idps_for_user`<a id="oktauserlist_idps_for_user"></a>

Lists the IdPs associated with the user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_idps_for_user_response = okta.user.list_idps_for_user(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserListIdpsForUserResponse`](./okta_python_sdk/pydantic/user_list_idps_for_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/idps` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.list_refresh_tokens_for_user_and_client`<a id="oktauserlist_refresh_tokens_for_user_and_client"></a>

Lists all refresh tokens issued for the specified User and Client.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_refresh_tokens_for_user_and_client_response = okta.user.list_refresh_tokens_for_user_and_client(
    user_id="userId_example",
    client_id="clientId_example",
    expand="string_example",
    after="string_example",
    limit=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### expand: `str`<a id="expand-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserListRefreshTokensForUserAndClientResponse`](./okta_python_sdk/pydantic/user_list_refresh_tokens_for_user_and_client_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/clients/{clientId}/tokens` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.list_role_targets_groups`<a id="oktauserlist_role_targets_groups"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_role_targets_groups_response = okta.user.list_role_targets_groups(
    user_id="userId_example",
    role_id="roleId_example",
    after="string_example",
    limit=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### after: `str`<a id="after-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserListRoleTargetsGroupsResponse`](./okta_python_sdk/pydantic/user_list_role_targets_groups_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/roles/{roleId}/targets/groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.list_subscriptions`<a id="oktauserlist_subscriptions"></a>

List subscriptions of a User. Only lists subscriptions for current user. An AccessDeniedException message is sent if requests are made from other users.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_subscriptions_response = okta.user.list_subscriptions(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserListSubscriptionsResponse`](./okta_python_sdk/pydantic/user_list_subscriptions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/subscriptions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.reactivate_user`<a id="oktauserreactivate_user"></a>

Reactivates a user.  This operation can only be performed on users with a `PROVISIONED` status.  This operation restarts the activation workflow if for some reason the user activation was not completed when using the activationToken from [Activate User](https://raw.githubusercontent.com).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
reactivate_user_response = okta.user.reactivate_user(
    user_id="userId_example",
    send_email=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### send_email: `bool`<a id="send_email-bool"></a>

Sends an activation email to the user if true

#### 🔄 Return<a id="🔄-return"></a>

[`UserActivationToken`](./okta_python_sdk/pydantic/user_activation_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/lifecycle/reactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.remove_app_instance_target_to_app_administrator_role_given_to`<a id="oktauserremove_app_instance_target_to_app_administrator_role_given_to"></a>

Remove App Instance Target to App Administrator Role given to a User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.remove_app_instance_target_to_app_administrator_role_given_to(
    user_id="userId_example",
    role_id="roleId_example",
    app_name="appName_example",
    application_id="applicationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### app_name: `str`<a id="app_name-str"></a>

##### application_id: `str`<a id="application_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.remove_target_group`<a id="oktauserremove_target_group"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.remove_target_group(
    user_id="userId_example",
    role_id="roleId_example",
    group_id="groupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/roles/{roleId}/targets/groups/{groupId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.reset_factors_operation`<a id="oktauserreset_factors_operation"></a>

This operation resets all factors for the specified user. All MFA factor enrollments returned to the unenrolled state. The user's status remains ACTIVE. This link is present only if the user is currently enrolled in one or more MFA factors.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.reset_factors_operation(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/lifecycle/reset_factors` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.revoke_all_sessions`<a id="oktauserrevoke_all_sessions"></a>

Removes all active identity provider sessions. This forces the user to authenticate on the next operation. Optionally revokes OpenID Connect and OAuth refresh and access tokens issued to the user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.revoke_all_sessions(
    user_id="userId_example",
    oauth_tokens=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### oauth_tokens: `bool`<a id="oauth_tokens-bool"></a>

Revoke issued OpenID Connect and OAuth refresh and access tokens

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/sessions` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.revoke_all_tokens`<a id="oktauserrevoke_all_tokens"></a>

Revokes all refresh tokens issued for the specified User and Client.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.revoke_all_tokens(
    user_id="userId_example",
    client_id="clientId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### client_id: `str`<a id="client_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/clients/{clientId}/tokens` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.revoke_grant`<a id="oktauserrevoke_grant"></a>

Revokes one grant for a specified user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.revoke_grant(
    user_id="userId_example",
    grant_id="grantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### grant_id: `str`<a id="grant_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/grants/{grantId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.revoke_grants`<a id="oktauserrevoke_grants"></a>

Revokes all grants for a specified user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.revoke_grants(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/grants` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.revoke_grants_for_user_and_client`<a id="oktauserrevoke_grants_for_user_and_client"></a>

Revokes all grants for the specified user and client

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.revoke_grants_for_user_and_client(
    user_id="userId_example",
    client_id="clientId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### client_id: `str`<a id="client_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/clients/{clientId}/grants` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.revoke_token_for_client`<a id="oktauserrevoke_token_for_client"></a>

Revokes the specified refresh token.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.revoke_token_for_client(
    user_id="userId_example",
    client_id="clientId_example",
    token_id="tokenId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### token_id: `str`<a id="token_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/clients/{clientId}/tokens/{tokenId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.suspend_lifecycle`<a id="oktausersuspend_lifecycle"></a>

Suspends a user.  This operation can only be performed on users with an `ACTIVE` status.  The user will have a status of `SUSPENDED` when the process is complete.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.suspend_lifecycle(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/lifecycle/suspend` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.unassign_role`<a id="oktauserunassign_role"></a>

Unassigns a role from a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.unassign_role(
    user_id="userId_example",
    role_id="roleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/roles/{roleId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.unlock_user_status`<a id="oktauserunlock_user_status"></a>

Unlocks a user with a `LOCKED_OUT` status and returns them to `ACTIVE` status.  Users will be able to login with their current password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.unlock_user_status(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/lifecycle/unlock` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.unsuspend_lifecycle`<a id="oktauserunsuspend_lifecycle"></a>

Unsuspends a user and returns them to the `ACTIVE` state.  This operation can only be performed on users that have a `SUSPENDED` status.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.unsuspend_lifecycle(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/lifecycle/unsuspend` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.update_linked_object`<a id="oktauserupdate_linked_object"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.update_linked_object(
    associated_user_id="associatedUserId_example",
    primary_relationship_name="primaryRelationshipName_example",
    primary_user_id="primaryUserId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### associated_user_id: `str`<a id="associated_user_id-str"></a>

##### primary_relationship_name: `str`<a id="primary_relationship_name-str"></a>

##### primary_user_id: `str`<a id="primary_user_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{associatedUserId}/linkedObjects/{primaryRelationshipName}/{primaryUserId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.update_profile`<a id="oktauserupdate_profile"></a>

Update a user's profile and/or credentials using strict-update semantics.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_profile_response = okta.user.update_profile(
    user_id="userId_example",
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    activated="1970-01-01T00:00:00.00Z",
    created="1970-01-01T00:00:00.00Z",
    credentials={
    },
    id="string_example",
    last_login="1970-01-01T00:00:00.00Z",
    last_updated="1970-01-01T00:00:00.00Z",
    password_changed="1970-01-01T00:00:00.00Z",
    profile={
    },
    status="ACTIVE",
    status_changed="1970-01-01T00:00:00.00Z",
    transitioning_to_status="ACTIVE",
    type={
    },
    strict=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### embedded: [`UserEmbedded`](./okta_python_sdk/type/user_embedded.py)<a id="embedded-userembeddedokta_python_sdktypeuser_embeddedpy"></a>

##### links: [`UserLinks`](./okta_python_sdk/type/user_links.py)<a id="links-userlinksokta_python_sdktypeuser_linkspy"></a>

##### activated: `datetime`<a id="activated-datetime"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### credentials: [`UserCredentials`](./okta_python_sdk/type/user_credentials.py)<a id="credentials-usercredentialsokta_python_sdktypeuser_credentialspy"></a>


##### id: `str`<a id="id-str"></a>

##### last_login: `datetime`<a id="last_login-datetime"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### password_changed: `datetime`<a id="password_changed-datetime"></a>

##### profile: [`UserProfile`](./okta_python_sdk/type/user_profile.py)<a id="profile-userprofileokta_python_sdktypeuser_profilepy"></a>


##### status: [`UserStatus`](./okta_python_sdk/type/user_status.py)<a id="status-userstatusokta_python_sdktypeuser_statuspy"></a>

##### status_changed: `datetime`<a id="status_changed-datetime"></a>

##### transitioning_to_status: [`UserStatus`](./okta_python_sdk/type/user_status.py)<a id="transitioning_to_status-userstatusokta_python_sdktypeuser_statuspy"></a>

##### type: [`UserType`](./okta_python_sdk/type/user_type.py)<a id="type-usertypeokta_python_sdktypeuser_typepy"></a>


##### strict: `bool`<a id="strict-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`User`](./okta_python_sdk/type/user.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./okta_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.update_profile_0`<a id="oktauserupdate_profile_0"></a>

Update a user's profile or credentials with partial update semantics.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_profile_0_response = okta.user.update_profile_0(
    user_id="userId_example",
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    activated="1970-01-01T00:00:00.00Z",
    created="1970-01-01T00:00:00.00Z",
    credentials={
    },
    id="string_example",
    last_login="1970-01-01T00:00:00.00Z",
    last_updated="1970-01-01T00:00:00.00Z",
    password_changed="1970-01-01T00:00:00.00Z",
    profile={
    },
    status="ACTIVE",
    status_changed="1970-01-01T00:00:00.00Z",
    transitioning_to_status="ACTIVE",
    type={
    },
    strict=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### embedded: [`UserEmbedded`](./okta_python_sdk/type/user_embedded.py)<a id="embedded-userembeddedokta_python_sdktypeuser_embeddedpy"></a>

##### links: [`UserLinks`](./okta_python_sdk/type/user_links.py)<a id="links-userlinksokta_python_sdktypeuser_linkspy"></a>

##### activated: `datetime`<a id="activated-datetime"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### credentials: [`UserCredentials`](./okta_python_sdk/type/user_credentials.py)<a id="credentials-usercredentialsokta_python_sdktypeuser_credentialspy"></a>


##### id: `str`<a id="id-str"></a>

##### last_login: `datetime`<a id="last_login-datetime"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### password_changed: `datetime`<a id="password_changed-datetime"></a>

##### profile: [`UserProfile`](./okta_python_sdk/type/user_profile.py)<a id="profile-userprofileokta_python_sdktypeuser_profilepy"></a>


##### status: [`UserStatus`](./okta_python_sdk/type/user_status.py)<a id="status-userstatusokta_python_sdktypeuser_statuspy"></a>

##### status_changed: `datetime`<a id="status_changed-datetime"></a>

##### transitioning_to_status: [`UserStatus`](./okta_python_sdk/type/user_status.py)<a id="transitioning_to_status-userstatusokta_python_sdktypeuser_statuspy"></a>

##### type: [`UserType`](./okta_python_sdk/type/user_type.py)<a id="type-usertypeokta_python_sdktypeuser_typepy"></a>


##### strict: `bool`<a id="strict-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`User`](./okta_python_sdk/type/user.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./okta_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.update_recovery_question`<a id="oktauserupdate_recovery_question"></a>

Changes a user's recovery question & answer credential by validating the user's current password.  This operation can only be performed on users in **STAGED**, **ACTIVE** or **RECOVERY** `status` that have a valid password credential

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_recovery_question_response = okta.user.update_recovery_question(
    user_id="userId_example",
    password={
    },
    provider={
        "type": "ACTIVE_DIRECTORY",
    },
    recovery_question={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### password: [`PasswordCredential`](./okta_python_sdk/type/password_credential.py)<a id="password-passwordcredentialokta_python_sdktypepassword_credentialpy"></a>


##### provider: [`AuthenticationProvider`](./okta_python_sdk/type/authentication_provider.py)<a id="provider-authenticationproviderokta_python_sdktypeauthentication_providerpy"></a>


##### recovery_question: [`RecoveryQuestionCredential`](./okta_python_sdk/type/recovery_question_credential.py)<a id="recovery_question-recoveryquestioncredentialokta_python_sdktyperecovery_question_credentialpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserCredentials`](./okta_python_sdk/type/user_credentials.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserCredentials`](./okta_python_sdk/pydantic/user_credentials.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/credentials/change_recovery_question` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.update_roles_catalog_apps`<a id="oktauserupdate_roles_catalog_apps"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.update_roles_catalog_apps(
    user_id="userId_example",
    role_id="roleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.update_roles_catalog_apps_0`<a id="oktauserupdate_roles_catalog_apps_0"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.update_roles_catalog_apps_0(
    user_id="userId_example",
    role_id="roleId_example",
    app_name="appName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### app_name: `str`<a id="app_name-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user.update_roles_catalog_apps_1`<a id="oktauserupdate_roles_catalog_apps_1"></a>

Success

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user.update_roles_catalog_apps_1(
    user_id="userId_example",
    role_id="roleId_example",
    group_id="groupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/roles/{roleId}/targets/groups/{groupId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_factor.activate_factor_lifecycle`<a id="oktauser_factoractivate_factor_lifecycle"></a>

The `sms` and `token:software:totp` factor types require activation to complete the enrollment process.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_factor_lifecycle_response = okta.user_factor.activate_factor_lifecycle(
    body=None,
    user_id="userId_example",
    factor_id="factorId_example",
    attestation="string_example",
    client_data="string_example",
    pass_code="string_example",
    registration_data="string_example",
    state_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### factor_id: `str`<a id="factor_id-str"></a>

##### attestation: `str`<a id="attestation-str"></a>

##### client_data: `str`<a id="client_data-str"></a>

##### pass_code: `str`<a id="pass_code-str"></a>

##### registration_data: `str`<a id="registration_data-str"></a>

##### state_token: `str`<a id="state_token-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ActivateFactorRequest`](./okta_python_sdk/type/activate_factor_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserFactor`](./okta_python_sdk/pydantic/user_factor.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/factors/{factorId}/lifecycle/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_factor.enroll_supported_factor`<a id="oktauser_factorenroll_supported_factor"></a>

Enrolls a user with a supported factor.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enroll_supported_factor_response = okta.user_factor.enroll_supported_factor(
    user_id="userId_example",
    embedded={
        "key": {},
    },
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    factor_type="call",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    provider="OKTA",
    status="PENDING_ACTIVATION",
    verify=None,
    update_phone=False,
    template_id="string_example",
    token_lifetime_seconds=300,
    activate=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### embedded: [`UserFactorEmbedded`](./okta_python_sdk/type/user_factor_embedded.py)<a id="embedded-userfactorembeddedokta_python_sdktypeuser_factor_embeddedpy"></a>

##### links: [`UserFactorLinks`](./okta_python_sdk/type/user_factor_links.py)<a id="links-userfactorlinksokta_python_sdktypeuser_factor_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### factor_type: [`FactorType`](./okta_python_sdk/type/factor_type.py)<a id="factor_type-factortypeokta_python_sdktypefactor_typepy"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### provider: [`FactorProvider`](./okta_python_sdk/type/factor_provider.py)<a id="provider-factorproviderokta_python_sdktypefactor_providerpy"></a>

##### status: [`FactorStatus`](./okta_python_sdk/type/factor_status.py)<a id="status-factorstatusokta_python_sdktypefactor_statuspy"></a>

##### verify: [`VerifyFactorRequest`](./okta_python_sdk/type/verify_factor_request.py)<a id="verify-verifyfactorrequestokta_python_sdktypeverify_factor_requestpy"></a>


##### update_phone: `bool`<a id="update_phone-bool"></a>

##### template_id: `str`<a id="template_id-str"></a>

id of SMS template (only for SMS factor)

##### token_lifetime_seconds: `int`<a id="token_lifetime_seconds-int"></a>

##### activate: `bool`<a id="activate-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserFactor`](./okta_python_sdk/type/user_factor.py)
Factor

#### 🔄 Return<a id="🔄-return"></a>

[`UserFactor`](./okta_python_sdk/pydantic/user_factor.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/factors` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_factor.enumerate_enrolled`<a id="oktauser_factorenumerate_enrolled"></a>

Enumerates all the enrolled factors for the specified user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enumerate_enrolled_response = okta.user_factor.enumerate_enrolled(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserFactorEnumerateEnrolledResponse`](./okta_python_sdk/pydantic/user_factor_enumerate_enrolled_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/factors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_factor.enumerate_security_questions`<a id="oktauser_factorenumerate_security_questions"></a>

Enumerates all available security questions for a user's `question` factor

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enumerate_security_questions_response = okta.user_factor.enumerate_security_questions(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserFactorEnumerateSecurityQuestionsResponse`](./okta_python_sdk/pydantic/user_factor_enumerate_security_questions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/factors/questions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_factor.enumerate_supported_factors`<a id="oktauser_factorenumerate_supported_factors"></a>

Enumerates all the supported factors that can be enrolled for the specified user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enumerate_supported_factors_response = okta.user_factor.enumerate_supported_factors(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserFactorEnumerateSupportedFactorsResponse`](./okta_python_sdk/pydantic/user_factor_enumerate_supported_factors_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/factors/catalog` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_factor.get_factor`<a id="oktauser_factorget_factor"></a>

Fetches a factor for the specified user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_factor_response = okta.user_factor.get_factor(
    user_id="userId_example",
    factor_id="factorId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### factor_id: `str`<a id="factor_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserFactor`](./okta_python_sdk/pydantic/user_factor.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/factors/{factorId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_factor.poll_factor_transaction_status`<a id="oktauser_factorpoll_factor_transaction_status"></a>

Polls factors verification transaction for status.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
poll_factor_transaction_status_response = okta.user_factor.poll_factor_transaction_status(
    user_id="userId_example",
    factor_id="factorId_example",
    transaction_id="transactionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### factor_id: `str`<a id="factor_id-str"></a>

##### transaction_id: `str`<a id="transaction_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`VerifyUserFactorResponse`](./okta_python_sdk/pydantic/verify_user_factor_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/factors/{factorId}/transactions/{transactionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_factor.unenroll_factor`<a id="oktauser_factorunenroll_factor"></a>

Unenrolls an existing factor for the specified user, allowing the user to enroll a new factor.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user_factor.unenroll_factor(
    user_id="userId_example",
    factor_id="factorId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### factor_id: `str`<a id="factor_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/factors/{factorId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_factor.verify_otp`<a id="oktauser_factorverify_otp"></a>

Verifies an OTP for a `token` or `token:hardware` factor

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_otp_response = okta.user_factor.verify_otp(
    body=None,
    user_id="userId_example",
    factor_id="factorId_example",
    activation_token="string_example",
    answer="string_example",
    attestation="string_example",
    client_data="string_example",
    next_pass_code="string_example",
    pass_code="string_example",
    registration_data="string_example",
    state_token="string_example",
    template_id="string_example",
    token_lifetime_seconds=300,
    x_forwarded_for="string_example",
    user_agent="string_example",
    accept_language="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### factor_id: `str`<a id="factor_id-str"></a>

##### activation_token: `str`<a id="activation_token-str"></a>

##### answer: `str`<a id="answer-str"></a>

##### attestation: `str`<a id="attestation-str"></a>

##### client_data: `str`<a id="client_data-str"></a>

##### next_pass_code: `str`<a id="next_pass_code-str"></a>

##### pass_code: `str`<a id="pass_code-str"></a>

##### registration_data: `str`<a id="registration_data-str"></a>

##### state_token: `str`<a id="state_token-str"></a>

##### template_id: `str`<a id="template_id-str"></a>

##### token_lifetime_seconds: `int`<a id="token_lifetime_seconds-int"></a>

##### x_forwarded_for: `str`<a id="x_forwarded_for-str"></a>

##### user_agent: `str`<a id="user_agent-str"></a>

##### accept_language: `str`<a id="accept_language-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VerifyFactorRequest`](./okta_python_sdk/type/verify_factor_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VerifyUserFactorResponse`](./okta_python_sdk/pydantic/verify_user_factor_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/users/{userId}/factors/{factorId}/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_schema.get_schema_by_id`<a id="oktauser_schemaget_schema_by_id"></a>

Fetches the schema for a Schema Id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_schema_by_id_response = okta.user_schema.get_schema_by_id(
    schema_id="schemaId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### schema_id: `str`<a id="schema_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserSchema`](./okta_python_sdk/pydantic/user_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/schemas/user/{schemaId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_schema.get_user_schema`<a id="oktauser_schemaget_user_schema"></a>

Fetches the Schema for an App User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_schema_response = okta.user_schema.get_user_schema(
    app_instance_id="appInstanceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_instance_id: `str`<a id="app_instance_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserSchema`](./okta_python_sdk/pydantic/user_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/schemas/apps/{appInstanceId}/default` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_schema.partial_update_user_profile`<a id="oktauser_schemapartial_update_user_profile"></a>

Partial updates on the User Profile properties of the Application User Schema.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
partial_update_user_profile_response = okta.user_schema.partial_update_user_profile(
    app_instance_id="appInstanceId_example",
    title="string_example",
    schema="string_example",
    links={
        "key": {},
    },
    created="string_example",
    definitions={
    },
    id="string_example",
    last_updated="string_example",
    name="string_example",
    properties={
    },
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_instance_id: `str`<a id="app_instance_id-str"></a>

##### title: `str`<a id="title-str"></a>

##### schema: `str`<a id="schema-str"></a>

##### links: [`UserSchemaLinks`](./okta_python_sdk/type/user_schema_links.py)<a id="links-userschemalinksokta_python_sdktypeuser_schema_linkspy"></a>

##### created: `str`<a id="created-str"></a>

##### definitions: [`UserSchemaDefinitions`](./okta_python_sdk/type/user_schema_definitions.py)<a id="definitions-userschemadefinitionsokta_python_sdktypeuser_schema_definitionspy"></a>


##### id: `str`<a id="id-str"></a>

##### last_updated: `str`<a id="last_updated-str"></a>

##### name: `str`<a id="name-str"></a>

##### properties: [`UserSchemaProperties`](./okta_python_sdk/type/user_schema_properties.py)<a id="properties-userschemapropertiesokta_python_sdktypeuser_schema_propertiespy"></a>


##### type: `str`<a id="type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserSchema`](./okta_python_sdk/type/user_schema.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserSchema`](./okta_python_sdk/pydantic/user_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/schemas/apps/{appInstanceId}/default` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_schema.partial_update_user_profile_0`<a id="oktauser_schemapartial_update_user_profile_0"></a>

Partial updates on the User Profile properties of the user schema.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
partial_update_user_profile_0_response = okta.user_schema.partial_update_user_profile_0(
    schema_id="schemaId_example",
    title="string_example",
    schema="string_example",
    links={
        "key": {},
    },
    created="string_example",
    definitions={
    },
    id="string_example",
    last_updated="string_example",
    name="string_example",
    properties={
    },
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### schema_id: `str`<a id="schema_id-str"></a>

##### title: `str`<a id="title-str"></a>

##### schema: `str`<a id="schema-str"></a>

##### links: [`UserSchemaLinks`](./okta_python_sdk/type/user_schema_links.py)<a id="links-userschemalinksokta_python_sdktypeuser_schema_linkspy"></a>

##### created: `str`<a id="created-str"></a>

##### definitions: [`UserSchemaDefinitions`](./okta_python_sdk/type/user_schema_definitions.py)<a id="definitions-userschemadefinitionsokta_python_sdktypeuser_schema_definitionspy"></a>


##### id: `str`<a id="id-str"></a>

##### last_updated: `str`<a id="last_updated-str"></a>

##### name: `str`<a id="name-str"></a>

##### properties: [`UserSchemaProperties`](./okta_python_sdk/type/user_schema_properties.py)<a id="properties-userschemapropertiesokta_python_sdktypeuser_schema_propertiespy"></a>


##### type: `str`<a id="type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserSchema`](./okta_python_sdk/type/user_schema.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserSchema`](./okta_python_sdk/pydantic/user_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/schemas/user/{schemaId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_type.create_new_user_type`<a id="oktauser_typecreate_new_user_type"></a>

Creates a new User Type. A default User Type is automatically created along with your org, and you may add another 9 User Types for a maximum of 10.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_user_type_response = okta.user_type.create_new_user_type(
    description="string_example",
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    created_by="string_example",
    default=True,
    display_name="string_example",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    last_updated_by="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

##### links: [`UserTypeLinks`](./okta_python_sdk/type/user_type_links.py)<a id="links-usertypelinksokta_python_sdktypeuser_type_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### created_by: `str`<a id="created_by-str"></a>

##### default: `bool`<a id="default-bool"></a>

##### display_name: `str`<a id="display_name-str"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### last_updated_by: `str`<a id="last_updated_by-str"></a>

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserType`](./okta_python_sdk/type/user_type.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserType`](./okta_python_sdk/pydantic/user_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/types/user` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_type.delete_permanently`<a id="oktauser_typedelete_permanently"></a>

Deletes a User Type permanently. This operation is not permitted for the default type, nor for any User Type that has existing users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
okta.user_type.delete_permanently(
    type_id="typeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type_id: `str`<a id="type_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/types/user/{typeId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_type.get_all_user_types`<a id="oktauser_typeget_all_user_types"></a>

Fetches all User Types in your org

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_user_types_response = okta.user_type.get_all_user_types()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UserTypeGetAllUserTypesResponse`](./okta_python_sdk/pydantic/user_type_get_all_user_types_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/types/user` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_type.get_by_id`<a id="oktauser_typeget_by_id"></a>

Fetches a User Type by ID. The special identifier `default` may be used to fetch the default User Type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = okta.user_type.get_by_id(
    type_id="typeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type_id: `str`<a id="type_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserType`](./okta_python_sdk/pydantic/user_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/types/user/{typeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_type.replace_existing_type`<a id="oktauser_typereplace_existing_type"></a>

Replace an existing User Type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_existing_type_response = okta.user_type.replace_existing_type(
    type_id="typeId_example",
    description="string_example",
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    created_by="string_example",
    default=True,
    display_name="string_example",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    last_updated_by="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type_id: `str`<a id="type_id-str"></a>

##### description: `str`<a id="description-str"></a>

##### links: [`UserTypeLinks`](./okta_python_sdk/type/user_type_links.py)<a id="links-usertypelinksokta_python_sdktypeuser_type_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### created_by: `str`<a id="created_by-str"></a>

##### default: `bool`<a id="default-bool"></a>

##### display_name: `str`<a id="display_name-str"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### last_updated_by: `str`<a id="last_updated_by-str"></a>

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserType`](./okta_python_sdk/type/user_type.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserType`](./okta_python_sdk/pydantic/user_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/types/user/{typeId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `okta.user_type.update_existing_type`<a id="oktauser_typeupdate_existing_type"></a>

Updates an existing User Type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_existing_type_response = okta.user_type.update_existing_type(
    type_id="typeId_example",
    description="string_example",
    links={
        "key": {},
    },
    created="1970-01-01T00:00:00.00Z",
    created_by="string_example",
    default=True,
    display_name="string_example",
    id="string_example",
    last_updated="1970-01-01T00:00:00.00Z",
    last_updated_by="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type_id: `str`<a id="type_id-str"></a>

##### description: `str`<a id="description-str"></a>

##### links: [`UserTypeLinks`](./okta_python_sdk/type/user_type_links.py)<a id="links-usertypelinksokta_python_sdktypeuser_type_linkspy"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### created_by: `str`<a id="created_by-str"></a>

##### default: `bool`<a id="default-bool"></a>

##### display_name: `str`<a id="display_name-str"></a>

##### id: `str`<a id="id-str"></a>

##### last_updated: `datetime`<a id="last_updated-datetime"></a>

##### last_updated_by: `str`<a id="last_updated_by-str"></a>

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserType`](./okta_python_sdk/type/user_type.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserType`](./okta_python_sdk/pydantic/user_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/meta/types/user/{typeId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
