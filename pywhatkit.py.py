from easygui import *
import pywhatkit as py
import csv
while True:
    title="Setup Page"
    msg="Enter password "
    defpass=""
    crctpass="sps@1112"
    pas=passwordbox(msg,title,defpass)
    if pas==None or pas!=crctpass:
        title="Exit"
        msg="---------------------------------------------"+"The password you entered is wrong"+"\n"+"\nTry again later"+"\n"+"---------------------------------------------"
        button="EXIT"
        msgbox(msg,title,button)
        break
    else:
        title="CSV"
        msg="Enter the Name of excel file with csv extension "
        location=enterbox(msg,title)
        while True:
            if location==None:
                title="Exit"
                msg="Enter a valid spreedsheet name"+"\n"+"Start the process from first"
                button="EXIT"
                msgbox(msg,title,button)
                break
            else:
                title="Ready State"
                msg="Your Setup has complete"+"\n"+"Press Start to send the fees details of the students to their respective parents whatsapp number"
                button="START"
                msgbox(msg,title,button)
                file=open(location+".csv","r")
                data=csv.reader(file)
                for i in data:
                    ph="+91"+i[9]
                    if i[4]=="Paid" and i[6]=="Paid":
                        continue
                    elif i[4]=="Paid" and i[6]=="Not Paid" :
                        msg=" Greetings from SPS,"+"\n"+i[1]+" You haven\'t pay the 2nd installment fees,we request you to pay the fees within the due date.Pending fees in 1st installment is : "+i[5]+"\n"+"Guys,This is program given by rishi sir.....Do not consider this message"
                        py.sendwhatmsg_instantly(ph,msg)
                        py.close_tab(5)
                    elif i[4]=="Not Paid" and i[6]=="Not Paid":
                        msg=" Greetings from SPS,"+"\n"+i[1]+"You haven\'t pay the 1st and 2nd installment fees,we request you to pay the fees within the due date."+"\n"+"Total fees you have to pay is : "+i[8]+"\n"+"Guys,This is program given by rishi sir.....Do not consider this message"
                        py.sendwhatmsg_instantly(ph,msg)
                        py.close_tab(5)
                    else:
                        continue
                file.close()