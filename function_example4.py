'Keyword variable length argument'
def person(name,**data):

    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)



person('keshav',age=25,city='Gurgaon',country='India',mob=6789)

