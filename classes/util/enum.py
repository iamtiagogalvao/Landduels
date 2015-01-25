from events.command import UnboundCommand

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    enums['values'] = UnboundCommand(values, enums)
    return type('Enum', (), enums)

# Example
# Numbers = enum('ZERO', 'ONE', 'TWO')
# >>> Numbers.ZERO
# 0
# >>> Numbers.ONE
# 1

def values(enumtype):
    return tuple([k for k,v in enumtype.items() if type(v) is int])