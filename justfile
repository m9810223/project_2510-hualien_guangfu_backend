[private]
default:
    just --fmt --unstable 2> /dev/null
    just --list --unsorted

DCO := "docker-compose"

# 產生 .env 檔案給 docker-compose 使用
[group('Docker Compose')]
env env_name="dev":
    ./gen_env.sh .env.{{ env_name }}*

[private]
_docs-compose_file := "compose.docs.yml"

# serve 文件
[group('docs')]
docs port="8002": changelog
    PORT={{ port }} {{ DCO }} --file {{ _docs-compose_file }} up --build --force-recreate

# 產生靜態文件檔案
[group('docs')]
build-docs:
    {{ DCO }} --file {{ _docs-compose_file }} build
    {{ DCO }} --file {{ _docs-compose_file }} run --rm -v $(pwd)/public/:/docs/public/ docs mkdocs --verbose --color build --clean --strict

    # docker-compose --file compose.docs.yml run --rm -v $(pwd)/:/docs/ -v ~/.gitconfig:/root/.gitconfig -v ~/.ssh/:/root/.ssh/ docs mike deploy -b _dev --push _dev

    # git config --file $(pwd)/.gitconfig user.name  $GITLAB_USER_LOGIN
    # git config --file $(pwd)/.gitconfig user.email $GITLAB_USER_EMAIL
    # docker-compose --file compose.docs.yml run --rm -v $(pwd)/:/docs/ -v $(pwd)/.gitconfig:/root/.gitconfig docs mike deploy -b docs-site xxx latest --update-aliases --push

# 產生 changelog
[group('changelog')]
[group('docs')]
changelog output='docs/docs/changelog.md':
    docker run --rm -t -v $(pwd):/app/ orhunp/git-cliff:2.8.0 --repository . --output {{ output }}

# 執行 pytest
[group('test')]
pytest-app *args:
    {{ DCO }} run --rm -i app pytest {{ args }}

# 執行 pytest 與產生 coverage
[group('coverage')]
[group('test')]
pytest-app-cov *args: (pytest-app "--cov --cov-report=html --cov-report=term" args)

# 打開 coverage
[group('coverage')]
pytest-app-cov-open:
    python -m webbrowser -t file://$(pwd)/src/app/htmlcov/function_index.html

uv-add:
    {{ DCO }} run --rm backend uv add fastapi-cli fastapi 'uvicorn' fastcrud pydantic alembic asyncpg pydantic-settings  sqlmodel email-validator python-multipart jinja2 httpx pydantic-settings pydantic-extra-types psycopg2-binary 'fastapi-users[sqlalchemy]'

[group('alembic')]
alembic *args:
    {{ DCO }} run --rm backend uv run alembic {{ args }}

delete-and-restart-db: && alembic-migrate
    {{ DCO }} down -v db
    {{ DCO }} up -d db --wait

[group('alembic')]
alembic-commit *args: (alembic "revision --autogenerate" args)

[group('alembic')]
alembic-commit-migrate *args: (alembic "revision --autogenerate" args) alembic-migrate

[group('alembic')]
alembic-migrate *args: (alembic "upgrade head")

# 重置資料庫
[group('alembic')]
alembic-reset-db: (alembic "downgrade base") (alembic "upgrade head")
