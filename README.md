## Como executar o projeto:

Os comandos abaixo devem ser executados no git bash dentro de uma pasta previamente criada.
Clonar o repositório:

``` git clone https://github.com/matheusalefe/tdd-aula-itau.git ```

Entrar na pasta:

``` cd sistema ```


Acessar a pasta e já deletar a pasta .git para depois subir para seu próprio github.


Criar virtualenv

``` python -m venv .venv ```

ou

``` py -m venv .venv ```


Ativar virtualenv

```source .venv/bin/activate (Mac e Linux) ```

``` source .venv/Scripts/activate (Windows)```

Instalar requisitos

```pip install -r requirements.txt```

Executar servidor do Django

``` python manage.py runserver ```

Neste caso, aparecerá a mensagem de que é necessário aplicar migrações, basta digitar:

``` python manage.py migrate ```

Para acessar o admin, digite localhost:8000/admin e digite:

```python manage.py createsuperuser```

Preencha os campos para criar usuário, email e senha e seu super usuário estará criado.

Para parar o servidor, usar o comando Ctrl-C

