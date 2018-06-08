"""
UCSC DevOps Class

Assignment 04 - Microservices and Vagrant 

DevOps, Assignment 04 
Create a simple file retrieval service that consists of two Microservices and a Client. The following depicts the architecture:
Client (Bash shell script) --> FrontEnd Microservice --> BackEnd Microservice

BackEnd Micorservice
The backend, BackEnd, is a simple Python program running in Nameko that has one method:
getFileContents(name-of-file) – return the contents of a file
In a subdirectory named “files”, which resides under the directory where BackEnd.py is, create 4 text files: a.txt, b.txt, c.txt, d.txt
 Put different text into each file.
To get the contents of file a.txt, a caller calls getFileContents(“a.txt”), to get the contents of b.txt, the caller calls getFileContents(“b.txt”), etc.
The BackEnd microservice must run in a Vagrant-based Ubuntu 16.04 VM. So, besides writing the code for the microservice, you must also write the vagrant file and the provisioning code needed to install Python 3, Nameko, and any other dependencies that are needed.

FrontEnd Microservice

The frontend microservice, FrontEnd, is a simple Python-based HTTP object that receives an HTTP request to get a specific file – a.txt, b.txt, c.txt, d.txt. This Python module is integrated into Nameko to receive the HTTP requests.
You only have to handle requests for files that exist. When a request comes in, the FrontEnd code needs to parse the request and call getFileContents in the BackEnd microservice, to get the requested file
When the FrontEnd microservice gets the return from the BackEnd microservice, it returns the file contents (returned by getFileContents) within the HTTP response it sends back to the client.
The FrontEnd microservice must run in a Vagrant-based Ubuntu 16.04 VM. So, besides writing the code for the microservice, you must also write the vagrant file and the provisioning code needed to install Python 3, Nameko, and any other dependencies that are needed.


http_service.py
"""
import os

path = os.path.join('/Mic/UCSC/DevOps/Assignment/assign041', 'files')
#path = os.path.join('/Mic/UCSC/Python/Files/section 5-classes/section 5-classes', 'files')


class getFileContents:
    
    def __init__(self, name):
        self.name = name
        
    def getFile(self):

        os.chdir(path)
        fo = open(self.name, 'r')
        n = 0
        lista = []

        for i in fo.readlines():
            str1 = str(i)
            print str1
            lista.append(str1)          
        fo.close()  
        
        return lista


"""
getFileContent.py

"""
import getFileContent
import json
from nameko.web.handlers import http
import http_service

class HttpService:
   name = "http_service"

   @http('GET', '/get/<value>')
   def get_method(self, request, value):
      a = getFileContent.getFileContents(value)
      b = a.getFile()
      #b = value
      return json.dumps(b)

   @http('POST', '/post')
   def do_post(self, request):
      return u"received: {}".format(request.get_data(as_text=True))
