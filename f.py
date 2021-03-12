#file = open("jeshu.txt", "w")
#file.write("this has been")

#file = open("jeshu.txt", "r")
#print(file.read())
#file.close()
#try:
  # f = open("jeshu.txt")
   #print(f.read())
#finally:
  # f.close()
#def sqr_n(k)
#return k*k
#squares = [0,1,4,9,16,25]
#sqr=list(map(sqr_n,squares))
#print(sqr)
#print("{0}{1}{0}{1}".format("abra","cad"))
#print(sum ([34,5]))
#print(min(1,2,3,4,50))
def Count_char(name,ch):
count = 0
for i in name:
    if i == ch:
        count += i
        return count
filename = input("enter a filename :")
with open(filename) as f:

    name = f.read()
    print(Count_char(name,"j"))
    



