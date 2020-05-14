import time
import sys
# how many spaces to indent
indent = 0
# whether the indentation is increasing or not
indentIncrease = True

try:
    while True:
        print(' ' * indent, end='')
        print('******')
        # pause for 0.1 second
        time.sleep(0.1)

        if indentIncrease:
            indent = indent + 1
            if indent == 20:
                indentIncrease = False

        else:
            indent = indent - 1
            if indent == 0:
                indentIncrease = True
except KeyboardInterrupt:
    sys.exit()
