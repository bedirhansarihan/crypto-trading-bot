def validate_parameters_info(parameters_info) -> None:
    if parameters_info is None:
        raise NotImplementedError(f"Concrete class must define '__PARAMETERS_INFO__' attribute.")

    elif not isinstance(parameters_info, dict):
        raise ValueError("'__PARAMETERS_INFO__' must be a dictionary.")

    elif not parameters_info:
        raise ValueError("'__PARAMETERS_INFO__' cannot be an empty dictionary.")

    for key, value in parameters_info.items():
        if not isinstance(value, dict):
            raise ValueError(f"Invalid value for parameter '{key}' in __PARAMETERS_INFO__. Must be a dictionary.")

        if 'type' not in value or 'name' not in value or 'default' not in value:
            raise ValueError(f"Missing 'type' or 'name' or default for parameter '{key}' in __PARAMETERS_INFO__.")

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


def validate_parameters(key_val: tuple, parameters: dict, parameters_info: dict) -> None:
    if key_val[0] in parameters:
        if isinstance(key_val[1], parameters_info[key_val[0]]['type']):
            if 'list' in parameters_info[key_val[0]]:
                if key_val[1] in parameters_info[key_val[0]]['list']:
                    parameters[key_val[0]] = key_val[1]
                else:
                    raise ValueError(
                        f"Invalid values '{key_val[1]}' for parameter '{key_val[0]}'. Allowed values: {', '.join(map(str, parameters_info[key_val[0]]['list']))}")
            else:
                if 'min' in parameters_info[key_val[0]]:
                    if key_val[1] < parameters_info[key_val[0]]['min']:
                        raise ValueError(
                            f"Parameter '{key_val[0]}' must be greater than or equal to {parameters_info[key_val[0]]['min']}")
                if 'max' in parameters_info[key_val[0]]:
                    if key_val[1] > parameters_info[key_val[0]]['max']:
                        raise ValueError(
                            f"Parameter '{key_val[0]}' must be less than or equal to {parameters_info[key_val[0]]['max']}")
                parameters[key_val[0]] = key_val[1]
        else:
            raise TypeError(
                f"Invalid type for parameter '{key_val[0]}'. Expected {parameters_info[key_val[0]]['type']}, got {type(key_val[1])}")
    else:
        raise KeyError(f"Unknown parameter '{key_val[0]}'")
