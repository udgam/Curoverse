import scrapy
from items import BloodTypeItem

known_hu_ids = ["hu011C57", "hu0E64A1", "hu2D6140", "hu4339C0", "hu5B8771", "hu687B6B", "hu7DCBF9", "huA05317", "huBAAC98", "huD10E53", "huED0F40", "hu016B28", "hu1187FF", "hu2DBF2D", "hu448C4B", "hu5CD2C6", "hu68929D", "hu8073B9", "huA0E089", "huBE0B25", "huD37D14", "huEDEA65", "hu0211D6", "hu132B5C", "hu2FEC01", "hu44DCFF", "hu5E55F5", "hu6C733E", "hu8229AE", "huA49E22", "huBEDA0B", "huD3A569", "huEDF7DA", "hu025CEA", "hu1378E3", "hu3073E3", "hu470099", "hu5FA322", "hu6E4515", "hu82436A", "huA4E2CF", "huC14AE1", "huD52556", "huF1DC30", "hu032C04", "hu15FECA", "hu33E2D9", "hu48C4EB", "hu5FB1B9", "hu704A85", "hu82E689", "huA4F281", "huC29627", "huD81F3D", "huF2DA6F", "hu034DB1", "hu1904EC", "hu342A08", "hu4B0812", "hu5FCE15", "hu7123C1", "hu868880", "huAA245C", "huC3160A", "huD9EE1E", "huF5AD12", "hu040C0A", "hu19C09F", "hu34D5B9", "hu4BE6F2", "hu60180F", "hu71E59D", "hu88A079", "huAE4A11", "huC434ED", "huDBD591", "huF5E0B6", "hu04DF3C", "hu1F73AB", "hu38168C", "hu4BF398", "hu602487", "hu72A81D", "hu8E2A35", "huAEADC0", "huC5733C", "huDBF9DD", "huF80F84", "hu04F220", "hu241DEA", "hu3A1B15", "hu4CA5B9", "hu60AB7C", "hu72C17A", "hu8E87A9", "huAEC1B0", "huC92BC9", "huDE435D", "huFA70A3", "hu050E9C", "hu24C863", "hu3A8D13", "hu4FE0D1", "hu619F51", "hu76CAA5", "hu8F918A", "huAFA81C", "huC93106", "huDF04CC", "huFAF983", "hu05FD49", "hu259AC7", "hu3C0611", "hu52B7E5", "hu620F18", "hu775356", "hu90B053", "huB1FD55", "huCA017E", "huE2E371", "huFCC1C1", "hu089792", "hu26B551", "hu3CAB43", "hu52F345", "hu627574", "hu7852C5", "hu92C40A", "huB4883B", "huCA14D2", "huE58004", "huFE71F3", "hu0A4518", "hu27FD1F", "hu3F864B", "hu553620", "hu63EB0A", "hu79F922", "hu92FD55", "huB4940E", "huCCAFD0", "huE9B698", "huFFAD87", "hu0CF2EE", "hu2843C9", "hu4040B8", "hu57A769", "hu64DBF7", "hu7A2F1D", "hu939B7C", "huB4D223", "huCD380F", "huEA4EE5", "huFFB09D", "hu0D1FA1", "hu297562", "hu42D651", "hu589D0B", "hu661AD0", "hu7A4AD1", "hu955EE1", "huB4F9B2", "huD09534", "huEBD467", "hu0D879F", "hu2C1D94", "hu432EB5", "hu599905", "hu67EBB3", "hu7B594C", "huA02824", "huBA30D4", "huD103CC", "huEC6EEC"]

class BloodtypeSpider(scrapy.Spider):
    name = "bloodtype"
    allowed_domains = ["my.pgp-hms.org"]
    start_urls = ["https://my.pgp-hms.org/profile/%s" % (huid) for huid in known_hu_ids]
    def parse(self, response):
        item = BloodTypeItem()
        assert response.status == 200, "Bad response"
        item['Sample'] = response.url.split('/')[-1]
        for sel in response.xpath('//table[@class="demographics"]/tr'):
            if sel.xpath('th/text()').extract() == ['Blood Type']:
                bloodtype_list = sel.xpath('td/text()').extract()
                if len(bloodtype_list) > 0:
                    assert len(bloodtype_list) == 1, "multiple bloodtypes? %s" % (bloodtype_list)
                    item['Bloodtype'] = bloodtype_list[0]
        yield item