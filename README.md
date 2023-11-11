# backend-template
Repositório dedicado ao template dos projetos a partir de 2023

## API Under construction 🚧
-  Authentication (Crypto or Hash)
- Add logger file (logging all the methods success and fails)
- Route to use getMany on repository (filter route) 

## How to execute in command line
- hypercorn Server.app --bind 0.0.0.0:8080 --reload

## Technologies
- FastAPI: Main Framework to API
- Hypercorn: ASGI Server to allows up the API client
- Tortoise: ORM
- Aerich: Database migration tool for Tortoise ORM
- Pydantic: Data validation

## Observations
- Why we are using the DTO?
    - For a way more easily data validation than manipulating the tortoise model.
- Why we have been using Hypercorn?
    - The hypercorn is a library that provides more scalability and durable for the next years because it allows us to use HTTP/1, HTTP/2, WebSockets (over HTTP/1 and HTTP/2), ASGI/2, and ASGI/3 specifications. 
        In contrast Univcorn supports just HTTP/1.1 and WebSockets.

    