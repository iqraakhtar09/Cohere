from backend.definitions import BACKEND_ROOT


def write_to_file(filename, output):
    f = open(f"{BACKEND_ROOT}\\output\\{filename}", "w")
    f.write(output)
    f.close()
