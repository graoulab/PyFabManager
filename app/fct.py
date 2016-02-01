from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.extras.widgets import SelectDateWidget
from django.http import HttpResponse
from django.forms import MultiWidget

def  pagination (data,NbPage = 1):
    paginator = Paginator(data, 5)
    try:
        contacts = paginator.page(NbPage)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return contacts
def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]