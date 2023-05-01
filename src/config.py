from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):

    parser = ConfigParser()
    parser.read(filename)
    database = {}
    if parser.has_section(section):
        for element in parser.items(section):
            database[element[0]] = element[1]
    else:
        raise Exception('There is no such section!')
    return database
