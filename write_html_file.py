

f1=open('newenglish.txt', 'r')
f2=open('thishtml.txt', 'w')
#line=fi.readline()
num=1

for line in f1:
	if num % 2 is not 0:
		f2.write('<tr>\n<td data-th="Movie Title">')
		f2.write(line)
		f2.write('</td>\n')
	else:
		f2.write('<td data-th="Genre">')
		f2.write(line)
		f2.write('</td>\n</tr>\n')
		

	num=num+1
f1.close()
f2.close()
