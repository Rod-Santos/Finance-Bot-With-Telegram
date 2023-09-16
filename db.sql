conforme necessidade
-- Cria a tabela de usuários
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    telegram_id BIGINT UNIQUE NOT NULL
);

-- Cria a tabela de categorias
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    usuario_id INTEGER REFERENCES usuarios(id) NULL
);

-- Cria a tabela de despesas
CREATE TABLE despesas (
    id SERIAL PRIMARY KEY,
    valor FLOAT NOT NULL,
    data DATE NOT NULL,
    categoria_id INTEGER REFERENCES categorias(id),
    usuario_id INTEGER REFERENCES usuarios(id)
);

-- Cria a tabela de receitas
CREATE TABLE receitas (
    id SERIAL PRIMARY KEY,
    valor FLOAT NOT NULL,
    data DATE NOT NULL,
    categoria_id INTEGER REFERENCES categorias(id),
    usuario_id INTEGER REFERENCES usuarios(id)
);

-- Inserir algumas categorias pré-definidas
INSERT INTO categorias (nome, usuario_id) VALUES ('Alimentação', NULL);
INSERT INTO categorias (nome, usuario_id) VALUES ('Transporte', NULL);
INSERT INTO categorias (nome, usuario_id) VALUES ('Saúde', NULL);
INSERT INTO categorias (nome, usuario_id) VALUES ('Educação', NULL);
INSERT INTO categorias (nome, usuario_id) VALUES ('Lazer', NULL);
