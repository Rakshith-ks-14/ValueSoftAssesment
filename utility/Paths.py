from pathlib import Path

class Paths:
    BASE_PATH = Path.cwd().parent

    @classmethod
    def get_folder_path(cls, folder_name):
        return cls.BASE_PATH.glob(f'**/{folder_name}')

    @classmethod
    def get_file_path(cls, folder, file_extension):
        return cls.BASE_PATH.glob(f'**/{folder}/*.{file_extension}')

