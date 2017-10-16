import os
import tempfile


# def change_value(url, success=0, fail=0):
#     log = open("log.txt", "r")
#     lines = log.readlines()
#     log.close()
#
#     addNewLine = True
#
#     newlines = []
#
#     for line in lines:
#         found = line[:len(url)] == url
#
#         if found:
#             values = [int(val) for val in line.split(">")[1].split("/")]
#             values = [values[0] + success, values[1] + fail]
#             newline = url + " > " + str(values[0]) + " / " + str(values[1]) + "\n"
#             newlines.append(newline)
#             print(newline)
#             addNewLine = False
#         else:
#             newlines.append(line)
#             print(line)
#
#     if addNewLine:
#         line = url + " > " + str(success) + " / " + str(fail) + "\n"
#         newlines.append(line)
#         print(line)
#
#     log = open("log.txt", "w")
#     for line in newlines:
#         log.write(line)
#     log.close()

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

fail("https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9101117")