from __future__ import division
import wave
import struct
from shutil import copyfile

w = wave.open('OSR_US_M_Harvard-30-1_8k.wav','r')
length = w.getnframes()

samples = []

for i in range(0,length):
    waveData = w.readframes(1)
    data = struct.unpack("<h", waveData)
    samples += [int(data[0])/2**15]
    
num_segments = 192
segment_length = int(len(samples)/num_segments)
segment_overlap = 1.0

out_str = ""

for i in range(num_segments):
    pos_amp = max(samples[i*segment_length:(i*segment_length)+int(segment_length*segment_overlap)])
    neg_amp = -min(samples[i*segment_length:(i*segment_length)+int(segment_length*segment_overlap)])
    out_str += "translate([segment_width*" + str(i) + ",0,0]) segment(width=segment_width,pos_amp=(max_amplitude-min_amplitude)*" +str(pos_amp)+ "+min_amplitude,neg_amp=(max_amplitude-min_amplitude)*" + str(neg_amp)+ "+min_amplitude);\n"
    
copyfile("header.scad","wave.scad")

f = open("wave.scad",'a')
f.write(out_str)
f.close()

