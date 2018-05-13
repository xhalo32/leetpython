#!/usr/bin/python

import learning
from difflib import get_close_matches

class Command:
    commands = 'help','override','printlast'

    def __init__(self, printer=print):
        self.printer = printer

    def override(self, args, last, **kwargs):
        '''
        Override the last word's last correct value to True
        '''
        if not last:
            return "The last word doesn't exist"
        data = learning.load()
        data[last][-1]['correct'] = True
        learning.save(data)
        return f"Last correct of '{last}' has been overridden"

    def printlast(self, args, last, **kwargs):
        if not last:
            return "No info available"
        data = learning.load()
        return f"{last}:\n"+data[last].__str__()

    def help(self, args, **kwargs):
        return "Available commands:\n    "+"\n    ".join(self.commands)

    def execute(self, name, arguments, **kwargs):
        return getattr(self, name)(arguments, **kwargs)

    def parse(self, string, last):
        if not string or string[0] != '/':
            return True

        command, *arguments = string.split(' ')
        command = command[1:]
        if command in self.commands:
            message = self.execute(command, arguments, last=last)
            self.printer(message)
        else:
            self.printer(f"'{command}' is not a valid command")
            self.execute('help', arguments)
        return False
