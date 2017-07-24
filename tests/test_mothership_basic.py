import socket
import unittest
import threading
from workers.basic_worker import *
from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):
    def test_basic_server_connection(self):

        mother = MothershipServer()
        mother_thread = threading.Thread(target = mother.run, args= (), daemon = True)
        #mother_thread.start()
        self.assertRaises(ValueError, mother_thread.start)
        #self.assertRaises(ValueError, mother.run)
        #maybe assert error on thread.start
        #self.assertRaises(ValueError, mother.run)

        worker = BasicUserParseWorker("https://www.reddit.com/user/Chrikelnel")
        worker.results = {}
       # self.assertEqual(bool(worker.results), True)
       # worker.send_to_mother(worker.results, worker.original_target)

    
        address = settings.MOTHERSHIP.get('host', 'localhost')
        port = settings.MOTHERSHIP.get('port', 8080)

        addr = (address, port)

        sock = socket.socket()
        sock.connect(addr)

        data = {}
        data_s = json.dumps(data)
        
    #    sock.send(bytes([]))
     #   sock.send(data_s.encode('utf-8'))
       # sock.send(bytes("", 'ascii'))
   #     mother.buff_size = None  
        sock.send(bytes("\00", 'ascii'))
      #  sock.write(sock, "", 0); )

       # self.assertRaises(ValueError, mother.handle_worker_contact, sock, addr)

    #    raise ValueError('No Value Given')

        sock.close()


   #  worker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   #  worker.close()
     
    
   
  


if __name__ == '__main__':
    unittest.main()
   
