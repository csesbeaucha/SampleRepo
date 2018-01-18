import PIL.Image 
import matplotlib.pyplot as plt
import os.path
import numpy as np
import PIL.ImageDraw
import os

def corners(og_image,radius_ratio):
    '''(image,radius_ratio) image is a string with file extension
    radius is a float <=1'''
    #directory=os.path.dirname(os.path.abspath(__file__))
    #filename=os.path.join(directory, image)
    
    #og_image=PIL.Image.open(filename)
    
    width,height=og_image.size
    
    if width<height:
        radius=width/2*radius_ratio
    else:
        radius=height/2*radius_ratio
        
    new_image=PIL.Image.new('RGBA',(width,height),(0,0,0,0))
    
    the_mask=PIL.Image.new('RGBA',(width,height),(0,0,0,0))
    draw_layer=PIL.ImageDraw.Draw(the_mask)
    draw_layer.rectangle([(radius,0),(width-radius,height)],fill=(200,50,70,255))
    draw_layer.rectangle([(0,radius),(width,height-radius)],fill=(200,50,70,255))
    draw_layer.ellipse([(0,0),(radius*2,radius*2)],fill=(255,255,255,255))
    draw_layer.ellipse([(width-radius*2,0),(width,radius*2)],fill=(255,255,255,255))
    draw_layer.ellipse([(0,height-radius*2),(radius*2,height)],fill=(255,255,255,255))
    draw_layer.ellipse([(width-radius*2,height-radius*2),(width,height)],fill=(255,255,255,255))
    
    #fig,ax=plt.subplots(1,1)
    new_image.paste(og_image,(0,0),mask=the_mask)
    #ax.imshow(new_image)
    #ax[1].imshow(og_image)
    #ax[2].imshow(the_mask)
    
    #fig.show()
    return new_image
def get_images():
    directory=os.getcwd()
    filelist=[]
    image_object_list=[]
    
    directory_list=os.listdir(directory)
    
    for i in directory_list:
        abspath=os.path.join(directory,i)
        try:
            image=PIL.Image.open(abspath)
            image_object_list+=[image]
            filelist+=[abspath]
        except IOError:
            pass
    return image_object_list,filelist
    
def round_all_pics(radius_ratio):
    image_object_list,filelist=get_images()
    
    for i in range(len(image_object_list)):
        new_image=corners(image_object_list[i],radius_ratio)
        new_image.save('image'+str(i)+'.png')    