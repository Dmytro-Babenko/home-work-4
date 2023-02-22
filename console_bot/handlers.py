from functools import reduce
def input_error(func):
    '''Decorator that handles errors in the handlers'''
    def inner(name, number, *args):
        try:
            output = func(name, number, *args)
        except KeyError:
            output = 'There no such contact'
        except ValueError:
            output = 'There no number in the command'
        except NameError:
            output = 'This contact is already in the list'
        return output
    return inner

def hello(*_):
    '''Return bots greeting'''
    output = 'How can I help you?'
    return output

@input_error
def adding(name, number):
    '''Add contact to dictionary'''
    if not number:
        raise ValueError
    if name in contacts:
        raise NameError
    contacts[name] = number
    output = f'Contact {name}: {number} is saved'
    return output

@input_error
def changing(name, number):
    '''Change contact in the dictionary'''
    if not number:
        raise ValueError
    if name not in contacts:
        raise KeyError
    contacts[name] = number
    output = f'Contact {name}: {number} is changed'
    return output

@input_error
def get_phone(name, *_):
    '''Return number received contact'''
    number = contacts[name]
    return number

def show_all(*_):
    '''Return message with all contacts'''
    if not contacts:
        return 'There are no contacts in list'

    output = reduce(lambda s, t: '\n'.join((s, f'{t[0]}: {t[1]}')), 
                        contacts.items(), 'Yor contacts:')
    return output

def good_bye(*_):
    '''Return bot goodbye'''
    output = "Good bye"
    return output

contacts = {}




