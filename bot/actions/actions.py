from rasa_core_sdk import Action
import telegram

class ActionEnviarDocEstatuto(Action):
    def name(self):
        return "action_enviar_doc_estatuto"

    def run(self, dispatcher, tracker, domain):

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = "https://ucb.catolica.edu.br/portal/wp-content/uploads/2019/12/ESTATUTO-UCB-2019-1.pdf"
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui te enviar o documento em anexo.")
            dispatcher.utter_message("Mas você pode acessá-lo por essa URL:")
            dispatcher.utter_message("https://ucb.catolica.edu.br/portal/wp-content/uploads/2019/12/ESTATUTO-UCB-2019-1.pdf")

class ActionEnviarManualDoCalouro(Action):
    def name(self):
        return "action_enviar_doc_manual_do_calouro"

    def run(self, dispatcher, tracker, domain):

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = "https://ucb.catolica.edu.br/portal/wp-content/uploads/2022/03/GUIA-DO-ESTUDANTE02.pdf"
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui te enviar o documento em anexo.")
            dispatcher.utter_message("Mas você pode acessá-lo por essa URL:")
            dispatcher.utter_message("https://ucb.catolica.edu.br/portal/wp-content/uploads/2022/03/GUIA-DO-ESTUDANTE02.pdf")

class ActionEnviarCodigoDeConduta(Action):
    def name(self):
        return "action_enviar_doc_codigo_de_conduta"

    def run(self, dispatcher, tracker, domain):

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = "https://ucb.catolica.edu.br/portal/wp-content/uploads/2020/12/CODIGO_CONDUTA_ETICA_UBEC.pdf"
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui te enviar o documento em anexo.")
            dispatcher.utter_message("Mas você pode acessá-lo por essa URL:")
            dispatcher.utter_message("https://ucb.catolica.edu.br/portal/wp-content/uploads/2020/12/CODIGO_CONDUTA_ETICA_UBEC.pdf")

class ActionEnviarCartaDePrincipios(Action):
    def name(self):
        return "action_enviar_doc_carta_de_principios"

    def run(self, dispatcher, tracker, domain):

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = "https://ucb.catolica.edu.br/portal/wp-content/uploads/2019/01/CartadePrincipios.pdf"
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui te enviar o documento em anexo.")
            dispatcher.utter_message("Mas você pode acessá-lo por essa URL:")
            dispatcher.utter_message("https://ucb.catolica.edu.br/portal/wp-content/uploads/2019/01/CartadePrincipios.pdf")

class ActionEnviarRegulamentoGeral(Action):
    def name(self):
        return "action_enviar_doc_regulamento_geral"

    def run(self, dispatcher, tracker, domain):

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = "https://ucb.catolica.edu.br/portal/wp-content/uploads/2022/02/Regulamento_Geral_da_Graduacao.pdf"
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui te enviar o documento em anexo.")
            dispatcher.utter_message("Mas você pode acessá-lo por essa URL:")
            dispatcher.utter_message("https://ucb.catolica.edu.br/portal/wp-content/uploads/2022/02/Regulamento_Geral_da_Graduacao.pdf")

class ActionEnviarNormaseProcedimentos(Action):
    def name(self):
        return "action_enviar_doc_normas_procedimentos"

    def run(self, dispatcher, tracker, domain):

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = "https://ucb.catolica.edu.br/portal/wp-content/uploads/2022/02/Normas-e-Procedimentos-Academicos.pdf"
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui te enviar o documento em anexo.")
            dispatcher.utter_message("Mas você pode acessá-lo por essa URL:")
            dispatcher.utter_message("https://ucb.catolica.edu.br/portal/wp-content/uploads/2022/02/Normas-e-Procedimentos-Academicos.pdf")

class ActionEnviarMIV(Action):
    def name(self):
        return "action_enviar_doc_miv"

    def run(self, dispatcher, tracker, domain):

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = "https://ucb.catolica.edu.br/portal/wp-content/uploads/2022/02/Manual-de-Identidade-CATOLICA-UCB-1.pdf"
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui te enviar o documento em anexo.")
            dispatcher.utter_message("Mas você pode acessá-lo por essa URL:")
            dispatcher.utter_message("https://ucb.catolica.edu.br/portal/wp-content/uploads/2022/02/Manual-de-Identidade-CATOLICA-UCB-1.pdf")

class ActionEnviarCalendario(Action):
    def name(self):
        return "action_enviar_doc_calendario"

    def run(self, dispatcher, tracker, domain):

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = "https://ucb.catolica.edu.br/portal/wp-content/uploads/2021/12/UCB-CALENDARIO-2022-A4-V5.pdf"
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui te enviar o documento em anexo.")
            dispatcher.utter_message("Mas você pode acessá-lo por essa URL:")
            dispatcher.utter_message("https://ucb.catolica.edu.br/portal/wp-content/uploads/2021/12/UCB-CALENDARIO-2022-A4-V5.pdf")