class Solution(object):
    def intToRoman(self, num):
        dictt={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        num=list(str(num))
        num.reverse()

        for x in range(len(num)):
            num[x]=int(num[x])*(10**x)

        num.reverse()

        stri = ""
        for z in num:
            flag=0
            if z in dictt:
                stri+=dictt[z]
            else:
                y=list(dictt.keys())
                y.reverse()
                for x in range(len(y)):
                    for a in range(x+1,len(y)):
                        if abs(y[x]-y[a])==z:
                            if y[a]<y[x]:
                                stri+=dictt[y[a]]
                                stri+=dictt[y[x]]
                            else:
                                stri+=dictt[y[x]]
                                stri+=dictt[y[a]]
                            flag=1

                if flag==0:
                    x=0
                    y=list(filter(lambda x:x<=z,dictt))
                    y.sort(reverse=True)
                    while(z>0):
                        if y[x]<=z:
                            stri+=dictt[y[x]]
                            z-=y[x]
                        else:
                            x+=1
        return(stri)
        