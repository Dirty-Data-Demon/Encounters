
import random
import pandas as pd
from tkinter import *
import tkinter
from tkinter import ttk
#import tkFont 
#Encounter Table
df=pd.read_excel('filepath', sheet_name='Encounter Table (Output)')
temp=pd.read_excel('filepath', sheet_name='Temp')
rain=pd.read_excel('filepath', sheet_name='Rain')
wind=pd.read_excel('filepath', sheet_name='Wind')
Distance=pd.read_excel('filepath', sheet_name='Distance')
Number=pd.read_excel('filepath', sheet_name='Number')
Goals=pd.read_excel('filepath', sheet_name='Goals')
Villains=pd.read_excel('filepath', sheet_name='Villain')
Patrons=pd.read_excel('filepath', sheet_name='Patrons')
Allies=pd.read_excel('filepath', sheet_name='Allies')
#Spells
All_Spells=pd.read_excel('filepath', sheet_name='Spells')
Spells=All_Spells[(All_Spells['Wizard']=="Yes")]
Wealth=pd.read_excel('filepath', sheet_name='Wealth')






#f = tkFont.Font(arguments)






def get_spells():
    spellwin=Toplevel(root)
    spellwin.title('Spellbook')
    level=int(levelbox.get())
    Wealth_name=wealth_box.get()
    School=school_box.get()

    #Create DF of all spells by level (gen=general)
    gen1=Spells[(Spells['Level']==1)]
    gen2=Spells[(Spells['Level']==2)]
    gen3=Spells[(Spells['Level']==3)]
    gen4=Spells[(Spells['Level']==4)]
    gen5=Spells[(Spells['Level']==5)]
    gen6=Spells[(Spells['Level']==6)]
    gen7=Spells[(Spells['Level']==7)]
    gen8=Spells[(Spells['Level']==8)]
    gen9=Spells[(Spells['Level']==9)]
    #Create DF of all spelling belonging to the correct school by level (sh=school)
    sh1=gen1[(gen1['School']==School)]
    sh2=gen2[(gen2['School']==School)]
    sh3=gen3[(gen3['School']==School)]
    sh4=gen4[(gen4['School']==School)]
    sh5=gen5[(gen5['School']==School)]
    sh6=gen6[(gen6['School']==School)]
    sh7=gen7[(gen7['School']==School)]
    sh8=gen8[(gen8['School']==School)]
    sh9=gen9[(gen9['School']==School)]
    # Create a -1 DF of all spell not from the school by level (u=update)
    genu1=gen1[(gen1['School']!=School)]
    genu2=gen2[(gen2['School']!=School)]
    genu3=gen3[(gen3['School']!=School)]
    genu4=gen4[(gen4['School']!=School)]
    genu5=gen5[(gen5['School']!=School)]
    genu6=gen6[(gen6['School']!=School)]
    genu7=gen7[(gen7['School']!=School)]
    genu8=gen8[(gen8['School']!=School)]
    genu9=gen9[(gen9['School']!=School)]
    #Re order all Dfs to  randomize the results
    sh1.sample(frac=1)
    sh2.sample(frac=1) 
    sh3.sample(frac=1)  
    sh4.sample(frac=1)   
    sh5.sample(frac=1)
    sh6.sample(frac=1)
    sh7.sample(frac=1)
    sh8.sample(frac=1)
    sh9.sample(frac=1)
    sh1.sample(frac=1)

    genu1.sample(frac=1)
    genu2.sample(frac=1)
    genu3.sample(frac=1)
    genu4.sample(frac=1)
    genu5.sample(frac=1)
    genu6.sample(frac=1)
    genu7.sample(frac=1)
    genu8.sample(frac=1)
    genu9.sample(frac=1)

    # By wealth level, assign the correct number of spells based on the level of the wizard. Repeat for all wealth levels
    if Wealth_name=="Poor":
       Spell1 = Label(spellwin,text="Spell 1: "+sh1['Name'].tail(1).iloc[0]).pack()
       Spell2 = Label(spellwin,text="Spell 2: "+genu1['Name'].tail(1).iloc[0]).pack()
       Spell3 = Label(spellwin,text="Spell 3: "+sh1['Name'].tail(2).iloc[0]).pack()
       Spell4 = Label(spellwin,text="Spell 4: "+genu1['Name'].tail(2).iloc[0]).pack()
       Spell5 = Label(spellwin,text="Spell 5: "+sh1['Name'].tail(3).iloc[0]).pack()
       Spell6 = Label(spellwin,text="Spell 6: "+genu1['Name'].tail(3).iloc[0]).pack()
       Spell7 = Label(spellwin,text="Spell 7: "+sh1['Name'].tail(4).iloc[0]).pack()
       Spell8 = Label(spellwin,text="Spell 8: "+genu1['Name'].tail(4).iloc[0]).pack()
       if level>=2:
          Spell9 = Label(spellwin,text="Spell 9: "+sh1['Name'].tail(5).iloc[0]).pack()
          Spell10 = Label(spellwin,text="Spell 10: "+genu1['Name'].tail(5).iloc[0]).pack()
       if level>=3:
          Spell11 = Label(spellwin,text="Spell 11: "+sh2['Name'].tail(1).iloc[0]).pack()
          Spell12 = Label(spellwin,text="Spell 12: "+genu2['Name'].tail(1).iloc[0]).pack()
       if level>=4:
          Spell13 = Label(spellwin,text="Spell 13: "+sh2['Name'].tail(2).iloc[0]).pack()
          Spell14 = Label(spellwin,text="Spell 14: "+genu2['Name'].tail(2).iloc[0]).pack()
       if level>=5:
          Spell15 = Label(spellwin,text="Spell 15: "+sh3['Name'].tail(1).iloc[0]).pack()
          Spell16 = Label(spellwin,text="Spell 16: "+genu3['Name'].tail(1).iloc[0]).pack()
       if level>=6:
          Spell17 = Label(spellwin,text="Spell 17: "+sh3['Name'].tail(2).iloc[0]).pack()
          Spell18 = Label(spellwin,text="Spell 18: "+genu3['Name'].tail(2).iloc[0]).pack()
       if level>=7:
          Spell19 = Label(spellwin,text="Spell 19: "+sh4['Name'].tail(5).iloc[0]).pack()
          Spell20 = Label(spellwin,text="Spell 20: "+genu4['Name'].tail(5).iloc[0]).pack()
       if level>=8:
          Spell21 = Label(spellwin,text="Spell 21: "+sh4['Name'].tail(1).iloc[0]).pack()
          Spell22 = Label(spellwin,text="Spell 22: "+genu4['Name'].tail(1).iloc[0]).pack()
       if level>=9:
          Spell23 = Label(spellwin,text="Spell 23: "+sh5['Name'].tail(2).iloc[0]).pack()
          Spell24 = Label(spellwin,text="Spell 24: "+genu5['Name'].tail(2).iloc[0]).pack()
       if level>=10:
          Spell25 = Label(spellwin,text="Spell 25: "+sh5['Name'].tail(1).iloc[0]).pack()
          Spell26 = Label(spellwin,text="Spell 26: "+genu5['Name'].tail(1).iloc[0]).pack()
       if level>=11:
          Spell27 = Label(spellwin,text="Spell 27: "+sh6['Name'].tail(2).iloc[0]).pack()
          Spell28 = Label(spellwin,text="Spell 28: "+genu6['Name'].tail(2).iloc[0]).pack()
       if level>=12:
          Spell29 = Label(spellwin,text="Spell 29: "+sh6['Name'].tail(5).iloc[0]).pack()
          Spell30 = Label(spellwin,text="Spell 30: "+genu6['Name'].tail(5).iloc[0]).pack()
       if level>=13:
          Spell31 = Label(spellwin,text="Spell 31: "+sh7['Name'].tail(1).iloc[0]).pack()
          Spell32 = Label(spellwin,text="Spell 32: "+genu7['Name'].tail(1).iloc[0]).pack()
       if level>=14:
          Spell33 = Label(spellwin,text="Spell 33: "+sh7['Name'].tail(2).iloc[0]).pack()
          Spell34 = Label(spellwin,text="Spell 34: "+genu7['Name'].tail(2).iloc[0]).pack()
       if level>=15:
          Spell35 = Label(spellwin,text="Spell 35: "+sh8['Name'].tail(1).iloc[0]).pack()
          Spell36 = Label(spellwin,text="Spell 36: "+genu8['Name'].tail(1).iloc[0]).pack()
       if level>=16:
          Spell37 = Label(spellwin,text="Spell 37: "+sh8['Name'].tail(2).iloc[0]).pack()
          Spell38 = Label(spellwin,text="Spell 38: "+genu8['Name'].tail(2).iloc[0]).pack()
       if level>=17:
          Spell39 = Label(spellwin,text="Spell 39: "+sh19['Name'].tail(5).iloc[0]).pack()
          Spell40 = Label(spellwin,text="Spell 40: "+genu9['Name'].tail(5).iloc[0]).pack()
       if level>=18:
          Spell41 = Label(spellwin,text="Spell 41: "+sh9['Name'].tail(1).iloc[0]).pack()
          Spell42 = Label(spellwin,text="Spell 42: "+genu9['Name'].tail(1).iloc[0]).pack()
       if level>=19:
          Spell43 = Label(spellwin,text="Spell 43: "+sh9['Name'].tail(2).iloc[0]).pack()
          Spell44 = Label(spellwin,text="Spell 44: "+genu9['Name'].tail(2).iloc[0]).pack()
       if level>=20:
          Spell45 = Label(spellwin,text="Spell 45: "+sh9['Name'].tail(1).iloc[0]).pack()
          Spell46 = Label(spellwin,text="Spell 46: "+genu9['Name'].tail(1).iloc[0]).pack()
  
    if Wealth_name=="Well Off":
       Spell1 = Label(spellwin,text="Spell 1: "+genu1['Name'].tail(1).iloc[0]).pack()
       Spell2 = Label(spellwin,text="Spell 2: "+genu1['Name'].tail(2).iloc[0]).pack()
       Spell3 = Label(spellwin,text="Spell 3: "+genu1['Name'].tail(3).iloc[0]).pack()
       Spell4 = Label(spellwin,text="Spell 4: "+genu1['Name'].tail(4).iloc[0]).pack()
       Spell5 = Label(spellwin,text="Spell 5: "+sh1['Name'].tail(1).iloc[0]).pack()
       Spell6 = Label(spellwin,text="Spell 6: "+genu1['Name'].tail(5).iloc[0]).pack()
       Spell7 = Label(spellwin,text="Spell 7: "+sh1['Name'].tail(2).iloc[0]).pack()
       Spell8 = Label(spellwin,text="Spell 8: "+genu1['Name'].tail(6).iloc[0]).pack()
       Spell9 = Label(spellwin,text="Spell 9: "+sh1['Name'].tail(3).iloc[0]).pack()

       if level>=2:
          Spell10 = Label(spellwin,text="Spell 10: "+genu1['Name'].tail(7).iloc[0]).pack()
          Spell11 = Label(spellwin,text="Spell 11: "+genu1['Name'].tail(8).iloc[0]).pack()
          Spell12 = Label(spellwin,text="Spell 12: "+genu1['Name'].tail(9).iloc[0]).pack()

       if level>=3:
          Spell10 = Label(spellwin,text="Spell 10: "+genu2['Name'].tail(1).iloc[0]).pack()
          Spell11 = Label(spellwin,text="Spell 11: "+sh2['Name'].tail(1).iloc[0]).pack()
          Spell12 = Label(spellwin,text="Spell 12: "+genu2['Name'].tail(2).iloc[0]).pack()

       if level>=4:
          Spell13 = Label(spellwin,text="Spell 13: "+sh2['Name'].tail(2).iloc[0]).pack()
          Spell14 = Label(spellwin,text="Spell 14: "+genu2['Name'].tail(3).iloc[0]).pack()
          Spell15 = Label(spellwin,text="Spell 15: "+sh2['Name'].tail(3).iloc[0]).pack()

       if level>=5:
          Spell14 = Label(spellwin,text="Spell 14: "+genu3['Name'].tail(1).iloc[0]).pack()
          Spell15 = Label(spellwin,text="Spell 15: "+sh3['Name'].tail(1).iloc[0]).pack()
          Spell16 = Label(spellwin,text="Spell 16: "+genu3['Name'].tail(2).iloc[0]).pack()

       if level>=6:
          Spell17 = Label(spellwin,text="Spell 17: "+sh3['Name'].tail(2).iloc[0]).pack()
          Spell18 = Label(spellwin,text="Spell 18: "+genu3['Name'].tail(3).iloc[0]).pack()
          Spell19 = Label(spellwin,text="Spell 19: "+sh3['Name'].tail(3).iloc[0]).pack()

       if level>=7:
          Spell20 = Label(spellwin,text="Spell 20: "+genu4['Name'].tail(1).iloc[0]).pack()
          Spell21 = Label(spellwin,text="Spell 21: "+sh4['Name'].tail(1).iloc[0]).pack()
          Spell22 = Label(spellwin,text="Spell 22: "+genu4['Name'].tail(2).iloc[0]).pack()

       if level>=8:
          Spell23 = Label(spellwin,text="Spell 23: "+sh4['Name'].tail(2).iloc[0]).pack()
          Spell24 = Label(spellwin,text="Spell 24: "+genu4['Name'].tail(3).iloc[0]).pack()
          Spell25 = Label(spellwin,text="Spell 25: "+sh4['Name'].tail(3).iloc[0]).pack()
       if level>=9:
          Spell26 = Label(spellwin,text="Spell 26: "+genu5['Name'].tail(1).iloc[0]).pack()
          Spell27 = Label(spellwin,text="Spell 27: "+sh5['Name'].tail(1).iloc[0]).pack()
          Spell28 = Label(spellwin,text="Spell 28: "+genu5['Name'].tail(2).iloc[0]).pack()

       if level>=10:
          Spell29 = Label(spellwin,text="Spell 29: "+sh5['Name'].tail(2).iloc[0]).pack()
          Spell30 = Label(spellwin,text="Spell 30: "+genu5['Name'].tail(3).iloc[0]).pack()
          Spell31 = Label(spellwin,text="Spell 31: "+sh5['Name'].tail(3).iloc[0]).pack()

       if level>=11:
          Spell32 = Label(spellwin,text="Spell 32: "+genu6['Name'].tail(1).iloc[0]).pack()
          Spell33 = Label(spellwin,text="Spell 33: "+sh6['Name'].tail(1).iloc[0]).pack()
          Spell34 = Label(spellwin,text="Spell 34: "+genu6['Name'].tail(2).iloc[0]).pack()

       if level>=12:
          Spell35 = Label(spellwin,text="Spell 35: "+sh6['Name'].tail(2).iloc[0]).pack()
          Spell36 = Label(spellwin,text="Spell 36: "+genu6['Name'].tail(3).iloc[0]).pack()
          Spell37 = Label(spellwin,text="Spell 37: "+sh6['Name'].tail(3).iloc[0]).pack()

       if level>=13:
          Spell38 = Label(spellwin,text="Spell 38: "+genu7['Name'].tail(1).iloc[0]).pack()
          Spell39 = Label(spellwin,text="Spell 39: "+sh7['Name'].tail(1).iloc[0]).pack()
          Spell40 = Label(spellwin,text="Spell 40: "+genu7['Name'].tail(2).iloc[0]).pack()

       if level>=14:
          Spell41 = Label(spellwin,text="Spell 41: "+sh7['Name'].tail(2).iloc[0]).pack()
          Spell42 = Label(spellwin,text="Spell 42: "+genu7['Name'].tail(3).iloc[0]).pack()
          Spell43 = Label(spellwin,text="Spell 43: "+sh7['Name'].tail(3).iloc[0]).pack()

       if level>=15:
          Spell44 = Label(spellwin,text="Spell 44: "+genu8['Name'].tail(1).iloc[0]).pack()
          Spell45 = Label(spellwin,text="Spell 45: "+sh8['Name'].tail(1).iloc[0]).pack()
          Spell46 = Label(spellwin,text="Spell 46: "+genu8['Name'].tail(2).iloc[0]).pack()

       if level>=16:
          Spell47 = Label(spellwin,text="Spell 47: "+sh8['Name'].tail(2).iloc[0]).pack()
          Spell48 = Label(spellwin,text="Spell 48: "+genu8['Name'].tail(3).iloc[0]).pack()
          Spell49 = Label(spellwin,text="Spell 49: "+sh8['Name'].tail(3).iloc[0]).pack()
       if level>=17:
          Spell50 = Label(spellwin,text="Spell 50: "+genu9['Name'].tail(1).iloc[0]).pack()
          Spell51 = Label(spellwin,text="Spell 51: "+sh9['Name'].tail(1).iloc[0]).pack()
          Spell52 = Label(spellwin,text="Spell 52: "+genu9['Name'].tail(2).iloc[0]).pack()

       if level>=18:
          Spell53 = Label(spellwin,text="Spell 53: "+sh9['Name'].tail(2).iloc[0]).pack()
          Spell54 = Label(spellwin,text="Spell 54: "+genu9['Name'].tail(3).iloc[0]).pack()
          Spell55 = Label(spellwin,text="Spell 55: "+sh9['Name'].tail(3).iloc[0]).pack()

       if level>=19:
          Spell56 = Label(spellwin,text="Spell 56: "+genu9['Name'].tail(1).iloc[0]).pack()
          Spell57 = Label(spellwin,text="Spell 57: "+sh9['Name'].tail(1).iloc[0]).pack()
          Spell58 = Label(spellwin,text="Spell 58: "+genu9['Name'].tail(2).iloc[0]).pack()   

       if level>=20:
          Spell59 = Label(spellwin,text="Spell 59: "+sh9['Name'].tail(2).iloc[0]).pack()
          Spell60 = Label(spellwin,text="Spell 60: "+genu9['Name'].tail(3).iloc[0]).pack()
          Spell61 = Label(spellwin,text="Spell 61: "+sh9['Name'].tail(3).iloc[0]).pack()


    if Wealth_name=="Rich":
       Spell1 = Label(spellwin,text="Spell 1: "+genu1['Name'].tail(1).iloc[0]).pack()
       Spell2 = Label(spellwin,text="Spell 2: "+genu1['Name'].tail(2).iloc[0]).pack()
       Spell3 = Label(spellwin,text="Spell 3: "+genu1['Name'].tail(3).iloc[0]).pack()
       Spell4 = Label(spellwin,text="Spell 4: "+genu1['Name'].tail(4).iloc[0]).pack()
       Spell5 = Label(spellwin,text="Spell 5: "+sh1['Name'].tail(1).iloc[0]).pack()
       Spell6 = Label(spellwin,text="Spell 6: "+genu1['Name'].tail(5).iloc[0]).pack()
       Spell7 = Label(spellwin,text="Spell 7: "+sh1['Name'].tail(2).iloc[0]).pack()
       Spell8 = Label(spellwin,text="Spell 8: "+genu1['Name'].tail(6).iloc[0]).pack()
       Spell9 = Label(spellwin,text="Spell 9: "+genu1['Name'].tail(7).iloc[0]).pack()
       Spell10 = Label(spellwin,text="Spell 10: "+genu1['Name'].tail(8).iloc[0]).pack()

       if level>=2:
          Spell11 = Label(spellwin,text="Spell 11: "+sh1['Name'].tail(3).iloc[0]).pack()
          Spell12 = Label(spellwin,text="Spell 12: "+genu1['Name'].tail(9).iloc[0]).pack()
          Spell13 = Label(spellwin,text="Spell 13: "+genu1['Name'].tail(10).iloc[0]).pack()
          Spell14 = Label(spellwin,text="Spell 14: "+genu1['Name'].tail(11).iloc[0]).pack()

       if level>=3:
          Spell15 = Label(spellwin,text="Spell 15: "+genu2['Name'].tail(1).iloc[0]).pack()
          Spell16 = Label(spellwin,text="Spell 16: "+sh2['Name'].tail(1).iloc[0]).pack()
          Spell17 = Label(spellwin,text="Spell 17: "+genu2['Name'].tail(2).iloc[0]).pack()
          Spell18 = Label(spellwin,text="Spell 18: "+sh2['Name'].tail(2).iloc[0]).pack()

       if level>=4:
          Spell19 = Label(spellwin,text="Spell 19: "+genu2['Name'].tail(3).iloc[0]).pack()
          Spell20 = Label(spellwin,text="Spell 20: "+sh2['Name'].tail(3).iloc[0]).pack()
          Spell21 = Label(spellwin,text="Spell 21: "+genu2['Name'].tail(4).iloc[0]).pack()
          Spell22 = Label(spellwin,text="Spell 22: "+sh2['Name'].tail(4).iloc[0]).pack()

       if level>=5:
          Spell23 = Label(spellwin,text="Spell 23: "+genu3['Name'].tail(1).iloc[0]).pack()
          Spell24 = Label(spellwin,text="Spell 24: "+sh3['Name'].tail(1).iloc[0]).pack()
          Spell25 = Label(spellwin,text="Spell 25: "+genu3['Name'].tail(2).iloc[0]).pack()
          Spell26 = Label(spellwin,text="Spell 26: "+sh3['Name'].tail(2).iloc[0]).pack()

       if level>=6:
          Spell27 = Label(spellwin,text="Spell 27: "+genu3['Name'].tail(3).iloc[0]).pack()
          Spell28 = Label(spellwin,text="Spell 28: "+sh3['Name'].tail(3).iloc[0]).pack()
          Spell29 = Label(spellwin,text="Spell 29: "+genu3['Name'].tail(4).iloc[0]).pack()
          Spell30 = Label(spellwin,text="Spell 30: "+sh3['Name'].tail(4).iloc[0]).pack()

       if level>=7:
          Spell31 = Label(spellwin,text="Spell 31: "+genu4['Name'].tail(1).iloc[0]).pack()
          Spell32 = Label(spellwin,text="Spell 32: "+sh4['Name'].tail(1).iloc[0]).pack()
          Spell33 = Label(spellwin,text="Spell 33: "+genu4['Name'].tail(2).iloc[0]).pack()
          Spell34 = Label(spellwin,text="Spell 34: "+sh4['Name'].tail(2).iloc[0]).pack()

       if level>=8:
          Spell35 = Label(spellwin,text="Spell 35: "+genu4['Name'].tail(3).iloc[0]).pack()
          Spell36 = Label(spellwin,text="Spell 36: "+sh4['Name'].tail(3).iloc[0]).pack()
          Spell37 = Label(spellwin,text="Spell 37: "+genu4['Name'].tail(4).iloc[0]).pack()
          Spell38 = Label(spellwin,text="Spell 38: "+sh4['Name'].tail(4).iloc[0]).pack()

       if level>=9:
          Spell39 = Label(spellwin,text="Spell 39: "+genu5['Name'].tail(1).iloc[0]).pack()
          Spell40 = Label(spellwin,text="Spell 40: "+sh5['Name'].tail(1).iloc[0]).pack()
          Spell41 = Label(spellwin,text="Spell 41: "+genu5['Name'].tail(2).iloc[0]).pack()
          Spell42 = Label(spellwin,text="Spell 42: "+sh5['Name'].tail(2).iloc[0]).pack()

       if level>=10:
          Spell43 = Label(spellwin,text="Spell 43: "+genu5['Name'].tail(3).iloc[0]).pack()
          Spell44 = Label(spellwin,text="Spell 44: "+sh5['Name'].tail(3).iloc[0]).pack()
          Spell45 = Label(spellwin,text="Spell 45: "+genu5['Name'].tail(4).iloc[0]).pack()
          Spell46 = Label(spellwin,text="Spell 46: "+sh5['Name'].tail(4).iloc[0]).pack()

       if level>=11:
          Spell47 = Label(spellwin,text="Spell 47: "+genu6['Name'].tail(1).iloc[0]).pack()
          Spell48 = Label(spellwin,text="Spell 48: "+sh6['Name'].tail(1).iloc[0]).pack()
          Spell49 = Label(spellwin,text="Spell 49: "+genu6['Name'].tail(2).iloc[0]).pack()
          Spell50 = Label(spellwin,text="Spell 50: "+sh6['Name'].tail(2).iloc[0]).pack()

       if level>=12:
          Spell51 = Label(spellwin,text="Spell 51: "+genu6['Name'].tail(3).iloc[0]).pack()
          Spell52 = Label(spellwin,text="Spell 52: "+sh6['Name'].tail(3).iloc[0]).pack()
          Spell53 = Label(spellwin,text="Spell 53: "+genu6['Name'].tail(4).iloc[0]).pack()
          Spell54 = Label(spellwin,text="Spell 54: "+sh6['Name'].tail(4).iloc[0]).pack()

       if level>=13:
          Spell55 = Label(spellwin,text="Spell 55: "+genu7['Name'].tail(1).iloc[0]).pack()
          Spell56 = Label(spellwin,text="Spell 56: "+sh7['Name'].tail(1).iloc[0]).pack()
          Spell57 = Label(spellwin,text="Spell 57: "+genu7['Name'].tail(2).iloc[0]).pack()
          Spell58 = Label(spellwin,text="Spell 58: "+sh7['Name'].tail(2).iloc[0]).pack()

       if level>=14:
          Spell59 = Label(spellwin,text="Spell 59: "+genu7['Name'].tail(3).iloc[0]).pack()
          Spell60 = Label(spellwin,text="Spell 60: "+sh7['Name'].tail(3).iloc[0]).pack()
          Spell61 = Label(spellwin,text="Spell 61: "+genu7['Name'].tail(4).iloc[0]).pack()
          Spell62 = Label(spellwin,text="Spell 62: "+sh['Name'].tail(4).iloc[0]).pack()

       if level>=15:
          Spell63 = Label(spellwin,text="Spell 63: "+genu8['Name'].tail(1).iloc[0]).pack()
          Spell64 = Label(spellwin,text="Spell 64: "+sh8['Name'].tail(1).iloc[0]).pack()
          Spell65 = Label(spellwin,text="Spell 65: "+genu8['Name'].tail(2).iloc[0]).pack()
          Spell66 = Label(spellwin,text="Spell 66: "+sh8['Name'].tail(2).iloc[0]).pack()

       if level>=16:
          Spell67 = Label(spellwin,text="Spell 67: "+genu8['Name'].tail(3).iloc[0]).pack()
          Spell68 = Label(spellwin,text="Spell 68: "+sh8['Name'].tail(3).iloc[0]).pack()
          Spell69 = Label(spellwin,text="Spell 69: "+genu8['Name'].tail(4).iloc[0]).pack()
          Spell70 = Label(spellwin,text="Spell 70: "+sh8['Name'].tail(4).iloc[0]).pack()

       if level>=17:
          Spell71 = Label(spellwin,text="Spell 71: "+genu9['Name'].tail(1).iloc[0]).pack()
          Spell72 = Label(spellwin,text="Spell 72: "+sh9['Name'].tail(1).iloc[0]).pack()
          Spell73 = Label(spellwin,text="Spell 73: "+genu9['Name'].tail(2).iloc[0]).pack()
          Spell74 = Label(spellwin,text="Spell 74: "+sh9['Name'].tail(2).iloc[0]).pack()

       if level>=18:
          Spell75 = Label(spellwin,text="Spell 75: "+genu9['Name'].tail(3).iloc[0]).pack()
          Spell76 = Label(spellwin,text="Spell 76: "+sh9['Name'].tail(3).iloc[0]).pack()
          Spell77 = Label(spellwin,text="Spell 77: "+genu9['Name'].tail(4).iloc[0]).pack()
          Spell78 = Label(spellwin,text="Spell 78: "+sh9['Name'].tail(4).iloc[0]).pack()

       if level>=19:
          Spell79 = Label(spellwin,text="Spell 79: "+genu7['Name'].tail(1).iloc[0]).pack()
          Spell80 = Label(spellwin,text="Spell 80: "+sh8['Name'].tail(1).iloc[0]).pack()
          Spell81 = Label(spellwin,text="Spell 81: "+genu7['Name'].tail(2).iloc[0]).pack()
          Spell82 = Label(spellwin,text="Spell 82: "+sh8['Name'].tail(2).iloc[0]).pack()

       if level>=20:
          Spell83 = Label(spellwin,text="Spell 83: "+genu9['Name'].tail(3).iloc[0]).pack()
          Spell84 = Label(spellwin,text="Spell 84: "+sh9['Name'].tail(3).iloc[0]).pack()
          Spell85 = Label(spellwin,text="Spell 85: "+genu9['Name'].tail(4).iloc[0]).pack()
          Spell86 = Label(spellwin,text="Spell 86: "+sh9['Name'].tail(4).iloc[0]).pack()

    if Wealth_name=="Financed":
       Spell1 = Label(spellwin,text="Spell 1: "+genu1['Name'].tail(1).iloc[0]).pack()
       Spell2 = Label(spellwin,text="Spell 2: "+genu1['Name'].tail(2).iloc[0]).pack()
       Spell3 = Label(spellwin,text="Spell 3: "+genu1['Name'].tail(3).iloc[0]).pack()
       Spell4 = Label(spellwin,text="Spell 4: "+genu1['Name'].tail(4).iloc[0]).pack()
       Spell5 = Label(spellwin,text="Spell 5: "+sh1['Name'].tail(1).iloc[0]).pack()
       Spell6 = Label(spellwin,text="Spell 6: "+genu1['Name'].tail(5).iloc[0]).pack()
       Spell7 = Label(spellwin,text="Spell 7: "+sh1['Name'].tail(2).iloc[0]).pack()
       Spell8 = Label(spellwin,text="Spell 8: "+genu1['Name'].tail(6).iloc[0]).pack()
       Spell9 = Label(spellwin,text="Spell 9: "+genu1['Name'].tail(7).iloc[0]).pack()
       Spell10 = Label(spellwin,text="Spell 10: "+genu1['Name'].tail(7).iloc[0]).pack()
       Spell11 = Label(spellwin,text="Spell 11: "+genu1['Name'].tail(8).iloc[0]).pack()

       if level>=2:
          Spell12 = Label(spellwin,text="Spell 12: "+sh1['Name'].tail(3).iloc[0]).pack()
          Spell13 = Label(spellwin,text="Spell 13: "+genu1['Name'].tail(9).iloc[0]).pack()
          Spell14 = Label(spellwin,text="Spell 14: "+genu1['Name'].tail(10).iloc[0]).pack()
          Spell15 = Label(spellwin,text="Spell 15: "+genu1['Name'].tail(11).iloc[0]).pack()
          Spell16 = Label(spellwin,text="Spell 16: "+genu1['Name'].tail(12).iloc[0]).pack()

       if level>=3:
          Spell17 = Label(spellwin,text="Spell 17: "+genu2['Name'].tail(1).iloc[0]).pack()
          Spell18 = Label(spellwin,text="Spell 18: "+sh2['Name'].tail(1).iloc[0]).pack()
          Spell19 = Label(spellwin,text="Spell 19: "+genu2['Name'].tail(2).iloc[0]).pack()
          Spell20 = Label(spellwin,text="Spell 20: "+sh2['Name'].tail(2).iloc[0]).pack()
          Spell21 = Label(spellwin,text="Spell 21: "+genu2['Name'].tail(3).iloc[0]).pack()

       if level>=4:
          Spell22 = Label(spellwin,text="Spell 22: "+sh2['Name'].tail(4).iloc[0]).pack()
          Spell23 = Label(spellwin,text="Spell 23: "+genu2['Name'].tail(4).iloc[0]).pack()
          Spell24 = Label(spellwin,text="Spell 24: "+genu2['Name'].tail(5).iloc[0]).pack()
          Spell25 = Label(spellwin,text="Spell 25: "+genu2['Name'].tail(6).iloc[0]).pack()
          Spell26 = Label(spellwin,text="Spell 26: "+genu2['Name'].tail(7).iloc[0]).pack()

       if level>=5:
          Spell27 = Label(spellwin,text="Spell 27: "+genu3['Name'].tail(1).iloc[0]).pack()
          Spell28 = Label(spellwin,text="Spell 28: "+sh3['Name'].tail(1).iloc[0]).pack()
          Spell29 = Label(spellwin,text="Spell 29: "+genu3['Name'].tail(2).iloc[0]).pack()
          Spell30 = Label(spellwin,text="Spell 30: "+sh3['Name'].tail(2).iloc[0]).pack()
          Spell31 = Label(spellwin,text="Spell 31: "+genu3['Name'].tail(3).iloc[0]).pack()

       if level>=6:
          Spell32 = Label(spellwin,text="Spell 32: "+sh3['Name'].tail(4).iloc[0]).pack()
          Spell33 = Label(spellwin,text="Spell 33: "+genu3['Name'].tail(4).iloc[0]).pack()
          Spell34 = Label(spellwin,text="Spell 34: "+genu3['Name'].tail(5).iloc[0]).pack()
          Spell35 = Label(spellwin,text="Spell 35: "+genu3['Name'].tail(6).iloc[0]).pack()
          Spell36 = Label(spellwin,text="Spell 36: "+genu3['Name'].tail(7).iloc[0]).pack()\

       if level>=7:
          Spell37 = Label(spellwin,text="Spell 37: "+genu4['Name'].tail(1).iloc[0]).pack()
          Spell38 = Label(spellwin,text="Spell 38: "+sh4['Name'].tail(1).iloc[0]).pack()
          Spell39 = Label(spellwin,text="Spell 39: "+genu4['Name'].tail(2).iloc[0]).pack()
          Spell40 = Label(spellwin,text="Spell 40: "+sh4['Name'].tail(2).iloc[0]).pack()
          Spell41 = Label(spellwin,text="Spell 41: "+genu4['Name'].tail(3).iloc[0]).pack()

       if level>=8:
          Spell42 = Label(spellwin,text="Spell 42: "+sh4['Name'].tail(4).iloc[0]).pack()
          Spell43 = Label(spellwin,text="Spell 43: "+genu4['Name'].tail(4).iloc[0]).pack()
          Spell44 = Label(spellwin,text="Spell 44: "+genu4['Name'].tail(5).iloc[0]).pack()
          Spell45 = Label(spellwin,text="Spell 45: "+genu4['Name'].tail(6).iloc[0]).pack()
          Spell46 = Label(spellwin,text="Spell 46: "+genu4['Name'].tail(7).iloc[0]).pack()
          
       if level>=9:
          Spell47 = Label(spellwin,text="Spell 47: "+genu5['Name'].tail(1).iloc[0]).pack()
          Spell48 = Label(spellwin,text="Spell 48: "+sh5['Name'].tail(1).iloc[0]).pack()
          Spell49 = Label(spellwin,text="Spell 49: "+genu5['Name'].tail(2).iloc[0]).pack()
          Spell50 = Label(spellwin,text="Spell 50: "+sh5['Name'].tail(2).iloc[0]).pack()
          Spell51 = Label(spellwin,text="Spell 51: "+genu5['Name'].tail(3).iloc[0]).pack()

       if level>=10:
          Spell52 = Label(spellwin,text="Spell 52: "+sh5['Name'].tail(4).iloc[0]).pack()
          Spell53 = Label(spellwin,text="Spell 53: "+genu5['Name'].tail(4).iloc[0]).pack()
          Spell54 = Label(spellwin,text="Spell 54: "+genu5['Name'].tail(5).iloc[0]).pack()
          Spell55 = Label(spellwin,text="Spell 55: "+genu5['Name'].tail(6).iloc[0]).pack()
          Spell56 = Label(spellwin,text="Spell 56: "+genu5['Name'].tail(7).iloc[0]).pack()

       if level>=11:
          Spell57 = Label(spellwin,text="Spell 57: "+genu6['Name'].tail(1).iloc[0]).pack()
          Spell58 = Label(spellwin,text="Spell 58: "+sh6['Name'].tail(1).iloc[0]).pack()
          Spell59 = Label(spellwin,text="Spell 59: "+genu6['Name'].tail(2).iloc[0]).pack()
          Spell60 = Label(spellwin,text="Spell 60: "+sh6['Name'].tail(2).iloc[0]).pack()
          Spell61 = Label(spellwin,text="Spell 61: "+genu6['Name'].tail(3).iloc[0]).pack()

       if level>=12:
          Spell62 = Label(spellwin,text="Spell 62: "+sh6['Name'].tail(4).iloc[0]).pack()
          Spell63 = Label(spellwin,text="Spell 63: "+genu6['Name'].tail(4).iloc[0]).pack()
          Spell64 = Label(spellwin,text="Spell 64: "+genu6['Name'].tail(5).iloc[0]).pack()
          Spell65 = Label(spellwin,text="Spell 65: "+genu6['Name'].tail(6).iloc[0]).pack()
          Spell66 = Label(spellwin,text="Spell 66: "+genu6['Name'].tail(7).iloc[0]).pack()\

       if level>=13:
          Spell67 = Label(spellwin,text="Spell 67: "+genu7['Name'].tail(1).iloc[0]).pack()
          Spell68 = Label(spellwin,text="Spell 68: "+sh7['Name'].tail(1).iloc[0]).pack()
          Spell69 = Label(spellwin,text="Spell 69: "+genu7['Name'].tail(2).iloc[0]).pack()
          Spell70 = Label(spellwin,text="Spell 70: "+sh7['Name'].tail(2).iloc[0]).pack()
          Spell71 = Label(spellwin,text="Spell 71: "+genu7['Name'].tail(3).iloc[0]).pack()

       if level>=14:
          Spell72 = Label(spellwin,text="Spell 72: "+sh7['Name'].tail(4).iloc[0]).pack()
          Spell73 = Label(spellwin,text="Spell 73: "+genu7['Name'].tail(4).iloc[0]).pack()
          Spell74 = Label(spellwin,text="Spell 74: "+genu7['Name'].tail(5).iloc[0]).pack()
          Spell75 = Label(spellwin,text="Spell 75: "+genu7['Name'].tail(6).iloc[0]).pack()
          Spell76 = Label(spellwin,text="Spell 76: "+genu7['Name'].tail(7).iloc[0]).pack()

       if level>=15:
          Spell77 = Label(spellwin,text="Spell 77: "+genu8['Name'].tail(1).iloc[0]).pack()
          Spell78 = Label(spellwin,text="Spell 78: "+sh8['Name'].tail(1).iloc[0]).pack()
          Spell79 = Label(spellwin,text="Spell 79: "+genu8['Name'].tail(2).iloc[0]).pack()
          Spell80 = Label(spellwin,text="Spell 80: "+sh8['Name'].tail(2).iloc[0]).pack()
          Spell81 = Label(spellwin,text="Spell 81: "+genu8['Name'].tail(3).iloc[0]).pack()

       if level>=16:
          Spell82 = Label(spellwin,text="Spell 82: "+sh8['Name'].tail(4).iloc[0]).pack()
          Spell83 = Label(spellwin,text="Spell 83: "+genu8['Name'].tail(4).iloc[0]).pack()
          Spell84 = Label(spellwin,text="Spell 84: "+genu8['Name'].tail(5).iloc[0]).pack()
          Spell85 = Label(spellwin,text="Spell 85: "+genu8['Name'].tail(6).iloc[0]).pack()
          Spell86 = Label(spellwin,text="Spell 86: "+genu8['Name'].tail(7).iloc[0]).pack()

       if level>=17:
          Spell87 = Label(spellwin,text="Spell 87: "+genu9['Name'].tail(1).iloc[0]).pack()
          Spell88 = Label(spellwin,text="Spell 88: "+sh9['Name'].tail(1).iloc[0]).pack()
          Spell89 = Label(spellwin,text="Spell 89: "+genu9['Name'].tail(2).iloc[0]).pack()
          Spell80 = Label(spellwin,text="Spell 90: "+sh9['Name'].tail(2).iloc[0]).pack()
          Spell81 = Label(spellwin,text="Spell 91: "+genu9['Name'].tail(3).iloc[0]).pack()

       if level>=18:
          Spell92 = Label(spellwin,text="Spell 92: "+sh9['Name'].tail(4).iloc[0]).pack()
          Spell93 = Label(spellwin,text="Spell 93: "+genu9['Name'].tail(4).iloc[0]).pack()
          Spell94 = Label(spellwin,text="Spell 94: "+genu9['Name'].tail(5).iloc[0]).pack()
          Spell95 = Label(spellwin,text="Spell 95: "+genu9['Name'].tail(6).iloc[0]).pack()
          Spell96 = Label(spellwin,text="Spell 96: "+genu9['Name'].tail(7).iloc[0]).pack()\

       if level>=19:
          Spell97 = Label(spellwin,text="Spell 97: "+genu6['Name'].tail(1).iloc[0]).pack()
          Spell98 = Label(spellwin,text="Spell 98: "+sh6['Name'].tail(1).iloc[0]).pack()
          Spell99 = Label(spellwin,text="Spell 99: "+genu7['Name'].tail(2).iloc[0]).pack()
          Spell100 = Label(spellwin,text="Spell 100: "+sh7['Name'].tail(2).iloc[0]).pack()
          Spell101 = Label(spellwin,text="Spell 101: "+genu8['Name'].tail(3).iloc[0]).pack()

       if level>=20:
          Spell102 = Label(spellwin,text="Spell 102: "+sh8['Name'].tail(4).iloc[0]).pack()
          Spell103 = Label(spellwin,text="Spell 103: "+genu6['Name'].tail(4).iloc[0]).pack()
          Spell104 = Label(spellwin,text="Spell 104: "+genu7['Name'].tail(5).iloc[0]).pack()
          Spell105 = Label(spellwin,text="Spell 105: "+genu8['Name'].tail(6).iloc[0]).pack()
          Spell106 = Label(spellwin,text="Spell 106: "+genu9['Name'].tail(7).iloc[0]).pack()
def Encounter_get():
#Pull in user input
   Development = int(entry.get())
   Location=Location_box.get()
    #Create new DF based on the only the current Location and removing Nulls
   df_loc_full=new_df=df[df[Location]!='  ']
   df_loc=new_df[['Monster',Location,'Tag']]
   # Store the rolls for the table
   roll_1=max(round(random.random()*100),df_loc[Location].min())
   roll_2=max(round(random.random()*100),df_loc[Location].min())
   roll_3=max(round(random.random()*100),df_loc[Location].min())
   roll_4=max(round(random.random()*100),df_loc[Location].min())
   roll_5=max(round(random.random()*100),df_loc[Location].min())
   # Take all results less than or equal to the roll
   df_r1=df_loc[(df_loc[Location]<=roll_1)]
   df_r2=df_loc[(df_loc[Location]<=roll_2)]
   df_r3=df_loc[(df_loc[Location]<=roll_3)]
   df_r4=df_loc[(df_loc[Location]<=roll_4)]
   df_r5=df_loc[(df_loc[Location]<=roll_5)]
   # Take the highest value of the remaining tables (what you would have rolled)
   df_value_1=df_r1[(df_r1[Location]==df_r1[Location].max())]
   df_value_2=df_r2[(df_r2[Location]==df_r2[Location].max())]
   df_value_3=df_r3[(df_r3[Location]==df_r3[Location].max())]
   df_value_4=df_r4[(df_r4[Location]==df_r4[Location].max())]
   df_value_5=df_r5[(df_r5[Location]==df_r5[Location].max())]
   #Get the results as a single word
   result_1=df_value_1['Monster'].iloc[0]
   result_2=df_value_2['Monster'].iloc[0]
   result_3=df_value_3['Monster'].iloc[0]
   result_4=df_value_4['Monster'].iloc[0]
   result_5=df_value_5['Monster'].iloc[0]



   #Find the correct type of encounter
   tag1=df_value_1['Tag'].iloc[0]
   tag2=df_value_2['Tag'].iloc[0]
   tag3=df_value_3['Tag'].iloc[0]
   tag4=df_value_4['Tag'].iloc[0]
   tag5=df_value_5['Tag'].iloc[0]
   #Roll the modifier table 
   mod_roll_1=round(random.random()*6+random.random()*6+random.random()*6)
   mod_roll_2=round(random.random()*6+random.random()*6+random.random()*6)
   mod_roll_3=round(random.random()*6+random.random()*6+random.random()*6)
   mod_roll_4=round(random.random()*6+random.random()*6+random.random()*6)
   mod_roll_5=round(random.random()*6+random.random()*6+random.random()*6)
   #Lookup the correct excel sheet based on the tag of the encounter
   df_tag1=pd.read_excel('C:/Users/matth/Downloads/My_Master_Encounter_Table_IX.xlsx', sheet_name=tag1)
   df_tag2=pd.read_excel('C:/Users/matth/Downloads/My_Master_Encounter_Table_IX.xlsx', sheet_name=tag2)
   df_tag3=pd.read_excel('C:/Users/matth/Downloads/My_Master_Encounter_Table_IX.xlsx', sheet_name=tag3)
   df_tag4=pd.read_excel('C:/Users/matth/Downloads/My_Master_Encounter_Table_IX.xlsx', sheet_name=tag4)
   df_tag5=pd.read_excel('C:/Users/matth/Downloads/My_Master_Encounter_Table_IX.xlsx', sheet_name=tag5)


   #Find the result of the roll
   df_mr1=df_tag1[(df_tag1['Roll']==mod_roll_1)]
   df_mr2=df_tag2[(df_tag2['Roll']==mod_roll_2)]
   df_mr3=df_tag3[(df_tag3['Roll']==mod_roll_3)]
   df_mr4=df_tag4[(df_tag4['Roll']==mod_roll_4)]
   df_mr5=df_tag5[(df_tag5['Roll']==mod_roll_5)]


   mresult_1=df_mr1['Result'].iloc[0]
   mresult_2=df_mr2['Result'].iloc[0]
   mresult_3=df_mr3['Result'].iloc[0]
   mresult_4=df_mr4['Result'].iloc[0]
   mresult_5=df_mr5['Result'].iloc[0]

# Roll on weather tables and compare using the same logic as the first two
    
   temp_roll_1=round(random.random()*6+random.random()*6+random.random()*6)
   temp_roll_2=min(round(random.random()*6)+temp_roll_1,18)
   temp_roll_3=max(-round(random.random()*6)+temp_roll_2,3)
   temp_roll_4=round(random.random()*6+random.random()*6+random.random()*6)
   temp_roll_5=round(random.random()*6+random.random()*6+random.random()*6)

   wind_roll_1=round(random.random()*6+random.random()*6+random.random()*6)
   wind_roll_2=max(min(wind_roll_1+round(random.random()*6)-round(random.random()*6),18),3)
   wind_roll_3=max(min(wind_roll_2+round(random.random()*6)-round(random.random()*6),18),3)
   wind_roll_4=round(random.random()*6+random.random()*6+random.random()*6)
   wind_roll_5=round(random.random()*6+random.random()*6+random.random()*6)

   rain_roll_1=round(random.random()*6+random.random()*6+random.random()*6)
   rain_roll_2=max(min(rain_roll_1+round(random.random()*6)+(round(random.random()*6)*-1),18),3)
   rain_roll_3=max(min(rain_roll_2+round(random.random()*6)+(round(random.random()*6)*-1),18),3)
   rain_roll_4=round(random.random()*6+random.random()*6+random.random()*6)
   rain_roll_5=round(random.random()*6+random.random()*6+random.random()*6)
    
    

    
   rain1=rain[(rain['Roll']==rain_roll_1)]
   rain2=rain[(rain['Roll']==rain_roll_2)]
   rain3=rain[(rain['Roll']==rain_roll_3)]
   rain4=rain[(rain['Roll']==rain_roll_4)]
   rain5=rain[(rain['Roll']==rain_roll_5)]

   wind1=wind[(wind['Roll']==wind_roll_1)]
   wind2=wind[(wind['Roll']==wind_roll_2)]
   wind3=wind[(wind['Roll']==wind_roll_3)]
   wind4=wind[(wind['Roll']==wind_roll_4)]
   wind5=wind[(wind['Roll']==wind_roll_5)]

   temp1=temp[(temp['Roll']==temp_roll_1)]
   temp2=temp[(temp['Roll']==temp_roll_2)]
   temp3=temp[(temp['Roll']==temp_roll_3)]
   temp4=temp[(temp['Roll']==temp_roll_4)]
   temp5=temp[(temp['Roll']==temp_roll_5)]


   rain_result_1=rain1['Result'].iloc[0]
   rain_result_2=rain2['Result'].iloc[0]
   rain_result_3=rain3['Result'].iloc[0]
   rain_result_4=rain4['Result'].iloc[0]
   rain_result_5=rain5['Result'].iloc[0]
    
   wind_result_1=wind1['Result'].iloc[0]
   wind_result_2=wind2['Result'].iloc[0]
   wind_result_3=wind3['Result'].iloc[0]
   wind_result_4=wind4['Result'].iloc[0]
   wind_result_5=wind5['Result'].iloc[0]
    
   temp_result_1=temp1['Result'].iloc[0]
   temp_result_2=temp2['Result'].iloc[0]
   temp_result_3=temp3['Result'].iloc[0]
   temp_result_4=temp4['Result'].iloc[0]
   temp_result_5=temp5['Result'].iloc[0]

   #Distance roll (d=distance)
 
   dist_roll_2=round(random.random()*6+random.random()*6+random.random()*6)
   dist_roll_1=round(random.random()*6+random.random()*6+random.random()*6) 
   dist_roll_3=round(random.random()*6+random.random()*6+random.random()*6)
   dist_roll_4=round(random.random()*6+random.random()*6+random.random()*6)
   dist_roll_5=round(random.random()*6+random.random()*6+random.random()*6)
 
   dist1=Distance[(Distance['Roll']==dist_roll_1)]
   dist2=Distance[(Distance['Roll']==dist_roll_2)]
   dist3=Distance[(Distance['Roll']==dist_roll_3)]
   dist4=Distance[(Distance['Roll']==dist_roll_4)]
   dist5=Distance[(Distance['Roll']==dist_roll_5)]


   d_result1=dist1['Result'].iloc[0]
   d_result2=dist2['Result'].iloc[0]
   d_result3=dist3['Result'].iloc[0]
   d_result4=dist4['Result'].iloc[0]
   d_result5=dist5['Result'].iloc[0]

    #Number roll (n=number)
 
    
   number_roll_1=round(random.random()*6+random.random()*6+random.random()*6)
   number_roll_2=round(random.random()*6+random.random()*6+random.random()*6)
   number_roll_3=round(random.random()*6+random.random()*6+random.random()*6)
   number_roll_4=round(random.random()*6+random.random()*6+random.random()*6)
   number_roll_5=round(random.random()*6+random.random()*6+random.random()*6)
   


    
   num1=Number[(Number['Roll']==number_roll_1)]
   num2=Number[(Number['Roll']==number_roll_2)]
   num3=Number[(Number['Roll']==number_roll_3)]
   num4=Number[(Number['Roll']==number_roll_4)]
   num5=Number[(Number['Roll']==number_roll_5)]


   num_result_1=num1['Result'].iloc[0]
   num_result_2=num2['Result'].iloc[0]
   num_result_3=num3['Result'].iloc[0]
   num_result_4=num4['Result'].iloc[0]
   num_result_5=num5['Result'].iloc[0]
   # If statements to determien how many encounters based on local area
   if (5-Development)>=1: Encounter1.configure(text="Encounter 1: "+num_result_1+" "+result_1+" at "+d_result1+" Distance " +mresult_1)
   if (5-Development)>=2: Encounter2.configure(text="Encounter 2: "+num_result_2+" "+result_2+" at "+d_result2+" Distance " +mresult_2)
   if (5-Development)>=3: Encounter3.configure(text="Encounter 3: "+num_result_3+" "+result_3+" at "+d_result3+" Distance " +mresult_3)
   if (5-Development)>=4: Encounter4.configure(text="Encounter 4: "+num_result_4+" "+result_4+" at "+d_result4+" Distance " +mresult_4)
   if (5-Development)>=5: Encounter5.configure(text="Encounter 5: "+num_result_5+" "+result_5+" at "+d_result5+" Distance " +mresult_5)

   if (5-Development)>=1 and tag1=="Location" :
            Encounter1.configure(text="Encounter 1: " + result_1+" at "+d_result1+" Distance " +mresult_1)
   elif (5-Development)>=1 : Encounter1.configure(text="Encounter 1: "+num_result_1+" "+result_1+" at "+d_result1+" Distance " +mresult_1)
            
   if (5-Development)>=2 and tag2=="Location" :
           Encounter2.configure(text="Encounter 2: " + result_2+" at "+d_result2+" Distance " +mresult_2)
   elif (5-Development)>=2: Encounter2.configure(text="Encounter 2: "+num_result_2+" "+result_2+" at "+d_result2+" Distance " +mresult_2)

   if (5-Development)>=3 and tag3=="Location" :
            Encounter3.configure(text="Encounter 3: " + result_3+" at "+d_result3+" Distance " +mresult_3)
   elif (5-Development)>=3 : Encounter3.configure(text="Encounter 3: "+num_result_3+" "+result_3+" at "+d_result3+" Distance " +mresult_3)

   if (5-Development)>=4 and tag4=="Location" :
           Encounter4.configure(text="Encounter 4: " + result_4+" at "+d_result4+" Distance " +mresult_4)
   elif (5-Development)>=4: Encounter4.configure(text="Encounter 4: "+num_result_4+" "+result_4+" at "+d_result4+" Distance " +mresult_4)
            
   if (5-Development)>=5 and tag5=="Location" :
            Encounter5.configure(text="Encounter 5: " + result_5+" at "+d_result5+" Distance " +mresult_5)
   elif (5-Development)>=5: Encounter5.configure(text="Encounter 5: "+num_result_5+" "+result_5+" at "+d_result5+" Distance " +mresult_5)

   morning.configure(text="Morning Weather: A "+temp_result_1+" Day With "+rain_result_1+" Air and "+wind_result_1)
   afternoon.configure(text="Afternoon Weather: A "+temp_result_2+" Day With "+rain_result_2+" Air and "+wind_result_2)
   night.configure(text="Night Weather: A "+temp_result_3+" Day With "+rain_result_3+" Air and "+wind_result_3)
#Roll on adventure tables from the DMG and crete a new window
def Quest ():
    jobwin=Toplevel(root)
    
    
    roll_1=round(random.uniform(1,38))
    roll_2=round(random.uniform(1,20))
    roll_3=round(random.uniform(1,20))
    roll_4=round(random.uniform(1,12))

    jobwin.title(roll_2)

    Goal=Goals[(Goals['Roll']==roll_1)]
    Villain=Villains[(Villains['Roll']==roll_2)]
    Patron=Patrons[(Patrons['Roll']==roll_3)]
    Ally=Allies[(Allies['Roll']==roll_4)]

    Goal_DESC=Goal['Result'].iloc[0]
    Villain_DESC=Villain['Result'].iloc[0]
    Patron_DESC=Patron['Result'].iloc[0]
    Ally_DESC=Ally['Result'].iloc[0]

    Job=Label(jobwin,text="A "+Patron_DESC+" looking to hire some help to "+Goal_DESC+". A "+Villain_DESC+" will oppose the party, but a "+Ally_DESC+" might help the party.").pack()
#Roll on a different table for only one encounter
def differeenttable():
    Location=Location_box.get()
    new=Toplevel(root)
    new.title("Encounters")    
    Encounter = Label(new,text="Encounter: ")

    Encounter.pack()

    df_loc_full=new_df=df[df[Location]!='  ']
    df_loc=new_df[['Monster',Location]]
    roll_1=max(round(random.random()*100),df_loc[Location].min())
    roll_2=max(round(random.random()*100),df_loc[Location].min())
    roll_3=max(round(random.random()*100),df_loc[Location].min())
    roll_4=max(round(random.random()*100),df_loc[Location].min())
    roll_5=max(round(random.random()*100),df_loc[Location].min())

    df_r1=df_loc[(df_loc[Location]<=roll_1)]
    df_r2=df_loc[(df_loc[Location]<=roll_2)]
    df_r3=df_loc[(df_loc[Location]<=roll_3)]
    df_r4=df_loc[(df_loc[Location]<=roll_4)]
    df_r5=df_loc[(df_loc[Location]<=roll_5)]

    df_value_1=df_r1[(df_r1[Location]==df_r1[Location].max())]
    df_value_2=df_r2[(df_r2[Location]==df_r2[Location].max())]
    df_value_3=df_r3[(df_r3[Location]==df_r3[Location].max())]

    df_value_4=df_r4[(df_r4[Location]==df_r4[Location].max())]
    df_value_5=df_r5[(df_r5[Location]==df_r5[Location].max())]
    result_1=df_value_1['Monster'].iloc[0]
    result_2=df_value_2['Monster'].iloc[0]
    result_3=df_value_3['Monster'].iloc[0]
    result_4=df_value_4['Monster'].iloc[0]
    result_5=df_value_5['Monster'].iloc[0]


    Encounter.configure(text="Encounter: "+result_1)
  
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    df.head(0)


  


    n = tkinter.StringVar()
 


#Reset all encounters
def reset():
  Encounter1.configure(text="Encounter 1: ")
  Encounter2.configure(text="Encounter 2: ")
  Encounter3.configure(text="Encounter 3: ")
  Encounter4.configure(text="Encounter 4: ")
  Encounter5.configure(text="Encounter 5: ")



### List of Locations


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df.head(0)

#Configure TK
root = Tk()
root.geometry("600x600")
root.title("Daily Encounters")
entry=ttk.Entry(root, width=3)
entry.pack()


n = tkinter.StringVar()
Location_box = ttk.Combobox(textvariable = n)
dfcol=df.drop(['Monster','Tag'],axis=1)
Location_box['values'] = (list(dfcol.columns))


Location_box.current()
Location_box.pack()
Encounters=Label(root,text="Encounters", font ='bold')

Encounter1 = Label(root,text="Encounter 1: ")
Encounter2 = Label(root,text="Encounter 2: ")
Encounter3 = Label(root,text="Encounter 3: ")
Encounter4 = Label(root,text="Encounter 4: ")
Encounter5 = Label(root,text="Encounter 5: ")
weather=Label(root,text="Weather", font ='bold')
morning=Label(root,text="Morning Weather:")
afternoon=Label(root,text="Afternoon Weather:")
night=Label(root,text="Night Weather:")

Encounters.pack()
Encounter1.pack()
Encounter2.pack()
Encounter3.pack()
Encounter4.pack()
Encounter5.pack()
weather.pack()
morning.pack()
afternoon.pack()
night.pack()


Encounter=ttk.Button(root,text="Roll on  Table",command=Encounter_get)
Encounter.pack()
Diff=ttk.Button(root,text="Roll on Different Table",command=differeenttable).pack()
Reset=ttk.Button(root,text="Reset",command=reset).pack()
Random=ttk.Button(root,text="Random Quest",command=Quest).pack()
levelbox=ttk.Entry(root, width=3)
Label(root,text='Spellbook Generator', font='bold').pack()
levelbox.pack()
schools=Spells['School'].tolist()
wealth_names=Wealth['Name'].tolist()
#Make a list of schools with no dups
schools_list = []
for x in schools:
  if x not in schools_list:
   schools_list.append(x)
#Just because
wealth_list = []
for x in wealth_names:
  if x not in wealth_list:
   wealth_list.append(x)

wealth_box = ttk.Combobox(root, values=wealth_list)
wealth_box.pack()
school_box = ttk.Combobox(root, values=schools_list)
school_box.pack()

   
Spellbook=ttk.Button(root,text="Get Spells",command=get_spells).pack()

root.mainloop()
