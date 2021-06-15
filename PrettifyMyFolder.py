# Oh Soldier Prettify My Folder
import os


def soldier(path, text_file, file_format):
    unchanged_files = []
    try:
        f = open(text_file)
        for line in f:
            line = line.rstrip()
            unchanged_files.append(line)
        f.close()
    except Exception as e:
        print(e)
    os.chdir(path)
    number = 1
    for name in os.listdir():
        if os.path.isdir(path + f"/{name}"):
            continue
        else:
            params = name.split('.')
            if params[0] in unchanged_files:
                continue
            elif params[1] == file_format:
                os.rename(name, f"{number}.{file_format}")
                number += 1
            else:
                os.rename(name, name.capitalize())


if __name__ == '__main__':
    print("-----Oh Soldier, Prettify My Folder!-----")
    user_path = input("Type in your directory path carefully, then hit enter:\n")
    user_text_file = input("Type in your dictionary text file name:\n")
    user_file_format = input("Type in your desired file format:\n")
    soldier(user_path, user_text_file, user_file_format)
    print("Your folder has been prettified!")
