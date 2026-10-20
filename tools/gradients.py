import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, sys

# andes dusk: ink, deep teal, terracotta, saffron, bone
PAL = np.array([[14,22,36],[24,70,82],[196,86,62],[240,164,92],[244,228,200]], float)/255

def ramp(t):
    t = np.clip(t,0,1)*(len(PAL)-1)
    i = np.minimum(t.astype(int), len(PAL)-2); f = (t-i)[...,None]
    f = f*f*(3-2*f)
    return PAL[i]*(1-f)+PAL[i+1]*f

def field(W,H,ph,seed=0,scale=1.0):
    y,x = np.mgrid[0:H,0:W].astype(float)
    x/=W; y/=H*W/H/ (W/H)  # normalise
    y = np.mgrid[0:H,0:W][0]/H
    x = np.mgrid[0:H,0:W][1]/W*(W/H)*0.35*scale
    y = y*scale
    a = 2*math.pi*ph
    # domain-warped sines, all periodic in ph -> seamless loop
    wx = x + 0.35*np.sin(2.1*y + a + seed) + 0.15*np.sin(3.3*x - a)
    wy = y + 0.30*np.sin(1.7*x - a + seed*0.7) + 0.12*np.cos(2.9*y + 2*a)
    v = 0.5 + 0.25*np.sin(2.4*wx + 1.3*wy + a) + 0.25*np.sin(1.1*wx - 2.2*wy - a + seed)
    return v

def grain(W,H,k):
    r = np.random.default_rng(k).normal(0,1,(H,W,1))
    return r

def frames(W,H,n,draw_fn=None,seed=0,scale=1.0,bias=0.0,gamp=0.035):
    out=[]
    for k in range(n):
        ph=k/n
        v=field(W,H,ph,seed,scale)+bias
        img=ramp(v)
        img=img+gamp*grain(W,H,k%4)  # 4 grain states cycle (compresses better)
        im=Image.fromarray((np.clip(img,0,1)*255).astype('uint8'))
        if draw_fn: draw_fn(im,ph)
        out.append(im)
    return out

def save(fr,path,ms=70,colors=96):
    # one shared palette from a few frames
    sample=Image.new('RGB',(fr[0].width,fr[0].height*3))
    for i,j in enumerate([0,len(fr)//3,2*len(fr)//3]): sample.paste(fr[j],(0,fr[0].height*i))
    pal=sample.quantize(colors=colors,method=Image.Quantize.MEDIANCUT)
    q=[f.quantize(palette=pal,dither=Image.Dither.FLOYDSTEINBERG) for f in fr]
    q[0].save(path,save_all=True,append_images=q[1:],duration=ms,loop=0,optimize=True,disposal=1)

MONO='/System/Library/Fonts/SFNSMono.ttf'
SANS='/System/Library/Fonts/SFNS.ttf'
def font(p,s):
    return ImageFont.truetype(p,s)

def text_shadow(d,xy,t,f,fill,shadow=(10,16,26,150)):
    x,y=xy
    d.text((x+2,y+2),t,font=f,fill=shadow)
    d.text((x,y),t,font=f,fill=fill)

def header(im,ph):
    d=ImageDraw.Draw(im,'RGBA')
    W,H=im.size
    # soft ink veil on the left for legibility
    veil=Image.new('L',(W,H),0); vd=ImageDraw.Draw(veil)
    for i in range(W//2):
        vd.line([(i,0),(i,H)],fill=int(150*(1-i/(W/2))**1.6))
    im.paste(Image.new('RGB',(W,H),(12,18,30)),(0,0),veil)
    d=ImageDraw.Draw(im,'RGBA')
    text_shadow(d,(64,74),'bolivian-peru',font(SANS,88),(246,236,216,255))
    text_shadow(d,(68,184),'builds rails for ai agents — proxies, servers, payments.',font(MONO,24),(246,236,216,230))
    # blinking caret (meaningful-ish: "still typing")
    if ph<0.5:
        d.rectangle([68+font(MONO,24).getlength('builds rails for ai agents — proxies, servers, payments.')+6,188,68+font(MONO,24).getlength('builds rails for ai agents — proxies, servers, payments.')+18,214],fill=(240,164,92,255))
    d.text((68,236),'ships small, ships often · lowercase since forever',font=font(MONO,18),fill=(246,236,216,150))

def divider_label(label):
    def fn(im,ph):
        d=ImageDraw.Draw(im,'RGBA'); W,H=im.size
        f=font(MONO,22)
        tw=f.getlength(label)
        d.rounded_rectangle([20,H//2-20,20+tw+28,H//2+20],radius=8,fill=(12,18,30,200))
        d.text((34,H//2-14),label,font=f,fill=(246,236,216,255))
    return fn

if __name__=='__main__':
    W,H=1200,300
    save(frames(W,H,36,header,seed=0.0,scale=1.0),'assets/header.gif',ms=80,colors=112)
    for name,label,seed,bias in [('now','~/now',1.3,0.05),('shipped','~/shipped',2.2,-0.05),('oss','~/open-source',3.1,0.1),('side','~/side-quests',4.4,-0.1),('contact','~/say-hi',5.2,0.0)]:
        save(frames(1200,64,24,divider_label(label),seed=seed,scale=0.6,bias=bias,gamp=0.025),f'assets/{name}.gif',ms=90,colors=64)
    # footer: thin strip, no text
    save(frames(1200,24,24,None,seed=6.0,scale=0.5,gamp=0.02),'assets/footer.gif',ms=90,colors=48)
