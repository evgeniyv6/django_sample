from django.template import Template, Context, RequestContext
from django.template.loader import get_template
from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render
import datetime

def dis_meta(req):
    val = req.META.items()
    html=[]
    for k,v in val:
        html.append('<tr><td>{}</td><td>{}</td></tr>'.format(k,v))
    return HttpResponse('<table>{}</table>'.format('\n'.join(html)))

def curdt(req):
    NOW = datetime.datetime.now()
    return render(req, 'curdate.html', {'curdt': NOW, 'i_list': ('Print','per', 'line'), 'company': 'BIGBR'})

def index(req):
    html = "<html><body>About page</body></html>"
    return HttpResponse(html)

def hours_ahead(req, offset):
    NOW = datetime.datetime.now()
    try:
        offset=int(offset)
    except ValueError as exc:
        raise Http404
    dt = NOW+datetime.timedelta(hours=offset)
    return render(req, 'hours_ahead.html',{'offset':offset, 'next_time': dt})

def localsdef():
    p1='param_one'
    p2=datetime.datetime.now()
    print(locals())

if __name__=='__main__':
    localsdef()
