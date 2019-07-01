def wsgi_application(environ, start_response):
        body = [bytes(i+"\n", "utf8") for i in environ['QUERY_STRING'].split('&')]
        status = '200 OK'
        headers = [
                ('Content-Type', 'text/plain')                                  
        ]
        start_response(status, headers)                                         
        return body     

def test_print(status, headers):
	print(status)
	print(headers)


wsgi_application({'QUERY_STRING': 'x=1&x=2&y=3',}, test_print)
