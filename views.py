from django.http import HttpResponse

def home(request):
   # interate through the dictionary items

    data = {'Name': 'Valerie Goins', 'Track': 'Backend(Python)', 'Message': 'Hello mentors. Thank you for all your help and guidance in making a new career path for me.'}
    print_data = ''

    print_data = '<br>'.join(': '.join((key,val)) for (key,val) in data.items())

    return HttpResponse(print_data)
 