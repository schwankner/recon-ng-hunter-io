from recon.core.module import BaseModule


class Module(BaseModule):
    meta = {
        'name': 'Hunter.io Contact Harvester',
        'author': 'schwankner',
        'version': '1.0',
        'description': 'Harvests contacts from hunter.io API V2 using domain.',
        'required_keys': ['emailhunter_key'],
        'query': 'SELECT DISTINCT domain FROM domains WHERE domain IS NOT NULL',
    }

    def get_page(self, base_url, api_key, domain, offset):
        resp = self.request('GET',
                            base_url + 'domain-search?domain=' + domain + '&api_key=' + api_key + '&limit=100&offset=' + str(
                                offset))
        json = resp.json()
        if resp.status_code == 200:
            print(resp.text)
            amount = json['meta']['results']
            if amount == 0:
                self.output('No emails found.')
            for email in json['data']['emails']:
                self.insert_contacts(first_name=email['first_name'], last_name=email['last_name'],
                                     email=email['value'], )
            return amount
        else:
            for error in json['errors']:
                self.output(error['details'])
            return -1

    def module_run(self, domains):
        base_url = 'https://api.hunter.io/v2/'
        api_key = self.get_key('emailhunter_key')

        for domain in domains:
            amount = self.get_page(base_url, api_key, domain, 0)
            if amount > 100:
                for offset in range(100,amount,100):
                    self.get_page(base_url, api_key, domain, offset)
