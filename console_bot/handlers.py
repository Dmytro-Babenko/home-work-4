import re

def input_error(func):
    def inner(name, number, *args):
        try:
            output = func(name, number, *args)
        except KeyError:
            output = 'There no such contact'
        except ValueError:
            output = 'There no number in the command'
        return output
    return inner


def choose_hendler(command, *_):

    def hello(*_):
        output = 'How can I help you?'
        return output

    @input_error
    def adding(name, number):
        if not number:
            raise ValueError
        contacts[name] = number
        output = f'Contact {name}: {number} is saved'
        return output

    @input_error
    def changing(name, number):
        if not number:
            raise ValueError
        if name not in contacts:
            raise KeyError
        contacts[name] = number
        output = f'Contact {name}: {number} is changed'
        return output

    @input_error
    def get_phone(name, *_):
        number = contacts[name]
        return number

    def show_all(*_):
        return contacts

    def good_bye(*_):
        output = "Good bye"
        return output

    OPERATIONS = {
        'hello': hello,
        'add': adding,
        'change': changing,
        'phone': get_phone,
        'show all': show_all,
        'close': good_bye,
        'good bye': good_bye,
        'exit': good_bye,

    }

    hendler =  OPERATIONS[command]   
    return hendler

def pharser(message: str) -> tuple[str, str, str]:
    KEY_WORDS = 'hello|add|change|phone|show all|good bye|close|exit'
    command, name, number = None, None, None
    message = message.strip()
    command_match = re.search(fr'^{KEY_WORDS}', message, re.IGNORECASE)
    if command_match:
        command = command_match.group()
        message = re.sub(command, '', message)
        command = command.lower()

    number_match = re.search(fr'\d+$', message)
    if number_match:
        number = number_match.group()
        message = re.sub(number, '', message)

    name = message.strip()

    # elements = re.search(fr'(?P<command>^{KEY_WORDS}) ?(?P<name>\D*) (?<!\d)(?P<number>\d*$)', message, re.IGNORECASE)
    # if not elements:
    #     return command, name, number
    # command = elements.group('command').lower()
    # name = elements.group('name').strip()
    # number = elements.group('number')
    return command, name, number
    
contacts = {}
def main():
    output = ''
    while output != 'Good bye':
        inp = input('Write your command: ')
        command, name, number  = pharser(inp)
        try:
            hendler = choose_hendler(command)
        except KeyError:
            print('There are no command')
            continue
        output = hendler(name, number)
        print(output)

if __name__ == '__main__':
    main()


# def sum(x, y):
#     return x + y

# sum(4)
