import json,subprocess,sys
d=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_type,codec_name,width,height,r_frame_rate','-of','json',sys.argv[1]]))
v=next(x for x in d['streams'] if x['codec_type']=='video')
assert v['codec_name']=='h264' and (v['width'],v['height'])==(1280,720) and v['r_frame_rate']=='24/1',v
assert abs(float(d['format']['duration'])-15)<.09,d['format']
assert any(x['codec_type']=='audio' and x['codec_name']=='aac' for x in d['streams'])
print('PASS: H264 1280x720 24fps 15s with AAC')
