import os
from Homework2 import Task5


entries2 = [f for f in os.listdir('Homework2') if not f.startswith('__')]
entries3 = [f for f in os.listdir('Homework3') if not f.startswith('__')]
entries4 = [f for f in os.listdir('Homework4') if not f.startswith('__')]

print(entries2)

