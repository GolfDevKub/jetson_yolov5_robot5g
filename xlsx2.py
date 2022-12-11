from datetime import datetime
import pandas as pd
import numpy as np

def date_time_people(count, now):

    now_time = now
    H = int(now_time.strftime("%H"))
    M = int(now_time.strftime("%M"))
    S = int(now_time.strftime("%S"))
    #print(S)

    if H == 6 and M == 46   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_people.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_people.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()

    if H == 2 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_people.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_people.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()

    if H == 4 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_people.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_people.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()

    if H == 6 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_people.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_people.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()  

    if H == 8 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_people.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_people.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()              

    if H == 10 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_people.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_people.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()

    if H == 12 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_people.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_people.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()

    if H == 14 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_people.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_people.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()

    if H == 16 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_people.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_people.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()        

    if H == 18 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_people.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_people.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()

    if H == 20 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_people.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_people.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()

    if H == 22 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_people.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_people.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def date_time_mask(count, now):

    now_time = now
    H = int(now_time.strftime("%H"))
    M = int(now_time.strftime("%M"))
    S = int(now_time.strftime("%S"))
    #print(S)

    if H == 1 and M == 52   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_mask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_mask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()        

    if H == 2 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_mask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_mask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save() 

    if H == 4 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_mask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_mask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save() 

    if H == 6 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_mask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_mask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save() 

    if H == 8 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_mask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_mask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save() 

    if H == 10 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_mask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_mask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save() 

    if H == 12 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_mask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_mask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save() 

    if H == 14 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_mask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_mask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save() 

    if H == 16 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_mask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_mask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save() 

    if H == 18 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_mask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_mask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save() 

    if H == 20 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_mask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_mask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save() 

    if H == 22 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_mask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_mask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save() 

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

def date_time_nomask(count, now):

    now_time = now
    H = int(now_time.strftime("%H"))
    M = int(now_time.strftime("%M"))
    S = int(now_time.strftime("%S"))
    #print(S)

    if H == 6 and M == 33   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_nomask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_nomask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()        

    if H == 2 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_nomask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_nomask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()  

    if H == 4 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_nomask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_nomask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()  

    if H == 6 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_nomask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_nomask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()  

    if H == 8 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_nomask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_nomask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()  

    if H == 10 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_nomask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_nomask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()  

    if H == 12 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_nomask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_nomask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()  

    if H == 14 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_nomask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_nomask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()  

    if H == 16 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_nomask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_nomask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()  

    if H == 18 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_nomask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_nomask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()  

    if H == 20 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_nomask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_nomask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()  

    if H == 22 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_nomask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_nomask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()  

#-----------------------------------------------------------------
#-----------------------------------------------------------------

def date_time_wrongmask(count, now):

    now_time = now
    H = int(now_time.strftime("%H"))
    M = int(now_time.strftime("%M"))
    S = int(now_time.strftime("%S"))
    #print(S)

    if H == 1 and M == 52   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_wrongmask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_wrongmask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()      

    if H == 2 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_wrongmask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_wrongmask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()          

    if H == 4 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_wrongmask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_wrongmask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()  

    if H == 6 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_wrongmask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_wrongmask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()        

    if H == 8 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_wrongmask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_wrongmask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()

    if H == 10 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_wrongmask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_wrongmask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()     

    if H == 12 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_wrongmask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_wrongmask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()           

    if H == 14 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_wrongmask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_wrongmask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()        

    if H == 16 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_wrongmask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_wrongmask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save() 

    if H == 18 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_wrongmask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_wrongmask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()   

    if H == 20 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_wrongmask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_wrongmask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()                    

    if H == 22 and M == 0   :

        print('Ok')

        # อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
        readDataframe = pd.read_excel (r'data_wrongmask.xlsx')

        # สร้างข้อมูลใหม่เป็นข้อมูลของ orange
        newDataframe = pd.DataFrame({'date-time' : [now], 'density' : [count]})
        
        # นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
        frames = [readDataframe, newDataframe]
        result = pd.concat(frames)
        
        # สร้าง Writer เหมือนกับตอนเขียนไฟล์
        writer = pd.ExcelWriter('data_wrongmask.xlsx', engine='xlsxwriter')
        
        # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
        result.to_excel(writer, index = False)
        writer.save()        

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------        
