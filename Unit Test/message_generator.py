def get_today_name():
    # This function returns the name of today. In a real implementation,
    # you might use datetime or a similar module to get the actual day name.
    raise NotImplementedError("This function should be mocked in tests.")


def get_message():
    today_name = get_today_name()
    return f'Hello {today_name}!'
