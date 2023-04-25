from ..models import Quote

if __name__ == '__main__':

    cl = Quote.objects.all()
    print(cl)

