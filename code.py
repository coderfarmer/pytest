#!/usr/bin/env python
# coding: utf-8

import web

urls = (
  '/', 'hello',
  '/bye/', 'bye')


app = web.application(urls, globals())
render = web.template.render('templates/')

class hello:
    def GET(self):
	    return render.hello("Templates demo", "Hello", "A long time ago...")
        #return 'Hello, web!'
class bye:
    def GET(self):
        return render.bye("Templates demo", "Bye", "14", "8", "25", "42", "19")	
        #return 'Bye, web!'
		
if __name__ == "__main__":
    app.run()