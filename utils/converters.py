import json

import yaml


def yaml_to_dict(yaml_str):
    """Convert YAML string to dictionary."""
    return yaml.load(yaml_str, Loader=yaml.Loader)


def dict_to_yaml(yaml_dict):
    """Convert dictionary to YAML string."""
    return yaml.dump(yaml_dict, Dumper=yaml.Dumper)


def json_to_dict(json_str):
    """Convert JSON string to dictionary."""
    return json.loads(json_str)


def dict_to_json(json_dict):
    """Convert dictionary to JSON string."""
    return json.dumps(json_dict)
