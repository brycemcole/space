import PySimpleGUI as sg
import password

sg.theme("DarkGrey10")
layout = [
    [sg.Text("Press \"Generate\" to create a new password")],
    [sg.InputText('#####-#####-#####', use_readonly_for_disable=True,
                  disabled=True, size=(50, 10), key="-OUTPUT-")],
    [[sg.Slider(range=(8, 32), default_value=18,
                orientation="horizontal", size=(50, 10), key="-LENGTH-")]],
    [sg.Text("Generation method:")],
    [
        sg.Radio("Default", "type", default=True,
                 key="-DEFAULT-", enable_events=True),
        sg.Radio("Custom", "type", default=False,
                 key="-DEFAULT-", enable_events=True)
    ],
    [
        sg.Checkbox("Lower Letters", default=True,
                    key="-LOWER-", visible=False),
        sg.Checkbox("Uppercase Letters", default=False,
                    key="-UPPER-", visible=False)
    ],
    [
        sg.Checkbox("Numbers", default=True, key="-NUMBERS-", visible=False),
        sg.Checkbox("Symbols", default=False, key="-SYMBOLS-", visible=False)
    ],
    [[sg.T("                        "), sg.Button("Generate", size=(10, 1.1))]], [sg.T("")], ]
window = sg.Window("Password Generator", layout, size=(300, 300))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Generate":
        if values["-DEFAULT-"]:
            window["-OUTPUT-"].update(password.build(int(values["-LENGTH-"])))
        else:
            type = []
            if not window["-OUTPUT-"] and not values["-NUMBERS-"] and not values["-UPPER-"] and not values["-LOWER-"]:
                window["-OUTPUT-"].update("Please select at least one option")
            if values["-LOWER-"]:
                type.append("lower")
            if values["-UPPER-"]:
                type.append("upper")
            if values["-NUMBERS-"]:
                type.append("numbers")
            if values["-SYMBOLS-"]:
                type.append("symbols")
            window["-OUTPUT-"].update(password.build(int(values["-LENGTH-"]), type))
    if values["-DEFAULT-"]:
        window["-LOWER-"].update(visible=False)
        window["-UPPER-"].update(visible=False)
        window["-NUMBERS-"].update(visible=False)
        window["-SYMBOLS-"].update(visible=False)
        window.refresh()
    elif not values["-DEFAULT-"]:
        window["-LOWER-"].update(visible=True)
        window["-UPPER-"].update(visible=True)
        window["-NUMBERS-"].update(visible=True)
        window["-SYMBOLS-"].update(visible=True)
