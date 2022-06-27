#****************************************************************MADLIBS GENERATOR - Team 9*************************************************************************************************

from tkinter import *

root = Tk() #creating a tkinter video


title=Label(root, text=" Welcome to the Mad Lib Generator", font = ("Times New Roman", 15),  #setting a title for the tkinter window and specifying font, background and foreground
          background = 'green',
          foreground = "white")
title.grid(row=0,column=1)

#******************************************************first madlib***************************************************************
def madlib1():
    gd=Toplevel(root)
    
#adding user inputs
    adj1=Label(gd, text="enter an adjective:")
    adj1.grid(row=2, column=0)
    e1=Entry(gd, width=100)
    e1.grid(row=2, column=1)

    adj2=Label(gd, text="enter an adjective:")
    adj2.grid(row=3, column=0)
    e2=Entry(gd, width=100)
    e2.grid(row=3, column=1)

    plnoun=Label(gd, text="enter a plural noun:")
    plnoun.grid(row=4, column=0)
    e3=Entry(gd, width=100)
    e3.grid(row=4, column=1)

    verb1=Label(gd, text="enter a verb:")
    verb1.grid(row=5, column=0)
    e4=Entry(gd, width=100)
    e4.grid(row=5, column=1)

    noun=Label(gd, text="enter a noun:")
    noun.grid(row=6, column=0)
    e5=Entry(gd, width=100)
    e5.grid(row=6, column=1)


    noun2=Label(gd, text="enter a noun:")
    noun2.grid(row=7, column=0)
    e6=Entry(gd, width=100)
    e6.grid(row=7, column=1)


    adj3=Label(gd, text="enter an adjective:")
    adj3.grid(row=8, column=0)
    e7=Entry(gd, width=100)
    e7.grid(row=8, column=1)

#defining the output function that will include the user inputs
    def onclick():
        newwindow=Toplevel(gd)
        g13=Label(gd, text="A girl's day on the beach", font=("Times New Roman", 15), background="green", foreground="white") 

        adj11= e1.get()  #get command used to obtain the user inputs 
        adj22= e2.get()
        plnoun1=e3.get()
        verb11=e4.get()
        noun11=e5.get()
        noun22=e6.get()
        adj33=e7.get()

        if adj11 and adj22 and plnoun1 and adj33 and verb11 and noun11 and  noun22 and adj33 !="":
                  madlibi=Label(newwindow, text="The following is an anecdote of a girl's day out on the beach:", font=("Times New Roman", 15), background="green", foreground="white")
                  madlibi.grid(row=1,column=1)
                  madlib1= Label(newwindow, text=  " \n \n   Yesterday, I went to the beach. I had such a fun time! \n When I arrived at the beach, I could not help but notice the "+ adj11+"  sand. \n My friend loved the "+ adj22+ " swimsuit I was wearing. \n I looked at the ocean and couldn't believe my eyes. \n I saw "+ plnoun1+ " swimming around! I wanted to go swimming with them but they were going to "+ verb11 +" me!\n Instead I decided to build a "+noun11+ " castle.\n  I used a shovel, pail and "+ noun22+ " to build it.\n  The sun started to set, and it was time to go home.\n I had a  " + adj33+ " time at the beach")

                  madlib1.grid(row=2, column=1) #final output madlib

        else:
          txt=Label(newwindow,text="Please enter all the inputs!", background="red", font=('Times New Roman',15))
          txt.grid(row=35,column=1)

    bt1 = Button(gd, text = "Click to generate madlib", command=onclick) #button to generate madlib once the user has finished input
    bt1.grid(row=9, column=1)

b1=Button(root,text="Girl's day out on beach",command=madlib1) #button to open first madlib
b1.grid(row=1,column=1)
             # callback

#***************************************************second madlib************************************************************

def madlib2(): 
#obtaining user inputs

    aa=Toplevel(root)

    a1=Label(aa,text="Flight Announcement", font=("Times New Roman", 15), background="green", foreground="white")
    a1.grid(row=10,column=1)
    
    birds=Label(aa, text="enter a birdcall:")
    birds.grid(row=11, column=0)
    e8=Entry(aa, width=100)
    e8.grid(row=11, column=1)

    number=Label(aa, text="enter a number:")
    number.grid(row=12, column=0)
    e9=Entry(aa, width=100)
    e9.grid(row=12, column=1)

    ficplace=Label(aa, text="enter a fictional place:")
    ficplace.grid(row=13, column=0)
    e10=Entry(aa, width=100)
    e10.grid(row=13, column=1)

    sillyword=Label(aa, text="enter a silly word:")
    sillyword.grid(row=14, column=0)
    e11=Entry(aa, width=100)
    e11.grid(row=14, column=1)


    fooditem=Label(aa, text="enter a food item:")
    fooditem.grid(row=15, column=0)
    e12=Entry(aa, width=100)
    e12.grid(row=15, column=1)

    weird=Label(aa, text="enter the weirdest name you can think of:")
    weird.grid(row=16, column=0)
    e13=Entry(aa, width=100)
    e13.grid(row=16, column=1)

    time=Label(aa, text="enter an amount of time:")
    time.grid(row=17, column=0)
    e14=Entry(aa, width=100)
    e14.grid(row=17, column=1)

    ins=Label(aa, text="enter an insect you're scared of:")
    ins.grid(row=18, column=0)
    e15=Entry(aa, width=100)
    e15.grid(row=18, column=1)

    verb4=Label(aa, text="enter a verb ending in 'ing':")
    verb4.grid(row=19, column=0)
    e16=Entry(aa, width=100)
    e16.grid(row=19, column=1)

    adj5=Label(aa, text="enter an adjective:")
    adj5.grid(row=20, column=0)
    e17=Entry(aa, width=100)
    e17.grid(row=20, column=1)


    med=Label(aa, text="enter a medical device:")
    med.grid(row=21, column=0)
    e18=Entry(aa, width=100)
    e18.grid(row=21, column=1)

    wait=Label(aa, text="a thing you wouldn't want your waiter saying:")
    wait.grid(row=22, column=0)
    e19=Entry(aa, width=100)
    e19.grid(row=22, column=1)

    number2=Label(aa, text="enter another number:")
    number2.grid(row=23, column=0)
    e20=Entry(aa, width=100)
    e20.grid(row=23, column=1)


    rest=Label(aa, text="enter a restauraunt chain:")
    rest.grid(row=24, column=0)
    e21=Entry(aa, width=100)
    e21.grid(row=24, column=1)

    event=Label(aa, text="enter an event that you celebrate:")
    event.grid(row=25, column=0)
    e22=Entry(aa, width=100)
    e22.grid(row=25, column=1)

    hide=Label(aa, text="something you would hide if a guest comes to your house:")
    hide.grid(row=26, column=0)
    e23=Entry(aa, width=100)
    e23.grid(row=26, column=1)

    cell=Label(aa, text="last thing you watched in your cellphone:")
    cell.grid(row=27, column=0)
    e24=Entry(aa, width=100)
    e24.grid(row=27, column=1)


    celeb=Label(aa, text="enter the name of a celebrity:")
    celeb.grid(row=28, column=0)
    e25=Entry(aa, width=100)
    e25.grid(row=28, column=1)


    verb10=Label(aa, text="enter a verb:")
    verb10.grid(row=29, column=0)
    e26=Entry(aa, width=100)
    e26.grid(row=29, column=1)

    google=Label(aa, text="enter the last question you googled:")
    google.grid(row=30, column=0)
    e27=Entry(aa, width=100)
    e27.grid(row=30, column=1)

    organ=Label(aa, text="enter the name of an organ:")
    organ.grid(row=31, column=0)
    e28=Entry(aa, width=100)
    e28.grid(row=31, column=1)

    dream=Label(aa, text="enter your dream profession:")
    dream.grid(row=32, column=0)
    e29=Entry(aa, width=100)
    e29.grid(row=32, column=1)

    stadium=Label(aa, text="enter a slogan you'd say at a stadium:")
    stadium.grid(row=33, column=0)
    e30=Entry(aa, width=100)
    e30.grid(row=33, column=1)


#function to get the user input
    def newclick():
        airplane=Toplevel(aa)

        birds1= e8.get()
        number010=e9.get()
        ficplace1=e10.get()
        sillyword1=e11.get()
        fooditem1=e12.get()
        weird1=e13.get()
        time1=e14.get()
        ins1=e15.get()
        verb41=e16.get()
        adj51=e17.get()
        med1=e18.get()
        wait1=e19.get()
        number02=e20.get()
        rest1=e21.get()
        event1=e22.get()
        hide1=e23.get()
        cell1=e24.get()
        celeb1=e25.get()
        verb101=e26.get()
        google1=e27.get()
        organ1=e28.get()
        dream1=e29.get()
        stadium1=e30.get()


        if birds1 and number010 and ficplace1 and sillyword1 and fooditem1 and weird1 and time1 and ins1 and verb41 and adj51 and med1 and wait1 and number02 and rest1 and event1 and hide1 and cell1 and celeb1 and verb101 and google1 and organ1 and dream1 and stadium1 !="":
            

      
#final output formed with user inputs
            madlib21=Label(airplane,text="The following is an announcement made on an aeroplane before the commencement of it's flight:", font = ("Times New Roman", 15), background="green", foreground="white")
            madlib21.grid(row=9, column=1)
            madlib2= Label(airplane, text= " \n \n Good afternoon ladies and gentlemen \n Welcome aboard  " + birds1+" airlines flight "+number010+" with non stop service to "+ficplace1+". I am Ron "+sillyword1+" your chief cabin crew. We aplogize for the "+time1+ " delay as we are stalled \n because "+ ins1+" are "+verb41+" on the runway. \n Before we depart we would like you to pay attention to this "+adj51+" safety announcement. Ensure that all electronic devices including mobile phones,\n laptops and "+med1+" are turned off and stowed.\n If we see you using one, we will kindly come up to you and say "+wait1+" There are "+number02+" exits on this airplane.\nIn case of emergency please locate your nearest "+rest1+ " In the event of an "+event1+" a "+hide1+" will drop from above your seat. Please ensure that \n you have yours on before assisting others. \nOur in flight entertainment includes "+cell1+" and a bonus documentary on "+celeb1+" learning to cook "+fooditem1+". If you have a question like \n "+google1+" please raise your "+ organ1+" and wave it. \nThis holiday season we hope you become a "+dream1+". On behalf of myself, the cabin crew, Captain Mark "+sillyword1+" and first officer "+weird1+", we at "+birds1+" Airlines wish you \n a pleasant flight and "+stadium1)

            madlib2.grid(row=10, column=1)

        else:
            txt1=Label(airplane,text="Please enter all the inputs!", background="red", font=('Times New Roman',15))
            txt1.grid(row=35,column=1)
        

    bt2 = Button(aa, text = "Click to generate madlib", command= newclick) #button to generate madlibs
    bt2.grid(row=34, column=1)



b2=Button(root,text="Flight Announcement",command=madlib2)#button to open the second madlib
b2.grid(row=10,column=1)




root.mainloop()
