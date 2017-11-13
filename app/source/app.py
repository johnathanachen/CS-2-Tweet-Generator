from donald_scrape import run_srape
from tokenize import histogram
import sample

# import cleanup
# import word_count
# import sentence

word_list = run_srape()
histogram(word_list)
