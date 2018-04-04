BOT_NAME = 'gazette'
SPIDER_MODULES = ['gazette.spiders']
NEWSPIDER_MODULE = 'gazette.spiders'
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    'scrapy.pipelines.files.FilesPipeline': 1,
    'gazette.pipelines.PdfParsingPipeline': 2,
    'gazette.pipelines.PostgreSQLPipeline': 3,
}
FILES_STORE = '/mnt/data/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36'
SPLASH_URL = 'http://splash:8050'
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
