def validate_parameters_info(parameters_info):

    if parameters_info is None:
        raise NotImplementedError(f"Concrete class must define '__PARAMETERS_INFO__' attribute.")

    elif not isinstance(parameters_info, dict):
        raise ValueError("'__PARAMETERS_INFO__' must be a dictionary.")

    elif not parameters_info:
        raise ValueError("'__PARAMETERS_INFO__' cannot be an empty dictionary.")

    for key, value in parameters_info.items():
        if not isinstance(value, dict):
            raise ValueError(f"Invalid value for parameter '{key}' in __PARAMETERS_INFO__. Must be a dictionary.")

        if 'type' not in value or 'name' not in value:
            raise ValueError(f"Missing 'type' or 'name' for parameter '{key}' in __PARAMETERS_INFO__.")

        if value['type'] == str:
            if 'list' not in value:
                raise ValueError(f"String parameter '{key}' requires 'list' in __PARAMETERS_INFO__.")
        elif value['type'] == float:
            if 'min' not in value or 'max' not in value or 'decimals' not in value:
                raise ValueError(
                    f"Float parameter '{key}' requires 'min', 'max', and 'decimals' in __PARAMETERS_INFO__.")
        elif value['type'] == int:
            if 'min' not in value or 'max' not in value:
                raise ValueError(f"Integer parameter '{key}' requires 'min' and 'max' in __PARAMETERS_INFO__.")
        else:
            raise ValueError(f"Unsupported type '{value['type']}' for parameter '{key}' in __PARAMETERS_INFO__.")
