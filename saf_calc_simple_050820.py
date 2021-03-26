import PySimpleGUI as sg
import math

xx=15
y=1
K=1

# dictionary for K value
K_dict={
    '1018 _ Brinell = 126' : 1.88 ,
    '4130 alloy steel  _ Brinell = 156' : 1.66 ,
    '4140 alloy steel _ Brinell = 200' : 1.44 ,
    'low carbon steel _ Brinell = 18-26Rc' : 1.08 ,
    'low carbon steel _ Brinell = 24-32Rc' : 1.14 ,
    '303 Stainless  _ Brinell = 135-185' : 1.001 ,
    '304 stainless cold rolled  _ Brinell = 225-275' : 0.633 ,
    '316 Stainless  _ Brinell = 185-220' : 0.689 ,
    '6061-t6 _ Brinell = 95' : 3.344 ,
    '7075-t6 _ Brinell = 150' : 2 ,
    }

klist= [0,0]
klist.clear()

for x in K_dict:
    klist.append(x)

print(klist)

def f_SFM():
    sfm=round((math.pi*rpm*tool_dia)/12)
    window['-SFM-'].update(sfm)

def f_IPM():
    sfm = round((math.pi*rpm*tool_dia)/12)
    window['-SFM-'].update(sfm)

def f_RPM():
    rpm = int((12*sfm)/(math.pi*tool_dia))
    window['-rpm-'].update(rpm)

def f_HP():
    combo=values['combo']
    K=K_dict[(combo)]
    est_hp = round(MMR / K,2)
    window['-est_hp-'].update(est_hp)

sg.theme('LightGreen1')
# all the stuff insde your window
layout = [ [sg.Button('Enter desired rpm', size=(xx,y), key='-bRPM-'), sg.InputText('0', key = '-rpm-')],
           [sg.Text('Enter # of flutes', size=(xx,y), justification='center'), sg.InputText('3', key='-num_fl-')],
           [sg.Text('Enter IPT:', size=(xx,y), justification='center'), sg.InputText('0.001', key='-ipt-')],
           [sg.Text('Enter tool dia', size=(xx,y), justification='center'), sg.InputText('0.25', key='-tool_dia')],
           [sg.Button('SFM', size=(xx,y), key='-bSFM-'), sg.InputText('0', key='-SFM-')],
           [sg.Button('IPM', size=(xx,y), key='-bIPM-'), sg.InputText('0', key='-IPM-')],
           [sg.Text('select material', size=(xx,y), justification='center'), sg.Combo(klist, key='combo')],
           [sg.Text('enter axial DOC', size=(xx,y), justification='center'), sg.InputText('0.25', key='-adoc-')],
           [sg.Text('enter radial DOC', size=(xx,y), justification='center'), sg.InputText('0.025', key='-rdoc-')],
           [sg.Button('Est. HP', size=(xx,y), key='-bEst_hp-'), sg.InputText('1', key='-est_hp-')],
           [sg.Button('Exit', size=(xx,y), key='-exit-')]
           ]

# create the window
window = sg.Window('Machining Calculator', layout)
#event loop

while True:
    event, values = window.read()
    rpm = int(values['-rpm-'])
    num_fl = int(values['-num_fl-'])
    ipt = float(values['-ipt-'])
    tool_dia = float(values['-tool_dia'])
    sfm = int(values['-SFM-'])
    ipm = float(values['-IPM-'])
    adoc = float(values['-adoc-'])
    rdoc = float(values['-rdoc-'])
    MMR = adoc*rdoc*ipm


    if event == '-bSFM-':
        f_SFM()

    if event == '-bIPM-':
        f_IPM()
        #ipm = round(rpm*ipt*num_fl,1)
        #window['-IPM-'].update(ipm)

    if event == '-bRPM-':
        f_RPM()
        #rpm = int((12*sfm)/(math.pi*tool_dia))
        #window['-rpm-'].update(rpm)

    if event == '-bEst_hp-':
        combo=values['combo']
        K=K_dict[(combo)]
        est_hp = round(MMR / K,2)
        window['-est_hp-'].update(est_hp)

    if event == '-exit-':
        window.close()

window.close()
