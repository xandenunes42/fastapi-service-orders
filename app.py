from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models, schemas
from database import engine, Base, get_db

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


from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
