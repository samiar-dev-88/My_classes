def show_info(**info):
    for key, value in info.items():
        print(key, "=", value)

show_info(
    name="Samiar",
    age=16,
    job="Programmer"
)