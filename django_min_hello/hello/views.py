from django.http import HttpResponse
from django.template import Context, Template

def hello(request):
    return HttpResponse("Hello from Django (without middleware)")


t1 = Template('Hello {{ name }}')
c1 = Context({ 'name': 'brian' })
def render_name(request):
    return HttpResponse(t1.render(c1))

data = []
data.append( [1, 2, 3, 4, 5, 6] )
data.append( ["Cat", "Fish", "Dog", "Aardvark", "Wallaby", "Zebra"] )
data.append( [1998, 1998, 1999, 2000, 2000, 2001] )
data.append( [1, 2, 1, 1, 1, 3] )


t2 = Template('''<html><head><title>Sample rendering</title></head><body>
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

c2 = Context({ 'data': data })
def hello_table(request):
    return HttpResponse(t2.render(c2))

import random
s = set()
for n in xrange(1000):
    s.add(random.randint(0, 2000))

def lookup(request):
    count = 0
    for n in range(1000):
        if n in s:
            count += 1
    return HttpResponse("Did lookups, found: %s" % count)


