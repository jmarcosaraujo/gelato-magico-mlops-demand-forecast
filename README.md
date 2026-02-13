# 🍦 Gelato Mágico — Demand Forecast com Machine Learning

![Python](https://img.shields.io/badge/python-3.10-blue)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-green)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-success)
![Status](https://img.shields.io/badge/status-Production_Ready-brightgreen)

---

## 📌 Visão Geral

Este projeto aplica técnicas de **Machine Learning e MLOps** para prever a quantidade de sorvetes vendidos com base na temperatura diária.

O objetivo é ajudar a sorveteria **Gelato Mágico** a:

- Reduzir desperdícios  
- Evitar falta de estoque  
- Otimizar produção  
- Maximizar lucro  

---

## 🧠 Problema de Negócio

A produção baseada apenas em intuição pode gerar:

- ❄️ Excesso de produção em dias frios  
- ☀️ Falta de estoque em dias muito quentes  

A solução proposta utiliza um modelo de **regressão supervisionada** para prever a demanda com base na temperatura.

---

## 🏗️ Arquitetura do Projeto

O projeto foi estruturado seguindo boas práticas de engenharia:
```
data → preprocess → train → evaluate → register (MLflow) → deploy (API)
```

Principais componentes:

- Pipeline estruturado
- Registro de experimentos com MLflow
- API REST com FastAPI
- Containerização com Docker
- CI automatizado com GitHub Actions
- Notebook de análise exploratória (EDA)

---

## 🛠️ Stack Tecnológica

- Python 3.10
- Pandas
- Scikit-learn
- MLflow
- FastAPI
- Docker
- Pytest
- GitHub Actions

---

## 📊 Análise Exploratória (EDA)

Principais insights:

- Forte correlação positiva entre temperatura e vendas
- Relação aproximadamente linear
- Maior variabilidade em temperaturas extremas

Gráfico exemplo:

Temperatura ↑ → Vendas ↑


---

## 🤖 Modelagem

Modelo selecionado:

- **Gradient Boosting Regressor**

Métricas obtidas:

- R² > 0.95
- RMSE baixo
- Alta estabilidade

Experimentos registrados via MLflow.

---

## 🔁 Pipeline

Execução completa:

python -m src.pipeline

Isso executa:

Treinamento

Avaliação

Registro no MLflow

Salvamento do modelo

---

## 📈 MLflow

Para visualizar experimentos:

mlflow ui


Acesse:

http://127.0.0.1:5000


Permite visualizar:

Métricas

Parâmetros

Comparação de execuções

Artefatos do modelo

---

## 🚀 Executando Localmente

Instalar dependências
pip install -r requirements.txt

Treinar modelo
python -m src.train

Rodar API
uvicorn api.app:app --reload


Acesse documentação interativa:

http://127.0.0.1:8000/docs

---

## 📡 Endpoint de Previsão

POST /predict

Exemplo:

{
  "temperatura": 30
}


Resposta:

{
  "vendas_previstas": 312.4
}

---

## 🐳 Docker

Build da imagem:

docker build -t gelato-magico .


Executar container:

docker run -p 8000:8000 gelato-magico

---

## 🧪 Testes Automatizados

Executar testes:

pytest


Pipeline de CI executa testes automaticamente a cada push.

---

## 📁 Estrutura do Projeto
```
gelato-magico-mlops-demand-forecast/
│
├── .github/workflows/ci.yml
├── data/
├── inputs/
├── notebooks/
├── models/
├── tests/
├── src/
├── api/
├── Dockerfile
├── requirements.txt
└── README.md
```
---

## 🔮 Melhorias Futuras

Incluir umidade e sazonalidade

Monitoramento de drift

Deploy em cloud

Ajuste automático de hiperparâmetros

CI/CD para deploy automático

---

## 🎯 O Que Este Projeto Demonstra

✔ Estrutura profissional
✔ MLOps básico aplicado
✔ Registro de experimentos
✔ API pronta para produção
✔ Containerização
✔ Integração contínua
✔ Organização modular

---

## 👨‍💻 Autor

Projeto desenvolvido para portfólio profissional com foco em Engenharia de Machine Learning e MLOps.

---

## 📜 Licença

Este projeto é apenas para fins educacionais.

---