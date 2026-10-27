
- Exercício de cada usuário ou globais?: os exercícios ficaram restritos individualmente para cada usuário que registra o exercício em sua propria tabela.
- Acesso ao recurso de outro usuário: O sistema deve responder 404 informando que (o recurso não foi encontrado), se caso as credenciais de nome e senha não estejam corretas.
- Comportamento das chaves estrangeira (FK): workout -> User CASCADE; WorkoutExercise -> Workout CASCADE; WoukoutExercise -> Exercise RESTRICT.
- Rotas: GET/PATCH_ID, POST, DELETE.
- Idioma das Rotas: Inglês (/workouts, /exercises).
- Fomrato de Erro: { "error": { "code": "...", "message": "..." } }.

-- Entidades

User (usuário)
atributos: id, nome, email, senha_hash

exercise
atributos: id, mome, grupo_muscular

workout ()
atributos: id, nome, descricao, user_id

WorkoutExercise ()
atributos: workout_id, exercise_id, series, repeticoes

2- Funcionalidades

- Criar novo Usuário
*id_user
*nome_user
*email_user
*password_hash

- Fazer Login
*nome_user
*email_user
*password_hash

- Criar um treino;
* POST /workout_create

- listar treino;
* GET /workouts

- Consultar um treino;
* GET /workouts /{workout_id}

- Atualizar um treino existente;
* PATCH /workouts /{workout_id}

- Excluir um treino;
* DELETE /workouts /{workout_id}

3- Regras de negócio

- Os campos de (nome | email | senha), devem obrigatoriamente serem preenchidos no momento do cadastro do usuário e Fazer login
- Os campos de cadastro e login devem ser do tido (str | str-email | hesh-senha)