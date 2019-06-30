from urlparse import parse_qs


def wsgi_application(environ, start_response):
	qs = parse_qs(environ['QUERY_STRING'])
	body =''
	for item in qs:
		body += item + "=" + qs[item][0] +'\n'
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	start_response(status, headers)
	return [body]

