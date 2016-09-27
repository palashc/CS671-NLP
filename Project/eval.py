from pyrouge import Rouge155

r = Rouge155()
r.system_dir = '/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/attempt1/'
r.model_dir = '/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/abstracts/'
r.system_filename_pattern = 'a(\d+).txt'
r.model_filename_pattern = 'a#ID#.txt'

output = r.convert_and_evaluate()
print(output)
output_dict = r.output_to_dict(output)