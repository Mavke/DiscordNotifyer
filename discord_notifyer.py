from discord import SyncWebhook

class Notifyer():
    def __init__(self, conf_path, seperator="|"):
        self.webhook_url = ''
        self._init_url(conf_path)
        self.webhook = SyncWebhook.from_url(self.webhook_url)        
        self. seperator = seperator

    def _init_url(self, conf_path):
        with open(conf_path, mode='r') as f:
            self.webhook_url = f.readline().strip('\n')
            f.close()


    def send_message(self, data):
        message = " "
        for k, v in data.items():
            message += " ".join((f' **{k}** :',str(v), self.seperator))

        self.webhook.send(message)

notifyer = Notifyer('./webhook.txt')
test_data = {'lr' : 0.001, 'iteration' : 1}

notifyer.send_message(test_data)
 

