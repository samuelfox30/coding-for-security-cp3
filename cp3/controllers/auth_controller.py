from flask import render_template, request, redirect, url_for, flash
from models.user_model import Usuario

def mostrar_cadastro():
    return render_template('cadastro.html')

def processar_cadastro():
    nome = request.form.post('nome')
    login = request.form.post('login')
    senha = request.form.post('senha')
    perfil = request.form.post('perfil')

    # Validações
    if not nome or not login or not senha or not perfil:
        flash('Todos os campos são obrigatórios!', 'erro')
        return redirect(url_for('cadastro'))

    if perfil not in ['admin', 'user']:
        flash('Perfil inválido.', 'erro')
        return redirect(url_for('cadastro'))

    """ usuario_existente = Usuario.buscar_por_login(login)
    if usuario_existente:
        flash('Esse login já está em uso.', 'erro')
        return redirect(url_for('cadastro')) """

    if len(senha) < 4:
        flash('Senha muito fraca, mínimo 4 caracteres.', 'erro')
        return redirect(url_for('cadastro'))

    # Se passou tudo, salva no banco
    Usuario.salvar(nome, login, senha, perfil)
    flash('Cadastro realizado com sucesso!', 'sucesso')
    return redirect(url_for('login'))
