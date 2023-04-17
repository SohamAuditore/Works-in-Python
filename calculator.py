import PySimpleGUI as py
def create_new_window(theme):
    py.theme(theme)
    py.set_options(font = 'Verdana 16')
    layout = [
        #[py.DropDown('DarkBlue12 DarkBlue13 DarkBlue14 DarkBlue15 DarkBlue16 DarkBlue17 Purple Python',key='-THEME-',expand_x=True)],
        [py.Text(
            'Themes (Right click to change)',
            key='-theme-',
            justification='left', 
            right_click_menu = themes
            )],
        [py.Text('Output',key='-TEXT-',expand_x=True)],
        [py.Input(key='-INPUT-', justification='right', pad=(10,20))],
        [py.Button('=',key='=',size=(6,2), expand_x=True), py.Button('Clear',key='Clear',size=(6,2), expand_x=True)],
        [py.Button(7, size=(3,1), expand_x=True),py.Button(8, size=(3,1), expand_x=True), py.Button(9, size=(3,1), expand_x=True), py.Button('/', size=(3,1), expand_x=True)],
        [py.Button(4, size=(3,1), expand_x=True),py.Button(5, size=(3,1), expand_x=True), py.Button(6, size=(3,1), expand_x=True), py.Button('*', size=(3,1), expand_x=True)],
        [py.Button(1, size=(3,1), expand_x=True),py.Button(2, size=(3,1), expand_x=True), py.Button(3, size=(3,1), expand_x=True), py.Button('-', size=(3,1), expand_x=True)],
        [py.Button('<-', size=(3,1), expand_x=True, key='back'),py.Button(0, size=(3,1), expand_x=True), py.Button('.', size=(3,1), expand_x=True), py.Button('+', size=(3,1), expand_x=True)],
    ]
    return py.Window('Calculator',layout)

themes = ['Menu',['DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17','Purple', 'Python']]
window = create_new_window('dark')
currentlist = []
full_operation = []

while True:
    event, values = window.read()
    if event == py.WIN_CLOSED:
        break

    if event in themes[1]:
        window.close()
        window = create_new_window(event)

    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        currentlist.append(event)
        num_string = ''.join(currentlist)
        window['-INPUT-'].update(num_string)

    if event in ['+','-','*','/','^']:
        full_operation.append(''.join(currentlist))
        currentlist=[]
        full_operation.append(event)
        window['-INPUT-'].update('')

    if event == 'back':
        currentlist.pop()
        num_string = ''.join(currentlist)
        window['-INPUT-'].update(num_string)
        

    if event == '=':
        full_operation.append(''.join(currentlist))
        result = eval(''.join(full_operation))
        window['-INPUT-'].update(result)
        full_operation = []

    if event == 'Clear':
        currentlist = []
        full_operation = []
        window['-INPUT-'].update('')

window.close()