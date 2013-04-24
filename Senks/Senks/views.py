from django.template.loader import get_template

from django.template import Context

from django.http import HttpResponse

from django.shortcuts import render_to_response

import datetime


def current_datetime(request):
	current_datetime = datetime.datetime.now()
	return render_to_response('current_datetime.html', locals())

#def current_datetime(request):
#	now = datetime.datetime.now()
#	t = get_template('current_datetime.html')
#	html = t.render(Context({'current_datetime' : now}))
	#html = "<html><body><h1><center>It is now %s. </center></h1></body></html>" % now
#	return HttpResponse(html)

#def hours_ahead(request, offset):
#	offset = int(offset)
#	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#	html = "<html><body><h1><center>In %s hours(s), it will be %s. </center></h1></body></html>" % (offset, dt)
#	return HttpResponse(html)
