from okta_python_sdk.paths.api_v1_org.get import ApiForget
from okta_python_sdk.paths.api_v1_org.put import ApiForput
from okta_python_sdk.paths.api_v1_org.post import ApiForpost


class ApiV1Org(
    ApiForget,
    ApiForput,
    ApiForpost,
):
    pass
