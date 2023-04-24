#python model sentence similarity
#from sentence_transformers import SentenceTransformer,util
import pandas as pd
import requests
import json
import openai
from model import Company
from ariadne import MutationType
from openai.embeddings_utils import get_embedding
from utils import addNewCompanyEmbedding

openai.api_key = "your_open_api_key"
mutation = MutationType()


#create embedding using REST APIs
@mutation.field("createSentenceEmbedding")
def resolve_create_sentence_embedding(_, info):
    input_file_path = 'company_info_table.csv'
    # Read CSV file
    data = pd.read_csv(input_file_path)
    # Combine the columns you want to use for generating embeddings
    company_info_sentences = []
    # Iterate through the DataFrame and create sentences
    for index, row in data.iterrows():
     company_info = f"company {row['NAME']} has {row['REVENUES ($M)']} in revenue and {int(row['EMPLOYEES'])} employees."
     company_info_sentences.append(company_info)
   # Generate embeddings for the company info sentences
    df = pd.DataFrame(company_info_sentences, columns=["sentence"])
    # Save the DataFrame to a CSV file
    df.to_csv('company_statement_table.csv')
    df['embedding'] = df['sentence'].apply(lambda x: get_embedding(x, engine='text-similarity-davinci-001'))
    # Convert embeddings to a DataFrame and merge with the original data
    #embeddings_df = pd.DataFrame(company_embeddings, columns=[f'embedding_{i}' for i in range(company_embeddings.shape[1])])
    df.to_csv('company_embedding_table.csv')
    return "Embedding Done!"

#mutation to add an new company
@mutation.field("addNewCompany")
def resolve_add_new_company(*_, company_json_str):
    js_obj = json.loads(company_json_str)
    new_data_df = pd.DataFrame(js_obj, index=[0])
    # Read the existing CSV file into a DataFrame
    csv_file = 'company_info_table.csv'
    existing_data_df = pd.read_csv(csv_file)
    # Concatenate the existing DataFrame with the new DataFrame
    combined_data_df = pd.concat([existing_data_df, new_data_df], ignore_index=True)
    combined_data_df.to_csv(csv_file, index=False)
    addNewCompanyEmbedding()
    company_to_return = Company(js_obj.name, js_obj.rank, js_obj.employees, js_obj.assets , js_obj.url_company,js_obj.profits ,js_obj.revenues ,js_obj.profits_percent_change, js_obj.revenue_percent_change)
    return company_to_return

@mutation.field("storeDataIntoCSVFromAPI")
def resolve_get_data_into_csv_from_apis(_, info, api_url):
    response = requests.get(api_url, verify=False)
    data = response.json()
    df = pd.DataFrame(data)
    for col in df.columns:
     if df[col].apply(lambda x: isinstance(x, dict)).any():
        df[col] = df[col].apply(json.dumps)
    df.to_csv("company_info_table.csv")
    return "Data Saved Successfully , do creating embedding for latest data"
    