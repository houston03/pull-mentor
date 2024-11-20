def tella(max_calls):
    def decor(func):
        calls = 0
        def ret(*args, **kwargs):
            nonlocal calls
            calls += 1
            if calls < max_calls:
                return func(*args, **kwargs)
            else:
                raise ValueError('calls limit')
        return ret
    return decor
@tella(3)
def call(name):
    print(f"Hello {name}")
    return "This should only print three times"

result = call('Pit')
result1 = call('Pit1')
result2 = call('Pit2')
result3 = call('Pit3')
print(result)