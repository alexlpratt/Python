import concurrent.futures as c_f

def printpow(num, power):
	print(pow(num, power))

with c_f.ThreadPoolExecutor(max_workers=10) as executor:
	threads = []
	for count in range(10):
		threads.append(executor.submit(printpow, 3, count))
	print(threads)
		
"""
Output:
$ python conc.py 
1
3
9
27
81
243
729
2187
6561
19683
[<Future at 0x101b83f28 state=finished returned NoneType>, <Future at 0x101d7eb00 state=finished returned NoneType>, 
<Future at 0x101e024e0 state=finished returned NoneType>, <Future at 0x101e02710 state=finished returned NoneType>, 
<Future at 0x101e02d30 state=finished returned NoneType>, <Future at 0x101e4ee80 state=finished returned NoneType>, 
<Future at 0x101eda2e8 state=finished returned NoneType>, <Future at 0x101edac18 state=finished returned NoneType>, 
<Future at 0x101edabe0 state=finished returned NoneType>, <Future at 0x101ee7320 state=finished returned NoneType>]
"""
