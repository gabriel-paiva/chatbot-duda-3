from rasa_core_sdk import Action
import telegram

class ActionEnviarDocEstatuto(Action):
    def name(self):
        return "action_enviar_doc_estatuto"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está o documento do Estatuto da UCB")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://ucb.catolica.edu.br/portal/wp-content/uploads/2019/12/ESTATUTO-UCB-2019-1.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar o documento :/")
            dispatcher.utter_message("Mas você pode me perguntar sua dúvida" +
                                     " específica que eu farei o máximo para" +
                                     " te responder!")

class ActionEnviarManualDoCalouro(Action):
    def name(self):
        return "action_enviar_doc_manual_do_calouro"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está o documento do Manual do Calouro")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://ucb.catolica.edu.br/portal/wp-content/uploads/2022/03/GUIA-DO-ESTUDANTE02.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar o documento :/")
            dispatcher.utter_message("Mas você pode me perguntar sua dúvida" +
                                     " específica que eu farei o máximo para" +
                                     " te responder!")

class ActionEnviarCodigoDeConduta(Action):
    def name(self):
        return "action_enviar_doc_codigo_de_conduta"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está o documento do Código de Conduta")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://ucb.catolica.edu.br/portal/wp-content/uploads/2020/12/CODIGO_CONDUTA_ETICA_UBEC.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar o documento :/")
            dispatcher.utter_message("Mas você pode me perguntar sua dúvida" +
                                     " específica que eu farei o máximo para" +
                                     " te responder!")

class ActionEnviarCartaDePrincipios(Action):
    def name(self):
        return "action_enviar_doc_carta_de_principios"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está o documento da Carta de Principios da UBEC")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://ucb.catolica.edu.br/portal/wp-content/uploads/2019/01/CartadePrincipios.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar o documento :/")
            dispatcher.utter_message("Mas você pode me perguntar sua dúvida" +
                                     " específica que eu farei o máximo para" +
                                     " te responder!")

class ActionEnviarRegulamentoGeral(Action):
    def name(self):
        return "action_enviar_doc_regulamento_geral"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está o documento de Regulamento Geral da Graduação")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://ucb.catolica.edu.br/portal/wp-content/uploads/2022/02/Regulamento_Geral_da_Graduacao.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar o documento :/")
            dispatcher.utter_message("Mas você pode me perguntar sua dúvida" +
                                     " específica que eu farei o máximo para" +
                                     " te responder!")

class ActionEnviarNormaseProcedimentos(Action):
    def name(self):
        return "action_enviar_doc_normas_procedimentos"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está o documento de Normas e Procedimentos Acadêmicos da UCB")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://ucb.catolica.edu.br/portal/wp-content/uploads/2022/02/Normas-e-Procedimentos-Academicos.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar o documento :/")
            dispatcher.utter_message("Mas você pode me perguntar sua dúvida" +
                                     " específica que eu farei o máximo para" +
                                     " te responder!")

class ActionEnviarMIV(Action):
    def name(self):
        return "action_enviar_doc_miv"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está o documento do Manual de Identidade Visual da UCB")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://ucb.catolica.edu.br/portal/wp-content/uploads/2022/02/Manual-de-Identidade-CATOLICA-UCB-1.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar o documento :/")
            dispatcher.utter_message("Mas você pode me perguntar sua dúvida" +
                                     " específica que eu farei o máximo para" +
                                     " te responder!")

class ActionEnviarCalendario(Action):
    def name(self):
        return "action_enviar_doc_calendario"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está o documento do Calendário Acadêmico de 2022")

        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://ucb.catolica.edu.br/portal/wp-content/uploads/2021/12/UCB-CALENDARIO-2022-A4-V5.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar o documento :/")
            dispatcher.utter_message("Mas você pode me perguntar sua dúvida" +
                                     " específica que eu farei o máximo para" +
                                     " te responder!")