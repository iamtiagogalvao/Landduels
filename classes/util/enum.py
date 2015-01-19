

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

# Example
# Numbers = enum('ZERO', 'ONE', 'TWO')
# >>> Numbers.ZERO
# 0
# >>> Numbers.ONE
# 1

def values(enumtype):
    return tuple([k for k,v in enumtype.__dict__.items() if type(v) is int])