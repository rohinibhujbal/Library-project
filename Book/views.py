from django.shortcuts import render,redirect
from Book.models import Book
from django.http import HttpResponse
# Create your views here.

# html--is hypertext markup language--
# render--we use to pass the data
# http--hypertxt transfer protocal
# browser acts as an client
# by default port is 8000
#

def homepage(request):  #view-for logic--function base view- #http reques accept-#user-defined function
    # all_books = Book.objects.all().filter(is_deleted='N')
    all_books = Book.active_objects.all()  #through custom manager

    # print(all_books)
    return render(request, template_name='home.html',context={"books":all_books})              #created file

def save_book(request):
    # print("in save book")
    # print(request.POST)
    b_name = request.POST.get("name")
    b_auther = request.POST.get("auther")
    b_quantity = request.POST.get("quantity")
    b_price = request.POST.get("price")
    b_published = request.POST.get("is_published")

    if b_published == 'on':
        flag = True
    else:
        flag = False

    if request.POST.get("id"):
        book_obj = Book.objects.get(id=request.POST.get("id"))
        book_obj.name = b_name
        book_obj.auther = b_auther
        book_obj.quantity = b_quantity
        book_obj.price = b_price
        book_obj.is_published = flag
        book_obj.save()
        return redirect('welcome')
    else:
        if b_published == 'on':
            flag = True
        else:
            flag = False

        b = Book(name=b_name,auther=b_auther,quantity=b_quantity,price=b_price,is_published=flag)
        b.save()
        return redirect('welcome')

def edit_book(request,id):      #primary key
    try:   
        book_obj = Book.objects.get(id=id)
    except Exception:
        msg = f"no book found for id :- {id}"
        return HttpResponse(msg)

    book_obj = Book.objects.get(id=id)
    # all_books = Book.objects.all().filter(is_deleted='N')
    all_books = Book.active_objects.all()
    return render(request, template_name='home.html',context={"book":book_obj,"books":all_books})              #created file

def delete_book(request,pk):
    book_obj = Book.objects.get(id=pk)
    # book_obj.delete()
    book_obj.is_deleted = 'Y'
    book_obj.save()
    return redirect('welcome')

def hard_delete_book(request,pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.delete()
    return redirect('welcome')

def restore_book(request,id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted = 'N'
    book_obj.save()
    return redirect('welcome')

def show_deleted_data(request):
    all_deleted_books = Book.inactive_objects.all()
    return render(request,template_name='home.html',context={'books':all_deleted_books})

def restore_all(request):
    all_books = Book.objects.all()
    for i in range(len(all_books)):
        all_books[i].is_deleted = 'N'
        all_books[i].save()
    return redirect('welcome')

def delete_all(request):
    all_books= Book.inactive_objects.all()
    all_books.delete()
    return redirect('welcome')







