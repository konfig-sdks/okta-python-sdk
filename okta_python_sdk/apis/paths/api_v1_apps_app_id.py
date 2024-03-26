from okta_python_sdk.paths.api_v1_apps_app_id.get import ApiForget
from okta_python_sdk.paths.api_v1_apps_app_id.put import ApiForput
from okta_python_sdk.paths.api_v1_apps_app_id.delete import ApiFordelete


class ApiV1AppsAppId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
