CREATE TABLE admin (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO admin (email, password) VALUES ('gutoadm@ecompjr.com', 'mudaeu123');
INSERT INTO admin (email, password) VALUES ('marcaoadm@ecompjr.com', 'mudaeu123');
INSERT INTO admin (email, password) VALUES ('brenoadm@ecompjr.com', 'mudaeu123');

CREATE TABLE form (
    id SERIAL PRIMARY KEY,
    client_name VARCHAR(255) NOT NULL,
    client_email VARCHAR(255) UNIQUE NOT NULL,
    service_description VARCHAR(512) NOT NULL,
);

INSERT INTO admin 
(client_name, client_email, service_description) VALUES 
('Comedian', 'comedian@rorschachcloud.com', 'Serviços brutais de computação em nuvem, sem perguntas.');

INSERT INTO admin 
(client_name, client_email, service_description) VALUES 
('Dan Dreiberg', 'dan@rorschachcloud.com', 'Parceiro de negócios do Comedian na Rorschach Cloud Services.');


INSERT INTO admin 
(client_name, client_email, service_description) VALUES 
('Ozymandias', 'bigbrains12@gmail.com', 'Primo de segundo grau do jogo do tigre');