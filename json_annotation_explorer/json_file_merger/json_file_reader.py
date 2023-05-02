import json


def read_json_file(file_path):
    """
    Parameters
    ----------
    file_path = the path of the single file you are looking at

    Returns a list of the JSON objects within that specific file
    -------
    """

    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

