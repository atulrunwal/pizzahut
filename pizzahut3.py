# pizzahut3.py
import requests
import re
import csv

# f=open('pizzahut_task.csv','a',newline='')
# csv_writer=csv.DictWriter(f,fieldnames=['Menu','Sub_Menu','Product','Crust','Size','Price'])

f = open('pizzahut_task.csv', 'w', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['Menu', 'Sub_Menu', 'Product', 'Crust', 'Size', 'Price'])
f.close()


url1 = 'https://www.pizzahut.com/api.php/site/api_pages/api_menu/getstoretiles'
cookies_ = 'SEGNUM=86; _scid=143cffab-3904-4add-b566-9a573744a4ac; _fbp=fb.1.1633070890978.192058841; _ga=GA1.2.772974057.1633070903; _rdt_uuid=1633070904138.1c72c1f5-dee0-4190-bc65-253b6357eeaf; _gcl_au=1.1.1345580477.1633070909; pizzabucket=101%7E43; optimizelyEndUserId=oeu1633071035183r0.4048335405104908; optimizelyBuckets=%7B%7D; optimizelySegments=%7B%22209642986%22%3A%22direct%22%2C%22209669694%22%3A%22gc%22%2C%22209692476%22%3A%22false%22%2C%22209740042%22%3A%22none%22%2C%22307825635%22%3A%22true%22%7D; UA_channel=WEB2; _pin_unauth=dWlkPU1tWmpOR0l3TldFdFptRXlNeTAwTlRReUxXSmhPV0V0TXpnM1ltUmxaall3TVRkaw; __adroll_fpc=60c980d265b63a26779e7ea08b19235a-1633071056582; _gid=GA1.2.1771193284.1633525437; localization-token=eyJhbGciOiJQUzUxMiIsImtpZCI6ImI3ZWZiZjdkLWVlNWMtNDM3MC1iN2VmLWQxOTAzNTM4YWY4NSIsInR5cCI6IkpXVCJ9.eyJhZGRyMSI6IjMzMTEgTGVlIEh3eSIsImF1ZCI6WyJQSERBUEkiLCJQSFBBWSJdLCJjaXR5IjoiQXJsaW5ndG9uIiwiZXhwIjoxNjM2MTkwOTE0LCJpYXQiOjE2MzM1OTg5MTQsImlzcyI6IlBIIENvbm5lY3QiLCJsYXQiOjM4Ljg5Njc5LCJsb25nIjotNzcuMTAxNzQ2LCJuYmYiOjE2MzM1OTg5MTQsIm9jYyI6IkNBUlJZT1VUIiwic24iOiIwMzc0NDkiLCJzdGF0ZSI6IlZBIiwic3ViIjoiQ2xpZW50IiwidHoiOiJBbWVyaWNhL05ld19Zb3JrIiwiemlwIjoiMjIyMDcifQ.lBUMqDFVg19K0LC_V3kKpBPWAkoKBVwIi6F-DxDsNp7ThVbWpnXadkscvC89j6fGThO6IbabdmUoE3q3MB-hfOdzj9NH-_DIPeytBhDByl0UqhPKc6cBGUYEBXcwUOo00NZuRj9wkfCqDYsA3tQMiFys-UI8vmTSaCvi9An43977Bk_pwHLn3P21eaZd6DGxwDiiUpQGX1a8PNCaT0WAMqBr5zk9D8BZa2KvKiwhNgBebwfQH10B_8sWV3ytMn8MN54oxuTIvdMGMNsNZBGeq9lUoSAWHcFYSMdn8pbCOVu6vX5DdoUYsnUxFDKvHaIg-TFeYujGcXxdDVB4DAcHHg; to_cart=a%3A4%3A%7Bs%3A5%3A%22total%22%3Bs%3A0%3A%22%22%3Bs%3A8%3A%22subtotal%22%3Bs%3A0%3A%22%22%3Bs%3A15%3A%22loyalty_removed%22%3Bi%3A0%3Bs%3A11%3A%22expiry_time%22%3Bi%3A1643966915%3B%7D; cart-id=bdcd46106a7a60074c20bb23fe78f9b32020089a; User-Experience=PH-WEB2; at_check=true; QOSESSID=vjd6r3f5738d79gtdfqluvf4f2; akadcgtm=live-va; _sctr=1|1633631400000; www-siteview=www; user_state=%7B%22occasion%22%3A%22C%22%2C%22StoreNumber%22%3A%22037449%22%2C%22storeLatitude%22%3A%2238.896789%22%2C%22storeLongitude%22%3A%22-77.101742%22%2C%22action%22%3A%22%22%2C%22deliveryAddress%22%3A%22%22%2C%22currentSavedLocationIndex%22%3Anull%2C%22zipcode%22%3A%2222207%22%2C%22status%22%3A%22recognized+unregistered%22%2C%22menu%22%3A%5B%22pizza%22%2C%22wings%22%2C%22sides%22%2C%22pasta%22%2C%22desserts%22%2C%22drinks%22%5D%2C%22wingstreetleadmkt%22%3A0%2C%22user_state_abbrev%22%3A%22RU%22%7D; UA_token=ea11lrk7mm814twhuaeum045y8pnjfn4nw6bpvzm0jkgnark0cdg11mq8n1yn333; __ar_v4=OTUCE2Z3VBGWFHOFWGQHTL%3A20210931%3A7%7CV5SJZXPENBCN7NX3FYVVIB%3A20210931%3A7%7CH6RSMMPK2BCVPNRJTV5AVK%3A20210931%3A7; bm_sz=73855EBCA025FD1AA94026237C0A2A0B~YAAQlCABFz+O+VJ8AQAAmzgxYA2V+ToQ/IuaKSL/uFnoC/ldYzqZtxNJjki/Cgs8VB2x0FdkFFudrPDIBWOcydhdWHRXHrnsAqVHfHPvYfs3BKQuHecQr360wjiEZxg9vruIcA8VUXlBXxbM4j1uNb4NuGx7VFosndFfOIWk0Gr3tCZ76GwMIyWqUE5AE9Aort9yi3uCh9OLhcVQFjIpT52GPhbI334FuTzL5mzLNI41mCjvU9HNI1UvKKSqRAnr0fEz0IElin5K7rm0IUmhQ3Qo7TQNp5EHWcNbPS5JVah/GxsHDA==~3684656~4473652; AKA_A2=A; QOitct=0; mboxEdgeCluster=34; ak_bmsc=74731BB203534CC1B5C07FCEE9AA8D1C~000000000000000000000000000000~YAAQ1ikhF8BoRFN8AQAAF4poYA16YU8rnd4yeYM4y7H2BwSEX6+c54yCLB745q8PZ4qpUCNC9igrrJU7QTlVvb+9u/dooYeJ4uMZUoDfEmteN70xbhvg7dMtykU8zvSeqrR0tbyfMLt+03fi7O9zLmwJGITHQAhSYZAGNgLbq80vZGetH4UdvNL1DvC3ZOjlqO78PVnRIMM1Fy+UlthioN4z+TJTOfrhJ0PW/U1VqP71Ys7FVAAOiiW6RKvWRdfIg5m2aBWabfLOS+KQJDhNPV3wxPKWlBN6kvm1Ug+mJr3hNzdIJC8jtAoNP7ADpYBrRRJIJ1vZaZbbU83ip9ZBoBHuzpKI2lJCe6vozE/9EQYxtdoQlO0/Gz/84Ww/3qtMDZKebRWJomvLnz8gvszIuyIUJYLhFqclfmi8JQ7fQdaB1/bV6JTLWyfvjKYyGNmyd+kfP/jR+Hj3S0CeYyHNjNeXb0kd55DUtEZl99uURBDxRqDN8QhrlmKrsftg; optimizelyPendingLogEvents=%5B%5D; mbox=PC#6f10af4e45484b4ea141050ee46ebb87.34_0#1696949856|session#81d7293254ef4f24a63cf159d3027d42#1633706889; gtm-session-start=1633705054425; _abck=8F1A283AF01D3AF7BCBC66EC5BCF59FA~-1~YAAQ1ikhF/VpRFN8AQAATt9oYAbWbjDeiFUf0EXvLWHRhcb8kka2uGRalbsUZCkNu8In/RDbCeKFaAZ8Y6Xd0KApUWV3WTBAUA3W8fW1i0G6HaninQP/45m4mWOboeui0WGPhsHYJMqm8r4pvVNYsEjiSvLu0fYFYjlH7APrG0o5zYL3mE0VgDo0MR70atc+9o+o/cwW3vI4mO/reycUYsCm3OUDYO9m1crV4VAjhy/mMH1HkMcMKZHv6c48CyvSw+yi/4bBxd8ck2cIZ0xOGRN08SuNJESC0m4fstWRkccvQZyTQqcBUy7KI/SckCRcWdaixVCHm2rQCi9Tx1IEYs75JydT0CqVlfabpHuNe5oHQyjzGfuvd2LEwBh77koYo+XZ6dVSdzr1QtIlvBGGK0hIiHzCn7e/36MJ8mU+RwITUgLNQpsxpV9DZsGoOk+RWb5jIfU=~-1~-1~-1; utag_main=v_id:017c3a9c1594001cc8dbe6a518a505072001906a0086e$_sn:14$_se:28$_ss:0$_st:1633706858084$dc_visit:14$ses_id:1633705035951%3Bexp-session$_pn:2%3Bexp-session$centro_sync_session:1633705035951%3Bexp-session$dcsyncran:1%3Bexp-session$dc_event:3%3Bexp-session$dc_region:eu-central-1%3Bexp-session$ispot_uid:v2%3Ade0f0c4648161984b569b5128f1d70afb58b3458820ded64d4b945f70a8d43ff%7C317732e071a72f070e090f9e7ae310abb9fd4845a1b218bd378947807c905678%3Bexp-session; AWSALB=HaBhC0Ey9uh7V8BeQ0kfH1dlfoc8bVK/j7NXBUQG1ECSjOQFP9tu5n4tpKYylV8ctzfFf3pkz+9DHt4HDAO6XjqnpFnQ5PNGd4Hr5lWABSABeeE+eLndFZONfDyE; AWSALBCORS=HaBhC0Ey9uh7V8BeQ0kfH1dlfoc8bVK/j7NXBUQG1ECSjOQFP9tu5n4tpKYylV8ctzfFf3pkz+9DHt4HDAO6XjqnpFnQ5PNGd4Hr5lWABSABeeE+eLndFZONfDyE; bm_sv=77E48E24B86B5201FC593E39F6C23783~CJPQWzCnqEIqcpmSnHCsDyOwPecASE8/XFZvXcngShuucknxijPCqtgbWvZNkNRGssPTskDr4DvrDqEh9bWUt3neMTzgcd+BeubF7KUwNiRPNgbUGgPAv5QOOde1CmeMrZqWZpHoCIP8H9O0vKwJpXd6xwslvszH0DamadRvUFk='

requests_headers = {
    'authority': 'www.pizzahut.com',
    'method': 'GET',
    'path': '/api.php/site/api_pages/api_menu/getstoretiles',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': cookies_,
    'referer': 'https://www.pizzahut.com/index.php?menu=pizza',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'x-sec-clge-req-type': 'ajax'
}


html_file = requests.get(url1, headers=requests_headers)

print(html_file.status_code)
total_data = html_file.json()['pages']['pizza']['sections'][0]['tiles']


f = open('pizzahut_task.csv', 'a', newline='')
csv_writer = csv.writer(f)

Menu = 'pizza'
Sub_Menu = 'popular pizza'

for c in total_data:
    title = c['title']

    price = c['tile_data']['prices']
    for each_curst in c['crusts']:
        crust_cleaner = re.compile(
            '<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        crust_clean = re.sub(crust_cleaner, '', each_curst['text'])
        crust = crust_clean

        if crust_clean == 'Hand Tossed Pizza':
            for s in c['sizes']:
                each_size_cleaner = re.compile(
                    '<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
                each_size_clean = re.sub(each_size_cleaner, '', s['text'])
                if each_size_clean == 'Large':
                    size = each_size_clean
                    price_ = price['L']
                    csv_writer.writerow(
                        [Menu, Sub_Menu, title, crust, size, price_])

                    print(Menu, Sub_Menu, title, crust, size, price_)

                if each_size_clean == 'Medium':
                    size = each_size_clean
                    price_ = price['M']

                    csv_writer.writerow(
                        [Menu, Sub_Menu, title, crust, size, price_])

                    print(Menu, Sub_Menu, title, crust, size, price_)

        if crust_clean == "Thin 'N Crispy ":
            for s in c['sizes']:
                each_size_cleaner = re.compile(
                    '<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
                each_size_clean = re.sub(each_size_cleaner, '', s['text'])
                if each_size_clean == 'Large':
                    size = each_size_clean
                    price_ = price['LT']

                    csv_writer.writerow(
                        [Menu, Sub_Menu, title, crust, size, price_])

                    print(Menu, Sub_Menu, title, crust, size, price_)

                if each_size_clean == 'Medium':
                    size = each_size_clean
                    price_ = price['MT']

                    csv_writer.writerow(
                        [Menu, Sub_Menu, title, crust, size, price_])

                    print(Menu, Sub_Menu, title, crust, size, price_)

        if crust_clean == 'Original Pan Pizza':
            for s in c['sizes']:
                each_size_cleaner = re.compile(
                    '<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
                each_size_clean = re.sub(each_size_cleaner, '', s['text'])
                if each_size_clean == 'Large':
                    size = each_size_clean
                    price_ = price['LD']

                    csv_writer.writerow(
                        [Menu, Sub_Menu, title, crust, size, price_])

                    print(Menu, Sub_Menu, title, crust, size, price_)

                if each_size_clean == 'Medium':
                    size = each_size_clean
                    price_ = price['MD']

                    csv_writer.writerow(
                        [Menu, Sub_Menu, title, crust, size, price_])

                    print(Menu, Sub_Menu, title, crust, size, price_)

                if each_size_clean == 'Personal Pan Pizza':
                    size = each_size_clean
                    price_ = price['PP']

                    csv_writer.writerow(
                        [Menu, Sub_Menu, title, crust, size, price_])

                    print(Menu, Sub_Menu, title, crust, size, price_)

        if crust_clean == 'Original Stuffed Crust':
            for s in c['sizes']:
                each_size_cleaner = re.compile(
                    '<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
                each_size_clean = re.sub(each_size_cleaner, '', s['text'])
                if each_size_clean == 'Large':
                    size = each_size_clean
                    price_ = price['LS']

                    csv_writer.writerow(
                        [Menu, Sub_Menu, title, crust, size, price_])

                    print(Menu, Sub_Menu, title, crust, size, price_)


print('all executed')
