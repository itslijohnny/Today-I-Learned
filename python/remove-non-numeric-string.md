# remove-non-numeric-string

  
## Remove non numeric string  
  
#python  
  
```python  
  
str='%1b4k&vwe@8s'  
  
def clean(str):  
	result = []  
	r =''  
	for i,j in enumerate(str):  
		if (not j.isalnum()) and i>0:  
			result.append(str[i-1])  
		else:  
			result.append(j)  
	return r.join(result)  
  
clean(str)  
  
```