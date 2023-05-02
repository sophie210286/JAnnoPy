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
        if isinstance(values, dict):
            annotators = values.get('reviewers')
            if annotators:
                for annotator in annotators:
                    email = annotator['email']
                    full_name = annotator['full_name']
                    annotator_counts[(email, full_name)] = \
                        annotator_counts.get((email, full_name), 0) + 1
        elif isinstance(values, list):
            for annotation in values:
                annotators = annotation.get('reviewers')
                if annotators:
                    for annotator in annotators:
                        email = annotator['email']
                        full_name = annotator['full_name']
                        annotator_counts[(email, full_name)] = \
                            annotator_counts.get((email, full_name), 0) + 1
    return annotator_counts


mega_file_path = os.path.abspath("../../combined_json")
mega_filename = "combined_json.json"
mega_json_data = read_json_file(os.path.join(mega_file_path, mega_filename))
print(get_annotator_info(mega_json_data))
