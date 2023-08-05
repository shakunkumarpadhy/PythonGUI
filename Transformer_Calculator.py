import math
from tkinter import *

def Answer():
    OpenCircuitTestResults, ShortCircuitTestResults = getvalues()

    CosTheta = OpenCircuitTestResults[2]/(OpenCircuitTestResults[0]*OpenCircuitTestResults[1])
    Theta = math.acos(CosTheta)
    SnTheta = math.sin(Theta)
    iMagnetizingLV = OpenCircuitTestResults[1]*SnTheta
    iCoreLossLV = OpenCircuitTestResults[1]*CosTheta
    rCoreLossLV = OpenCircuitTestResults[0]/iMagnetizingLV
    rCoreLossLV = round(rCoreLossLV,2)
    xMagnetizingLV = OpenCircuitTestResults[0]/iCoreLossLV
    xMagnetizingLV = round(xMagnetizingLV,2)

    rEquivalentHV = ShortCircuitTestResults[2]/ShortCircuitTestResults[1]**2
    rEquivalentHV = round(rEquivalentHV,2)
    zShortCircuitHV = ShortCircuitTestResults[0]/ShortCircuitTestResults[1]
    xEquivalentHVsquare = zShortCircuitHV**2- rEquivalentHV**2
    xEquivalentHV = xEquivalentHVsquare**0.5
    xEquivalentHV = round(xEquivalentHV,2)
    t1=f'Resistance representing core loss reffered to LV is {xMagnetizingLV}Ω.'
    t2=f'Magnetizing reactance reffered to LV is {rCoreLossLV}Ω.'
    t3=f'Equivalent resistance reffered to HV is {rEquivalentHV}Ω.'
    t4=f'Equivalent reactance reffered to HV is {xEquivalentHV}Ω.'
    text1=Message(main,text=t1,bg='red',fg='black',font=('algerian',10,'bold'),width=5000)
    text2=Message(main,text=t2,bg='red',fg='black',font=('algerian',10,'bold'),width=5000)
    text3=Message(main,text=t3,bg='red',fg='black',font=('algerian',10,'bold'),width=5000)
    text4=Message(main,text=t4,bg='red',fg='black',font=('algerian',10,'bold'),width=5000)
    text1.grid(row=5,column=2)
    text2.grid(row=6,column=2)
    text3.grid(row=7,column=2)
    text4.grid(row=8,column=2)
##    print("###########################values are#########################")
##    print(f'Resistance representing core loss reffered to LV is {xMagnetizingLV}Ω.')
##    print(f'Magnetizing reactance reffered to LV is {rCoreLossLV}Ω.')
##    print(f'Equivalent resistance reffered to HV is {rEquivalentHV}Ω.')
##    print(f'Equivalent reactance reffered to HV is {xEquivalentHV}Ω.')

def getvalues():
    p = []
    q = []
    Vsc = float(ValueVoltageShortCircuit.get())
    Voc = float(ValueVoltageOPenCircuit.get())
    Isc = float(ValueCurrentShortCircuit.get())
    Ioc = float(ValueCurrentOpenCircuit.get())
    Psc = float(ValuePowerShortCircuit.get())
    Poc = float(ValuePowerOpenCircuit.get())
    ShirtcircuitData = [Vsc,Isc,Psc]
    oc_data = [Voc,Ioc,Poc]
    for i in oc_data:
        p.append(i)
    for j in ShirtcircuitData:
        q.append(j)
    return p, q

main = Tk()
main['bg'] = 'blue'
main.geometry('1000x500')
main.title('###TRANSFORMER_PARAMETERS###')
OpenCircuit_Test = Label(main, text='Open Circuit Test', borderwidth=6, relief=SUNKEN, font='comicsanms 12 bold', padx=25, pady=25,bg='orange')
ShortCircuit_Test = Label(main, text='Short Circuit Test', borderwidth=6, relief=SUNKEN, font='comicsanms 12 bold', padx=25, pady=25,bg='orange')
voltage = Label(main, text="Voltage (V)", font='comicsanms 12 bold', padx=25, pady=12, borderwidth=6, relief=SUNKEN,bg='orange')
current = Label(main, text="Current (A)", font='comicsanms 12 bold', padx=25, pady=12, borderwidth=6, relief=SUNKEN,bg='orange')
power = Label(main, text="Power (W)", font='comicsanms 12 bold', padx=25, pady=12, borderwidth=6, relief=SUNKEN,bg='orange')
OpenCircuit_Test.grid(row=1)
ShortCircuit_Test.grid(row=2)
voltage.grid(row=0,column=1)
current.grid(row=0,column=2)
power.grid(row=0,column=3)

ValueVoltageOPenCircuit = StringVar()
ValueVoltageShortCircuit = StringVar()
ValueCurrentOpenCircuit = StringVar()
ValueCurrentShortCircuit = StringVar()
ValuePowerOpenCircuit = StringVar()
ValuePowerShortCircuit = StringVar()

Voltage_At_Opencircuit = Entry(main, textvariable=ValueVoltageOPenCircuit, relief=SUNKEN, borderwidth=7)
Voltage_At_ShortCircuit = Entry(main, textvariable=ValueVoltageShortCircuit, relief=SUNKEN, borderwidth=7)
Current_At_Opencircuit = Entry(main, textvariable=ValueCurrentOpenCircuit, relief=SUNKEN, borderwidth=7)
Current_At_ShortCircuit = Entry(main, textvariable=ValueCurrentShortCircuit, relief=SUNKEN, borderwidth=7)
Power_At_OpenCircuit = Entry(main, textvariable=ValuePowerOpenCircuit, relief=SUNKEN, borderwidth=7)
Power_At_ShortCircuit = Entry(main, textvariable=ValuePowerShortCircuit, relief=SUNKEN, borderwidth=7)
Voltage_At_Opencircuit.grid(row=1, column=1)
Voltage_At_ShortCircuit.grid(row=2, column=1)
Current_At_Opencircuit.grid(row=1, column=2)
Current_At_ShortCircuit.grid(row=2, column=2)
Power_At_OpenCircuit.grid(row=1, column=3)
Power_At_ShortCircuit.grid(row=2, column=3)

submit = Button(main, text="SUBMIT", font=('comicsanms 14 bold'), borderwidth=6, command=Answer)
submit.grid(row=3, column=2)


main.mainloop()
