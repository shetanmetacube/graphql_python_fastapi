#python model sentence similarity
from sentence_transformers import SentenceTransformer,util
import pandas as pd
from openai.embeddings_utils import cosine_similarity
import numpy as np
from openai.embeddings_utils import get_embedding
from ariadne import QueryType
from model import Company
import openai
from getpass import getpass

query = QueryType()

orders = []
openai.api_key = "your_open_api_key"

#resolver to get all companies list
@query.field("getAllCompanyInfo")
def resolve_all_companies(_, info):
    all_company_list = []
    df = pd.read_csv("company_info_table.csv")
    lis_index = df['Unnamed: 0'].index.to_list()
    for i in lis_index:
     row = df.iloc[i]
     com = Company(row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
     all_company_list.append(com)
    return all_company_list

#get similar statement resolver
@query.field("getSimilarCompaniesInfo")
def resolve_get_similar_sentenece(_, info, name, top_k):
  df = pd.read_csv('company_embedding_table.csv')
  df['embedding'] = df['embedding'].apply(eval).apply(np.array)
  search_term_vector = get_embedding(name, engine='text-similarity-davinci-001')
  #This for returning the info of similar company
  df["similarities"] = df['embedding'].apply(lambda x: cosine_similarity(x, search_term_vector))
  df1 = df.sort_values("similarities", ascending=False).head(top_k)
  lis_index = df1['Unnamed: 0'].index.to_list()
  info_df = pd.read_csv('company_info_table.csv')
  similar_company_list = []
  for i in lis_index:
    row = info_df.iloc[i]
    com = Company(row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
    similar_company_list.append(com)
  return similar_company_list
   
#get total statement present
@query.field("allStatementsForSimilaritySearch")
def resolve_all_senteneces_list(_, info):
    #get embedding from csv
  embeddings_df = pd.read_csv("company_statement_table.csv")
  #get sentence from embeddings_df
  corpus = embeddings_df["sentence"].tolist()
  return corpus

