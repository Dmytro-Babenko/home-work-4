import re

def input_error(func):
    def inner(*args):
        try:
            output = func(*args)
        except KeyError:
            output = 'There no such contact'
        except ValueError:
            output = 'Its not number'
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
        'close': good_bye
    }

    hendler =  OPERATIONS[command]   
    return hendler

def pharser(message: str) -> tuple[str, str, str]:
    KEY_WORDS = 'hello|add|change|phone|show all|good bye|close'
    elements = re.search(f'(?P<command>^{KEY_WORDS}) ?(?P<name>\D*) ?(?P<number> ?\d*)', message, re.IGNORECASE)
    if not elements:
        return '', '', ''
    command = elements.group('command').lower()
    name = elements.group('name').strip()
    number = elements.group('number')
    return command, name, number
    
contacts = {}
def main():
    output = ''
    while output != 'Good bye':
        inp = input('Write your command: ')
        command, name, number  = pharser(inp)
        print(command)
        try:
            hendler = choose_hendler(command)
        except KeyError:
            print('There are no such command')
            continue
        output = hendler(name, number)
        print(output)

if __name__ == '__main__':
    main()


# def sum(x, y):
#     return x + y

# sum(4)
