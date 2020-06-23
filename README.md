# Download do arquivo de dados sobre a covid 19 no Brasil pelo Painel https://covid.saude.gov.br/

O Painel Coronavírus do Ministério da Saúde possui a opção para o download direito do arquivo. Mas se você quer automatizar o download
dos dados, este script pode lhe ser útil.


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
  
**ATENÇÃO:** caso não queira usar o *virtualenv*, pule para o passo 5.
 
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

#### Me siga
* [@ojpojao](https://twitter.com/ojpojao)

#### Sobre mim
Estudante de Tecnologia em Redes de Computadores no IFAp. Gosto de coisas relacionadas a cultura DevOps e programação, e claro, Redes de Computadores em geral. Fã de futsal e futebol. Chama pra gente marcar um fut.
  
