# This file contains all the util methods
from sentence_transformers import SentenceTransformer,util
import pandas as pd
import openai
from openai.embeddings_utils import get_embedding
from ariadne import MutationType
from model import Company

openai.api_key = "your_open_api_key"
#load schema file into typedef
def load_schema_from_path(path: str) -> str:
    with open(path, "r") as file:
        return file.read()
    
#update the company_statement_table , company_embedding_table on adding an single comapany
def addNewCompanyEmbedding():
   input_file_path = 'company_info_table.csv'
   data = pd.read_csv(input_file_path)
   company_info_sentences = []
   for index, row in data.iterrows():
     company_info = f"{row['NAME']} has {row['REVENUES ($M)']} in revenue and {row['EMPLOYEES']} employees."
     company_info_sentences.append(company_info)
     
   df = pd.DataFrame(company_info_sentences, columns=["sentence"])
   df.to_csv('company_statement_table.csv', index=False)
   df['embedding'] = df['sentence'].apply(lambda x: get_embedding(x, engine='text-similarity-davinci-001'))
   df.to_csv('company_embedding_table.csv', index=False)
