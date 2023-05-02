import glob
import json
import os


def combine_json_files(directory, pattern):
    """
    Parameters
    ----------
    directory
    pattern

    Returns
    -------
    """
    # Use glob to find all files in the directory that match the pattern
    file_list = glob.glob(os.path.join(directory, pattern))

    # Initialize an empty dictionary to hold the combined data
    combined_data = {}

    # Loop through each file and add its data to the combined data dictionary
    for file_path in file_list:
        with open(file_path, "r") as f:
            data = json.load(f)
            for key, value in data.items():
                if key in combined_data:
                    if isinstance(combined_data[key], list):
                        combined_data[key].append(value)
                    else:
                        combined_data[key] = [combined_data[key], value]
                else:
                    combined_data[key] = value

    # Define the path to the new directory where the file will be saved
    new_directory = "../../combined_json"
    # Create the new directory if it doesn't already exist
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

    # Write the combined data dictionary to a new JSON file in the new directory
    with open(os.path.join(new_directory, "combined_json.json"), "w") as f:
        json.dump(combined_data, f, indent=4)

    return combined_data


files_directory = "../../downloaded_json_files/json2"
file_pattern = "*_2.json"

# Get the absolute path of the directory
directory_path = os.path.abspath(files_directory)

# Call the function to combine JSON files
combined_data_files = combine_json_files(directory_path, file_pattern)

print(combined_data_files)
