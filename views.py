from django.http import HttpResponse

data={"Name": "Valerie Goins", "Track": "Backend(Python)", "Message": "Hello mentors. Thank you for all your help and guidance in making a new career path for me."}

#Iterate over key, values and print
def home(data):
    for key, value in data.items():
        print_data = key, ":", value
    
    #return HttpResponse(print_data)
    return HttpResponse("Hello")