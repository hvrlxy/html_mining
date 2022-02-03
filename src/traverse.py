import bs4
from bs4 import Comment

def get_children(node):
    '''
    return a list of node
    :param node:
    :return:
    '''
    child_list = []
    for child in node.children:
        if child.name is not None:
            child_list.append(child)

    return child_list

def print_children(node):
    '''
    print a list of direct children names
    :param child_list:
    :return:
    '''

    child_list = get_children(node)
    for child in child_list:
        print(child.name)

def compare_node_structure(node1, node2):
    '''
    given two soup nodes, return whether they have the same node structure
    :param node1: a soup node
    :param node2: a soup node
    :return: true or false
    '''
    if node1 == '\n' and node2 == '\n':
        return True
    if isinstance(node1, bs4.element.NavigableString) and isinstance(node2, bs4.element.NavigableString):
        return True

    if node1.name != node2.name:
        # print('tag name error')
        return False
    if node1.has_attr('class') and node2.has_attr('class') and node1['class'] != node2['class']:
        # print('class name error')
        return False

    children1 = node1.contents
    children2 = node2.contents
    children1 = [child for child in children1 if child != '\n']
    children2 = [child for child in children2 if child != '\n']
    if len(children1) != len(children2):
        return False

    for i in range(len(children1)):
        if not compare_node_structure(children1[i], children2[i]):
            return False
    return True

def check_contain_info(node):
    '''
    check if a html tag contain any useful data (navigable string)
    :param node: a soup node
    :return: true or false
    '''
    if node.string is not None:
        return True
    children = [child for child in node.contents if child.name is not None and child.name != '\n']
    for child in children:
        if check_contain_info(child):
            return True
    return False


def check_contain_df(node):
    '''
    Given a soup tree node, check if it or its subtree contains any valuable data
    :param node: a soup node
    :return: list of data
    '''
    children = node.contents
    children = [child for child in children if child != '\n']
    final_list = []
    if len(children) < 2:
        return []
    starting = children[0]
    counter = 1
    while (not check_contain_info(starting) or isinstance(starting,Comment)) and counter < len(children):
        starting = children[counter]
        counter += 1

    for i in range(1, len(children)):
        if isinstance(children[i],Comment):
            continue
        if compare_node_structure(starting, children[i]):
            final_list.append(children[i])
    if len(final_list) < 3:
        return []
    final_list.append(starting)
    return final_list

def find_keys_name(strings_dict, orig_name):
    '''
    Given a dictionary consists of df name available, return the appropriate name for the df
    :param strings_dict: dictionary consist of df name and content
    :param orig_name: the original name given by the traversal
    :return: a new name for the df
    '''
    if orig_name not in strings_dict.keys():
        return orig_name
    count = 1
    name = orig_name
    while name in strings_dict.keys():
        name = orig_name + str(count)
        count += 1
    return name

def traverse(head):
    '''
    traverse the tree, find all dataframe available and return a dictionary of the df name
    and its content
    :param head: soup tree node
    :return: a dictionary of df name - df content
    '''
    items_dict = {}

    def find_all_df(node):
        final_list = check_contain_df(node)
        if node.has_attr('class'):
            print(node['class'])

        if len(final_list) != 0:
            if node.has_attr('class'):
                items_dict[find_keys_name(items_dict, ''.join([word for word in node['class']]))] = final_list
            else:
                items_dict[find_keys_name(items_dict, node.name)] = final_list

        children = [child for child in node.contents if child != '\n' and child.name is not None]
        for child in children:
            find_all_df(child)

    find_all_df(head)

    if len(items_dict) == 0:
        print('There is no dataframe detected')
    return items_dict










