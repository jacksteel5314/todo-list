import PySimpleGUI as sg

label_one = sg.Text("Enter feet: ")
input_one = sg.Input(key="feet")

label_two = sg.Text("Enter inches: ")
input_two = sg.Input(key="inches")

output_label = sg.Text("", key="output")

convert_button = sg.Button("Convert")
convert = sg.Window("Converter", [[label_one, input_one],[label_two, input_two],[convert_button, output_label]])

while True:
    event, values = convert.read()
    feet = float(values['feet'])
    inches = float(values['inches'])
    meter = feet * 0.3048 + inches * .0254
    meters = str(meter) + " m"
    convert["output"].update(value=meters, text_color="white")

convert.close()