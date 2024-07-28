string1 ="Vo van"
print(string1.upper())
print(string1.lower())
print(string1[2:4])
print(string1.split())
print(string1.split(sep="o"))
print(string1.strip())
my = "-"
joined = my.join(string1)
print(joined)
print(joined.find("o",2))
joined2 = joined.replace('0','k',1)
print(string1.isupper())
