def pascal(n):
    if n == 1:
        return [1]
    else:
        p_line = pascal(n-1)
        print p_line
        line = [ p_line[i]+p_line[i+1] for i in range(len(p_line)-1)]
        line.insert(0,1)
        line.append(1)
    	return line

print(pascal(3))