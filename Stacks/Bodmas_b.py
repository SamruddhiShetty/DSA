s="a+(b-c)-(d-e)-(f+g)+(h+i)"
i=0
stack=[0]
result=""
while i<len(s):
    if s[i]=='(' and i==0:
        continue
    if s[i]=="+":
        if stack[-1]==0:
            result+="+"
        elif stack[-1]==1:
            result+="-"
    elif s[i]=="-":
        if stack[-1]==1:
            result+="+"
        elif stack[-1]==0:
            result+="-"
    elif s[i]=='(' and i>0:
        if s[i-1]=="-":
            stack.append(1)
        elif s[i-1]=="+":
            stack.append(0)
    elif s[i]==')':
        stack.pop()
    else:
        result+=s[i]
    i+=1
print(result)

#output a+b-c-d+e-f-g+h+i
