#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = list(map(lambda new_list: new_list.replace("search", "replace"), my_list))
