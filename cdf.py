def fact (n):
	if n == 1 or n == 0:
		return 1
	else:
		return n * fact (n-1)

def nCr (n, r):
	return fact (n) / (fact (r) * fact (n-r))
	
def nPr (n, r):
	return fact (n) / fact (n-r)
	
def cdf (n, p):
        temp = []
        if p > 1:
                print "Probability cannot be greater than 1"
        else:
        	for r in range (n+1):
        		temp.append (nCr (n, r) * (p ** r) * ((1-p) ** (n-r)))
        	for r in range (1, n+1):
        		temp[r] += temp[r-1]
        return temp	

def place (p):
        i = 0
        if p > 1:
        	print "Probability cannot be greater than 1"
        else:
        	x1 = input ("Enter number of trials: " )
        	x2 = input ("Enter the base probability: " )
        	temp = cdf (x1, x2)
        	while temp[i] < p:
        		i += 1
        return i
