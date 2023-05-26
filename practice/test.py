import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Hello, webapp2 World!")

app = webapp2.WSGIApplication([("/", MainPage)], debug=True)




# app.yaml
# application: pythonapp
# runtime: python27
# api_version: 1.0
# threadsafe: true # allow multiple threads to access the app

# handlers:
#   - url: /.*
#     script: main.app





#for vm1 to vm2 
#ifconfig
# ls
# touch vai.txt
# cat vai.txt
# nano vai.txt
# ctrl+s ctrl+x
# cat vai.txt
# scp vai.txt vagrant@10.0.2.16:/home/vagrant





