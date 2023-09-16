-- Limpar tabelas existentes
DROP TABLE IF EXISTS despesas, receitas, categorias, usuarios CASCADE;

-- Criar a tabela de usuários
CREATE TABLE usuarios (
    id BIGINT PRIMARY KEY,
    nome TEXT NOT NULL,
    username TEXT
);

-- Criar a tabela de categorias
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL
);

-- Preencher a tabela de categorias
INSERT INTO categorias (nome) VALUES
('Alimentação'),
('Transporte'),
('Saúde'),
('Educação'),
('Lazer');

-- Criar a tabela de despesas
CREATE TABLE despesas (
    id SERIAL PRIMARY KEY,
    valor FLOAT NOT NULL,
    data DATE NOT NULL,
    categoria_id INTEGER REFERENCES categorias(id),
    usuario_id BIGINT REFERENCES usuarios(id)
);

-- Criar a tabela de receitas
CREATE TABLE receitas (
    id SERIAL PRIMARY KEY,
    valor FLOAT NOT NULL,
    data DATE NOT NULL,
    categoria_id INTEGER REFERENCES categorias(id),
    usuario_id BIGINT REFERENCES usuarios(id)
);