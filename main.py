import _thread

DEBUG_MODE = False


# decorator Errors handling
def decorator(func):
    if DEBUG_MODE:
        print("Debugger mode is on")

    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return f"Wrong input{IndexError} (*tip format of string in CMD: 1st - command, 2nd - Name, 3rd - Phone#). Try again!"
        except ValueError:
            return f"Wrong input. Valid command should be first.({ValueError}) Try again!"
        except KeyError:
            return f"Wrong input. No such entity.({KeyError}) Try again!"

    return inner


class UserDict:
    pass


class AddressBook(UserDict):
    def __init__(self):
        self.contacts = {'Gill': '+42218454556', 'Bill': '+4742988567',
                         'Ostap': '+380001112233', 'Olena': '+380002323234'}

    @decorator
    def show_all(self):
        f = 'Address Book:\n'
        if self.contacts:
            for k, v in self.contacts.items():
                f += f'\nUser {k} with phone:\t|  {v}'
            print(f.rstrip())
        else:
            print(f'{f.rstrip()} no enteties yet')

    @decorator
    def hello(self):
        return '[class] How can I help you?'

    @decorator
    def clear(self):
        self.contacts.clear()
        return f"Address Book removed"

    @decorator
    def abort(self):
        print("Closing... \nGood bye! See you later.")
        _thread.exit()


class Name:
    pass


class Phone:
    pass


class Record:
    @decorator
    def phone(self):
        if ab.contacts[self]:
            return f"Phone number of user '{self}' is: '{ab.contacts.get(self)}'"
        else:
            return KeyError

    @decorator
    def remove(self):
        ab.contacts.pop(self)
        return f"Contact '{self}' removed from Address Book"

    @decorator
    def add_contacts(self, lst=None):
        if lst:
            ab.contacts.update({self: lst})
        else:
            ab.contacts.update({self: 'no number set'})

    @decorator
    def change(self, new_phone):
        ab.contacts.update({self: new_phone})
        return f"New phone number for user '{self}' to new: '{new_phone}'"


# initial_dict = {'Gill': '+42218454556', 'Bill': '+4742988567', 'Ostap': '+380001112233', 'Olena': '+380002323234'}
contacts = {'Gill': '+42218454556', 'Bill': '+4742988567',
            'Ostap': '+380001112233', 'Olena': '+380002323234'}


@decorator
def change(*args):
    contacts.update({args[0]: args[1]})
    return f"New phone number for user '{args[0]}' to new: '{args[1]}'"


ab = AddressBook()


INSTRUCTIONS = {
    ab.hello: ['hello', 'hi', 'Bonjourno'],
    Record.add_contacts: ['add', '+'],
    Record.change: ['change', '='],
    Record.phone: ['phone', 'new_phone'],
    Record.remove: ['delete', 'remove', '-'],
    ab.clear: ['clear', 'destroy'],
    ab.show_all: ['show', 'view'],
    ab.abort: ['close', '.', 'exit', 'quit', 'good bye']
}


def instructions_parser(user_input: str):
    new_str = None, None
    for instr, key_word in INSTRUCTIONS.items():
        for i in range(len(key_word)):
            if user_input.lower().startswith(key_word[i]):
                new_str = instr, user_input.replace(
                    key_word[i], "").strip().split()
    return new_str


def main():
    print("Hello. This is Address Book v 0.1.1")
    while True:
        user_input = input(">>>")
        command, data = instructions_parser(user_input)
        if not command:
            print(f"Unsupported command.")
        else:
            print(command(*data))


if __name__ == "__main__":
    main()
