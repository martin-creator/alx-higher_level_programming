#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    index_search = new_list.index(search)
    new_list[index_search] = replace
    return (new_list)    
