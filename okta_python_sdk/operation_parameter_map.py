operation_parameter_map = {
    '/api/v1/apps/{appId}/credentials/secrets/{secretId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'secretId'
            },
        ]
    },
    '/api/v1/apps/{appId}/connections/default/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/api/v1/apps/{appId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/secrets-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'client_secret'
            },
        ]
    },
    '/api/v1/apps/{appId}/groups/{groupId}-PUT': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'groupId'
            },
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'profile'
            },
        ]
    },
    '/api/v1/apps/{appId}/policies/{policyId}-PUT': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'policyId'
            },
        ]
    },
    '/api/v1/apps/{appId}/users-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'credentials'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastSync'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'passwordChanged'
            },
            {
                'name': 'profile'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'status'
            },
            {
                'name': 'statusChanged'
            },
            {
                'name': 'syncState'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/keys/{keyId}/clone-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'keyId'
            },
            {
                'name': 'targetAid'
            },
        ]
    },
    '/api/v1/apps-POST': {
        'parameters': [
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'accessibility'
            },
            {
                'name': 'created'
            },
            {
                'name': 'credentials'
            },
            {
                'name': 'features'
            },
            {
                'name': 'id'
            },
            {
                'name': 'label'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'licensing'
            },
            {
                'name': 'name'
            },
            {
                'name': 'profile'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'signOnMode'
            },
            {
                'name': 'status'
            },
            {
                'name': 'visibility'
            },
            {
                'name': 'activate'
            },
            {
                'name': 'OktaAccessGateway-Agent'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/secrets/{secretId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'secretId'
            },
        ]
    },
    '/api/v1/apps/{appId}/connections/default/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/api/v1/apps/{appId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/csrs/{csrId}-DELETE': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'csrId'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/csrs-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'subjectAltNames'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/keys/generate-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'validityYears'
            },
        ]
    },
    '/api/v1/apps/{appId}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/secrets/{secretId}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'secretId'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/csrs/{csrId}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'csrId'
            },
        ]
    },
    '/api/v1/apps/{appId}/connections/default-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/api/v1/apps/{appId}/features/{name}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/api/v1/apps/{appId}/groups/{groupId}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/keys/{keyId}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'keyId'
            },
        ]
    },
    '/api/v1/apps/{appId}/grants/{grantId}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'grantId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/apps/{appId}/users/{userId}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/apps/{appId}/tokens/{tokenId}-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'tokenId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/apps/{appId}/grants-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'created'
            },
            {
                'name': 'createdBy'
            },
            {
                'name': 'id'
            },
            {
                'name': 'issuer'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'scopeId'
            },
            {
                'name': 'source'
            },
            {
                'name': 'status'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/apps-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'includeNonDeleted'
            },
        ]
    },
    '/api/v1/apps/{appId}/users-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'q'
            },
            {
                'name': 'query_scope'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/secrets-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/csrs-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/api/v1/apps/{appId}/features-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/api/v1/apps/{appId}/groups-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'q'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/keys-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/api/v1/apps/{appId}/grants-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/apps/{appId}/tokens-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/apps/{appId}/sso/saml/metadata-GET': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'kid'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/csrs/{csrId}/lifecycle/publish-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'csrId'
            },
        ]
    },
    '/api/v1/apps/{appId}/groups/{groupId}-DELETE': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'groupId'
            },
        ]
    },
    '/api/v1/apps/{appId}-DELETE': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/api/v1/apps/{appId}/credentials/secrets/{secretId}-DELETE': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'secretId'
            },
        ]
    },
    '/api/v1/apps/{appId}/users/{userId}-DELETE': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'sendEmail'
            },
        ]
    },
    '/api/v1/apps/{appId}/tokens-DELETE': {
        'parameters': [
            {
                'name': 'appId'
            },
        ]
    },
    '/api/v1/apps/{appId}/grants/{grantId}-DELETE': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'grantId'
            },
        ]
    },
    '/api/v1/apps/{appId}/tokens/{tokenId}-DELETE': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'tokenId'
            },
        ]
    },
    '/api/v1/apps/{appId}/connections/default-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'profile'
            },
            {
                'name': 'activate'
            },
        ]
    },
    '/api/v1/apps/{appId}-PUT': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'accessibility'
            },
            {
                'name': 'created'
            },
            {
                'name': 'credentials'
            },
            {
                'name': 'features'
            },
            {
                'name': 'id'
            },
            {
                'name': 'label'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'licensing'
            },
            {
                'name': 'name'
            },
            {
                'name': 'profile'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'signOnMode'
            },
            {
                'name': 'status'
            },
            {
                'name': 'visibility'
            },
        ]
    },
    '/api/v1/apps/{appId}/features/{name}-PUT': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'create'
            },
            {
                'name': 'update'
            },
        ]
    },
    '/api/v1/apps/{appId}/logo-POST': {
        'parameters': [
            {
                'name': 'file'
            },
            {
                'name': 'appId'
            },
        ]
    },
    '/api/v1/apps/{appId}/users/{userId}-POST': {
        'parameters': [
            {
                'name': 'appId'
            },
            {
                'name': 'userId'
            },
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'credentials'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastSync'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'passwordChanged'
            },
            {
                'name': 'profile'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'status'
            },
            {
                'name': 'statusChanged'
            },
            {
                'name': 'syncState'
            },
        ]
    },
    '/api/v1/authenticators/{authenticatorId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'authenticatorId'
            },
        ]
    },
    '/api/v1/authenticators-POST': {
        'parameters': [
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'key'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
            {
                'name': 'activate'
            },
        ]
    },
    '/api/v1/authenticators/{authenticatorId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'authenticatorId'
            },
        ]
    },
    '/api/v1/authenticators/{authenticatorId}-GET': {
        'parameters': [
            {
                'name': 'authenticatorId'
            },
        ]
    },
    '/api/v1/authenticators-GET': {
        'parameters': [
        ]
    },
    '/api/v1/authenticators/{authenticatorId}-PUT': {
        'parameters': [
            {
                'name': 'authenticatorId'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'key'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'authServerId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies/{policyId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'policyId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'policyId'
            },
            {
                'name': 'ruleId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/claims-POST': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': '_links'
            },
            {
                'name': 'alwaysIncludeInToken'
            },
            {
                'name': 'claimType'
            },
            {
                'name': 'conditions'
            },
            {
                'name': 'group_filter_type'
            },
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
            {
                'name': 'system'
            },
            {
                'name': 'value'
            },
            {
                'name': 'valueType'
            },
        ]
    },
    '/api/v1/authorizationServers-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': '_links'
            },
            {
                'name': 'audiences'
            },
            {
                'name': 'created'
            },
            {
                'name': 'credentials'
            },
            {
                'name': 'default'
            },
            {
                'name': 'id'
            },
            {
                'name': 'issuer'
            },
            {
                'name': 'issuerMode'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies-POST': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'description'
            },
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'conditions'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'status'
            },
            {
                'name': 'system'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules-POST': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'policyId'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'conditions'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'status'
            },
            {
                'name': 'system'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/scopes-POST': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'consent'
            },
            {
                'name': 'default'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'id'
            },
            {
                'name': 'metadataPublish'
            },
            {
                'name': 'name'
            },
            {
                'name': 'system'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'authServerId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies/{policyId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'policyId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'policyId'
            },
            {
                'name': 'ruleId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens/{tokenId}-DELETE': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'tokenId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/claims/{claimId}-DELETE': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'claimId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens-DELETE': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'clientId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies/{policyId}-DELETE': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'policyId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}-DELETE': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'policyId'
            },
            {
                'name': 'ruleId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/scopes/{scopeId}-DELETE': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'scopeId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}-DELETE': {
        'parameters': [
            {
                'name': 'authServerId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules-GET': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'policyId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}-GET': {
        'parameters': [
            {
                'name': 'authServerId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/claims-GET': {
        'parameters': [
            {
                'name': 'authServerId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/claims/{claimId}-GET': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'claimId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens/{tokenId}-GET': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'tokenId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens-GET': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies/{policyId}-GET': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'policyId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies-GET': {
        'parameters': [
            {
                'name': 'authServerId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}-GET': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'policyId'
            },
            {
                'name': 'ruleId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/scopes-GET': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'q'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/scopes/{scopeId}-GET': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'scopeId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/clients-GET': {
        'parameters': [
            {
                'name': 'authServerId'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/credentials/keys-GET': {
        'parameters': [
            {
                'name': 'authServerId'
            },
        ]
    },
    '/api/v1/authorizationServers-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'after'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/credentials/lifecycle/keyRotate-POST': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'use'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}-PUT': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'description'
            },
            {
                'name': '_links'
            },
            {
                'name': 'audiences'
            },
            {
                'name': 'created'
            },
            {
                'name': 'credentials'
            },
            {
                'name': 'default'
            },
            {
                'name': 'id'
            },
            {
                'name': 'issuer'
            },
            {
                'name': 'issuerMode'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/claims/{claimId}-PUT': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'claimId'
            },
            {
                'name': '_links'
            },
            {
                'name': 'alwaysIncludeInToken'
            },
            {
                'name': 'claimType'
            },
            {
                'name': 'conditions'
            },
            {
                'name': 'group_filter_type'
            },
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
            {
                'name': 'system'
            },
            {
                'name': 'value'
            },
            {
                'name': 'valueType'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}-PUT': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'policyId'
            },
            {
                'name': 'ruleId'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'conditions'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'status'
            },
            {
                'name': 'system'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/policies/{policyId}-PUT': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'policyId'
            },
            {
                'name': 'description'
            },
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'conditions'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'status'
            },
            {
                'name': 'system'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/authorizationServers/{authServerId}/scopes/{scopeId}-PUT': {
        'parameters': [
            {
                'name': 'authServerId'
            },
            {
                'name': 'scopeId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'consent'
            },
            {
                'name': 'default'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'id'
            },
            {
                'name': 'metadataPublish'
            },
            {
                'name': 'name'
            },
            {
                'name': 'system'
            },
        ]
    },
    '/api/v1/brands/{brandId}/templates/email/{templateName}/customizations-POST': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'templateName'
            },
            {
                'name': 'body'
            },
            {
                'name': 'isDefault'
            },
            {
                'name': 'language'
            },
            {
                'name': 'subject'
            },
        ]
    },
    '/api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId}-DELETE': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'templateName'
            },
            {
                'name': 'customizationId'
            },
        ]
    },
    '/api/v1/brands/{brandId}/templates/email/{templateName}/customizations-DELETE': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'templateName'
            },
        ]
    },
    '/api/v1/brands/{brandId}/themes/{themeId}/background-image-DELETE': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'themeId'
            },
        ]
    },
    '/api/v1/brands/{brandId}/themes/{themeId}/favicon-DELETE': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'themeId'
            },
        ]
    },
    '/api/v1/brands/{brandId}/themes/{themeId}/logo-DELETE': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'themeId'
            },
        ]
    },
    '/api/v1/brands-GET': {
        'parameters': [
        ]
    },
    '/api/v1/brands/{brandId}-GET': {
        'parameters': [
            {
                'name': 'brandId'
            },
        ]
    },
    '/api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId}/preview-GET': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'templateName'
            },
            {
                'name': 'customizationId'
            },
        ]
    },
    '/api/v1/brands/{brandId}/templates/email/{templateName}-GET': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'templateName'
            },
        ]
    },
    '/api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId}-GET': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'templateName'
            },
            {
                'name': 'customizationId'
            },
        ]
    },
    '/api/v1/brands/{brandId}/templates/email/{templateName}/default-content-GET': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'templateName'
            },
        ]
    },
    '/api/v1/brands/{brandId}/templates/email/{templateName}/default-content/preview-GET': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'templateName'
            },
        ]
    },
    '/api/v1/brands/{brandId}/templates/email/{templateName}/test-POST': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'templateName'
            },
            {
                'name': 'customizationId'
            },
        ]
    },
    '/api/v1/brands/{brandId}/themes/{themeId}-GET': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'themeId'
            },
        ]
    },
    '/api/v1/brands/{brandId}/themes-GET': {
        'parameters': [
            {
                'name': 'brandId'
            },
        ]
    },
    '/api/v1/brands/{brandId}/templates/email/{templateName}/customizations-GET': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'templateName'
            },
        ]
    },
    '/api/v1/brands/{brandId}/templates/email-GET': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/brands/{brandId}-PUT': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': '_links'
            },
            {
                'name': 'agreeToCustomPrivacyPolicy'
            },
            {
                'name': 'customPrivacyPolicyUrl'
            },
            {
                'name': 'id'
            },
            {
                'name': 'removePoweredByOkta'
            },
        ]
    },
    '/api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId}-PUT': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'templateName'
            },
            {
                'name': 'customizationId'
            },
            {
                'name': 'body'
            },
            {
                'name': 'isDefault'
            },
            {
                'name': 'language'
            },
            {
                'name': 'subject'
            },
        ]
    },
    '/api/v1/brands/{brandId}/themes/{themeId}-PUT': {
        'parameters': [
            {
                'name': 'brandId'
            },
            {
                'name': 'themeId'
            },
            {
                'name': '_links'
            },
            {
                'name': 'backgroundImage'
            },
            {
                'name': 'emailTemplateTouchPointVariant'
            },
            {
                'name': 'endUserDashboardTouchPointVariant'
            },
            {
                'name': 'errorPageTouchPointVariant'
            },
            {
                'name': 'primaryColorContrastHex'
            },
            {
                'name': 'primaryColorHex'
            },
            {
                'name': 'secondaryColorContrastHex'
            },
            {
                'name': 'secondaryColorHex'
            },
            {
                'name': 'signInPageTouchPointVariant'
            },
        ]
    },
    '/api/v1/brands/{brandId}/themes/{themeId}/background-image-POST': {
        'parameters': [
            {
                'name': 'file'
            },
            {
                'name': 'brandId'
            },
            {
                'name': 'themeId'
            },
        ]
    },
    '/api/v1/brands/{brandId}/themes/{themeId}/favicon-POST': {
        'parameters': [
            {
                'name': 'file'
            },
            {
                'name': 'brandId'
            },
            {
                'name': 'themeId'
            },
        ]
    },
    '/api/v1/brands/{brandId}/themes/{themeId}/logo-POST': {
        'parameters': [
            {
                'name': 'file'
            },
            {
                'name': 'brandId'
            },
            {
                'name': 'themeId'
            },
        ]
    },
    '/api/v1/domains/{domainId}/certificate-PUT': {
        'parameters': [
            {
                'name': 'domainId'
            },
            {
                'name': 'certificate'
            },
            {
                'name': 'certificateChain'
            },
            {
                'name': 'privateKey'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/domains-POST': {
        'parameters': [
            {
                'name': 'certificateSourceType'
            },
            {
                'name': 'dnsRecords'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'id'
            },
            {
                'name': 'publicCertificate'
            },
            {
                'name': 'validationStatus'
            },
        ]
    },
    '/api/v1/domains/{domainId}-GET': {
        'parameters': [
            {
                'name': 'domainId'
            },
        ]
    },
    '/api/v1/domains-GET': {
        'parameters': [
        ]
    },
    '/api/v1/domains/{domainId}-DELETE': {
        'parameters': [
            {
                'name': 'domainId'
            },
        ]
    },
    '/api/v1/domains/{domainId}/verify-POST': {
        'parameters': [
            {
                'name': 'domainId'
            },
        ]
    },
    '/api/v1/eventHooks/{eventHookId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'eventHookId'
            },
        ]
    },
    '/api/v1/eventHooks-POST': {
        'parameters': [
            {
                'name': '_links'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'created'
            },
            {
                'name': 'createdBy'
            },
            {
                'name': 'events'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
            {
                'name': 'verificationStatus'
            },
        ]
    },
    '/api/v1/eventHooks/{eventHookId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'eventHookId'
            },
        ]
    },
    '/api/v1/eventHooks/{eventHookId}-GET': {
        'parameters': [
            {
                'name': 'eventHookId'
            },
        ]
    },
    '/api/v1/eventHooks-GET': {
        'parameters': [
        ]
    },
    '/api/v1/eventHooks/{eventHookId}-DELETE': {
        'parameters': [
            {
                'name': 'eventHookId'
            },
        ]
    },
    '/api/v1/eventHooks/{eventHookId}-PUT': {
        'parameters': [
            {
                'name': 'eventHookId'
            },
            {
                'name': '_links'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'created'
            },
            {
                'name': 'createdBy'
            },
            {
                'name': 'events'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
            {
                'name': 'verificationStatus'
            },
        ]
    },
    '/api/v1/eventHooks/{eventHookId}/lifecycle/verify-POST': {
        'parameters': [
            {
                'name': 'eventHookId'
            },
        ]
    },
    '/api/v1/features/{featureId}/{lifecycle}-POST': {
        'parameters': [
            {
                'name': 'featureId'
            },
            {
                'name': 'lifecycle'
            },
            {
                'name': 'mode'
            },
        ]
    },
    '/api/v1/features-GET': {
        'parameters': [
        ]
    },
    '/api/v1/features/{featureId}-GET': {
        'parameters': [
            {
                'name': 'featureId'
            },
        ]
    },
    '/api/v1/features/{featureId}/dependencies-GET': {
        'parameters': [
            {
                'name': 'featureId'
            },
        ]
    },
    '/api/v1/features/{featureId}/dependents-GET': {
        'parameters': [
            {
                'name': 'featureId'
            },
        ]
    },
    '/api/v1/groups/rules/{ruleId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'ruleId'
            },
        ]
    },
    '/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId}-PUT': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'appName'
            },
            {
                'name': 'applicationId'
            },
        ]
    },
    '/api/v1/groups/rules-POST': {
        'parameters': [
            {
                'name': 'actions'
            },
            {
                'name': 'conditions'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/groups/{groupId}/users/{userId}-PUT': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/groups/{groupId}/roles-POST': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'disableNotifications'
            },
        ]
    },
    '/api/v1/groups-POST': {
        'parameters': [
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastMembershipUpdated'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'objectClass'
            },
            {
                'name': 'profile'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/groups/rules/{ruleId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'ruleId'
            },
        ]
    },
    '/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}-DELETE': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'appName'
            },
        ]
    },
    '/api/v1/groups/{groupId}/users-GET': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/groups/rules-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'after'
            },
            {
                'name': 'search'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/groups/rules/{ruleId}-GET': {
        'parameters': [
            {
                'name': 'ruleId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/groups/{groupId}/roles-GET': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/groups/{groupId}/roles/{roleId}-GET': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'roleId'
            },
        ]
    },
    '/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps-GET': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/groups/{groupId}-GET': {
        'parameters': [
            {
                'name': 'groupId'
            },
        ]
    },
    '/api/v1/groups-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/api/v1/groups/{groupId}/apps-GET': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/groups/{groupId}/roles/{roleId}/targets/groups-GET': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId}-DELETE': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'appName'
            },
            {
                'name': 'applicationId'
            },
        ]
    },
    '/api/v1/groups/{groupId}-DELETE': {
        'parameters': [
            {
                'name': 'groupId'
            },
        ]
    },
    '/api/v1/groups/rules/{ruleId}-DELETE': {
        'parameters': [
            {
                'name': 'ruleId'
            },
            {
                'name': 'removeUsers'
            },
        ]
    },
    '/api/v1/groups/{groupId}/roles/{roleId}/targets/groups/{targetGroupId}-DELETE': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'targetGroupId'
            },
        ]
    },
    '/api/v1/groups/{groupId}/users/{userId}-DELETE': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/groups/{groupId}/roles/{roleId}-DELETE': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'roleId'
            },
        ]
    },
    '/api/v1/groups/{groupId}-PUT': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastMembershipUpdated'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'objectClass'
            },
            {
                'name': 'profile'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}-PUT': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'appName'
            },
        ]
    },
    '/api/v1/groups/rules/{ruleId}-PUT': {
        'parameters': [
            {
                'name': 'ruleId'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'conditions'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/groups/{groupId}/roles/{roleId}/targets/groups/{targetGroupId}-PUT': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'targetGroupId'
            },
        ]
    },
    '/api/v1/meta/schemas/group/default-GET': {
        'parameters': [
        ]
    },
    '/api/v1/meta/schemas/group/default-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': '$schema'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'definitions'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/idps/{idpId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'idpId'
            },
        ]
    },
    '/api/v1/idps-POST': {
        'parameters': [
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'issuerMode'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'policy'
            },
            {
                'name': 'protocol'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/idps/credentials/keys-POST': {
        'parameters': [
            {
                'name': '_links'
            },
            {
                'name': 'alg'
            },
            {
                'name': 'created'
            },
            {
                'name': 'e'
            },
            {
                'name': 'expiresAt'
            },
            {
                'name': 'key_ops'
            },
            {
                'name': 'kid'
            },
            {
                'name': 'kty'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'n'
            },
            {
                'name': 'status'
            },
            {
                'name': 'use'
            },
            {
                'name': 'x5c'
            },
            {
                'name': 'x5t'
            },
            {
                'name': 'x5t#S256'
            },
            {
                'name': 'x5u'
            },
        ]
    },
    '/api/v1/idps/{idpId}/credentials/keys/{keyId}/clone-POST': {
        'parameters': [
            {
                'name': 'idpId'
            },
            {
                'name': 'keyId'
            },
            {
                'name': 'targetIdpId'
            },
        ]
    },
    '/api/v1/idps/{idpId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'idpId'
            },
        ]
    },
    '/api/v1/idps/credentials/keys/{keyId}-DELETE': {
        'parameters': [
            {
                'name': 'keyId'
            },
        ]
    },
    '/api/v1/idps/credentials/keys-GET': {
        'parameters': [
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/idps/{idpId}/credentials/csrs-POST': {
        'parameters': [
            {
                'name': 'idpId'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'subjectAltNames'
            },
        ]
    },
    '/api/v1/idps/{idpId}/credentials/keys/generate-POST': {
        'parameters': [
            {
                'name': 'idpId'
            },
            {
                'name': 'validityYears'
            },
        ]
    },
    '/api/v1/idps/{idpId}-GET': {
        'parameters': [
            {
                'name': 'idpId'
            },
        ]
    },
    '/api/v1/idps/{idpId}/credentials/csrs/{csrId}-GET': {
        'parameters': [
            {
                'name': 'idpId'
            },
            {
                'name': 'csrId'
            },
        ]
    },
    '/api/v1/idps/credentials/keys/{keyId}-GET': {
        'parameters': [
            {
                'name': 'keyId'
            },
        ]
    },
    '/api/v1/idps/{idpId}/users/{userId}-GET': {
        'parameters': [
            {
                'name': 'idpId'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/idps/{idpId}/credentials/keys/{keyId}-GET': {
        'parameters': [
            {
                'name': 'idpId'
            },
            {
                'name': 'keyId'
            },
        ]
    },
    '/api/v1/idps/{idpId}/users/{userId}/credentials/tokens-GET': {
        'parameters': [
            {
                'name': 'idpId'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/idps/{idpId}/users-GET': {
        'parameters': [
            {
                'name': 'idpId'
            },
        ]
    },
    '/api/v1/idps/{idpId}/users/{userId}-POST': {
        'parameters': [
            {
                'name': 'idpId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'externalId'
            },
        ]
    },
    '/api/v1/idps-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/idps/{idpId}/credentials/csrs-GET': {
        'parameters': [
            {
                'name': 'idpId'
            },
        ]
    },
    '/api/v1/idps/{idpId}/credentials/keys-GET': {
        'parameters': [
            {
                'name': 'idpId'
            },
        ]
    },
    '/api/v1/idps/{idpId}-DELETE': {
        'parameters': [
            {
                'name': 'idpId'
            },
        ]
    },
    '/api/v1/idps/{idpId}/credentials/csrs/{csrId}-DELETE': {
        'parameters': [
            {
                'name': 'idpId'
            },
            {
                'name': 'csrId'
            },
        ]
    },
    '/api/v1/idps/{idpId}/users/{userId}-DELETE': {
        'parameters': [
            {
                'name': 'idpId'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/idps/{idpId}-PUT': {
        'parameters': [
            {
                'name': 'idpId'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'issuerMode'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'policy'
            },
            {
                'name': 'protocol'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/idps/{idpId}/credentials/csrs/{csrId}/lifecycle/publish-POST': {
        'parameters': [
            {
                'name': 'idpId'
            },
            {
                'name': 'csrId'
            },
        ]
    },
    '/api/v1/inlineHooks/{inlineHookId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'inlineHookId'
            },
        ]
    },
    '/api/v1/inlineHooks-POST': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': '_links'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/inlineHooks/{inlineHookId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'inlineHookId'
            },
        ]
    },
    '/api/v1/inlineHooks/{inlineHookId}-DELETE': {
        'parameters': [
            {
                'name': 'inlineHookId'
            },
        ]
    },
    '/api/v1/inlineHooks/{inlineHookId}/execute-POST': {
        'parameters': [
            {
                'name': 'inlineHookId'
            },
        ]
    },
    '/api/v1/inlineHooks/{inlineHookId}-GET': {
        'parameters': [
            {
                'name': 'inlineHookId'
            },
        ]
    },
    '/api/v1/inlineHooks-GET': {
        'parameters': [
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/inlineHooks/{inlineHookId}-PUT': {
        'parameters': [
            {
                'name': 'inlineHookId'
            },
            {
                'name': 'version'
            },
            {
                'name': '_links'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/meta/schemas/user/linkedObjects-POST': {
        'parameters': [
            {
                'name': '_links'
            },
            {
                'name': 'associated'
            },
            {
                'name': 'primary'
            },
        ]
    },
    '/api/v1/meta/schemas/user/linkedObjects/{linkedObjectName}-DELETE': {
        'parameters': [
            {
                'name': 'linkedObjectName'
            },
        ]
    },
    '/api/v1/meta/schemas/user/linkedObjects-GET': {
        'parameters': [
        ]
    },
    '/api/v1/meta/schemas/user/linkedObjects/{linkedObjectName}-GET': {
        'parameters': [
            {
                'name': 'linkedObjectName'
            },
        ]
    },
    '/api/v1/logs-GET': {
        'parameters': [
            {
                'name': 'since'
            },
            {
                'name': 'until'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sortOrder'
            },
            {
                'name': 'after'
            },
        ]
    },
    '/api/v1/zones/{zoneId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'zoneId'
            },
        ]
    },
    '/api/v1/zones-POST': {
        'parameters': [
            {
                'name': '_links'
            },
            {
                'name': 'asns'
            },
            {
                'name': 'created'
            },
            {
                'name': 'gateways'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'locations'
            },
            {
                'name': 'name'
            },
            {
                'name': 'proxies'
            },
            {
                'name': 'proxyType'
            },
            {
                'name': 'status'
            },
            {
                'name': 'system'
            },
            {
                'name': 'type'
            },
            {
                'name': 'usage'
            },
        ]
    },
    '/api/v1/zones/{zoneId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'zoneId'
            },
        ]
    },
    '/api/v1/zones/{zoneId}-GET': {
        'parameters': [
            {
                'name': 'zoneId'
            },
        ]
    },
    '/api/v1/zones-GET': {
        'parameters': [
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/api/v1/zones/{zoneId}-DELETE': {
        'parameters': [
            {
                'name': 'zoneId'
            },
        ]
    },
    '/api/v1/zones/{zoneId}-PUT': {
        'parameters': [
            {
                'name': 'zoneId'
            },
            {
                'name': '_links'
            },
            {
                'name': 'asns'
            },
            {
                'name': 'created'
            },
            {
                'name': 'gateways'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'locations'
            },
            {
                'name': 'name'
            },
            {
                'name': 'proxies'
            },
            {
                'name': 'proxyType'
            },
            {
                'name': 'status'
            },
            {
                'name': 'system'
            },
            {
                'name': 'type'
            },
            {
                'name': 'usage'
            },
        ]
    },
    '/api/v1/org/privacy/oktaSupport/extend-POST': {
        'parameters': [
        ]
    },
    '/api/v1/org/privacy/oktaSupport/revoke-POST': {
        'parameters': [
        ]
    },
    '/api/v1/org/contacts/{contactType}-GET': {
        'parameters': [
            {
                'name': 'contactType'
            },
        ]
    },
    '/api/v1/org/privacy/oktaCommunication-GET': {
        'parameters': [
        ]
    },
    '/api/v1/org/privacy/oktaSupport-GET': {
        'parameters': [
        ]
    },
    '/api/v1/org/preferences-GET': {
        'parameters': [
        ]
    },
    '/api/v1/org-GET': {
        'parameters': [
        ]
    },
    '/api/v1/org/privacy/oktaSupport/grant-POST': {
        'parameters': [
        ]
    },
    '/api/v1/org/preferences/hideEndUserFooter-POST': {
        'parameters': [
        ]
    },
    '/api/v1/org/contacts-GET': {
        'parameters': [
        ]
    },
    '/api/v1/org/preferences/showEndUserFooter-POST': {
        'parameters': [
        ]
    },
    '/api/v1/org/privacy/oktaCommunication/optIn-POST': {
        'parameters': [
        ]
    },
    '/api/v1/org/privacy/oktaCommunication/optOut-POST': {
        'parameters': [
        ]
    },
    '/api/v1/org/contacts/{contactType}-PUT': {
        'parameters': [
            {
                'name': 'contactType'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/org/logo-POST': {
        'parameters': [
            {
                'name': 'file'
            },
        ]
    },
    '/api/v1/org-PUT': {
        'parameters': [
            {
                'name': '_links'
            },
            {
                'name': 'address1'
            },
            {
                'name': 'address2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'companyName'
            },
            {
                'name': 'country'
            },
            {
                'name': 'created'
            },
            {
                'name': 'endUserSupportHelpURL'
            },
            {
                'name': 'expiresAt'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'phoneNumber'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'state'
            },
            {
                'name': 'status'
            },
            {
                'name': 'subdomain'
            },
            {
                'name': 'supportPhoneNumber'
            },
            {
                'name': 'website'
            },
        ]
    },
    '/api/v1/org-POST': {
        'parameters': [
            {
                'name': '_links'
            },
            {
                'name': 'address1'
            },
            {
                'name': 'address2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'companyName'
            },
            {
                'name': 'country'
            },
            {
                'name': 'created'
            },
            {
                'name': 'endUserSupportHelpURL'
            },
            {
                'name': 'expiresAt'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'phoneNumber'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'state'
            },
            {
                'name': 'status'
            },
            {
                'name': 'subdomain'
            },
            {
                'name': 'supportPhoneNumber'
            },
            {
                'name': 'website'
            },
        ]
    },
    '/api/v1/policies/{policyId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'policyId'
            },
        ]
    },
    '/api/v1/policies/{policyId}/rules/{ruleId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'policyId'
            },
            {
                'name': 'ruleId'
            },
        ]
    },
    '/api/v1/policies-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'conditions'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'status'
            },
            {
                'name': 'system'
            },
            {
                'name': 'type'
            },
            {
                'name': 'activate'
            },
        ]
    },
    '/api/v1/policies/{policyId}/rules-POST': {
        'parameters': [
            {
                'name': 'policyId'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'conditions'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'status'
            },
            {
                'name': 'system'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/policies/{policyId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'policyId'
            },
        ]
    },
    '/api/v1/policies/{policyId}/rules/{ruleId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'policyId'
            },
            {
                'name': 'ruleId'
            },
        ]
    },
    '/api/v1/policies/{policyId}/rules-GET': {
        'parameters': [
            {
                'name': 'policyId'
            },
        ]
    },
    '/api/v1/policies-GET': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'status'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/policies/{policyId}-GET': {
        'parameters': [
            {
                'name': 'policyId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/policies/{policyId}/rules/{ruleId}-GET': {
        'parameters': [
            {
                'name': 'policyId'
            },
            {
                'name': 'ruleId'
            },
        ]
    },
    '/api/v1/policies/{policyId}-DELETE': {
        'parameters': [
            {
                'name': 'policyId'
            },
        ]
    },
    '/api/v1/policies/{policyId}/rules/{ruleId}-DELETE': {
        'parameters': [
            {
                'name': 'policyId'
            },
            {
                'name': 'ruleId'
            },
        ]
    },
    '/api/v1/policies/{policyId}-PUT': {
        'parameters': [
            {
                'name': 'policyId'
            },
            {
                'name': 'description'
            },
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'conditions'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'status'
            },
            {
                'name': 'system'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/policies/{policyId}/rules/{ruleId}-PUT': {
        'parameters': [
            {
                'name': 'policyId'
            },
            {
                'name': 'ruleId'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'conditions'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'status'
            },
            {
                'name': 'system'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/mappings/{mappingId}-GET': {
        'parameters': [
            {
                'name': 'mappingId'
            },
        ]
    },
    '/api/v1/mappings-GET': {
        'parameters': [
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sourceId'
            },
            {
                'name': 'targetId'
            },
        ]
    },
    '/api/v1/mappings/{mappingId}-POST': {
        'parameters': [
            {
                'name': 'mappingId'
            },
            {
                'name': '_links'
            },
            {
                'name': 'id'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'source'
            },
            {
                'name': 'target'
            },
        ]
    },
    '/api/v1/sessions/{sessionId}-DELETE': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/api/v1/sessions-POST': {
        'parameters': [
            {
                'name': 'sessionToken'
            },
        ]
    },
    '/api/v1/sessions/{sessionId}-GET': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/api/v1/sessions/{sessionId}/lifecycle/refresh-POST': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/api/v1/roles/{roleTypeOrRoleId}/subscriptions/{notificationType}/unsubscribe-POST': {
        'parameters': [
            {
                'name': 'roleTypeOrRoleId'
            },
            {
                'name': 'notificationType'
            },
        ]
    },
    '/api/v1/roles/{roleTypeOrRoleId}/subscriptions/{notificationType}-GET': {
        'parameters': [
            {
                'name': 'roleTypeOrRoleId'
            },
            {
                'name': 'notificationType'
            },
        ]
    },
    '/api/v1/roles/{roleTypeOrRoleId}/subscriptions-GET': {
        'parameters': [
            {
                'name': 'roleTypeOrRoleId'
            },
        ]
    },
    '/api/v1/roles/{roleTypeOrRoleId}/subscriptions/{notificationType}/subscribe-POST': {
        'parameters': [
            {
                'name': 'roleTypeOrRoleId'
            },
            {
                'name': 'notificationType'
            },
        ]
    },
    '/api/v1/users/{userId}/subscriptions/{notificationType}/unsubscribe-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'notificationType'
            },
        ]
    },
    '/api/v1/users/{userId}/subscriptions/{notificationType}/subscribe-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'notificationType'
            },
        ]
    },
    '/api/v1/templates/sms-POST': {
        'parameters': [
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'template'
            },
            {
                'name': 'translations'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/templates/sms-GET': {
        'parameters': [
            {
                'name': 'templateType'
            },
        ]
    },
    '/api/v1/templates/sms/{templateId}-GET': {
        'parameters': [
            {
                'name': 'templateId'
            },
        ]
    },
    '/api/v1/templates/sms/{templateId}-POST': {
        'parameters': [
            {
                'name': 'templateId'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'template'
            },
            {
                'name': 'translations'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/templates/sms/{templateId}-DELETE': {
        'parameters': [
            {
                'name': 'templateId'
            },
        ]
    },
    '/api/v1/templates/sms/{templateId}-PUT': {
        'parameters': [
            {
                'name': 'templateId'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'template'
            },
            {
                'name': 'translations'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/threats/configuration-GET': {
        'parameters': [
        ]
    },
    '/api/v1/threats/configuration-POST': {
        'parameters': [
            {
                'name': '_links'
            },
            {
                'name': 'action'
            },
            {
                'name': 'created'
            },
            {
                'name': 'excludeZones'
            },
            {
                'name': 'lastUpdated'
            },
        ]
    },
    '/api/v1/trustedOrigins/{trustedOriginId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'trustedOriginId'
            },
        ]
    },
    '/api/v1/trustedOrigins-POST': {
        'parameters': [
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'createdBy'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'lastUpdatedBy'
            },
            {
                'name': 'name'
            },
            {
                'name': 'origin'
            },
            {
                'name': 'scopes'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/v1/trustedOrigins/{trustedOriginId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'trustedOriginId'
            },
        ]
    },
    '/api/v1/trustedOrigins/{trustedOriginId}-DELETE': {
        'parameters': [
            {
                'name': 'trustedOriginId'
            },
        ]
    },
    '/api/v1/trustedOrigins-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/trustedOrigins/{trustedOriginId}-GET': {
        'parameters': [
            {
                'name': 'trustedOriginId'
            },
        ]
    },
    '/api/v1/trustedOrigins/{trustedOriginId}-PUT': {
        'parameters': [
            {
                'name': 'trustedOriginId'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'createdBy'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'lastUpdatedBy'
            },
            {
                'name': 'name'
            },
            {
                'name': 'origin'
            },
            {
                'name': 'scopes'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/v1/users/{userId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'sendEmail'
            },
        ]
    },
    '/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId}-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'appName'
            },
            {
                'name': 'applicationId'
            },
        ]
    },
    '/api/v1/users/{userId}/roles-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'disableNotifications'
            },
        ]
    },
    '/api/v1/users/{userId}/credentials/change_password-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'newPassword'
            },
            {
                'name': 'oldPassword'
            },
            {
                'name': 'strict'
            },
        ]
    },
    '/api/v1/users-POST': {
        'parameters': [
            {
                'name': 'credentials'
            },
            {
                'name': 'groupIds'
            },
            {
                'name': 'profile'
            },
            {
                'name': 'type'
            },
            {
                'name': 'activate'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'nextLogin'
            },
        ]
    },
    '/api/v1/users/{userId}/lifecycle/deactivate-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'sendEmail'
            },
        ]
    },
    '/api/v1/users/{userId}/linkedObjects/{relationshipName}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'relationshipName'
            },
        ]
    },
    '/api/v1/users/{userId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'sendEmail'
            },
        ]
    },
    '/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'appName'
            },
        ]
    },
    '/api/v1/users/{userId}/lifecycle/expire_password?tempPassword=false-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/lifecycle/expire_password?tempPassword=true-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/credentials/forgot_password-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/lifecycle/reset_password-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'sendEmail'
            },
        ]
    },
    '/api/v1/users/{userId}/roles/{roleId}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'roleId'
            },
        ]
    },
    '/api/v1/users/{userId}/clients/{clientId}/tokens/{tokenId}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'tokenId'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'after'
            },
        ]
    },
    '/api/v1/users/{userId}/grants/{grantId}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'grantId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/users/{userId}/linkedObjects/{relationshipName}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'relationshipName'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/users/{userId}/groups-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/subscriptions/{notificationType}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'notificationType'
            },
        ]
    },
    '/api/v1/users-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'search'
            },
            {
                'name': 'sortBy'
            },
            {
                'name': 'sortOrder'
            },
        ]
    },
    '/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/users/{userId}/appLinks-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/roles-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/api/v1/users/{userId}/clients-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/grants-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'scopeId'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/users/{userId}/clients/{clientId}/grants-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/users/{userId}/idps-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/clients/{clientId}/tokens-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/users/{userId}/roles/{roleId}/targets/groups-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'after'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/api/v1/users/{userId}/subscriptions-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/lifecycle/reactivate-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'sendEmail'
            },
        ]
    },
    '/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'appName'
            },
            {
                'name': 'applicationId'
            },
        ]
    },
    '/api/v1/users/{userId}/roles/{roleId}/targets/groups/{groupId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'groupId'
            },
        ]
    },
    '/api/v1/users/{userId}/lifecycle/reset_factors-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/sessions-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'oauthTokens'
            },
        ]
    },
    '/api/v1/users/{userId}/clients/{clientId}/tokens-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'clientId'
            },
        ]
    },
    '/api/v1/users/{userId}/grants/{grantId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'grantId'
            },
        ]
    },
    '/api/v1/users/{userId}/grants-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/clients/{clientId}/grants-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'clientId'
            },
        ]
    },
    '/api/v1/users/{userId}/clients/{clientId}/tokens/{tokenId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'tokenId'
            },
        ]
    },
    '/api/v1/users/{userId}/lifecycle/suspend-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/roles/{roleId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'roleId'
            },
        ]
    },
    '/api/v1/users/{userId}/lifecycle/unlock-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/lifecycle/unsuspend-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{associatedUserId}/linkedObjects/{primaryRelationshipName}/{primaryUserId}-PUT': {
        'parameters': [
            {
                'name': 'associatedUserId'
            },
            {
                'name': 'primaryRelationshipName'
            },
            {
                'name': 'primaryUserId'
            },
        ]
    },
    '/api/v1/users/{userId}-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'activated'
            },
            {
                'name': 'created'
            },
            {
                'name': 'credentials'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastLogin'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'passwordChanged'
            },
            {
                'name': 'profile'
            },
            {
                'name': 'status'
            },
            {
                'name': 'statusChanged'
            },
            {
                'name': 'transitioningToStatus'
            },
            {
                'name': 'type'
            },
            {
                'name': 'strict'
            },
        ]
    },
    '/api/v1/users/{userId}-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'activated'
            },
            {
                'name': 'created'
            },
            {
                'name': 'credentials'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastLogin'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'passwordChanged'
            },
            {
                'name': 'profile'
            },
            {
                'name': 'status'
            },
            {
                'name': 'statusChanged'
            },
            {
                'name': 'transitioningToStatus'
            },
            {
                'name': 'type'
            },
            {
                'name': 'strict'
            },
        ]
    },
    '/api/v1/users/{userId}/credentials/change_recovery_question-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'password'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'recovery_question'
            },
        ]
    },
    '/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'roleId'
            },
        ]
    },
    '/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'appName'
            },
        ]
    },
    '/api/v1/users/{userId}/roles/{roleId}/targets/groups/{groupId}-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'groupId'
            },
        ]
    },
    '/api/v1/users/{userId}/factors/{factorId}/lifecycle/activate-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'factorId'
            },
            {
                'name': 'attestation'
            },
            {
                'name': 'clientData'
            },
            {
                'name': 'passCode'
            },
            {
                'name': 'registrationData'
            },
            {
                'name': 'stateToken'
            },
        ]
    },
    '/api/v1/users/{userId}/factors-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': '_embedded'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'factorType'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'status'
            },
            {
                'name': 'verify'
            },
            {
                'name': 'updatePhone'
            },
            {
                'name': 'templateId'
            },
            {
                'name': 'tokenLifetimeSeconds'
            },
            {
                'name': 'activate'
            },
        ]
    },
    '/api/v1/users/{userId}/factors-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/factors/questions-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/factors/catalog-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/api/v1/users/{userId}/factors/{factorId}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'factorId'
            },
        ]
    },
    '/api/v1/users/{userId}/factors/{factorId}/transactions/{transactionId}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'factorId'
            },
            {
                'name': 'transactionId'
            },
        ]
    },
    '/api/v1/users/{userId}/factors/{factorId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'factorId'
            },
        ]
    },
    '/api/v1/users/{userId}/factors/{factorId}/verify-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'factorId'
            },
            {
                'name': 'activationToken'
            },
            {
                'name': 'answer'
            },
            {
                'name': 'attestation'
            },
            {
                'name': 'clientData'
            },
            {
                'name': 'nextPassCode'
            },
            {
                'name': 'passCode'
            },
            {
                'name': 'registrationData'
            },
            {
                'name': 'stateToken'
            },
            {
                'name': 'templateId'
            },
            {
                'name': 'tokenLifetimeSeconds'
            },
            {
                'name': 'X-Forwarded-For'
            },
            {
                'name': 'User-Agent'
            },
            {
                'name': 'Accept-Language'
            },
        ]
    },
    '/api/v1/meta/schemas/user/{schemaId}-GET': {
        'parameters': [
            {
                'name': 'schemaId'
            },
        ]
    },
    '/api/v1/meta/schemas/apps/{appInstanceId}/default-GET': {
        'parameters': [
            {
                'name': 'appInstanceId'
            },
        ]
    },
    '/api/v1/meta/schemas/apps/{appInstanceId}/default-POST': {
        'parameters': [
            {
                'name': 'appInstanceId'
            },
            {
                'name': 'title'
            },
            {
                'name': '$schema'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'definitions'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/meta/schemas/user/{schemaId}-POST': {
        'parameters': [
            {
                'name': 'schemaId'
            },
            {
                'name': 'title'
            },
            {
                'name': '$schema'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'definitions'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'name'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/api/v1/meta/types/user-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'createdBy'
            },
            {
                'name': 'default'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'lastUpdatedBy'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/api/v1/meta/types/user/{typeId}-DELETE': {
        'parameters': [
            {
                'name': 'typeId'
            },
        ]
    },
    '/api/v1/meta/types/user-GET': {
        'parameters': [
        ]
    },
    '/api/v1/meta/types/user/{typeId}-GET': {
        'parameters': [
            {
                'name': 'typeId'
            },
        ]
    },
    '/api/v1/meta/types/user/{typeId}-PUT': {
        'parameters': [
            {
                'name': 'typeId'
            },
            {
                'name': 'description'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'createdBy'
            },
            {
                'name': 'default'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'lastUpdatedBy'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/api/v1/meta/types/user/{typeId}-POST': {
        'parameters': [
            {
                'name': 'typeId'
            },
            {
                'name': 'description'
            },
            {
                'name': '_links'
            },
            {
                'name': 'created'
            },
            {
                'name': 'createdBy'
            },
            {
                'name': 'default'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'id'
            },
            {
                'name': 'lastUpdated'
            },
            {
                'name': 'lastUpdatedBy'
            },
            {
                'name': 'name'
            },
        ]
    },
};