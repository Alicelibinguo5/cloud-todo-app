FILE_PATH = 'todo.txt'

def get_todos(filepath = FILE_PATH ):
    """
    Read a text file and return the list of to-do items
    :param filepath:
    :return:
    """
    with  open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write(todos_args, filepath = FILE_PATH):
    """ Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_args)