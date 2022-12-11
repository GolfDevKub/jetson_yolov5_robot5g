 # YOLOv5 🚀 by Ultralytics, GPL-3.0 license

import argparse
import os
import sys
from pathlib import Path
import pyrealsense2 as rs
import numpy as np
import cv2
import torch
import torch.backends.cudnn as cudnn
#import time
#from time import sleep,time
#from time import time
from time import sleep
from time import *             #meaning from time import EVERYTHING
import time

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from models.common import DetectMultiBackend
from utils.datasets import IMG_FORMATS, VID_FORMATS, LoadImages, LoadStreams
from utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, time_sync

#mqtt import 
from calendar import c
import paho.mqtt.client as mqtt
import random
import json
import requests

#google drive
from google_drive_backup import delete_file, upload_drive, upload_drive_excel, upload_and_delete
#from time import sleep,time
from datetime import datetime

#centroid
import ctksum
import xlsx

#--------------------------------------------------------------------------------------------------------------------------
#                                                  START RUN ROBOT 5G 
#                                                     (Welcome)
#
#                                                 Thank you Supporters
#
#                                           DPU University , AIS 5G , HUAWEI
#--------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------
#                                            OPEN CENTROIDTRACKER_PERSON 

OPEN_CENTROIDTRACKER_PERSON = True      # ON = True , OFF = False
OPEN_CENTROIDTRACKER_MASK = True        # ON = True , OFF = False
OPEN_CENTROIDTRACKER_NOMASK = True      # ON = True , OFF = False
OPEN_CENTROIDTRACKER_WRONGMASK = True   # ON = True , OFF = False
#--------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------
#                                              SEND INFORMATION TO WEB

SEND_DENSITY_TXT = True                 # ON = True , OFF = False
SEND_ON_STOP = True                     # ON = True , OFF = False
SEND_STATUS = True                      # ON = True , OFF = False

UPLOAD_DATA_EXCEL = True                # ON = True , OFF = False
UPLOAD_PICTURE_DRIVE_TIME = True        # ON = True , OFF = False
UPLOAD_PICTURE_DRIVE_PERSON = False      # ON = True , OFF = False
#--------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------
#                                          Show DRAW TEXT CIRCLE RACTANGLE

SHOW_TEXT_XYZ = True                    # ON = True , OFF = False
SHOW_COLOR_RACTANGLE = True             # ON = True , OFF = False
SHOW_TEXT_INFORMATION = True            # ON = True , OFF = False
#--------------------------------------------------------------------------------------------------------------------------
def Convert_Json():
    global MQTT_MSG
    MQTT_MSG=json.dumps({
        "Density" : person_current,             #ความหนาแน่นคนในพื้นที่
        "Count_Density": count_people,          #จำนวนคนที่เจอทั้งหมด
        "Count_Mask": count_mask,               #count mask
        "Count_Nomask": count_nomask,           #count mask fail
        "Count_Wrongmask": count_wrongmask,     #count wrong mask
        "Count_Person": count_people_density,   #จำนวนคนที่เจอ ณ ขณะนั้น
        "Seq_Patrol": seq_patrol                #check status working
        })

def Convert_Jstop():
    global MQTT_MST
    MQTT_MST=json.dumps({
        "Stop": stop  #count density
        })

#funtion mqtt
def on_connect(self, client, userdata, rc):
    print("MQTT Connected.")
        
def on_message1(client, userdata,msg):
    print("Test")
    
def on_publish(client, userdata, mid):
    countpub = format(mid)

#mqtt
host = "broker.hivemq.com"
port = 1883  

print("start")
client = mqtt.Client()
client.connect(host)
client.on_connect = on_connect
client.on_message = on_message1
client.on_publish = on_publish   

client.loop_start() 

font = cv2.FONT_HERSHEY_SIMPLEX

DATA_PEOPLE = []
DATA_MASK = []
DATA_NOMASK = []
DATA_WRONGMASK = []
DATA_DENSITY = ''

@torch.no_grad()
def run(weights=ROOT / 'detect_two.pt',  # model.pt path(s)
        source=ROOT / 'data/images',  # file/dir/URL/glob, 0 for webcam
        data=ROOT / 'data/coco128.yaml',  # dataset.yaml path
        imgsz=(416, 224 ),  # inference size (height, width)
        conf_thres=0.25,  # confidence threshold
        iou_thres=0.45,  # NMS IOU threshold
        max_det=600,  # maximum detections per image
        device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
        view_img=False,  # show results
        save_txt=False,  # save results to *.txt
        save_conf=False,  # save confidences in --save-txt labels
        save_crop=False,  # save cropped prediction boxes
        nosave=False,  # do not save images/videos
        classes=None,  # filter by class: --class 0, or --class 0 2 3
        agnostic_nms=False,  # class-agnostic NMS
        augment=False,  # augmented inference
        visualize=False,  # visualize features
        update=False,  # update all models
        project=ROOT / 'runs/detect',  # save results to project/name
        name='exp',  # save results to project/name
        exist_ok=False,  # existing project/name ok, do not increment
        line_thickness=3,  # bounding box thickness (pixels)
        hide_labels=False,  # hide labels
        hide_conf=False,  # hide confidences
        half=False,  # use FP16 half-precision inference
        dnn=False,  # use OpenCV DNN for ONNX inference
        ):
    source = str(source)
    save_img = not nosave and not source.endswith('.txt')  # save inference images
    is_file = Path(source).suffix[1:] in (IMG_FORMATS + VID_FORMATS)
    is_url = source.lower().startswith(('rtsp://', 'rtmp://', 'http://', 'https://'))
    webcam = source.isnumeric() or source.endswith('.txt') or (is_url and not is_file)
    if is_url and is_file:
        source = check_file(source)  # download

    # Directories
    save_dir = increment_path(Path(project) / name, exist_ok=exist_ok)  # increment run
    (save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir

    # Load model
    print("device" + str(device))
    device = select_device(device)
    model = DetectMultiBackend(weights, device=device, dnn=dnn, data=data)
    stride, names, pt, jit, onnx, engine = model.stride, model.names, model.pt, model.jit, model.onnx, model.engine
    imgsz = check_img_size(imgsz, s=stride)  # check image size

    # Half
    half &= (pt or jit or engine) and device.type != 'cpu'  # half precision only supported by PyTorch on CUDA
    if pt or jit:
        model.model.half() if half else model.model.float()

    # Dataloader
    if webcam:
        view_img = check_imshow()
        cudnn.benchmark = True  # set True to speed up constant image size inference
        dataset = LoadStreams(source, img_size=imgsz, stride=stride, auto=pt)
        bs = len(dataset)  # batch_size
    else:
        dataset = LoadImages(source, img_size=imgsz, stride=stride, auto=pt)
        bs = 1  # batch_size
    vid_path, vid_writer = [None] * bs, [None] * bs

    # Run inference
    model.warmup(imgsz=(1, 3, *imgsz), half=half)  # warmup
    dt, seen = [0.0, 0.0, 0.0], 0

    config = rs.config()
    config.enable_stream(rs.stream.color, 424, 240, rs.format.bgr8, 30)
    config.enable_stream(rs.stream.depth, 424, 240, rs.format.z16, 30)

    pipeline = rs.pipeline()
    profile = pipeline.start(config)

    align_to = rs.stream.color
    align = rs.align(align_to)

    intr = profile.get_stream(rs.stream.color).as_video_stream_profile().get_intrinsics()

    Status1 = 0
    Status2 = 0
    pTime = 0

    import time  
    #count_density = 0

    while(True):

        global seq_patrol, stop
        stop = 0

        global DATA_PEOPLE, DATA_MASK, DATA_NOMASK, DATA_WRONGMASK, DATA_DENSITY, DATA_COUNT_DENSITY
    
        data_mask = len(DATA_MASK)
        data_nomask = len(DATA_NOMASK)
        data_wrongmask = len(DATA_WRONGMASK)   
        data_people = len(DATA_PEOPLE) 
        data_density = DATA_DENSITY

        global count_mask
        count_mask = 0
        global count_nomask
        count_nomask = 0
        global count_wrongmask
        count_wrongmask = 0
        global count_people
        count_people = 0

        global person_current
        person_current = ''

        global count_people_density
        count_people_density = 0

        count_density = 0


        '''RECTS_PERSON = []
        RECTS_MASK = []
        RECTS_NOMASK = []
        RECTS_WRONGMASK = []'''

        RECTS = []

        #t0 = time.time()
        now = datetime.today()
        date = now.strftime("%d-%m-%Y")
        HMS = now.strftime("%H.%M.%S")
        H = int( now.strftime("%H") )
        M_S = float( now.strftime("%M.%S") )

        frames = pipeline.wait_for_frames()

        aligned_frames = align.process(frames)
        color_frame = aligned_frames.get_color_frame()
        depth_frame = aligned_frames.get_depth_frame()
        if not depth_frame or not color_frame:
            continue

        img = np.asanyarray(color_frame.get_data())
        im = img[8:232,4:420]
        depth_image = np.asanyarray(depth_frame.get_data())

        # Letterbox
        im0 = im.copy()
        im = im[np.newaxis, :, :, :]        

        # Stack
        im = np.stack(im, 0)

        # Convert
        im = im[..., ::-1].transpose((0, 3, 1, 2))  # BGR to RGB, BHWC to BCHW
        im = np.ascontiguousarray(im)

        t1 = time_sync()
        im = torch.from_numpy(im).to(device)
        im = im.half() if half else im.float()  # uint8 to fp16/32
        im /= 255  # 0 - 255 to 0.0 - 1.0
        if len(im.shape) == 3:
            im = im[None]  # expand for batch dim
        t2 = time_sync()
        dt[0] += t2 - t1

        # Inference
        path = ''
        visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if visualize else False
        pred = model(im, augment=augment, visualize=False)
        t3 = time_sync()
        dt[1] += t3 - t2

        # NMS
        pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)
        dt[2] += time_sync() - t3

        # Process predictions
        for i, det in enumerate(pred):  # per image
            seen += 1

            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            imc = im0.copy() if save_crop else im0  # for save_crop
            annotator = Annotator(im0, line_width=line_thickness, example=str(names))

            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(im.shape[2:], det[:, :4], im0.shape).round()
                #print()
                # Write results
                for *xyxy, conf, cls in reversed(det):
                    c = int(cls)  # integer class
                    label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
                    #print(names[c])
                    box = [ int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3]) ] #x,y,w,h
                    boxs = np.array(box)
                    circle = ( (box[0] + box[2]) / 2, (box[1] + box[3]) / 2 )
                    RECTS.append(boxs)
                    #print(boxs)
                    if(OPEN_CENTROIDTRACKER_PERSON == True):
                        if(names[c] == 'person'):
                            #RECTS_PERSON.append(boxs)
                            ctksum.count_current_person(RECTS, im0, 0, DATA_PEOPLE, 0, 0, 0,  now, data_people)
                            count_density += 1   
                            #print(count_density)                                 

                            '''if circle[0] < 60 or circle[0] > 356:
                            #count_people -= 1
                            data_people += 1
                            #count_people = data_people'''
                    
                            count_people_density = count_density

                            if(UPLOAD_PICTURE_DRIVE_PERSON == True):
                                now = datetime.today() 
                                name = now.strftime("%H.%MTime%d-%m-%YDate"+'.jpg') 
                                cv2.imwrite(name,im0)                       
                                upload_drive(name)
                                os.remove(name)


                    if(OPEN_CENTROIDTRACKER_MASK == True):
                        if(names[c] == 'mask'):
                            #RECTS_MASK.append(boxs)
                            ctksum.count_current_mask(RECTS, im0, 0, DATA_MASK, 0, 0, 0,  now)

                            '''if circle[0] < 60 or circle[0] > 356:
                            #count_mask -= 1
                            data_mask += 1
                            #count_mask = data_mask'''
                    
                    if(OPEN_CENTROIDTRACKER_NOMASK == True):
                        if(names[c] == 'no mask'):
                            #RECTS_NOMASK.append(boxs)
                            ctksum.count_current_nomask(RECTS, im0, 0, DATA_NOMASK, 0, 0, 0,  now)

                            '''if circle[0] < 60 or circle[0] > 356:
                            #count_nomask -= 1
                            data_nomask += 1
                            #count_nomask = data_nomask'''

                    if(OPEN_CENTROIDTRACKER_WRONGMASK == True):
                        if(names[c] == 'wrong mask'):
                            #RECTS_WRONGMASK.append(boxs)
                            ctksum.count_current_wrongmask(RECTS, im0, 0, DATA_WRONGMASK, 0, 0, 0,  now)

                            '''if circle[0] < 60 or circle[0] > 356:
                            #count_wrongmask -= 1
                            data_wrongmask += 1
                            #count_wrongmask = data_wrongmask'''

                    #print(count_one)  
                    #Person_current = count_one
                    if count_density > 9 :
                       num_txt = 'มาก'
                    if count_density > 4 and count_density < 9 :
                       num_txt = 'ปานกลาง'
                    if count_density < 4 :
                       num_txt = 'น้อย'

                    data_density = DATA_DENSITY.replace('', num_txt)

                    if(SEND_DENSITY_TXT == True):
                        person_current = data_density
                        #print(person_current)

                    if(SHOW_COLOR_RACTANGLE == True):
                        annotator.box_label(xyxy, label, color=colors(c, True)) # rectangle color

                    x = int((xyxy[0] + xyxy[2])/2)
                    y = int((xyxy[1] + xyxy[3])/2)
                    #'''
                    dist = depth_frame.get_distance(x + 4, y + 8)*600
                    Xtarget = dist*(x+4 - intr.ppx)/intr.fx - 35 #the distance from RGB camera to realsense center
                    Ytarget = dist*(y+8 - intr.ppy)/intr.fy
                    Ztarget = dist
                    coordinate_text = "(" + str(round(Xtarget)) + ", " + str(round(Ytarget)) + ", " + str(round(Ztarget)) + ")"

                    #print((round(Ztarget*1.70)) / 10, "cm")
                    distance_cm = (round(Ztarget*1.70)) / 10
                    #print(type(distance_cm))
                    
                    if(SEND_ON_STOP == True):
                        if (distance_cm <= 65):
                            stop = 1
                        else:
                            stop = 0    
                        #print(stop)
                        #print(distance_cm)

                        Convert_Jstop() # put after
                        client.publish("Robot5G/All/Stop",MQTT_MST)      

                    if(SHOW_TEXT_XYZ == True):
                        cv2.putText(im0, text=coordinate_text, org=(int((xyxy[0] + xyxy[2])/2), int((xyxy[1] + xyxy[3])/2)),
                        fontFace = font, fontScale = 0.5, color=(255,255,255), thickness=2, lineType = cv2.LINE_AA) #show distance to desktop


        minute =  M_S * 60

        if(UPLOAD_DATA_EXCEL == True):
            if(minute <= 3599.0 and minute >= 3598.0): # 3598.0 - 3599.0 
                xlsx.excel_upload_text(date, data_people,HMS, 'data_people.xlsx')
                xlsx.excel_upload_text(date, data_mask, HMS, 'data_mask.xlsx')
                xlsx.excel_upload_text(date, data_nomask, HMS, 'data_nomask.xlsx')
                xlsx.excel_upload_text(date, data_wrongmask, HMS, 'data_wrongmask.xlsx')

                data_people = 0
                data_mask = 0
                data_nomask = 0
                data_wrongmask = 0
                print(data_people)

                #print(data_people)

                #upload excel to googlo drive
                upload_and_delete("data_mask.xlsx")
                upload_and_delete("data_nomask.xlsx")
                upload_and_delete("data_wrongmask.xlsx")
                upload_and_delete("data_people.xlsx")

        Status1 += 1
        Status2 += 1
        #print(Status1)
        if(UPLOAD_PICTURE_DRIVE_TIME == True):
            if(Status1 == 3600):
                now = datetime.today() 
                name = now.strftime("%H.%MTime%d-%m-%YDate"+'.jpg') 
                cv2.imwrite(name,im0)                       
                upload_drive(name)
                os.remove(name)

                Status1 = 0
        
        if(SEND_STATUS == True):
            if(Status2 == 30):
                count_people = data_people
                count_mask = data_mask
                count_nomask = data_nomask
                count_wrongmask = data_wrongmask
                #person_current = data_density

                Convert_Json() # put after
                client.publish("Robot5G/Jetson2/Mask",MQTT_MSG)  

                #print(Status2)
                Status2 = 0

            seq_patrol = Status2  
          
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        #cv2.putText(im0, 'density' + ': ' + str(count_density), (20,20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1) 
        #cv2.putText(im0, 'person' + ': ' + str(data_people), (220,20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
        #cv2.putText(im0, 'mask' + ': ' + str(data_mask), (220,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
        #cv2.putText(im0, 'no mask' + ': ' + str(data_nomask), (220,80), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
        #cv2.putText(im0, 'wrong mask' + ': ' + str(data_wrongmask), (220,110), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)

        if(SHOW_TEXT_INFORMATION == True):
            cv2.putText(im0,'density' + ': ' + str(count_density), org=(340, 15), fontFace = font, fontScale = 0.3, color=(255,255,255),thickness=1,lineType = cv2.LINE_AA) 
            cv2.putText(im0,'person'+': '+str(data_people), org=(340, 30), fontFace = font, fontScale = 0.3, color=(255,255,255), thickness=1, lineType =cv2.LINE_AA)
            cv2.putText(im0,'mask' + ': ' + str(data_mask),org=(340, 45), fontFace = font, fontScale = 0.3, color=(255,255,255), thickness=1, lineType = cv2.LINE_AA)
            cv2.putText(im0,'no mask' + ': ' + str(data_nomask), (340,60), fontFace = font, fontScale = 0.3, color=(255,255,255), thickness=1, lineType = cv2.LINE_AA)
            cv2.putText(im0,'wrong mask' + ': ' + str(data_wrongmask), org=(340, 75), fontFace = font,fontScale =0.3,color=(255,255,255),thickness=1,lineType = cv2.LINE_AA)
            cv2.putText(im0,f'FPS: {int(fps)}', org=(340, 90), fontFace = font,fontScale =0.3,color=(255,255,255),thickness=1,lineType = cv2.LINE_AA)

            cv2.line(im0, (30, 0), (30, 224),(0,0,255),1)
            cv2.line(im0, (396, 0), (396, 224),(0,0,255),1)

        cv2.imshow("IMAGE", im0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 


if __name__ == "__main__":
    run()

#--------------------------------------------------------------------------------------------------------------------------------------------
#                                                                 End Code
#                                                                (Robot 5G)
#                                                                    (: 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#--------------------------------------------------------------------------------------------------------------------------------------------
#############################################################################################################################################
#############################################################################################################################################
