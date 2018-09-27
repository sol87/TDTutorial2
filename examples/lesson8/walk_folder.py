import os


def walk_folders(folder_path):
    sub_file_list = []
    for sub_file_name in os.listdir(folder_path):
        sub_path = os.path.join(folder_path, sub_file_name)
        if os.path.isfile(sub_path):
            sub_file = {"type": "file", "name": sub_file_name}
            sub_file_list.append(sub_file)
        else:
            sub_folder = {"type": "folder", "name": sub_file_name, "sub_files": walk_folders(sub_path)}
            sub_file_list.append(sub_folder)
    return sub_file_list


if __name__ == "__main__":
    print walk_folders("e:/temp")
