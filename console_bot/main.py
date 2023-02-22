import re
import handlers

OPERATIONS = {
    'hello': handlers.hello,
    'add': handlers.adding,
    'change': handlers.changing,
    'phone': handlers.get_phone,
    'show all': handlers.show_all,
    'close': handlers.good_bye,
    'good bye': handlers.good_bye,
    'exit':handlers.good_bye,
}

COMMAND_WORDS = '|'.join(OPERATIONS)

def parser(message: str) -> tuple[str|None, str|None, str|None]:
    '''
    Parse message to command, name and number.
    command: one of the COMMAND_WORD at the beginning
    number: didgits at the end of the message after space
    name: all symbols between command and number
    '''
    command, name, number = None, None, None
    message = message.strip()
    command_match = re.search(fr'^{COMMAND_WORDS}', message, re.IGNORECASE)
    if command_match:
        command = command_match.group()
        message = re.sub(command, '', message)
        command = command.lower()

    number_match = re.search(fr' (\d+)$', message)
    if number_match:
        number = number_match.group(1).strip()
        message = re.sub(number, '', message)

    name = message.strip()
    return command, name, number

contacts = handlers.contacts

def main():
    while True:
        inp = input('Write your command: ')
        command, name, number  = parser(inp)
        try:
            hendler = OPERATIONS[command]
        except KeyError:
            print('There are no command')
            continue
        output = hendler(name, number)
        print(output)
        if output == 'Good bye':
            break
    return contacts

if __name__ == '__main__':
    main()

