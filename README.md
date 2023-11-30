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

<h1>## How to consume the APIs</h1>
<code>$ docker-compose up</code><br>
<p>You aways need a token to access the form data. Using postman or insomnia clients, first make a POST request to auth server (port 3309) </p>
<code>$ docker-compose up</code><br>
<p>Make a POST request to the auth-server. The request body has to be in a format like this below:</p>
<code>
    {
    	"email":"example@gmail.com",
    	"password":"123456"
    }
</code>
<p>The server then sends back 2 types of JWT tokens to be used to pass authorization test that guaranties security in each and every request make to an form endpoint.</p>

<p>Used IPs:</p>
<ul>
    <li>
        Auth Server:
            <code>http://host-ip:3309/signup</code>
            <code>http://host-ip:3309/login</code>
    </li>
    <li>
        Form Server:
            <code>http://host-ip:8080/api/v1/read-form</code>
            <code>http://host-ip:8080/api/v1/read-form</code>
    </li>
</ul>
<p>See an response example below:</p>
<img width="344" alt="image" src="https://github.com/AnesioSousa/ecompJR2023.2/assets/39014361/5986ba1b-1f7c-460e-80bc-77dee7b33ee3">
<p>Copy the given access token and paste in a estructure like this:</p>
<img width="350" alt="image" src="https://github.com/AnesioSousa/ecompJR2023.2/assets/39014361/f5f72c98-8c4a-4454-b941-bc72ea422465">

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
