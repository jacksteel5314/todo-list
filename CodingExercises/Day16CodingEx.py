import PySimpleGUI as sg

label_one = sg.Text("Enter feet: ")
input_one = sg.Input()

label_two = sg.Text("Enter inches: ")
input_two = sg.Input()

convert_button = sg.Button("Convert")
convert = sg.Window("Converter", [[label_one, input_one],[label_two, input_two],[convert_button]])
convert.read()
convert.close()