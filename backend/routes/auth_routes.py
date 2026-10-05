from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import session_db
from main import bcrypt_context, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

auth_router = APIRouter(prefix="/autenticacao", tags=["autenticacao"])

def criar_token(id_usuario, duracao_token=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    data_expiracao = datetime.now(timezone.utc) + duracao_token
    dict_info = {
        "sub": id_usuario,
        "exp": data_expiracao
    }
    jwt_codificado = jwt.encode(dict_info, SECRET_KEY, ALGORITHM)
    
    return jwt_codificado

def verificar_token(token, session: Session=Depends(session_db)):
    usuario = session.query(Usuario).filter(Usuario.id==1).first()
    return 

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()

    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """
    return {
        "mensagem": "Você acessou a rota de autenticação",
        "autenticado": False
    }

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session=Depends(session_db)):
    nome = usuario_schema.nome
    email = usuario_schema.email
    senha = usuario_schema.senha
    ativo = usuario_schema.ativo
    admin = usuario_schema.admin
    usuario = session.query(Usuario).filter(Usuario.email==nome).first()

    if usuario:
        raise HTTPException(status_code=400, detail="Este e-mail já está cadastrado no sistema.")
    else:
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome, email, senha_criptografada, ativo, admin)
        session.add(novo_usuario)
        session.commit()

        return {"mensagem": f"{email} cadastrado com sucesso"}

@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session=Depends(session_db)):
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)

    if not usuario:
        raise HTTPException(status_code=400, detail="E-mail e/ou senha incorretos")
    else:
        access_token = criar_token(usuario.id)
        refresh_token = criar_token(usuario.id, duracao_token=timedelta(days=7))
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer"
        }

@auth_router.get("/refresh")
async def use_refresh_token(token):
    usuario = verificar_token(token)
    access_token = criar_token(usuario.id)

    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }