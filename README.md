# scrapy-test

    git clone https://gitlab.com/j.mpinheiros/scrapy-test.git

# URLs file

- Put in urls.txt all the sites to scrap, one per line.

# RUN PROJECT with docker-compose
    docker-compose up
OR
    docker-compose down && docker-compose up --build

# Results

- The result will be save in output/output.json file

```bash
    {"url": "https://",
    "phone_numbers": ["(xxx) xxx xxxx"],
    "logo_urls": ["https://"]}
```

## Project
```bash
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
```

# ------More----------
# BUILD
install requirements.txt with pip.

    pip install -r requirements.txt

Put in urls.txt all the sites to scrap, one per line.

# RUN
with urls file

    scrapy crawl website -a urls_file=urls.txt -o output.json

with urls direct

    scrapy crawl website -a urls="https://url01\nhttps://url02\nhttps://url03\" -o output.json

# Only Dockerfile
    docker build -t scrapy_test .
    docker run scrapy_test
    docker cp <container_id>:/app/output.json output.json
