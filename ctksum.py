import random
import centroidtracker as ctk
import cv2
from trackable_object import TrackableObject
import xlsx2
from datetime import datetime

import xlsx

ct = ctk.CentroidTracker()

def count_current_person(REC, frame, count, data, 
                number_txt, count2, txt_class, now, data_people):     
    
    '''nowtime = now
    date = nowtime.strftime("%d-%m-%Y")
    H = int( nowtime.strftime("%H") )
    M = int( nowtime.strftime("%M") )'''

    color_rank = []
    while len(color_rank) <= 2:
        rank_c = random.randrange(0,255)
        color_rank.append(rank_c)
    color = (color_rank[0],color_rank[1],color_rank[2]) 
       
    objects = ct.update(REC)
    for (objectID, centroid) in objects.items(): 

        text =  "ID {}".format(objectID)
        #print(text,'person')
        #cv2.putText(frame, text, (centroid[0] -10, centroid[1] -10 ),cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.circle(frame, (centroid[0], centroid[1]), 4, color, -1)

        if(centroid[0] > 30 and centroid[0] < 394):
            if(objectID not in data):
                #count += 1
                data.append(objectID)
                #x = len(data)
                #x += 1
                #xlsx2.date_time_people(x, now)
                #xlsx.data_xlsx_people(x, now)
                #print(now)
                #del data[0]
                #print(data,'person')

            elif(objectID in data) :
                data.pop()  
        elif(objectID not in  data):
            data.append(objectID)
        elif(objectID in data):
            data.pop()        

        '''elif(centroid[0] < 60 or centroid[0] > 356):
            if(objectID in data):
                data.pop()'''             

        count2 = objectID   

def count_current_mask(REC, frame, count, data, 
                number_txt, count2, txt_class, now):   

    color_rank = []
    while len(color_rank) <= 2:
        rank_c = random.randrange(0,255)
        color_rank.append(rank_c)
    color = (color_rank[0],color_rank[1],color_rank[2]) 
   
    objects = ct.update(REC)
    for (objectID, centroid) in objects.items():  
        text =  "ID {}".format(objectID)
        #print(text,'mask')
        #cv2.putText(frame, text, (centroid[0] -10, centroid[1] -10 ),cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.circle(frame, (centroid[0], centroid[1]), 4, color, -1)
    
        if(centroid[0] < 30 or centroid[0] > 394):
            if(objectID not in data):
                #count += 1
                data.append(objectID)
                #x = len(data)
                #x += 1   
                #xlsx2.date_time_mask(x, now)
                #xlsx.data_xlsx_mask(x, now)             
                #del data[0]
                #print(data,'mask')  

            elif(objectID in data):
                data.pop()   
        elif(objectID not in  data):
            data.append(objectID)
        elif(objectID in data):
            data.pop()  

        '''elif(centroid[0] > 60 and centroid[0] < 356):
            if(objectID in data):
                data.pop()'''

        count2 = objectID   

def count_current_nomask(REC, frame, count, data, 
                number_txt, count2, txt_class, now):   

    color_rank = []
    while len(color_rank) <= 2:
        rank_c = random.randrange(0,255)
        color_rank.append(rank_c)
    color = (color_rank[0],color_rank[1],color_rank[2]) 

    objects = ct.update(REC)
    for (objectID, centroid) in objects.items():  
        text =  "ID {}".format(objectID)
        #cv2.putText(frame, text, (centroid[0] -10, centroid[1] -10 ),cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.circle(frame, (centroid[0], centroid[1]), 4, color, -1)
    
        if(centroid[0] < 30 or centroid[0] > 394):
            if(objectID not in data):
                #count += 1
                data.append(objectID)
                #x = len(data)
                #x += 1 
                #xlsx2.date_time_nomask(x, now)
                #xlsx.data_xlsx_nomask(x, now)               
                #del data[0]
                #print(data,txt_class)

            elif(objectID in data):
                data.pop()    
        elif(objectID not in  data):
            data.append(objectID)
        elif(objectID in data):
            data.pop()  

        '''elif(centroid[0] > 60 and centroid[0] < 356):
            if(objectID in data):
                data.pop()'''  

        count2 = objectID    

def count_current_wrongmask(REC, frame, count, data, 
                number_txt, count2, txt_class, now):   

    color_rank = []
    while len(color_rank) <= 2:
        rank_c = random.randrange(0,255)
        color_rank.append(rank_c)
    color = (color_rank[0],color_rank[1],color_rank[2]) 

    objects = ct.update(REC)
    for (objectID, centroid) in objects.items():  
        text =  "ID {}".format(objectID)
        #cv2.putText(frame, text, (centroid[0] -10, centroid[1] -10 ),cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.circle(frame, (centroid[0], centroid[1]), 4, color, -1)
    
        if(centroid[0] < 30 or centroid[0] > 394):
            if(objectID not in data):
                #count += 1
                data.append(objectID)
                #x = len(data)
                #x += 1  
                #xlsx2.date_time_wrongmask(x, now)
                #xlsx.data_xlsx_wrongmask(x, now)              
                #del data[0]
                #print(data,txt_class)
                
            elif(objuectID in data):
                data.pop()    
        elif(objectID not in  data):
            data.append(objectID)
        elif(objectID in data):
            data.pop()  

        '''elif(centroid[0] < 60 and centroid[0] > 356):
            if(objectID in data):
                data.pop()'''   

        count2 = objectID     
