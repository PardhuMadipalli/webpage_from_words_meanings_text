
fi=open('words_with_colons', 'r')
fn=open('words_meanings_rearranged.txt', 'w')

for line in fi:
	for ch in line:
		if ch is not ':':
			fn.write(ch)
		else:
			fn.write('\n')
fi.close()
fn.close()
