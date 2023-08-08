# scrapy-test

```
git clone https://gitlab.com/j.mpinheiros/scrapy-test.git

```
# RUN
    scrapy crawl website -o output.json
    scrapy crawl website -a urls_file=urls.txt -o output.json
# Docker
    docker build -t scrapy_test .
    docker run scrapy_test
    docker cp <container_id>:/app/output.json output.json



## Project
SCRAPY-TEST/
    scrapy_test/
        spiders/
            __init__.py
            website.py
        items.py
        middlewares.py
        pipelines.py
        settings.py
    scrapy.cfg            
    Dockerfile
    requirements.txt

