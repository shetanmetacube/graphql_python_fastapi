from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from ariadne import make_executable_schema, gql
from ariadne.asgi import GraphQL
from query_resolver import query
from muatation_resolver import mutation
from utils import load_schema_from_path



type_defs = gql(load_schema_from_path("schema.graphql"))
schema = make_executable_schema(type_defs, query, mutation)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/graphql")
async def graphql_playground():
    return HTMLResponse(content=PLAYGROUND_HTML, status_code=200)

app = FastAPI()
app.add_route("/", GraphQL(schema=schema))
