FROM python:3.10.13-alpine3.18

# Set the working directory inside the container
WORKDIR /home/EcompJrProjects/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /home/EcompJrProjects/app

EXPOSE 8080

ENV APP_NAME = "Landing Page"
ENV APP_DESCRIPTION = "Desafio técnico EcompJr 2023.2"
ENV ACCESS_TOKEN_SECRET = bdcdbdf616228d81ae19eac9c57e44a644015fc99a4a3155add5982c26e1ea1cd5c9c1f869988b039660c9057b6fbbdcc21378c838ac3827e438d18c0aa901d7
ENV REFRESH_TOKEN_SECRET = 123
ENV REFRESH_TOKEN_EXPIRATION = 60
ENV GENERATE_SCHEMAS=True
ENV APP_PORT=8080
ENV SERVER_AUTH_PORT=3309
ENV SERVER_DATABASE_HOST=127.0.0.1
ENV POSTGRES_USER=admin_ecompjr
ENV POSTGRES_PASSWORD=EcompJr123@



# Command to run your application
CMD ["python", "Server.py"]