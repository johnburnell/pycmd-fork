
class Commands(object):
    def __init__(self):
        self._aliases = {}
        self._commands = {}

commands = Commands()

def add_alias(cmd, alias):
    commands._aliases[cmd] = alias
    
def get_alias(cmd):
    if (cmd in commands._aliases):
        return commands._aliases[cmd]
    return None

#def get_command(cmd):
#    return None
