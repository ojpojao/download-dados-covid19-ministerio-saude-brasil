# download-dados-covid19-ministerio-saude-brasil
Download do arquivo de dados sobre a covid 19 no Brasil pelo Painel https://covid.saude.gov.br/


#### Pré-requisitos
- [Python 3.6+](https://www.python.org/downloads/)
- [git](https://git-scm.com/)
- Pip3
- virtualenv **(*opcional*)**
- módulo *requests*

#### Setup Básico
1. baixe o repositório, zipado, neste [link](https://github.com/ojpojao/download-dados-covid19-ministerio-saude-brasil) e extraia em alguma pasta ou use o comando

  ```
    git clone https://github.com/ojpojao/download-dados-covid19-ministerio-saude-brasil.git
    cd download-dados-covid19-ministerio-saude-brasil
  ```
  
**ATENÇÂO:** caso não queira usar o *virtualenv*, pule para o passo 5.
 
2. Instalando virtualenv
  ```
    pip install virtualenv
  ```
  
3. Criando um ambiente virtual
  ```
     python -m virtual venv
  ```
  
4. Ativando o ambiente Virtual

No Windows, através do CMD
  ```
    venv\Scripts\activate.bat
  ```
  
No Windows, através do git-bash
  ```
    source venv/Scripts/activate
  ```
  
5. instalando o módulo *requests*

  ```
    pip install -r requirements.txt
  ```

#### Uso do script

```
python main.py
```

  
