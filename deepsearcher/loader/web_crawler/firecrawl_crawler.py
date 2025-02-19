import os
from typing import List

from firecrawl import FirecrawlApp
from langchain_core.documents import Document

from deepsearcher.loader.web_crawler.base import BaseCrawler


class FireCrawlCrawler(BaseCrawler):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



    def crawl_url(self, url: str) -> List[Document]:
        # Lazy init
        self.app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
        scrape_result = self.app.scrape_url(
            url,
            params={"formats": ["markdown"]},
        )

        markdown_content = scrape_result.get('markdown', '')
        metadata = scrape_result.get('metadata', {})
        metadata['reference'] = url

        return [Document(page_content=markdown_content, metadata=metadata)]