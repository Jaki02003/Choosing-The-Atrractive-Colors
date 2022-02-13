import math
import cv2 as cv
import numpy as np
import colorsys

#1st Part
img = cv.imread('Photos/cats.jpg')
cv.imshow('Image' , img)


height = img.shape[0] 
weight = img.shape[1]
cnt = 0
str 

b , g , r = img[height-1 , weight-1]
Color_Suggestion = []
Color_rgb_val = []
blank = np.zeros((150 , 1300 , 3) , dtype = 'uint8')                               #creating a blank image

#2nd part
#Showing Choosen Colors In a Blank Page 
def Show_Colors_Serial_By_Serial():
    for i in range(len(Color_rgb_val)):
        X_Co_ordinate = (i*150) + (i*10)
        Y_Co_Ordinate = X_Co_ordinate + 150
        cv.rectangle(blank , (X_Co_ordinate , 0) , (Y_Co_Ordinate , 150) , Color_rgb_val[i] , thickness=-1)  

    cv.imshow('Color Which Can be Choosen: ' , blank)

#Showing the RGB value of Choosen Colors
def Show_RGB_Val():
    for i in range(len(Color_rgb_val)):
        print(f'Rgb value of color {i+1}: {Color_rgb_val[i]}')


#for Analogous Scheme(Degrees can be 30 or -30)

def Do_Analytical_Analogous(val , d):                                              
    d = d/360.0

    r , g , b = map(lambda x: x/255.0, val)                                         #converting rgb values into range between 0 and 1
    h , l , s = colorsys.rgb_to_hls(r , g , b)                                      #h,l,s means hue,lightness and saturation respectively

    new_h = [(h+d) % 1 for d in (-d, d)]

    ret_list = []                                                                   #list which will contain the rgb value
    for nh in range(len(new_h)):
        #print(new_h[nh])
        new_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(new_h[nh], l, s)))  #converting hls to rgb value
        #print(new_rgb)
        Color_rgb_val.append(new_rgb)
        ret_list.append(new_rgb)

    return ret_list


def analogous(d):
    val = [r , g , b]
    ret = Do_Analytical_Analogous(val , d)
    return ret


#For Complimentary Scheme(Degree is 180)
def Do_Analytical_Complimentary(val , d):
    r , g , b = map(lambda x: x/255.0, val)
    h , l , s = colorsys.rgb_to_hls(r , g , b)
    Degree_180_hue = h+(180.0/360.0)
    Color_180_hue = list(map(lambda x: round(x*255) , colorsys.hls_to_rgb(Degree_180_hue , l , s)))
    Color_rgb_val.append(Color_180_hue)
    return Color_180_hue

def Complimentary(d):
    val = [r , g , b]
    ret =  Do_Analytical_Complimentary(val , d)
    #print(ret)
    return ret
 
#For Split_Complimentary(Degrees can be 150 and 210)
def Do_Analytical_Split_Complimentary(val):
    r , g , b = map(lambda x: x/255.0 , val)

    h , l , s = colorsys.rgb_to_hls(r , g , b)
    Degree_150_hue = h + (150.0/360.0)
    Degree_210_hue = h+ (210.0/360.0)

    color_150_rgb = list(map(lambda x: round(x *255), colorsys.hls_to_rgb(Degree_150_hue , l , s)))
    color_210_rgb = list(map(lambda x: round(x * 255) , colorsys.hls_to_rgb(Degree_210_hue , l , s)))

    Color_rgb_val.append(color_150_rgb)
    Color_rgb_val.append(color_210_rgb)

    return [color_150_rgb , color_210_rgb]

def split_complimentary_val():
    val = [r , g , b]
    ret = Do_Analytical_Split_Complimentary(val)
    return ret

#For Triadric Scheme(Degrees can be 120 and 240)
def Do_Analytical_Triadric(val):
    r , g , b = map(lambda x: x/255.0 , val)
    h , l , s = colorsys.rgb_to_hls(r , g , b)

    Degree_120_hue = h + (120.0/360.0)
    Degree_240_hue = h + (240.0/360.0)

    color_120_rgb = list(map(lambda x: round(x*255) , colorsys.hls_to_rgb(Degree_120_hue , l , s)))
    color_240_rgb = list(map(lambda x: round(x*255) , colorsys.hls_to_rgb(Degree_240_hue , l , s)))

    Color_rgb_val.append(color_120_rgb)
    Color_rgb_val.append(color_240_rgb)

    return [color_120_rgb , color_240_rgb]

def triadric():
    val = [r , g , b]
    ret = Do_Analytical_Triadric(val)
    return ret


#For Tetriadic Scheme(Degrees can be 60 , 180 and 240 . since we calculated 180 and 240 before I only calculated for 60 degree)
def Do_Analytical_Tetriadic(val):
    r ,g , b = map(lambda x: x/255.0 , val)
    h , l , s = colorsys.rgb_to_hls(r , g , b)

    Degree_60_hue = h + (60.0/360.0)

    color_60_rgb = list(map(lambda x: round(x*255) , colorsys.hls_to_rgb(Degree_60_hue , l , s)))
    Color_rgb_val.append(color_60_rgb)

    return color_60_rgb

def tetriadic():
    val = [r , g , b]
    ret = Do_Analytical_Tetriadic(val)
    return ret

#3rd Part
com_val = Complimentary(180)                      #returns a list which contains rgb value of complimentary scheme

tet_com_val = tetriadic()                         #returns a list which contains rgb value of tetriadric scheme


ana_val = analogous(30)                           #returns a list which contains rgb value of analogous scheme
Color_Suggestion.append(ana_val)

sp_com_val = split_complimentary_val()            #returns a list which contains rgb value of split complimentary scheme
Color_Suggestion.append(sp_com_val)

tr_com_val = triadric()                           #returns a list which contains rgb value of triadric scheme
Color_Suggestion.append(tr_com_val)


Show_RGB_Val()                                    #Function call for showing the choosen rgb value

Show_Colors_Serial_By_Serial()                    #Function call for showing the choosen colors in a blank image serial by serial

cv.waitKey(0)
