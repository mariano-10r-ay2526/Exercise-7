# getting data from a textbox
from pyscript import display, document


def get_name(e):
    document.getElementById('div1').innerHTML = ' '
    ruby_students = ['barlisan', 'allas', 'panela', 'tabije', 'piansay', 'tan', 'veran']

    l_name = document.getElementById('lname').value.lower().strip()
    name_checker = l_name in ruby_students  # true (1) or false (0)

    display_message = ('Sorry, your name is not in the list', f'{l_name} is in the list!')

    display(display_message[name_checker], target='div1') # displays the message