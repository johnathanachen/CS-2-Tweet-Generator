from cleanup import Clean
from markov import Markov

file_name = "transcript.txt"
data = Clean(file_name)
x = Markov(data, 10)

print(x)
