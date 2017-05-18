filename = raw_input(">")

txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again"
file_aganin = raw_input(">")

txt_again = open(file_aganin)

print txt_again.read()
