from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import session_db, verificar_token
from schemas import PedidoSchema, ItemPedidoSchema, ResponsePedidoSchema
from models import Pedido, Usuario, ItensPedido
from typing import List

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(verificar_token)])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do nosso sistema. Todas as rotas dos pedidos precisam de autenticação
    """
    return {
        "mensagem": "Você acessou a rota de pedidos"
    }


@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session=Depends(session_db)):
    novo_pedido = Pedido(usuario=pedido_schema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido criado com sucesso. Pedido Nº {novo_pedido.id}"}


@order_router.post("/pedido/cancelar/{id_pedido}")
async def cancelar_pedido(id_pedido: int, session: Session=Depends(session_db), usuario: Usuario=Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()

    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido não encontrado")

    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Você não pode cancelar esse pedido")
    
    pedido.status = "CANCELADO"
    session.commit()
    return {
        "mensagem": f"Pedido Nº {pedido.id} cancelado com suecesso", 
        "pedido": pedido
    }


@order_router.get("/listar_pedidos")
async def listar_pedidos(session: Session=Depends(session_db), usuario: Usuario=Depends(verificar_token)):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Você não pode acessar essa rota.")
    else:
        pedidos = session.query(Pedido).all()
        return {"pedidos": pedidos}


@order_router.post("/pedido/adicionar_item/{id_pedido}")
async def adicionar_item_pedido(
    id_pedido: int, 
    item_pedido_schema: ItemPedidoSchema, 
    session: Session=Depends(session_db), 
    usuario: Usuario=Depends(verificar_token)
):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()

    if not pedido:
        raise HTTPException(status_code=400, detail="Este pedido não existe")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Você não pode acessar essa rota")

    item_pedido = ItensPedido(
        item_pedido_schema.quantidade_itens,
        item_pedido_schema.sabor,
        item_pedido_schema.tamanho,
        item_pedido_schema.preco_unitario,
        id_pedido
    )
    session.add(item_pedido)
    pedido.calcular_preco()
    session.commit()

    return {
        "mensagem": "Item criado com sucesso",
        "item_pedido": item_pedido.id,
        "preco_pedido": pedido.preco_total
    }


@order_router.post("/pedido/remover_item/{id_item_pedido}")
async def remover_item_pedido(
    id_item_pedido: int, 
    session: Session=Depends(session_db), 
    usuario: Usuario=Depends(verificar_token)
):
    item_pedido = session.query(ItensPedido).filter(ItensPedido.id==id_item_pedido).first()
    pedido = session.query(Pedido).filter(Pedido.id==item_pedido.pedido).first()

    if not item_pedido:
        raise HTTPException(status_code=400, detail="Este item não existe")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Você não pode acessar essa rota")

    session.delete(item_pedido)
    pedido.calcular_preco()
    session.commit()

    return {
        "mensagem": "Item removido com sucesso",
        "itens_pedido": pedido.itens,
        "pedido": pedido
    }


@order_router.post("/pedido/finalizar/{id_pedido}")
async def finalizar_pedido(id_pedido: int, session: Session=Depends(session_db), usuario: Usuario=Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()

    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido não encontrado")

    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Você não pode cancelar esse pedido")
    
    pedido.status = "FINALIZADO"
    session.commit()
    return {
        "mensagem": f"Pedido Nº {pedido.id} finalizado com suecesso", 
        "pedido": pedido
    }


@order_router.get("/pedido/{id_pedido}")
async def visualizar_pedido(id_pedido: int, session: Session=Depends(session_db), usuario: Usuario=Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    
    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido não encontrado")

    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Você não pode cancelar esse pedido")
    
    return {
        "quantidade_itens_pedido": len(pedido.itens),
        "pedido": pedido
    }


@order_router.get("/listar_pedidos/usuario", response_model=List[ResponsePedidoSchema])
async def listar_pedidos(session: Session=Depends(session_db), usuario: Usuario=Depends(verificar_token)):
    pedidos = session.query(Pedido).filter(Pedido.usuario==usuario.id).all()
    return pedidos