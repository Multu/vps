import os


def files_list(directory):
    files = []

    dir_content = os.listdir(directory)

    for file in dir_content:
        file_path = directory + os.sep + file

        if os.path.isfile(file_path):
            files.append(file_path)

        if os.path.isdir(file_path):
            files += files_list(file_path)

    return files
