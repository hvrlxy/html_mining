import pandas as pd

def find_keys_name(strings_dict, orig_name):
    '''
    given a dictionary of key names and the original name, check if the name exist in the
    dictionary and make modification accordingly
    :param strings_dict: a dictionary of df name and content
    :param orig_name: string of name
    :return: new string
    '''
    if orig_name not in strings_dict.keys():
        return orig_name
    count = 1
    name = orig_name
    while name in strings_dict.keys():
        name = orig_name + str(count)
        count += 1
    return name

def extract_strings(head):
    '''
    given a soup node, extract all data available inside it/its subtree
    :param head: a soup node
    :return: a dictionary, with keys are the tag of the data and the value are the content
    '''
    strings_dict = {}

    def recursive_string(node):
        if node.name is None:
            return
        if node.string is not None and node.string.strip() != '':
            if node.has_attr('class'):
                strings_dict[find_keys_name(strings_dict, node['class'][0])] = node.string
                return
            else:
                strings_dict[find_keys_name(strings_dict, node.name)] = node.string
                return

        children = [child for child in node.contents if child != '\n' and child.name is not None]
        for child in children:
            recursive_string(child)

    recursive_string(head)
    return strings_dict

def convert_to_df(items_list):
    '''
    given a list of dictionary, turn them into a pandas df
    :param items_list: list of dictionary
    :return: pandas dataframe
    '''
    if len(extract_strings(items_list[0]).keys()) < 2:
        return None
    data_dict = [extract_strings(item) for item in items_list]
    data_df = pd.DataFrame(data_dict)
    return data_df

def convert_all_df(items_dict):
    '''
    convert all dataframes found in the webpage into pandas dataframe
    :param items_dict:
    :return: dictionary of pandas dataframes
    '''
    df_dict = {}
    for name in items_dict.keys():
        print(name)
        convert_df = convert_to_df(items_dict[name])
        if convert_df is not None:
            print(name)
            df_dict[name] = convert_df

    return df_dict

def convert_to_excel(df_dict, file_name):
    '''
    convert the dataframes found into an excel file
    :param df_dict:
    :param file_name: intended excel file
    :return: an excel file
    '''
    writer = pd.ExcelWriter(file_name)
    for df_name in df_dict.keys():
        new_name = df_name.replace('[', '').replace(']', '')[:30]
        df_dict[df_name].to_excel(writer, new_name)

    writer.save()





