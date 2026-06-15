CREATE DATABASE IF NOT EXISTS salao_db;
USE salao_db;

CREATE TABLE IF NOT EXISTS profissionais (
    prof_id INT AUTO_INCREMENT PRIMARY KEY,
    prof_nome VARCHAR(100) NOT NULL,
    prof_especialidade VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS agendamentos (
    agend_id INT AUTO_INCREMENT PRIMARY KEY,
    prof_id INT NOT NULL,
    cli_id INT NOT NULL,
    data_hora DATETIME NOT NULL,
    FOREIGN KEY (prof_id) REFERENCES profissionais(prof_id)
);

INSERT INTO profissionais (prof_nome, prof_especialidade) VALUES
('Ana Silva', 'Cabelo'),
('Mariana Costa', 'Manicure');