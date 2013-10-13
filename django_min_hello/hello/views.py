from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello from Django (without middleware)")

data = []
data.append( [1, 2, 3, 4, 5, 6] )
data.append( ["Cat", "Fish", "Dog", "Aardvark", "Wallaby", "Zebra"] )
data.append( [1998, 1998, 1999, 2000, 2000, 2001] )
data.append( [1, 2, 1, 1, 1, 3] )

from django.template import Context, Template
t = Template('''<html><head><title>Sample rendering</title></head><body>
<table>
{% for row in data%}
    <tr>
        <td>{{ row.0 }}</td>
        <td>{{ row.1 }}</td>
        <td>{{ row.2 }}</td>
        <td>{{ row.3 }}</td>
        <td>{{ row.4 }}</td>
        <td>{{ row.5 }}</td>
    </tr>
{% endfor %}
</table>
</body><html>''')

c = Context({ 'data': data })
def hello_table(request):
    return HttpResponse(t.render(c))

