import sqlite3

# 1. Conectando ao banco de dados
conexao = sqlite3.connect("laboratorio.db")

# 2. Criando o cursor
cursor = conexao.cursor()

# 3. Criando a tabela de análises químicas
cursor.execute("""
CREATE TABLE IF NOT EXISTS analises (
    id INTEGER PRIMARY KEY,
    substancia TEXT NOT NULL,
    concentracao REAL NOT NULL,
    unidade TEXT NOT NULL
)
""")

# 4. Inserindo dados
cursor.execute("""
INSERT INTO analises (substancia, concentracao, unidade)
VALUES (?, ?, ?)
""", ("Ácido Clorídrico", 0.5, "mol/L"))

cursor.execute("""
INSERT INTO analises (substancia, concentracao, unidade)
VALUES (?, ?, ?)
""", ("Hidróxido de Sódio", 0.8, "mol/L"))

cursor.execute("""
INSERT INTO analises (substancia, concentracao, unidade)
VALUES (?, ?, ?)
""", ("Cloreto de Sódio", 1.2, "mol/L"))

# Salvando as alterações
conexao.commit()

# 5. Consultando os dados
print("\n--- ANÁLISES CADASTRADAS ---")

cursor.execute("SELECT * FROM analises")

analises = cursor.fetchall()

for analise in analises:
    print(analise)

# 6. Atualizando um registro
cursor.execute("""
UPDATE analises
SET concentracao = ?
WHERE id = ?
""", (0.6, 1))

conexao.commit()

print("\n--- APÓS A ATUALIZAÇÃO ---")

cursor.execute("SELECT * FROM analises")

analises = cursor.fetchall()

for analise in analises:
    print(analise)

# 7. Excluindo um registro
cursor.execute("""
DELETE FROM analises
WHERE id = ?
""", (3,))

conexao.commit()

print("\n--- APÓS A EXCLUSÃO ---")

cursor.execute("SELECT * FROM analises")

analises = cursor.fetchall()

for analise in analises:
    print(analise)

# 8. Fechando a conexão
conexao.close()

print("\nBanco de dados fechado!")
