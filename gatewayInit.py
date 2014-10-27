#!/usr/bin/env python

import pexpect
import sys
import time
from sensor_calcs import *
import json
import select
import gdpAccess
import sensorTag
from multiprocessing import Process

def main():
    global config
    global barometer


    #init gdp without GCL_name
    sensor1GCL = gdpAccess.GCL(sys.argv[2])
    #sensor2GCL = gdpAccess.GCL("sensor2")
    
     
    tag1 = sensorTag.SensorTag(sys.argv[1], sensor1GCL)
    #tag2 = sensorTag.SensorTag(sys.argv[2], sensor2GCL)

    cbs = sensorTag.SensorCallbacks() 
    command = sys.argv[3]
    
    if (command == "temp"):
        tag1.register_cb(0x25, cbs.tmp006)
        tag1.char_write_cmd(0x29, 0x01)
        tag1.char_write_cmd(0x26, 0x0100)
    
    elif (command == "gyro"):
        tag1.register_cb(0x57, cbs.gyro)
        tag1.char_write_cmd(0x5b, 0x07)
        tag1.write_cmd(0x58, 0x0100)
    
    elif (command == "magnet"):
        tag1.register_cb(0x40, cbs.magnet)
        tag1.char_write_cmd(0x44, 0x01)
        tag1.char_write_cmd(0x41, 0x0100)
    
    elif (command == "accel"):
        tag1.register_cb(0x2d, cbs.accel)
        tag1.char_write_cmd(0x31, 0x01)
        tag1.char_write_cmd(0x2e, 0x0100)
    elif (command == "button"):
        tag1.register_cb(0x6b, cbs.button)
        tag1.char_write_cmd(0x6c, 0x0100)
    


    tag1thread = Process(target=tag1.notification_loop())
    tag1thread.start()
    tag1thread.join()
    while True:
      print "looping"
      
      

      # enable accelerometer
      #tag.register_cb(0x2d,cbs.accel)
      #tag.char_write_cmd(0x31,0x01)
      #tag.char_write_cmd(0x2e,0x0100)

      # enable humidity
      #tag.register_cb(0x38, cbs.humidity)
      #tag.char_write_cmd(0x3c,0x01)
      #tag.char_write_cmd(0x39,0x0100)

      # enable magnetometer
      #tag.register_cb(0x40,cbs.magnet)
      #tag.char_write_cmd(0x44,0x01)
      #tag.char_write_cmd(0x41,0x0100)

      # enable gyroscope
      #tag.register_cb(0x57,cbs.gyro)
      #tag.char_write_cmd(0x5b,0x07)
      #tag.char_write_cmd(0x58,0x0100)

      """# fetch barometer calibration
      tag.char_write_cmd(0x4f,0x02)
      rawcal = tag.char_read_hnd(0x52)
      print rawcal
      barometer = Barometer( rawcal )
      # enable barometer
      tag.register_cb(0x4b,cbs.baro)
      tag.char_write_cmd(0x4f,0x01)
      #tag.char_write_cmd(0x4c,0x0100)"""
    
    else:
        sys.exit()

      
if __name__ == "__main__":
    main()

