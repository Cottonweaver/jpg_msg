#!/usr/bin/python

import sys

action = ''

print(sys.argv)
len_argv = len(sys.argv)

for i in range(len_argv):
    print (sys.argv[i])
    if(sys.argv[i] == "-a"):
        if (i+1 < len_argv):
            action = sys.argv[i+1]
            print("action=" + action)
        else:
            print("no action specified")
            exit()

    elif(sys.argv[i] == "-f"):
        if (i+1 < len_argv):
            filename = sys.argv[i+1]
            print("file: " + filename)
        else:
            print("no file specified")
            exit()

    elif(sys.argv[i] == "-c"):
        if(action == "w" or action == "write"):
            if (i+1 < len_argv):
                content = sys.argv[i+1]
                print("written content: " + content)
            else:
                print("no content specified")
                exit()
        else:
            print("no content in non write mode allowed.")
            exit()

    elif(sys.argv[i] == "-h"):
        print("jpg_msg is a small programm to appen and read messages to an from jpg files.\n-a specify if you wanna read (r) or write (w) from or to an file.\n-f specify the you wann performe the action on. Could be a path or a file name.")
        exit()


#action = input("write or read to or from jpeg?\nwrite (1)\nread (2)")

#filename = input("on what do you wanna perform the action?")

if(action == "w"):
    with open(filename, 'ab') as f:
        #content = input("what do you wanna append")
        f.write(str.encode(content))

elif(action == "r"):
    with open(filename, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))

        f.seek(offset + 2)
        print(f.read())

else:
    print("no action was selected")
