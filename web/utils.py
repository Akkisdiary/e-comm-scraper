import random


def random_user_agent() -> str:
    uas = (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{}.0.{}.{} Safari/537.{}',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/{}.0',
    )

    ua = random.choice(uas).format(
        random.choice([str(i) for i in range(89, 104)]),
        random.randint(2000, 6000),
        random.randint(10, 99),
        random.randint(10, 99)
    )
    
    return ua


def random_accept() -> str:
    accs = (
        "*/*",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    )
    return random.choice(accs)


def random_headers(**override_kwargs):
    h = {
        'accept': random_accept(),
        'user-agent': random_user_agent(),
    }
    
    h.update(override_kwargs)
    
    return h