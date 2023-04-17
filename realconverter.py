import PySimpleGUI as sg

layout = [
    [
     sg.Input(key = '-INPUT-'),
     sg.Text('From'),
     sg.Spin(['km','kg','sec'], key = '-UNITS-'), 
     sg.Text('To'),
     sg.Spin(['mile','pound','min'], key = '-UNITS2-'),
     sg.Button('Convert', key = '-CONVERT-')
    ],
    [sg.Text('Output: '),sg.Text('Here', key = '-OUTPUT-')],
    [],
    [],
]


window = sg.Window('Converter',layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '-CONVERT-':
        val = (values['-INPUT-'])
        if val.isnumeric():
           if values['-UNITS-']=='kg':
            if values['-UNITS2-']=='pound':
                output = round(float(val)*2.20462,6)
                out_str = f'{val} kgs = {output} pounds'
            else:
                out_str = "Incompatible"
            window['-OUTPUT-'].update(out_str)

           if values['-UNITS-']=='km':
             if values['-UNITS2-']=='mile':
                output = round(float(val)*0.6214,6)
                out_str = f'{val} km = {output} miles'
             else:
                out_str = "Incompatible"
             window['-OUTPUT-'].update(out_str)

           if values['-UNITS-']=='sec':
                if values['-UNITS2-']=='min':
                    output = round(float(val)/60,2)
                    out_str = f'{val} secs = {output} min'
                else:
                    out_str = "Incompatible"
                window['-OUTPUT-'].update(out_str)
        else:
            print("Enter numbers not strings/ characters")

window.close()