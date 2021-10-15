import sys
text= sys.stdin.read()
textUpper=text.upper()
if 'QUIT' in textUpper:
    print("Bye!", file=sys.stderr)
else:
    print(textUpper)
