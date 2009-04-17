import os
import simplejson as json

class MessageBoard:
    def __init__(self, filename):
        self.filepath = os.path.join ('./store',
                                      'messageboard-%s' % filename)
        open(self.filepath,'a').close()

    def write(self, writable):
        file = open(self.filepath,'w')
        writable_json = json.dumps(writable, indent=4) 
        file.write(writable_json)
        file.close()
        return None
    
    def read(self):
        file = open(self.filepath,'r')
        readable_json = file.read()
        file.close()
        try:
            readable = json.loads(readable_json)
        except ValueError:
            readable = None 
        return readable

loop = MessageBoard('loop.txt')
