TITLE_PATHS = (
    '//div[@id="aod-asin-title"]/h5//text()',
    '//h1[@id="title"]/span[@id="productTitle"]/text()',
    '//div[@id="title_feature_div"]//h1[@id="title"]/text()',
    '//span[contains(@id, "btAsinTitle")]/span/text()',
    '//span[contains(@id, "btAsinTitle")]/text()',
    '//span[contains(@id, "ebooksProductTitle")]/text()',
    '//div[contains(@class, "dpSubDetailProductTitle")]/text()',
    '//h1[@id="title"]/text()',
    '//span[@id="title"]/text()',
    '//table[contains(@class, "layout")]' '//span[contains(@class, "title")]/text()',
    '//div[@id="mediaProductTitle_feature' '_div"]//span[@id="productTitle"]/text()',
    '//b[@id="product-title"]/text()',
    '//div[contains(@class, "olpNavBackTo") '
    'and contains(@class, "hideOnSecondaryView")]//text()',
    '//div[contains(@class, "olp-text")]/span/text()',
    '//div[@id="olpProductDetails"]/h1/text()[last()]',
    '//h1[@data-automation-id="title"]/text()',
    '//div[contains(@id, "ProductTitle")]/h1/text()',
)

AVAILABILITY_PATHS = (
    '//span[@class="availGreen" or @class="availRed"]/text()',
    '//div[@id="availability"]/span/text()',
    '//span[@id="availability"]/text()',
    '//span[@id="pantry-availability"]/text()',
    '//div[contains(@id,"Availability_feature")]/div/*/text()',
    '//div[@id="availability"]/span//text()',
)

PRICE_PATHS = [
    '//div[contains(@id, "price_feature_div")]//span['
    'contains(@id, "saleprice")]/text()',
    '//table[contains(@class, "product")]//span['
    'contains(@id, "actualPriceValue")]/b/text()',
    '//div[contains(@class, "mbcContainer")]//span['
    'contains(@class, "price")]/text()',
    '//span[contains(@id, "ourprice")]/text()',
    '//div[contains(@id, "buybox")]//div['
    'contains(@id, "buyNewSection")]//span['
    'contains(@class, "offer-price")]/text()',
    '//span[contains(@id, "priceblock_ourprice")]/text()',
    '//div[contains(@id, "price_feature_div")]//span['
    'contains(@id, "dealprice")]/text()',
    '//div[@id="newOfferAccordionRow"]//span[contains('
    '@class, "header-price")]/text()',
    '//div[contains(@id, "MultiOfferEgress_feature")]//span[contains('
    '@class, "a-color-price")]/text()',
    '//div[@class="sub-priceBlock"]//span[contains(@class, "a-color-price")]/text()',
    '//div[@id="cerberus-data-metrics"]//@data-asin-price',
    '//div[contains(@id, "Price_feature_div") or contains(@id,"corePrice_desktop")]'
    '//*[contains(@id,"ourprice")]/*[contains(@class,"color-price")]/text()',
    '//div[contains(@id, "newAccordionRow")]//div[contains(@id, "Price_feature_div")]//span[@class="a-offscreen"]/text()',
    '//div[contains(@id, "Price_feature_div") or contains(@id,"corePrice_desktop")]//*[not(ancestor-or-self::div[contains(@id,"usedAccordionRow")])]'
    '//*[@data-a-color="price" or @data-a-color="base"]/*[contains(@class,"a-offscreen")]/text()',
    '//span[contains(@class,"reinventPricePriceToPayMargin priceToPay")]/span[@class="a-offscreen"]/text()',
    '//span[contains(@class,"a-color-price priceBlockBuyingPriceString")]/span[contains(@class,"a-color-price")]/text()',
]

ASIN_PATHS = (
    '//form[contains(@id, "addToCart")]//input[@name="ASIN"]/@value',
    '//input[@name="ASIN"]/@value',
    '//input[contains(@name, "metric-asin")][1]/@name[1]',
    '//input[@name="a"]/@value',
    '//form[contains(@name, "kindle-order")]/input[@name="ASIN.0"]/@value',
    '//a[@id="olpDetailPageLink"]/@href',
    '//div[contains(@class, "olpNavBackTo")]/a/@href',
    '//span[contains(@class, "a-text-bold") and contains(text(), "ASIN")]'
    "/following-sibling::span/text()",
    '//span[contains(@class, "asinReviewsSummary")]/@name',
    '//div[@id="dynamicDeliveryMessage" or @id="deliveryBlockMessage"]/parent::'
    '*/input[contains(@id, "SelectAsin")]/@value',
)

ASIN_REGEXES = (
    r"/(B[\d][\w]{8})(?:[^\w-]|$)",
    r"/gp/aw/ol/(\w+)/?",
    r"/gp/offer-listing/(\w+)/?",
    r"/dp/(\w+)/?",
    r"/dp/product-listing/(\w+)/?",
    r"/gp/aw/d/(\w+)/?",
    r"[\?&]?asin=(\w+)&?",
    r"/gp/product/(\w+)/?",
)

SELLER_NAME_PATHS = [
    '//div[@id="tabular-buybox"]//tr//span[contains(text(),"Sold by")]'
    '/ancestor::td/ancestor::tr//span[contains(@class,"truncate-full")]/'
    'span[contains(@class,"tabular-buybox-text")]//text()',
    '//div[@class="buying" and contains(., "sold by")]//b/text()',
    '//*[@id="merchant-info" and contains(./text(),"sold by")]//text()',
    '//div[@id="merchant-info" and contains(., "Sold by")]/a/text()',
    '//div[@id="desktop_qualifiedBuyBox"]//div[@class="tabular-buybox-text" and @tabular-attribute-name="Sold by"]//text()',
    '//div[contains(@class,"tabular-buybox")]/div[contains(@class,"buybox-text") '
    'and @tabular-attribute-name="Sold by"]//text()',
    '//*[contains(@id,"desktop_qualifiedBuyBox")]//*[contains(text(), "Sold by")]/parent::div/following-sibling::div/div/span//text()',
    '//div[@id="merchant-info"]//text()',
    '//div[@id="fresh-merchant-info"]//text()',
    '//*[@id="merchant-info"]//text()',
    '//a[contains(@class, "MerchantName")]/text()',
    '//div[contains(@class, "buying")]/b/a/text()',
    '//div[contains(@id, "pantry-availability")]/text()',
    '//div[@id="buybox-tabular"]//tr//span[contains(text(),"Sold by")]'
    '/ancestor::td/ancestor::tr//span[contains(@class,"truncate-full")]//text()',
    '//*[contains(text(), "Sold by")]/parent::td/following-sibling::td/*/text()',
]


LIST_PRICE_PATHS = (
    '//span[contains(@id, "listPriceValue")]/text()',
    '//td[contains(text(), "List Price")]'
    '/following-sibling::td[contains(@class, "a-text-strike")]/text()',
    '//span[contains(@class, "listprice")]/text()',
    '//td[@class="listprice"]/text()',
    '//td[contains(text(), "List Price")]/following-sibling::td//text()',
    '//div[@id="corePriceDisplay_desktop_feature_div"]//span[contains(@class,"price") and @data-a-strike="true"]//span[@class="a-offscreen"]/text()',
    '//div[contains(@id, "kindle-price-block")]'
    '//span[contains(@class, "listPrice")]/text()',
    '//div[@id="newOfferAccordionRow"]//span[contains(@class, "a-text-strike")]/text()',
    '//div[@id="price"]//span[contains(@class, "a-text-strike")]/text()',
    '//span[contains(@class, "priceBlockStrikePriceString")]/text()',
    '//div[contains(@id,"corePrice_desktop")]//*[@data-a-color="secondary"]/*[contains(@class,"a-offscreen")]/text()',
    '//div[@id="newAccordionRow_0"]//span[@data-a-color="price"]/span[@class="a-offscreen"]/text()',
    '//div[@id="newAccordionRow_0"]//span[@data-a-color="secondary"]/span[@class="a-offscreen"]/text()',
    '//div[contains(@id, "Price_feature_div")]//*[@data-a-color="price"]/*[contains(@class,"a-offscreen")]/text()',
    '//div[contains(@id, "Price_feature_div")]//*[@data-a-color="secondary"]/*[contains(@class,"a-offscreen")]/text()',
    '//span[contains(@class,"basisPrice") and contains(text(),"Suggested price")]//span[contains(@class,"a-offscreen")]/text()',
    '//div[@id="qualifiedBuybox"]//div[@id="corePrice_feature_div"]//span[@class="a-offscreen"]/text()',
    '//div[@id="ppd"]//div[contains(@id,"corePriceDisplay")]//span[@data-a-strike="true"]//span[@class="a-offscreen" ]//text()',
    '//div[contains(@id, "buybox")]' '//span[contains(@class, "a-text-strike")]/text()',
)


BRAND_PATHS = (
    '//a[contains(@id, "brand")]/text()',
    '//div[@id="mbc"]/@data-brand',
    '//span[@id="brand"]/text()',
    '//a[@id="bylineInfo"]/text()',
    'translate(substring-after(substring-before(//a[contains(@id, "brand")]/@href, "/b/"),"https://www.amazon.com/"),"-"," ")',
)

IMAGE_PATHS = (
    '//td[@id="prodImageCell"]/a/img/@src',
    '//img[contains(@id, "main-image")]/@data-hires-replacement',
    '//img[contains(@id, "main-image")]/@src',
    '//div[@id="avod-main"]//img[@id="prod-img"]/@src',
    '//div[@id="rwImages_hidden"]/img/@src',
    '//span[@data-action="thumb-action"]//img/@src',
    '//div[contains(@class, "imgTagWrapper")]/img/@data-old-hires',
)