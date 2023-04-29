# zafferano-news-archiver

Zafferano.news is an independent news website. This repository contains the code of a scraper that archives the news published on the website in a PostgreSQL database.

***

## How to use it

Using this scraper is very simple. You just need to follow the steps below and you will be able to run it on your machine.

### Clone the repository

`git clone git@github.com:drcoccodrillus/zafferano-news-archiver.git`

### Build the image

`docker-compose up --build -d`

### Run the scraper

`docker exec -it zafferano-archiver pull`
