from django.http import HttpResponse

temp = """
    <ol>
        <li>GFG: <a href="https://www.geeksforgeeks.org/">GeeksforGeeks</a></li> <br>
        <li>Tutorials Point: <a href="https://www.tutorialspoint.com/index.htm">Tutorials Point</a></li> <br>
        <li>Django: <a href="https://docs.djangoproject.com/en/5.0/">Django Documentation</a></li> <br>
    </ol>
"""
def index(request):
    return HttpResponse(temp)

