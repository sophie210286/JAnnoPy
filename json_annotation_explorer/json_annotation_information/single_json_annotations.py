from json_annotation_explorer.json_annotation_information\
    .json_nested_key_counter import get_nested_key_values
from json_annotation_explorer.json_file_merger.json_file_reader \
    import read_json_file
from json_annotation_explorer.json_annotation_information.json_nested_keys \
    import count_unique_values
import os


def process_json_file(filename, key):
    """
    Parameters
    ----------
    filename : str
        The name of the JSON file to process.
    key : str
        The key to search for in the JSON file.

    Returns
    -------
    Counter
        A Counter object that contains the count of each unique value
        associated with the specified key in the input JSON file.
    """

    download_dir = os.path.abspath("../../downloaded_json_files/json2")
    json_file_path = os.path.join(download_dir, filename)
    data = read_json_file(json_file_path)
    key_values = get_nested_key_values(data, key)
    unique_value_counts = count_unique_values(key_values)

    return unique_value_counts


json_key = 'name'
single_filename = "20120205172414Mh_2.json"
result = process_json_file(single_filename, json_key)
print(result)
