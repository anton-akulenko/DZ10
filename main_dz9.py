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
            return f"Wrong input. Valid command should be first.({KeyError}) Try again!"

    return inner


# initial_dict = {'Gill': '+42218454556', 'Bill': '+4742988567', 'Ostap': '+380001112233', 'Olena': '+380002323234'}
contacts = {'Gill': '+42218454556', 'Bill': '+4742988567', 'Ostap': '+380001112233', 'Olena': '+380002323234'}


@decorator
def hello(*args):
    return 'How can I help you?'


@decorator
def add(*args):
    contacts.update({args[0]: args[1]})
    return f"Successfully added new entry, with name: '{args[0]}' and phone number: '{args[1]}'"


@decorator
def change(*args):
    contacts.update({args[0]: args[1]})
    return f"New phone number for user '{args[0]}' to new: '{args[1]}'"


@decorator
def phone(*args):
    if isinstance(contacts[args[0]]):
        contacts.get(args[0])
        return f"Phone number of user '{args[0]}' is: '{args[1]}'"
    else:
        return KeyError


@decorator
def remove(*args):
    contacts.pop(args[0])
    return f"Contact '{args[0]}' removed from Address Book"


@decorator
def show_all(*args):
    f = 'Address Book:\n'
    for k, v in contacts.items():
        f += f'User name:\t{k} with phone:\t{v} \n'
    return print(f.strip())


@decorator
def clear(*args):
    contacts.clear()
    return f"Address Book removed"


@decorator
def abort(*args):
    print("Closing... \nGood bye! See you later.")
    _thread.exit()


INSTRUCTIONS = {
    hello: ['hello', 'hi', 'Bonjourno'],
    add: ['add', '+'],
    change: ['change', '='],
    phone: ['phone', 'new_phone'],
    remove: ['delete', 'remove', '-'],
    clear: ['clear', 'destroy'],
    show_all: ['show', 'view'],
    abort: ['close', '.', 'exit', 'quit', 'good bye']
}


def instructions_parser(user_input: str):
    new_str = None, None
    for instr, key_word in INSTRUCTIONS.items():
        for i in range(len(key_word)):
            if user_input.lower().startswith(key_word[i]):
                new_str = instr, user_input.replace(key_word[i], "").strip().split()
    return new_str


def main():
    print("Hello. This is Address Book v0.0.1")
    while True:
        user_input = input(">>>")
        command, data = instructions_parser(user_input)
        if not command:
            print(f"Unsupported command.")
        else:
            print(command(*data))


if __name__ == "__main__":
    main()
