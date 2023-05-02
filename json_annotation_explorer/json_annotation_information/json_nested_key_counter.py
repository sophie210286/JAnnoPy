from json_annotation_explorer.json_file_merger.json_file_reader \
    import read_json_file
import os


def get_nested_key_values(data, key):
    """
    Parameters
    ----------
    data = the specified json object (from load_json_file)
    key = the specific key you are looking for

    Returns the values of the specific key
    -------
    """
    key_values = []
    # check if the data variable a dictionary type
    if isinstance(data, dict):

        # iterates over the key-value pairs of the data
        for k, v in data.items():

            # if the key matches the specified key
            if k == key:

                # add the value to key_values
                key_values.append(v)

            else:

                # recursive call
                key_values.extend(get_nested_key_values(v, key))
                # continues until all the nested dictionaries have been
                # searched and their values matching the key have been added to
                # the key_values list.

    # check if the data variable a list type
    elif isinstance(data, list):

        # iterate through the items of the data
        for item in data:
            # recursive call again
            key_values.extend(get_nested_key_values(item, key))

    return key_values


json_key = 'name'
download_dir = "../../downloaded_json_files/json2"

filename = "20120205172414Mh_2.json"

json_file_path = os.path.join(download_dir, filename)
json_data = read_json_file(json_file_path)

print(get_nested_key_values(json_data, json_key))
