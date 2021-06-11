#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import numpy as np
import cv2

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip="192.168.0.2"
port=4321

while True:
    cap=cv2.VideoCapture(0)
    ret,photo=cap.read()
    ret,photo1 = cv2.imencode(".jpg",photo[:400,:400])
    ds=photo1.tobytes()
    s.sendto(ds, (ip, port))
    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows()
cap.release()

