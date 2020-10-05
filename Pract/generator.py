import os


def generate_filenames():
    """
    generates a sequence of opened files
    matching a specific extension
    """
    for dir_path, dir_names, file_names in os.walk('/home/kaushik/PROGRAMMING/Python'):
        for file_name in file_names:
            if file_name.endswith('.py'):
                yield open(os.path.join(dir_path, file_name))


def cat_files(files):
    """
    takes in an iterable of filenames
    """
    for fname in files:
        for line in fname:
            yield line


def grep_files(lines, pattern=None):
    """
    takes in an iterable of lines
    """
    for line in lines:
        if pattern in line:
            yield line


py_files = generate_filenames()
py_file = cat_files(py_files)
lines = grep_files(py_file, 'python')
for line in lines:
    print(line)
