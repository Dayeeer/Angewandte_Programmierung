from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
import json
from pathlib import Path

app = FastAPI(
    title="Applied Programming Course HS-Coburg",
    description="Simple note management API",
    version="1.0.0",
)

### Class endpoints ###

@app.get("/")
def root():
    return {"message": "Hello, World"}


@app.get("/status")
def get_status():
    return {"status": "offline", "version": "0.2.0", "day": 1}


@app.get("/about")
def get_about():
    return {
        "project": "My First API",
        "author": "Yeromina Daria",  
        "course": "Applied Programming",
    }


@app.get("/name/{name}")
def greet_name(name: str):
    return {"message": f"Hello, {name}!"}

### Homework endpoints ###

@app.get("/square/{number}")
def calculate_square(number: int):
    result = number * number
    return {
        "number": number,
        "square": result,
        "calculation": f"{number} × {number} = {result}",
    }


@app.get("/student")
def get_student():
    return {
        "name": "Daria Yeromina",  
        "semester": 1,              
        "course": "Wirtschaftsinformatik",
        "university": "HS Coburg"    
    }


@app.get("/double/{number}")
def calculate_double(number: int):
    result = number * 2
    return{
        "number": number,
        "double": result,
        "calculation": f"{number} * 2 = {result}",
    }


@app.get("/even/{number}")
def check_even(number: int):
    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return {
        "number": number,
        "type": result
    }

