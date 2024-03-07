import scrapy

class JobSpider(scrapy.Spider):
    name = 'job_spider'
    start_urls = ['https://www.reed.co.uk/jobs/data-analyst-jobs']

    def parse(self, response):
        # Extract job card information
        job_cards = response.css('article.card.job-card_jobCard__MkcJD')

        for job_card in job_cards:
            detail_url = job_card.css('a.job-card_jobCard__blockLink__PeeZx::attr(href)').get()
            title = job_card.css('a.job-card_jobCard__blockLink__PeeZx::text').get().strip()
            salary = job_card.css('li.job-card_jobMetadata__item___QNud:nth-of-type(1)::text').get().strip()
            contract_type = job_card.css('li.job-card_jobMetadata__item___QNud:nth-of-type(3)::text').get().strip()
            location = job_card.css('li.job-card_jobMetadata__item___QNud:nth-of-type(2)::text').get().strip()

            # Extracting job type and splitting by comma
            job_type = job_card.css('ul.job-card_jobMetadata__gjkG3 li:nth-child(4)::text').get()
            if job_type:
                job_type = job_type.split(',')

            yield {
                'Detail URL': response.urljoin(detail_url),
                'Title': title,
                'Salary': salary,
                'Contract Type': contract_type,
                'Job Type': job_type,
                'Location': location
            }

        # Follow pagination link to the next page
        next_page = response.css('a.page-link.next::attr(href)').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)
