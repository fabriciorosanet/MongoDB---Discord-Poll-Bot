![alt text](image.png)

# MongoDB - Discord Poll Bot

Este é um bot para Discord que cria enquetes interativas em um ou mais canais e salva as respostas em um banco de dados MongoDB Atlas.

O bot permite que os usuários votem em opções configuradas e, após o término da enquete, armazena as respostas com detalhes como nome do usuário, resposta e data/hora do voto.

## Funcionalidades

- Criação de Enquetes Interativas: O bot cria enquetes com botões de votação.
- Armazenamento das Respostas: As respostas dos usuários são salvas diretamente em um banco de dados MongoDB Atlas.
- Suporte para Fusos Horários: Utiliza pytz para garantir que a hora de cada voto seja registrada com base no fuso horário correto (ex: America/Sao_Paulo).
- Desabilita a Enquete Após o Tempo Limite: O bot desativa os botões após o tempo de duração da enquete.
- Comando para Salvar Respostas: O comando !salvar_respostas pode ser usado para salvar as respostas diretamente no banco de dados MongoDB.

## Requisitos

- Python 3.9+
- Discord.py (`discord.py`)
- MongoDB para Python (`pymongo`)
- Pandas (`pandas`)
- Pytz (`pytz`)
- Para carregar variáveis de ambiente (`dotenv`)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio


2. Instale as dependências:

   ```bash
   pip install -r requirements.txt

3. Crie um arquivo .env com as seguintes variáveis:

   ```bash
    DISCORD_TOKEN=seu_token_aqui
    MONGO_URI=sua_uri_do_mongodb_atlas_aqui
    MONGO_DB=nome_do_seu_banco
    MONGO_COLLECTION=nome_da_sua_colecao

4. Execute o bot:

   ```bash
   python main.py

## Como usar
1. O bot será iniciado e pronto para enviar enquetes. 
2. Configure os channel_ids com os IDs dos canais onde você deseja enviar as enquetes.
3. A enquete será enviada com um conjunto de opções, e os usuários poderão votar clicando em botões.
4. O comando !salvar_respostas pode ser usado para salvar as respostas coletadas diretamente no banco de dados MongoDB.

<h2 id="colab">🤝 Colaboradores</h2>

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://media.licdn.com/dms/image/v2/D4D03AQFhg6aT98EYyQ/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1697061290400?e=1735171200&v=beta&t=I7QymWDGwsoAsobMDPcCba6KiP3cvSA8LnWUF2G9nzU" width="100px;" alt="Fabricio Rosa"/><br>
        <sub>
          <b>Fabrício Rosa</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://media.licdn.com/dms/image/v2/D4D03AQE-5o3qpWIN9g/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1710954940792?e=1735171200&v=beta&t=7vLCKrr7DJio8MREsd9pBijdp8TjUFA5RdkCJpetsS0" width="100px;" alt="Eduardo Bortoli"/><br>
        <sub>
          <b>Eduardo Bortoli</b>
        </sub>
      </a>
    </td>
</table>
