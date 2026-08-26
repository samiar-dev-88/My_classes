def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(10, 20, 30, name="Samiar", age=16)