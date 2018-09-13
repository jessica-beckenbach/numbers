#fibonacci.py
# 
#
# This script prints out values of the fibonacci sequence
#######################

loop=1

n1=0
n2=1

while loop==1:
	try:
		seq = int(raw_input("How many numbers in the Fibonacci seqence do you want?\n"))
		print "\n"
		
		if seq==0:
			print "Please input an integer greater than 0.\n"
			
		elif seq==1:
			print "The first number is: 0"
			loop=0
			
		elif seq==2:
			print "The first two numbers are: 0, 1"
			loop=0

		else:
			print seq , "values of the Fibonacci sequence are:\n"
			
			print n1
			print n2
			
			for i in range(seq-2):
				nth=n1+n2
				n1=n2
				n2=nth
				print nth
			
			loop=0
	except:
		print "Please input an integer.\n"
