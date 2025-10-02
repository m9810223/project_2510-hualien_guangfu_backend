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
[group('app')]
[group('test')]
pytest-app *args:
    {{ DCO }} run --rm -i app pytest {{ args }}

# 執行 pytest 與產生 coverage
[group('coverage')]
[group('app')]
[group('test')]
pytest-app-cov *args: (pytest-app "--cov --cov-report=html --cov-report=term" args)

# 打開 coverage
[group('coverage')]
[group('app')]
pytest-app-cov-open:
    python -m webbrowser -t file://$(pwd)/src/app/htmlcov/function_index.html
