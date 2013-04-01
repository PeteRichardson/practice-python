import os
import logging


def get_makefiles(top):
    for (root, dirs, files) in os.walk(top):
        for f in files:
            if f.lower() == "makefile":
                yield os.path.join(root, f)


def fix_line(line):
    return line.replace("prometheus", "CE")


def edit_in_place(file, backup_extension=".bak"):
    assert os.path.exists(file), "ERROR: file {0} doesn't exist!".format(file)
    saved_file = file + backup_extension
    logging.debug("Renaming {0} to {1}".format(file, saved_file))
    os.rename(file, saved_file)
    assert os.path.exists(saved_file)
    assert not os.path.exists(file)
    new_file = open(file, "w")
    for line in open(saved_file):
        line = fix_line(line)
        logging.debug("modified line is {0}".format(line))
        new_file.write(line)
    new_file.close()
    logging.debug("# closed {0}".format(new_file))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    for makefile in get_makefiles("foo"):
        logging.debug("Processing {0}".format(makefile))
        edit_in_place(makefile)
