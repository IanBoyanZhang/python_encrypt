def setColor(color, text):
    if color == 'red':
        return '\033[91m'+text+'\033[0m'
    if color == 'green':
        return '\033[92m'+text+'\033[0m'
    if color == 'yellow':
        return '\033[93m'+text+'\033[0m'
    if color == 'purple':
        return '\033[94m'+text+'\033[0m'
    if color == 'pink':
        return '\033[95m'+text+'\033[0m'
    if color == 'blue':
        return '\033[96m'+text+'\033[0m'
    if color == 'gray':
        return '\033[90m'+text+'\033[0m'
    if color == 'dark_red':
        return '\033[31m'+text+'\033[0m'
    if color == 'dark_green':
        return '\033[32m'+text+'\033[0m'
    if color == 'dark_yellow':
        return '\033[33m'+text+'\033[0m'
    if color == 'dark_purple':
        return '\033[34m'+text+'\033[0m'
    if color == 'dark_pink':
        return '\033[35m'+text+'\033[0m'
    if color == 'dark_blue':
        return '\033[36m'+text+'\033[0m'
    else:
        return text

def test():
    for a in xrange(0,100):
        print '\033['+str(a)+'m'+str(a)+'\033[0m'

if __name__ == '__main__':
    test()
