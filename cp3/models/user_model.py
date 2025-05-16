from models.db.py import get_connection

class Usuario:
    def __init__(self, id, nome, login, senha, perfil):
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha
        self.perfil = perfil

    @staticmethod
    def criar_tabelas():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                login TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                perfil TEXT CHECK(perfil IN ('admin', 'user')) NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logins (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def salvar(nome, login, senha, perfil):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nome, login, senha, perfil)
            VALUES (?, ?, ?, ?)
        ''', (nome, login, senha, perfil))
        conn.commit()
        conn.close()

    @staticmethod
    def buscar_por_login(login):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE login = ?', (login,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Usuario(row['id'], row['nome'], row['login'], row['senha'], row['perfil'])
        return None

    @staticmethod
    def registrar_login(usuario_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO logins (usuario_id) VALUES (?)', (usuario_id,))
        conn.commit()
        conn.close()
