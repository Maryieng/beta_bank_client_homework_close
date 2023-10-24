import os
import os.path


def directory_dictionary(path="../src", recursive_counting=None) -> None:
    """Функция принимает путь до директории и выводит словарь с содержимым"""
    print(
        f"""files: {len([name for name in os.listdir(path) if os.path.isfile(name)])}
folders: {len([name for name in os.listdir(path) if not os.path.isfile(name)])}"""
    )
    if recursive_counting is not None:
        for root, dirs, files in os.walk(path):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))


print(directory_dictionary("../tests", 'yes'))
