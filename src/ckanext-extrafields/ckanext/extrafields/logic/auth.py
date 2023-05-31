import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def extrafields_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "extrafields_get_sum": extrafields_get_sum,
    }
