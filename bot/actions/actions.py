from rasa_core_sdk import Action
import telegram

class ActionEnviarDocEstatuto(Action):
    def name(self):
        return "action_enviar_doc_estatuto"

    def run(self, dispatcher, tracker, domain):

        try:
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
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
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
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
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
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
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
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
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
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
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
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
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
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
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
            url = "https://ucb.catolica.edu.br/portal/wp-content/uploads/2021/12/UCB-CALENDARIO-2022-A4-V5.pdf"
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui te enviar o documento em anexo.")
            dispatcher.utter_message("Mas você pode acessá-lo por essa URL:")
            dispatcher.utter_message("https://ucb.catolica.edu.br/portal/wp-content/uploads/2021/12/UCB-CALENDARIO-2022-A4-V5.pdf")

class ActionEnviarLocalizacaoBlocoABCD(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_abcd"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização dos blocos A, B, C e D")

        try:
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
            latitude = -15.867332217513887
            longitude = -48.03043820754369
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoE(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_e"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco E")

        try:
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
            latitude = -15.866730550500023
            longitude = -48.03057020039818
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoF(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_f"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco F")

        try:
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
            latitude = -15.866918891682571
            longitude = -48.03113078209065
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoG(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_g"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco G")

        try:
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
            latitude = -15.867045112251532
            longitude = -48.02809843045367
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoL(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_l"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco L")

        try:
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
            latitude = -15.868033550396934
            longitude = -48.02955231442692
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoS(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_s"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco S")

        try:
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
            latitude =  -15.868791220436874
            longitude = -48.02926837863404
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoM(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_m"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco M")

        try:
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
            latitude =  -15.865674398700659
            longitude = -48.029780635744665
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoN(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_n"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco N")

        try:
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
            latitude =  -15.863852272963632
            longitude = -48.029248943207456
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")
class ActionEnviarLocalizacaoBlocoK(Action):
    def name(self):
        return "action_enviar_localizacao_bloco_k"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Aqui está a localização do bloco K")

        try:
            bot = telegram.Bot(token="5804984228:AAGsKl-TIhSQ_2SFpIqsLWqINTjxUvXRkDI")
            latitude =  -15.864691062768392
            longitude = -48.0295616180415
            bot.sendLocation(chat_id=tracker.sender_id, latitude=latitude, longitude=longitude)
        except Exception:
            dispatcher.utter_message("Desculpe, não consegui acessar as coordenadas para te enviar a localização :/")