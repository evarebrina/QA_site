from urlparse import parse_qs


def wsgi_application(environ, start_response):
	qs = parse_qs(environ['QUERY_STRING'])
	body =''
	for header in qs:
		for value in qs[header]:
			body += header + "=" + value +'\n'
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	start_response(status, headers)
	return [body]

