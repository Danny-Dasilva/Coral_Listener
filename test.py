apple = b"\x80\x00\x00"
hello = apple.decode('iso-8859-1').encode('utf8')
print(hello)