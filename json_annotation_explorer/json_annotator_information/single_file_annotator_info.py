from json_annotation_explorer.json_file_merger.json_file_reader \
    import read_json_file
import os


def get_annotator_info(data):
    """
    Parameters
    ----------
    data : dict
        The JSON objects within the file.

    Returns
    -------
    dict
        Unique annotator email(s) and full name(s) and the counts of each.
    """
    annotator_counts = {}
    for values in data['annotations']:
        annotators = values.get('annotators')
        if annotators:
            for annotator in annotators:
                email = annotator['email']
                full_name = annotator['full_name']
                annotator_counts[(email, full_name)] = \
                    annotator_counts.get((email, full_name), 0)+1
    return annotator_counts


single_file_path = os.path.abspath("../../downloaded_json_files/json2")
single_filename = "20120205172414Mh_2.json"
single_json_data = read_json_file(os.path.join(single_file_path,
                                               single_filename))
print(get_annotator_info(single_json_data))
