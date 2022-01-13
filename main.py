import PySimpleGUI as sg

sg.theme('LightBrown3')

layout = [
  [sg.Text("BMI Calculator")],
  [sg.Text('Enter your age, height, and weight to get your Body Mass Index value and description.', size=(40,3))],
  [sg.Text("Age: "), sg.Input(size=(3, 1), key='-AGE-'),
    sg.Text("Weight: "), sg.Input(size=(3,1), key='-WEIGHT-'),
    sg.Text("lbs.")],
  [sg.Button('Get BMI'), sg.Button('Exit')],
  [sg.Text("Results: "), sg.Text("", size=(25, 4), key='-OUTPUT-')],
          ]

window = sg.Window('BMI Calculator', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Get BMI':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update("You are " + values['-AGE-'] + " years old.")

window.close()