#!/usr/bin/python

import learning

class Command:
    commands = 'help','override','printlast'

    def __init__(self, printer=print):
        self.printer = printer

    def override(self, args, last):
        data = learning.load()
        data[last][-1]['correct'] = True
        learning.save(data)
        return f"Last correct of {last} has been overridden"

    def printlast(self, args, last):
        data = learning.load()
        return f"{last}:\n"+data[last].__str__()

    def parse(self, string, last):
        if not string or string[0] != '/':
            return True

        command, *arguments = string.split(' ')
        command = command[1:]
        if command == 'help':
            self.printer("Available commands:\n    "+"\n    ".join(self.commands))
        elif command in self.commands:
            message = getattr(self,command)(arguments,
                   **{'last':last})
            self.printer(message)
        return False
