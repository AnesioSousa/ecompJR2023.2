# backend-template

Clone do repositório template usado na EcompJr que tem por objetivo padronizar a criação de projetos a partir de 2023.

## API Under construction 🚧

- Authentication (Crypto or Hash)
- Add logger file (logging all the methods success and fails)
- Route to use getMany on repository (filter route)

<h1>## How to run the application</h1>
The simplest way to test the project is having docker installed, download the docker-compose.yml file in this repository and then typing:<br>
<code>$ docker-compose up</code><br>
<p>in a command interpreter like unix shell. </p>
<h3>Other ways of running:</h3>
<p>Clone the repository. Open the downloaded folder in your favorite code editor. Type:</p>
<ul>
    <li><code>hypercorn Server.app --bind 0.0.0.0:8080 --reload</code><br><p>or</p></li>
    <li><code>python Server.py</code></li>
</ul>

## Technologies
- FastAPI: Main Framework to API
- Hypercorn: ASGI Server to allows up the API client
- Tortoise: ORM
- Aerich: Database migration tool for Tortoise ORM
- Pydantic: Data validation
<br>
## Observations

- Why we are using the DTO?
  - For a way more easily data validation than manipulating the tortoise model.
- Why we have been using Hypercorn?
  - The hypercorn is a library that provides more scalability and durable for the next years because it allows us to use HTTP/1, HTTP/2, WebSockets (over HTTP/1 and HTTP/2), ASGI/2, and ASGI/3 specifications.
    In contrast Univcorn supports just HTTP/1.1 and WebSockets.
