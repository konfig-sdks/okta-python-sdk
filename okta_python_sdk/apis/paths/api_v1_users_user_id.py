from okta_python_sdk.paths.api_v1_users_user_id.get import ApiForget
from okta_python_sdk.paths.api_v1_users_user_id.put import ApiForput
from okta_python_sdk.paths.api_v1_users_user_id.post import ApiForpost
from okta_python_sdk.paths.api_v1_users_user_id.delete import ApiFordelete


class ApiV1UsersUserId(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
