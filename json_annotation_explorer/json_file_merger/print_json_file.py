from json_annotation_explorer.json_file_merger.json_file_reader \
    import read_json_file
import os


def print_json_file(file_path):
    """
    Parameters
    ----------
    file_path : str
        The path of the single file you are looking at.

    Returns
    -------
    None
    """
    json_data = read_json_file(file_path)
    print(json_data)


# replace with the path to the directory where the file was downloaded
download_dir = "../../downloaded_json_files/json2"

# replace with the name of the file you downloaded
filename = "20120205172414Mh_2.json"

the_file_path = os.path.join(download_dir, filename)
json_file_path = os.path.abspath(the_file_path)

print_json_file(json_file_path)
