import os
import tempfile

def make_log_file(url, success):
    dir = "./logs"
    if not os.path.exists(dir):
        os.makedirs(dir)
    file = tempfile.NamedTemporaryFile(dir=dir, delete=False, mode="w")
    file.write(url + "\n" + str(success))
    file.close()

def success(url):
    make_log_file(url, success=True)


def fail(url):
    make_log_file(url, success=False)