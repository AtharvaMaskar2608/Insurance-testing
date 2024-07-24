from tree_class import Tree
from dotenv import load_dotenv

load_dotenv()

tree = Tree("/home/choice/Desktop/Insuarance/mapping/hierarchical_data_ICICI.json")

query = "Mumbai, Car, OD, Petrol, 1500cc, Rs. 1,50,000"

commission = tree.get_commision_rate(query)

print(commission)
