print("Enter the marks of your subject")
markone=int(input())
marktwo=int(input())
markthree=int(input())
markfour=int(input())
markfive=int(input())

total=markone+marktwo+markthree+markfour+markfive
avg=total/5

if avg>=91 and avg<=100:
    print("Yzour grade is A1")
elif avg>=81 and avg<91:
    print("Yzour grade is A2")
elif avg>=71 and avg<81:
    print("Yzour grade is B1")
elif avg>=61 and avg<71:
    print("Yzour grade is B2")
elif avg>=51 and avg<61:
    print("Yzour grade is C1")
elif avg>=41 and avg<51:
    print("Yzour grade is C2")
elif avg>=33 and avg<41:
    print("Yzour grade is D")
elif avg>=21 and avg<33:
    print("Yzour grade is E1")
elif avg>=0 and avg<=21:
    print("Yzour grade is E2")
else:
    print("invalid input")
