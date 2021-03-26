#liquid in a microwave

''' ---- NOTE: I did simple testing with my 1000 watt microwave and found that
it seemed to only output around 525 watts. I did initial testing to understand
the actual wattage of the microwave then used that number (525) to do additional
tests to heat water to different end temperatures, all of which seemed to check
out

You can use this program to help you heat up your liquids in a microwave more accurately.

'''

import PySimpleGUI as sg
from math import floor

''' ----------- variables -----------'''
sph_h2o = 4184      #specific heat of h2o, units joules/kg C
weight_1fl_oz_h2o = 0.03    #weight of 1 fl oz of h2o in kg
#oz_h2o = 0.03       #weight of 1 fl oz of h2o in kg
x=25
y=1
just = 'left'

''' --------------GUI Layout ---------------- '''
layout_main = [[sg.Text('Choose unknown value')],
                [sg.B('get time'), sg.B('get temp')]]
window_main = sg.Window('Main Window', layout_main)


layout1 = [[sg.Text('Input information below', font = ('', 28), justification = just, text_color = 'black')],
            [sg.Text('input wattage of microwave:', size = (x,y), justification=just), sg.InputText('1000', size = (x,y), justification=just, key = 'micro_watt')],
            [sg.Text('efficiency of microwave in %:', size = (x,y), justification=just), sg.InputText('52.5', size = (x,y), justification=just, key = 'eff')],
            [sg.Text('input oz of liquid to heat:', size = (x,y), justification=just), sg.InputText('8', size = (x,y), justification=just, key = 'fl_oz')],
            [sg.Text('input starting temp of liquid in °F:', size = (x,y), justification=just), sg.InputText('70', size = (x,y), justification=just, key = 's_temp')],
            [sg.Text('input ending temp of liquid in °F:', size = (x,y), justification=just), sg.InputText('120', size = (x,y), justification=just, key = 'e_temp')],
            [sg.Text('time needed in microwave:', size = (x,y), justification=just), sg.Text("? seconds", size = (22,y), justification=just, key = 'time_micro', background_color='white',text_color='black')],
            [sg.Button("total time"), sg.Button("EXIT")]]

window1 = sg.Window('liquid in a microwave (time)', layout1)

layout2 = [[sg.Text('Input information below', font = ('', 28), justification = just, text_color = 'black')],
            [sg.Text('input wattage of microwave:', size = (x,y), justification=just), sg.InputText('1000', size = (x,y), justification=just, key = 'micro_watt')],
            [sg.Text('efficiency of microwave in %:', size = (x,y), justification=just), sg.InputText('52.5', size = (x,y), justification=just, key = 'eff')],
            [sg.Text('input oz of liquid to heat:', size = (x,y), justification=just), sg.InputText('8', size = (x,y), justification=just, key = 'fl_oz')],
            [sg.Text('input starting temp of liquid in °F:', size = (x,y), justification=just), sg.InputText('70', size = (x,y), justification=just, key = 's_temp')],
            [sg.Text('input time in microwave', size = (x,y), justification=just), sg.InputText('60', size = (x,y), justification=just, key = 'sec')],
            [sg.Text('ending temp of liquid in °F', size = (x,y), justification=just), sg.Text("? °F", size = (22,y), justification=just, key = 'temp_micro', background_color='white',text_color='black')],
            [sg.Button("get temp"), sg.Button("EXIT")]]

window2 = sg.Window('liquid in a microwave (temp)', layout2)

''' ------------- Loop ------------------ '''
while True:
    event, values = window_main.read()
    if event in (None, 'EXIT'):
        break

    if event == 'get time':
        window_main.close()
        while True:
            event1, values = window1.read()

            if event1 in (None,'EXIT'):
                break

            if event1 == "total time":
                watt_of_micro = int(values['micro_watt'])
                eff = round(float(values['eff']),0)/100
                mug_oz = float(values['fl_oz'])
                s_temp_f = float(values['s_temp'])
                e_temp_f = float(values['e_temp'])
                delta_temp_c = round(((e_temp_f-32)*5/9) - ((s_temp_f-32)*5/9),1)
                J_per_mug_to_increase_1c = sph_h2o*weight_1fl_oz_h2o*mug_oz
                J_to_heat_mug_to_end_t = J_per_mug_to_increase_1c*delta_temp_c
                sec_in_microwave = J_to_heat_mug_to_end_t / (watt_of_micro*eff)
                if sec_in_microwave >=60:
                    minute = floor(sec_in_microwave/60)
                else:
                    minute = 0
                sec = int(sec_in_microwave%60)
                time = str(minute) + ' min, ' + str(sec) + ' sec'

                #time = str(int(sec_in_microwave)) + ' seconds'
                window1['time_micro'].update(time)

    if event == 'get temp':
        window_main.close()
        while True:
            event2, values = window2.read()

            if event2 in (None,'EXIT'):
                break
            if event2 == 'get temp':
                watt_of_micro = int(values['micro_watt'])
                eff = round(float(values['eff']),0)/100
                mug_oz = float(values['fl_oz'])
                s_temp_f = float(values['s_temp'])
                s_temp_c = (s_temp_f-32)*5/9
                #e_temp_f = float(values['e_temp'])
                sec = float(values['sec'])
                J_per_mug_to_increase_1c = sph_h2o*weight_1fl_oz_h2o*mug_oz
                temp_end_c = ((sec * watt_of_micro * eff)/(J_per_mug_to_increase_1c)) + s_temp_c
                temp_end_f = (temp_end_c * 9/5) + 32
                temp_end_f_str = str(int(temp_end_f)) + ' °F'
                window2['temp_micro'].update(temp_end_f_str)


window1.close()
