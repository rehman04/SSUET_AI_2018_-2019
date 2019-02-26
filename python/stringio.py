from io import StringIO
message='tis is some text'
f=StringIO(message)
print(f.read())
f.write(' this is new text')
f.seek(0)
print(f.read())