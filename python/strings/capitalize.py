def capitalize(string):
    result = string.split(' ')
    for i in xrange(len(result)):
        if (result[i] != ''):
            result[i] = result[i][0].upper()+result[i][1:]
    return ' '.join(result)

if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string
