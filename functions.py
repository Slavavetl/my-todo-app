FILEPATH = "./todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read the text file and return the
    list of TO DO items in it
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, path=FILEPATH):
    """ Write a TO DO item in the text file """
    with open(path, 'w') as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("Hey!")
