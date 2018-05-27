import cv2
import os
import sys

print 'your opencv version : %s' %(cv2.__version__)

if len(sys.argv) < 3 :
  print 'usage : python vid2frame.py videofile output_dir frameskip filename_prefix, exiting'
  print sys.argv
  sys.exit(-1)

frameskip = 0
filename_prefix = ''

filename = sys.argv[1]
outdir = sys.argv[2]
if len(sys.argv) >= 4 :
  frameskip = int(sys.argv[3])

if len(sys.argv) >= 5 :
  filename_prefix = sys.argv[4]

vidcap = cv2.VideoCapture(filename)
count = 0
success = True

while success :
  success, image = vidcap.read()
  print 'process frame %d' %count
  cv2.imwrite("%s/%s_frame%d.jpg" %(outdir,filename_prefix,count), image)
  for i in range(frameskip) :
    success, image = vidcap.read()
  count += 1+frameskip

print 'done'