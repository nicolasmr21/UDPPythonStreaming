import socket
import time
import cv2
import numpy as np
import base64
import pickle

HEADERSIZE = 4

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1"
port = 49001

def start_video():
    a = True

    #cv2.startWindowThread()
    try:
        while True: 
            data, client = s.recvfrom(2**16)
            if data is None:
                break
            print(len(data))
            nparr = np.frombuffer(pickle.loads(data), np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            #encoded_frame = data[HEADERSIZE:]
            #encoded_frame = data[1]
            #frame = base64.b64decode(encoded_frame)
            if a:
                cv2.imshow('Ad', frame)
            elif not a:
            	break    
          
            k = cv2.waitKey(33)
            if k==27:    # Esc key to stop
                s.sendto(bytes("dis", "utf-8"),(ip,port))
                a=False
                cv2.destroyAllWindows()

    except Exception as e:
        print(e)


    cv2.destroyAllWindows()
    s.close()

def main():
    s.sendto(bytes("connect", "utf-8"),(ip,port))
    print(f'[+] Connected to server...')
    start_video()

main()
