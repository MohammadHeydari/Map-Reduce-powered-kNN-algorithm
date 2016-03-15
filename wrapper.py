#!/usr/bin/env python
from random import randrange
from subprocess import call,check_output
import os,time

start_time = time.time()
FNULL = open(os.devnull, 'w')
OUTPUT_DIR = '/locals/knn/output'


lps = raw_input("What processor speed of your laptop?			:	")
lrm = raw_input("What is the RAM memory of your laptop?			:	")
lhd = raw_input("What is the Hard Disk Capacity of your laptop?		:	")
lss = raw_input("What is the screen size of your laptop?		:	")
nn = raw_input("Enter the number of nearest neighbours to compare	:	")

status = call("hdfs dfs -test -d "+OUTPUT_DIR,stdout=FNULL,stderr=FNULL,shell=True)
if status == 0:call("hdfs dfs -rm -r "+OUTPUT_DIR,stdout=FNULL,stderr=FNULL,shell=True)
command_string = "hadoop  jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /locals/knn/input \
-output /locals/knn/output \
-mapper 'mapper.py "+str(lps)+" "+str(lrm)+" "+str(lhd)+" "+str(lss)+" "+"' \
-reducer 'reducer.py "+str(nn)+"' \
-file ~/projects/bigdata/mapreduce/knn/mapper.py \
-file ~/projects/bigdata/mapreduce/knn/reducer.py"

return_code = call(command_string,stdout=FNULL,stderr=FNULL,shell=True)
if return_code == 0: 
	estval = check_output("hdfs dfs -cat "+OUTPUT_DIR+"/*",shell=True)
	print "\n"
	print "	===	RESULTS		==="	
	print "\n"
	print "Estimated price for your configuration : $"+str(estval)
	print "Time Taken	:	%s seconds " % (time.time() - start_time)

		
