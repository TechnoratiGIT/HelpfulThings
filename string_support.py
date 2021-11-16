import bugfixing_help as bh


def string_to_int_bool(string_: str):
    """
    turns an String into an integer or an bool or doesn't change it at all
    :param string_: ein string mit True, False einer integer oder ein ganz normaler
    :return: value of that string as an integer an boolean or if the string is not purely one of those the string back
    """
    if string_ == "True":
        return True
    elif string_ == "False":
        return False
    elif string_ == "None":
        return None
    else:
        try:
            string_ = int(string_)
        finally:
            return string_


def string_to_list(string_: str):
    list_ = []
    for i in range(len(string_)):
        list_.append(string_[i])
    return list_


def exchange(list_: list, old, new):
    for i in range(len(list_)):
        if list_[i] == old:
            list_[i] = new


def sort_out(list_: list, out1, out2=None):
    b = list_
    s = []
    for value in b:
        if value != out1 and value != out2:
            s.append(value)
    return s
