from CustomCommands import get_alias

def command_hook(cmd, tokens):
    '''Provide a hook to reinterpret the current command.
       Mainly used for aliases
    '''

    # New code adding custom commands
    alias = get_alias(cmd.lower())
    if alias is not None:
        cmd = alias[0]
        tokens = alias + tokens[1:]

    return cmd, tokens
