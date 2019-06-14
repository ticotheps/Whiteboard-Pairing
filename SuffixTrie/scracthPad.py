anything = {'p': {'o': {'g': {'o': {'*': True}}}}, 'o': {'g': {'o': {'*': True}}, '*': True}, 'g': {'o': {'*': True}}}

another_variable = {
    "p": {
        "o": {
            "g": {
                "o": {'*': True}
            }
        }
    },
    "o": {
        "g": {
            "o": {'*': True}
        },
        "*": True},
    "g": {
        "o": {'*': True}
    }
}

print(anything == another_variable)