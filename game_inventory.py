
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.
from tabulate import tabulate
import csv
dict_invetory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    '''Display the inventory like this:
    rope: 1
    torch: 6
    '''
    dict_invetory = [[key, value] for key, value in dict_invetory.items()]
    key = (0)
    dict_invetory = sorted(dict_invetory, key=lambda z: z[key])
    dict_invetory = dict((key, value) for key, value in dict_invetory)
    for key, value in dict_invetory.items():
        print(key + ":", value)


def add_to_inventory(inventory, added_items):
    '''Add to the inventory dictionary a list of items from added_items.'''
    for key, value in dict_invetory.items():
        if key in list_loot_inventory:
            dict_invetory[key] += list_loot_inventory.count(key)
    for key in list_loot_inventory:
        if key not in dict_invetory.keys():
            dict_invetory[key] = list_loot_inventory.count(key)
    return dict_invetory


def print_table(inventory, order=None):
    '''
    Take your inventory and display it in a well-organized table with
    each column right-justified like this:

    -----------------
    item name | count
    -----------------
         rope |     1
        torch |     6
    -----------------

    The 'order' parameter (string) works as follows:
    - None (by default) means the table is unordered
    - "count,desc" means the table is ordered by count (of items in the
      inventory) in descending order
    - "count,asc" means the table is ordered by count in ascending order
    '''
    try:
        if order[0] == "count,asc":
            print(tabulate(dict_invetory, headers=['Item name', 'Count'], tablefmt='orgtbl'))
        elif order[0] == "count,desc":
            print(tabulate((dict_invetory[::-1]), headers=['Item name', 'Count'], tablefmt='orgtbl'))
    except IndexError:
        print(tabulate(dict_invetory, headers=['Item name', 'Count'], tablefmt='orgtbl'))


def import_inventory(inventory, filename="import_inventory.csv"):
    '''
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    '''

    with open(filename, 'r') as f:
        read = f.readlines()
        import_list_items = ''.join(read).split(',')
        import_list_items = add_to_inventory(dict_invetory, import_list_items)
        import_list_items = [[key, value] for key, value in import_list_items.items()]
        list_of_tup_of_import_invent = sorted(import_list_items, key=lambda z: z[1])
    return list_of_tup_of_import_invent

def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
	'''
   with open(filename, "w", newline='') as f:
        the_writer = csv.writer(f)
        for element in dict_invetory:
            the_writer.writerow(element)


display_inventory(dict_invetory)
print()
display_inventory(add_to_inventory(dict_invetory, dragon_loot))
dict_invetory = import_inventory(dict_invetory)
print(dict_invetory)
print_table(dict_invetory,"count,desc" )
export_inventory(dict_invetory)