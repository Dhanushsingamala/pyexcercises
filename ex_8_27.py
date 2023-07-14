class MyClass:
    def __init__(self, int1, float1, str1, tuple1, list1, dict1):
        self.vars = {'int': int1, 'float': float1, 'str': str1,
                     'tuple': tuple1, 'list': list1, 'dict': dict1}

    def __repr__(self):
        # Convert variables to their string representations
        int1 = self.vars['int']
        float1 = self.vars['float']
        str1 = self.vars['str']
        tuple1 = self.vars['tuple']
        list1 = self.vars['list']
        dict1 = self.vars['dict']
        # Return a string that can be used to recreate the object
        return f"MyClass({int1}, {float1}, '{str1}', {tuple1}, {list1}, {dict1})"

    def __str__(self):
        # Return a nicely formatted string representation of the data structures
        return f"int: {self.vars['int']}\n" \
               f"float: {self.vars['float']}\n" \
               f"str: {self.vars['str']}\n" \
               f"tuple: {self.vars['tuple']}\n" \
               f"list: {self.vars['list']}\n" \
               f"dict: {self.vars['dict']}"

    def load(self, string):
        string = string.strip()
        # Split the string representation into individual values
        values = string.split(',')
        # Extract and convert each value to its appropriate type
        int1 = int(values[0])           
        float1 = float(values[1])
        str1 = values[2].strip()[1:-1]
        tuple1 = tuple(values[3].strip()[1:-1].split("'"))
        list1 = [item.strip() for item in values[4].strip()[1:-1].split(",")]
        # Accessing the dictionaary items first using index 4 in string format
        dict_items = values[5].strip()[1:-1].split(',')
        dict1 = {}
        # Convert dictionary string representation to a dictionary object
        for item in dict_items:
            key, value = item.split(':')
            dict1[key.strip()[1:-1]] = value.strip()
        # Update the variables in the instance with the loaded values
        self.vars = {'int': int1, 'float': float1, 'str': str1,
                     'tuple': tuple1, 'list': list1, 'dict': dict1}
        
# Usage of Myclass 
a = MyClass(4, 5.1, 'some string', ('some', 'tuple'),
             ['another', 'list', 'with', 5, 6],
             {'key1': 1, 'key2': ('another', 'tuple')})

b = repr(a)
print(b)
output = str(a)
print(output)
