import django
django.setup()
from online_shopping_system .db.shopping_model.models import BOOK

def create_book(object_book):
    title = object_book['Title']
    pages = object_book['Pages']
    price = object_book['Price']
    author = object_book['Author']
    print ("in create class",title,pages,price,author)
    try:
        book_object=BOOK.objects.create(B_Title=title,
                                        B_pages =pages,
                                        B_Price=price,
                                        B_Author =author )
        return book_object
    except Exception as e:
        print e
        return  None