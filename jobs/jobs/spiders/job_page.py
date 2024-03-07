import scrapy

'''
scrapes data by visting each job page in search results
'''
class ReedSpider(scrapy.Spider):
    name = 'job_page'
    start_urls = ['https://www.reed.co.uk/jobs/data-analyst-jobs']
    
    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # Add a delay of 2 seconds between requests
    }

    def parse(self, response):
        for job in response.css('div.job-card_jobCard__body__86jgk'):
            relative_url = job.css('h2.job-card_jobResultHeading__title__IQ8iT a::attr(href)').get()
            job_url = response.urljoin(relative_url)
            yield response.follow(job_url, callback=self.parse_job)

        '''
        pagination logic for following next page of search results
        '''
        next_page = response.css('a.page-link.next::attr(href)').get()
        print(next_page)
        if next_page:
            print(next_page)
            yield response.follow(next_page, callback=self.parse)

    """
Function to parse each page of job and yeild the results


    """
    def parse_job(self, response):
        def clean_job_type(value):
            return value.strip() if value else None

        job_types = response.css('div.time span a::text').getall()
        contract_type, job_type = [clean_job_type(value) for value in job_types[:2]] if job_types else [None, None]

        yield {
            'Detail URL': response.url,
            'Title': response.css('header.job-header h1::text').get(),
            'Salary': response.css('div.salary span span::text').get(),
            'Contract Type': contract_type,
            'Job Type': job_type,
            'Location': response.css('div.location span:nth-child(1)::text').get(),
        }
