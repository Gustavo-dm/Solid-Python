# single responsibility  principle in python


# class FileManager:
#     def __init__(self, file_path):
#         self.file_path = file_path

#     def read_file(self):
#         with open(self.file_path, "r") as file:
#             data = file.read()
#         return data

#     def write_file(self, content):
#         with open(self.file_path, "w") as file:
#             file.write(content)


# Applying single responsibility  principle
class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, "r") as file:
            data = file.read()
        return data


class FileWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_file(self, content):
        with open(self.file_path, "w") as file:
            file.write(content)
