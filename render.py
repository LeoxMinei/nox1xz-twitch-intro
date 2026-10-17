#!/usr/bin/env python3
"""Procedural Nox1Xz Twitch intro; original shapes and synthesized soundtrack."""
import argparse, math, subprocess, wave
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
COLORS=[(40,190,255),(245,56,222),(133,64,248)]
def smooth(x):
 x=max(0,min(1,x));return x*x*(3-2*x)
def render(t,w,h):
 im=Image.new("RGB",(w,h),(9,9,28));d=ImageDraw.Draw(im)
 def p(x,y):return (int(x*w),int(y*h))
 for i in range(0,h,3):d.rectangle((0,i,w,i+3),fill=(9+i//80,9+i//160,28+i//35))
 if t<3:
  d.polygon([p(0,.45),p(1,.25),p(1,1),p(0,1)],fill=(21,15,53))
  for j in range(11):d.line([p(0,.49+j*.065),p(1,.29+j*.065)],fill=(36,46,105),width=2)
  d.ellipse((*p(.3,.3),*p(.71,.92)),fill=(13,17,35),outline=COLORS[0],width=max(2,w//190))
  d.polygon([p(.36,.41),p(.5,.34),p(.65,.48),p(.66,.7),p(.5,.83),p(.34,.69)],fill=(35,35,70))
  d.line([p(.5,.37),p(.5,.6)],fill=COLORS[1],width=max(2,w//150))
  d.arc((*p(.35,.45),*p(.66,.85)),20,150,fill=COLORS[0],width=max(2,w//125))
 elif t<10:
  d.polygon([p(0,.13),p(.65,.08),p(.65,.73),p(0,.84)],fill=(22,17,49))
  d.polygon([p(.65,.08),p(1,.15),p(1,.84),p(.65,.73)],fill=(14,23,52))
  d.polygon([p(0,.84),p(.65,.73),p(1,.84),p(1,1),p(0,1)],fill=(24,13,49))
  d.line([p(.06,.16),p(.64,.12),p(.93,.21)],fill=COLORS[1],width=max(3,w//130))
  d.polygon([p(.14,.68),p(.75,.6),p(.96,.73),p(.28,.83)],fill=(46,43,83))
  d.line([p(.28,.83),p(.96,.73)],fill=COLORS[0],width=max(3,w//160))
  for x,y,r in [(.24,.37,.205),(.46,.32,.24),(.7,.38,.19)]:
   d.rectangle((*p(x-r/2,y-.12),*p(x+r/2,y+.16)),fill=(7,11,32),outline=COLORS[0],width=max(2,w//250))
   for j in range(3):d.line([p(x-r*.4+j*r*.23,y+.1),p(x-r*.15+j*r*.23,y-.03)],fill=COLORS[j],width=2)
   d.line([p(x,y+.16),p(x,y+.24)],fill=(102,106,148),width=3)
  d.polygon([p(.36,.72),p(.58,.69),p(.62,.73),p(.4,.77)],fill=(11,18,34))
  for j in range(9):d.line([p(.37+j*.022,.73),p(.41+j*.022,.758)],fill=COLORS[j%3],width=2)
  d.line([p(.89,.37),p(.86,.52),p(.76,.58)],fill=(163,137,208),width=4)
  d.rounded_rectangle((*p(.72,.49),*p(.755,.6)),radius=4,fill=(18,19,45),outline=COLORS[1],width=3)
  # hoodie, face, hood and simplified thumb gesture
  cy=.67+.009*math.sin(t*4)
  d.polygon([p(.53,cy+.2),p(.52,cy-.14),p(.6,cy-.21),p(.68,cy-.14),p(.7,cy+.2)],fill=(37,27,86),outline=COLORS[2],width=3)
  d.ellipse((*p(.56,cy-.36),*p(.655,cy-.15)),fill=(192,128,110))
  d.arc((*p(.53,cy-.39),*p(.685,cy-.14)),175,355,fill=(43,30,83),width=max(7,w//48))
  d.line([p(.53,cy-.04),p(.48,cy+.1),p(.56,cy+.14)],fill=(119,64,201),width=max(4,w//55))
  if t<7:d.line([p(.69,cy-.03),p(.76,cy+.13)],fill=(119,64,201),width=max(4,w//55))
  else:
   e=smooth((t-7)/.8)
   d.line([p(.69,cy-.03),p(.75,cy-.12-e*.06),p(.81,cy-.2-e*.1)],fill=(119,64,201),width=max(4,w//55))
   d.ellipse((*p(.8,cy-.23-e*.1),*p(.84,cy-.18-e*.1)),fill=(230,156,139))
   d.line([p(.82,cy-.2-e*.1),p(.825,cy-.275-e*.1)],fill=(230,156,139),width=max(3,w//95))
 else:
  # Electric expanding logo field and 3D-type shadow
  for j in range(12):
   a=t*2.5+j*math.pi/6;r=.24+.09*math.sin(t*3+j)
   x,y=p(.5+r*math.cos(a),.48+r*.65*math.sin(a))
   d.ellipse((x-10,y-10,x+10,y+10),fill=COLORS[j%3])
   if t<12:d.line([(x,y),p(.5,.47)],fill=COLORS[j%3],width=2)
  path="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
  f=ImageFont.truetype(path,max(10,int(w*.112)))
  label="Nox1Xz";bb=d.textbbox((0,0),label,font=f)
  x=int((w-(bb[2]-bb[0]))/2);y=int(h*.31)
  if t>10.15:
   for s in range(11,0,-1):d.text((x+s,y+s),label,font=f,fill=(29+s,13,70+s))
   d.text((x,y),label,font=f,fill=(240,246,255),stroke_width=max(1,w//400),stroke_fill=COLORS[0])
  if t>=12:
   f2=ImageFont.truetype(path,max(9,int(w*.035)));txt="STREAM STARTING SOON";bb=d.textbbox((0,0),txt,font=f2)
   d.text(((w-(bb[2]-bb[0]))//2,int(.63*h)),txt,font=f2,fill=(242,204,255))
   d.line([p(.28,.76),p(.72,.76)],fill=COLORS[0],width=max(2,w//300))
 for i in range(80):
  x=int((i*191+23*t*(i%6+1))%w);y=int((i*137-11*t*(i%5+1))%h)
  d.ellipse((x,y,x+1+(i%3==0),y+1+(i%3==0)),fill=COLORS[i%3])
 return im
def sound(path,seconds,rate=24000):
 tm=np.arange(round(seconds*rate))/rate;a=np.zeros(len(tm))
 for freq in (110,138.59,164.81,220):a+=.048*np.sin(2*np.pi*freq*tm)
 beat=tm%.5;a+=.17*np.exp(-beat*28)*np.sin(2*np.pi*75*tm)
 a*=np.minimum(1,tm/.25)*np.minimum(1,(seconds-tm)/.5)
 with wave.open(str(path),'wb') as f:
  f.setnchannels(1);f.setsampwidth(2);f.setframerate(rate);f.writeframes((np.clip(a,-1,1)*32767).astype('<i2').tobytes())
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--width',type=int,default=1280);ap.add_argument('--height',type=int,default=720)
 ap.add_argument('--seconds',type=float,default=15);ap.add_argument('--fps',type=int,default=24)
 ap.add_argument('--output',default='dist/Nox1Xz-intro.mp4')
 a=ap.parse_args();out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
 wav=out.with_suffix('.wav');sound(wav,a.seconds)
 cmd=['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pixel_format','rgb24','-video_size',f'{a.width}x{a.height}','-framerate',str(a.fps),'-i','-','-i',str(wav),'-c:v','libx264','-preset','veryfast','-crf','21','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-movflags','+faststart','-t',str(a.seconds),str(out)]
 proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
 for i in range(round(a.seconds*a.fps)):proc.stdin.write(render(i/a.fps,a.width,a.height).tobytes())
 proc.stdin.close()
 if proc.wait():raise RuntimeError('ffmpeg returned nonzero')
 wav.unlink();print('Rendered',out)
if __name__=='__main__':main()
