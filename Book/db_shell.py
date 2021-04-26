from Book.models import Book


# to run python file 
# exec(open(f"C:\\Users\\ROHINI\\djangonew\\Library\\Book\\db_shell.py").read())

#hwenever we do changes in a models.py we have to reopen thhe shell again to ru the de_shell.py 

# # for all data
# all_data = Book.objects.all()
# print(all_data)
# print("------------------------------------------------")

# # for single data

# all = Book.objects.get(id=1)
# print(all)
# print("------------------------------------------------")

# # creating a data

# b = Book.objects.create(name="mathematics",auther="rajas",quantity=22,price=567)
# print(b)
# print("------------------------------------------------")

# # update data

# b2 = Book.objects.get(id=3)
# b2.name="RRRRR"
# b2.auther="BBBBB"
# b2.save()
# print("------------------------------------------------")

# # deleting the data

# b1 = Book.objects.get(id=1)
# b1.delete()
# print("------------------------------------------------")

# ---------------------------------------

# all_data = len(Book.objects.all())             #for length
# --------------------------------------

# to print all book info
# all_data = Book.objects.all()
# # print(all_data)

# for Book in all_data:
#     print("--------details for id number:-",Book.id,"----------")
#     print("bookname:-",Book.name)
#     print("bookauther:-",Book.auther)
#     print("bookquantity:-",Book.quantity)
#     print("bookprice:-",Book.price)

# ---------------------------------------------------------------------------

# to updsate a data at a time

# all_data = Book.objects.all()
# for Book in all_data:
#     Book.quantity = 88
#     Book.price = 900
#     Book.save()

    # Book.delete()                         #for deleting the data

# for i in all_data:
#     print(i.__dict__)                 #for dictionary

# -------------------------------------
# for particular data
# select id,name from book_info;
# all_data = Book.objects.values('id','name')
# for i in all_data:
    # print(i)
    # print(list(i))
# --------------------------------------

# all_data = Book.objects.values_list()
# print(all_data)   #it gives list of tuple and in tuple there is single single values

# for i in all_data:
    # print(i)       #for tuple format
    # print(i[0])   #gives index values---id's

# ---------------------------------------------------

# filter querry

# import random

# for i in range(1,10):
#     b = Book(name=(chr(random.randint(65,90)))*5,auther="abc",quantity=random.randint(15,85),price=random.randint(100,500))
#     b.save()

# -------------------------------------------------------------------------------------------

# using filter

# books=Book.objects.filter(id__gt=15)    #greater than
# # books=Book.objects.filter(id__gte=15)      #greater than equal to
# # books=Book.objects.filter(id__lte=15)      #less than equal to
# for i in books:
#     print(i.__dict__)

# --------for perticular values----------------
# books=Book.objects.filter(id__gt=15).values('id','name')
# for i in books:
#     print(i)

# ------------filteration on name basis----------
# # books=Book.objects.filter(name__startswith='O').values('id','name')
# # books=Book.objects.filter(name__endswith='O').values('id','name')
# books=Book.objects.filter(name__istartswith='i').values('id','name')  #insensitive case
# for i in books:
#     print(i)

# --------------------------------------------------------

# -----------data in alphabetical order---------

# # b = Book.objects.all().order_by("name")        #ascending order
# b = Book.objects.all().order_by("-name") #descending order
# print(b)

# ----------------------------------------

# # to count the data
# # b = Book.objects.all().count()
# b = Book.objects.count()
# print(b)

# -----based on idexing------

# # b = Book.objects.all()[0]
# b = Book.objects.all()[24]
# print(b.id)

# b = Book.objects.all()[1:6]
# print(b)                       #for multiple data we cant give the id

# -----------------------------------------

# ---assecing the ids which is inside the list--
# l = [i for i in range(1,16)]
# books = Book.objects.filter(id__in=l)
# print(books)

# -----------------------------------------------
# ------creating a bulk---more rhan one

# Book.objects.bulk_create([
# Book(name="mathematics1",auther=" A rajas",quantity=222,price=5567),
# Book(name="mathematics2",auther="B rajas",quantity=225,price=5657),
# Book(name="mathematics3",auther="C rajas",quantity=225,price=5677),
# Book(name="mathematics4",auther="D rajas",quantity=262,price=56700),
# Book(name="mathematics5",auther="E rajas",quantity=2882,price=5867)])

# ------------------------------------------

# updating multiple data using filter
# Book.objects.filter(id__in=[26,27,28,29,30]).update(price=900)
# ----------------------------------

# we are creating a UI----we write a bussiness logic in views.py file--





