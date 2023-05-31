import ckan.plugins.toolkit as tk
import ckanext.extrafields.logic.schema as schema


@tk.side_effect_free
def extrafields_get_sum(context, data_dict):
    tk.check_access(
        "extrafields_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.extrafields_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'extrafields_get_sum': extrafields_get_sum,
    }
