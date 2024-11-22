from fastapi import FastAPI, HTTPException, Depends, Request, Form
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
from models import OrdemServico, Cliente
from schemas import OrdemServicoCreate
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import Base
from typing import List
from fastapi.responses import RedirectResponse
from datetime import datetime
import models

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Configuração do FastAPI e templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/clientes", response_class=HTMLResponse)
def listar_clientes(request: Request, db: Session = Depends(get_db)):
    clientes = db.query(models.Cliente).all()
    return templates.TemplateResponse("clientes.html", {"request": request, "clientes": clientes})

@app.get("/clientes/novo", response_class=HTMLResponse)
def criar_cliente_form(request: Request):
    return templates.TemplateResponse("cliente_form.html", {"request": request})

@app.post("/clientes/novo", response_class=HTMLResponse)
def criar_cliente(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    db: Session = Depends(get_db),
):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.email == email).first()
    if db_cliente:
        raise HTTPException(status_code=400, detail="Cliente com esse email já cadastrado")
    novo_cliente = models.Cliente(nome=nome, email=email, telefone=telefone)
    db.add(novo_cliente)
    db.commit()
    return RedirectResponse(url="/clientes", status_code=303)

# Montando diretórios estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Rota GET para exibir o formulário de criação de ordem de serviço
@app.get("/criar_ordem_de_servico", response_class=HTMLResponse)
def criar_ordem_de_servico_form(request: Request, db: Session = Depends(get_db)):
    clientes = db.query(models.Cliente).all()  # Pega a lista de clientes para o formulário
    return templates.TemplateResponse("criar_ordem_de_servico.html", {"request": request, "clientes": clientes})

# Rota POST para criar a ordem de serviço
@app.post("/ordens_de_servico/", response_class=RedirectResponse)
def criar_ordem_de_servico(
    cliente_id: int = Form(...),  # Recebendo dados de formulário
    descricao: str = Form(...),
    status: str = Form("Em andamento"),  # Valor padrão para status
    data_abertura: datetime = Form(...),  # Recebe a data como datetime
    db: Session = Depends(get_db)
):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    nova_ordem = OrdemServico(
        cliente_id=cliente_id,
        descricao=descricao,
        data_abertura=data_abertura,
        status=status,
    )
    db.add(nova_ordem)
    db.commit()
    db.refresh(nova_ordem)

    # Redireciona para a página de ordens de serviço após a criação
    return RedirectResponse(url="/ordens_de_servico", status_code=303)


# Rota GET para listar ordens de serviço
@app.get("/ordens_de_servico", response_class=HTMLResponse)
def listar_ordens_de_servico(request: Request, db: Session = Depends(get_db)):
    ordens = db.query(OrdemServico).all()
    return templates.TemplateResponse("ordens_de_servico.html", {"request": request, "ordens": ordens})
