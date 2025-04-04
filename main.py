# from dotenv import load_dotenv
import time
import socket
import json
# import random
from concurrent import futures
from src.handlers.modelos import handlers_modelos

HOST = '127.0.0.1' 
PORT = 65432  

#base de datos init
from src.DB.mongoDB.config.init import check_mongo_is_running



def tcpServer():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor TCP escuchando en {HOST}:{PORT}")
        try:        
            while True:
                conn, addr = s.accept()  
                print("Conectado por:", addr)
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break

                        data_str = data.decode().strip()
                        data_obj = json.loads(data_str)
                        action = data_obj["action"]

                        
                        if action in handlers_modelos:

                            response = handlers_modelos[action](data_obj)
                            response_str = json.dumps(response)
                            conn.sendall(response_str.encode())
                        else:
                            err_message = {
                                "status": 700,
                                "message": "No existe esa accion",
                                "data":{}
                            }
                            response_err = json.dumps({"response": err_message})
                            conn.sendall(response_err.encode())

        except KeyboardInterrupt:
            print("\nServidor detenido manualmente con Ctrl+C")

if __name__ == '__main__':
    # load_dotenv()
    check_mongo_is_running()
    # serve()
    tcpServer()