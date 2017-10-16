def change_value(url, success=0, fail=0):
    log = open("log.txt", "r")
    lines = log.readlines()
    log.close()

    addNewLine = True

    newlines = []

    for line in lines:
        found = line[:len(url)] == url

        if found:
            values = [int(val) for val in line.split(">")[1].split("/")]
            values = [values[0] + success, values[1] + fail]
            newline = url + " > " + str(values[0]) + " / " + str(values[1]) + "\n"
            newlines.append(newline)
            addNewLine = False
        else:
            newlines.append(line)

    if addNewLine:
        line = url + " > " + str(success) + " / " + str(fail) + "\n"
        newlines.append(line)

    log = open("log.txt", "w")
    for line in newlines:
        log.write(line)
    log.close()

def success(url):
    change_value(url, success=1)


def fail(url):
    change_value(url, fail=1)
