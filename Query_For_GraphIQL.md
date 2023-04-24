# Mutation Queries

## To fetch data from api to csv file()
```
 mutation StoreDataIntoCSVFromAPI{
   storeDataIntoCSVFromAPI(api_url:"https://api-generator.retool.com/wCVJ2c/searchcompanies")
}
```
# To create sentence embedding
```
 mutation{
   createSentenceEmbedding
}
```

## To add an Single New Company
```
  mutation AddNewCompany($comJson: String!){
    addNewCompany(company_json_str: $comJson)
}

variable tab:- 

{
  "comJson": "{\"id\":1,\"NAME\":\"Metacube\",\"RANK\":\"1\",\"EMPLOYEES\":\"2200000\",\"ASSETS ($M)\":\"$219,295.0\",\"URL_COMPANY\":\"http://www.walmart.com\",\"PROFITS ($M)\":\"$6,670.0\",\"REVENUES ($M)\":\"$514,405.0\",\"PROFITS PERCENT CHANGE\":\"-32.4%\",\"REVENUE PERCENT CHANGE\":\"2.8%\",\"MARKET VALUE - AS OF MARCH 29, 2019 ($M)\":\"$279,880.3\"}"
}
```


## Queries

# 1. To get All Companies Info, Get List Of Companies
```
 query GetAllCompanyInfos{
  getAllCompanyInfo{
    id
    name
    revenues
    revenue_percent_change
    profits_percent_change
    url_company
  }
}
```

## 2. To Get Similar Comapanies , For an given company
```
query GetSimilarCompaniesInfo($name: String!, $top_k: Int!){
  getSimilarCompaniesInfo(name: $name, top_k: $top_k){
    id
    name
    revenues
    profits
    
  } 
  
}

{
  "name": "Metacube company",
  "top_k": 10
}
```

## 3.To get All Statement stored in file
```
query AllStatementsForSimilaritySearch{
  allStatementsForSimilaritySearch
}
```

