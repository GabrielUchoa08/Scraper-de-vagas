Projeto pessoal de ciência de dados que coleta vagas de emprego de várias áreas, identifica quais skills e tecnologias elas pedem, estima a senioridade de cada vaga e apresenta tudo em um dashboard interativo.

O projeto é um pipeline com três etapas, seguindo a seguinte ordem:
collect.py -> process.py -> dashboard.py

No qual:
1. collect.py: é o responsável por consultar a API da Adzuna com vários termos de busca, agrupados por área e salvar os resultados como json
2. process.py: lê o json mais recente, extrai o nome da empresa e o local, identifica as skills mencionadas na descrição (pegando com base skills.py) e a senioridade a partir do título (senioridade.py).
3. dashboard.py: aplicação em streamlit que lê os CSVs e permite filtrar por área e senioridade

O que o dashboard mostra:
- Tabela de vagas encontradas, com link da vaga original;
- Ranking das skills mais demandadas;
- Distribuição de vagas por senioridade;
- Filtros interativos por área e por senioridade.

Tecnologias usadas:
- **Python**
- **requests**: chamadas a API
- **pandas**: limpeza e transformação dos dados
- **streamlit**: dashboard web 

## Como usar 

## Pré-requisitos 
- Python 3.10 ou superior
- Uma conta gratuita na API da Adzuna para obter 'API_ID' e 'API_KEY'

### 1. Clonar e instalar

```bash
git clone https://github.com/GabrielUchoa08/Scraper-de-vagas.git
cd Scraper-de-vagas

# (opcional, recomendado) criar um ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/macOS/Git Bash
venv\Scripts\activate           # Windows (cmd/PowerShell)

pip install -r requirements.txt
```

### 2. Configurar as credenciais

Copie o arquivo de exemplo e preencha com as suas chaves:

```bash
cp .env.example .env
```

```
ADZUNA_APP_ID=seu_app_id_aqui
ADZUNA_APP_KEY=sua_app_key_aqui
```

O arquivo `.env` está no `.gitignore` e **nunca deve ser enviado ao GitHub**.

### 3. Executar o pipeline

Rode os comandos a partir da **raiz do projeto**, pois os caminhos dos arquivos são relativos:

```bash
python src/collect.py      # coleta as vagas e salva em data/raw/
python src/process.py      # gera os CSVs em data/processed/
streamlit run src/dashboard.py
```

O último comando abre o dashboard no navegador (normalmente em `http://localhost:8501`).

## Autor

Gabriel Uchôa — [GitHub](https://github.com/GabrielUchoa08)