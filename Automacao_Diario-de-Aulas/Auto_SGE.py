import PySimpleGUI as sg
from time import sleep as sl
from playwright.sync_api import sync_playwright
from datetime import date


class Loguin:

    def __init__(self):

        self.listaunid_curr = None

        self.log_usu = None
        self.sen_usu = None
        self.log_sge = None
        self.sen_sge = None

    def verificacao_log(self, valores):

        self.Usuario = valores['-Usu-']
        self.senha = valores['-Sen-']

        usuarios = []
        with open('Validação.txt', 'r+', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                usuarios.append(linha.split())

            for usuario in usuarios:
                nome = usuario[0]
                password = usuario[-1]

                if self.Usuario == nome and self.senha == password:
                    self.janela_sge = self.sge_tela()
                    self.janela_log.close()
                    print('Loguim Conluído com sucesso')
                elif self.Usuario == 'Ricardo_Silva' and self.senha == 'XAlfa13':
                    self.janela_usu = self.janela_cadastrousuario()
                    self.janela_log.close()
                    print('Entrando na janela de cadastro')

                else:
                    sg.popup_ok('Usuário ou Senha inválidos')

    # REQUIÇÃO DE SENHA ANTIGA PARA ACESSO AO NOVO CADASTRO

    def req_senhanovocadastro(self, valores):

        self.antsenha = valores['-ANSENHA-']

        usuarios = []
        with open('Validação.txt', 'r+', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                usuarios.append(linha.split())

            for usuario in usuarios:
                nome = usuario[0]
                password = usuario[-1]
                if self.antsenha == password:
                    self.janela_usu = self.janela_cadastrousuario()
                    self.janela_apsenha.close()
                    print('Senha antiga correta')
                else:
                    sg.popup_ok('Senha inválida')

    # EM CADASTRO, ATRIBUIÇÃO DAS VARIÁVEIS AOS VALORES DA JANELA JUNTO COM A O CADASTRAMENTO

    def verificacao_senha(self, valores):

        self.usuario = valores['-NU-']

        self.s1 = valores['-S1-']
        self.s2 = valores['-S2-']

        spaceusu = (self.usuario).find(' ')
        spacesenha = (self.s1).find(' ')

        if self.usuario == self.s1:
            sg.popup_ok('Nome de usuário não pode ser igual a Senha')

        elif spaceusu != -1:
            sg.popup_ok('Nome de usuário não pode conter espaços')
        elif spacesenha != -1:
            sg.popup_ok('A senha não pode conter espaços')

        elif self.usuario == '':
            sg.popup_ok('Você deve digitar algum nome')
        elif self.s1 == '':
            sg.popup_ok('Você deve digitar alguma senha')

        elif self.s1 != self.s2:
            sg.popup_ok('As senhas digitadas não correspondem')
        else:
            with open('Validação.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.writelines(f'{self.usuario} {self.s2}')

            sg.popup_ok('Usuário cadastrado com sucesso')
            self.janela_cadsge = self.janela_cadastrosge()
            self.janela_usu.hide()

    # CADASTRAMENTO DOS DADOS PARA LOGUIN NO SGE
    def salvar_sge(self, valores):

        self.msge = valores['-MSGE-']
        self.ssge = valores['-SSGE-']

        if self.msge == '':
            sg.popup_ok('Você deve digitar um E-mail válido')
        elif self.ssge == '':
            sg.popup_ok('Você deve digitar uma senha válida')
        else:
            sg.popup_ok(f'Os dados para acesso ao SGE são:\nE-mail: {self.msge}\nSenha: {self.ssge}')
            with open('SGEloguim.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.writelines(f'{self.msge} {self.ssge}')
            self.janela_cadsge.close()


    # ATRIBUIÇÃO DOS DADOS PARA SALVAMENTO EM ARQUIVO DE TEXTO

    def salvar_loguin(self):

        log_sge = self.msge
        sen_sge = self.ssge

        with open('SGE.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write(f'{log_sge} {sen_sge}')

    # CADASTRO DAS UNIDADES CURRICULARES

    def listaUcs(self, valores):
        print('Lendo as Unidades Curriculares')

        with open('UCS.txt', 'r', encoding='utf-8') as arquivo:
            self.linha = arquivo.read()

        self.ucs = (self.linha)
        self.ucs1 = str(self.ucs).replace('_', ' ')

    def salvar_ucs(self, valores):
        

        self.nucs = valores['-UCS-']

        with open('UCS.txt', 'w', encoding='utf-8') as arquivo:

            for i in self.nucs:
                self.novas_ucs = str(i).upper().replace(' ', '_')
                arquivo.write(self.novas_ucs)
        print('Salvando as Unidades Curriculares')

        self.unid_curr = []
        a = len(self.unid_curr)
        with open('UCS.txt', 'r+', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                self.unid_curr.append(linha.split())

        if a <= 5:
            sg.popup_ok(f'Unidade Curricular {self.unid_curr[-1]}\nCadastrada com sucesso.')

        else:
            sg.popup_ok('So poderá cadastrar até 6 UCs.\nPor favor delete ou substitua alguma')
            print(f'Estão cadastradas {len(self.unid_curr)} de 6 possíveis.\nÀ(s) UC(s) {self.unid_curr[5:]} não funcionarão no programa.')

    # PROGRAMA PRINCIPAL

    def auto_sge(self, valores):

        mes1 = valores['mes']
        ano = valores['ano']
        d1 = valores['d1']
        d2 = valores['d2']
        capacidade = valores['cp']
        cad = valores['ucs']
        plano1 = valores['-Seg-']

        a = len(cad) - 3
        a2 = cad[2:a]
        a3 = str(a2).replace('_', ' ')
        
        with open('Capacidades.txt', 'w', encoding='utf-8')as cap:
            cap.write(f'{capacidade}')
            
        
                

        unid_curr = []

        with open('UCS.txt', 'r+', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                unid_curr.append(linha.split())
                

        sgeloguim = []
        with open('SGEloguim.txt', 'r+', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                sgeloguim.append(linha.split())

            for usuario in sgeloguim:
                sge_email = usuario[0]
                sge_senha = usuario[1]

        ghelist = []

        with open('GHEsave.txt', 'r+', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                ghelist.append(linha.split())

            for item in ghelist:
                gh1 = item[0]
                gh2 = item[1]
                gh3 = item[2]
                gh4 = item[3]
                gh5 = item[4]



        meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

        # REQUISIÇÃO DA DATA DE REFERÊNCIA
        print('Requisitando as datas')

        try:
            mes = meses[mes1]
            mes = str(meses[mes1 - 1]).upper()
            # atual = date.today().year
            print(f'Data requisitada:\nInicial >> {d1}/{mes}/{ano}\nFinal >> {d2}/{mes}/{ano}')

        except Exception:
            sg.popup_error('Problema na requisição da data')

        c = 0

        with sync_playwright() as p:
            for navegador in [p.chromium]:

                if plano1 == False:
                    chrome = navegador.launch()
                elif plano1 == True:
                    chrome = navegador.launch(headless=False)
                print('Abrindo navegador')
                pagina = chrome.new_page()
                pagina.goto('https://www2.fiemg.com.br/Corpore.Net/Login.aspx')

                # pagina.locator('xpath=//*[@id="txtUser"]').click() #LOCALIZAR E CLICAR
                print('Página aberta com sucesso..')
                print('Fazendo o loguim..')
                # LOCALIZAR E PREENCHER O lOGUIN
                pagina.fill('xpath=//*[@id="txtUser"]', f'{sge_email}')
                pagina.fill('xpath=//*[@id="txtPass"]', f'{sge_senha}')

                # CLICAR NO BOTÃO DO LOGUIM
                pagina.locator('xpath=//*[@id="btnLogin"]').click()
                print()

                # CLICA EM DIÁRIO DE CLASSE
                pagina.locator('xpath=//*[@id="ctl18_EDU_EduDiarioClasseActionWeb_LinkControl"]').click()

                # ESCOLHE A TURMA E A DISCIPLINA

                # FECHA JANELA FLUTUANTE
                pagina.locator(
                    'xpath=//*[@id="ctl24_EduTurmasProfRadioButtonWebForm1_ctl00_xpcContexto_HCB-1"]/img').click()
                sl(5)

                # SELECIONA TURMA E DISCIPLINA

                try:



                    if a2 in unid_curr[0]:
                        pagina.locator(
                            f'xpath=//*[@id="ctl24_EduTurmasProfRadioButtonWebForm1_xtabPeriodosLetivos_xpnlTurmaDisciplina_{gh1}"]/span').click()
                       # pagina.locator(
                           # 'xpath=//*[@id="ctl24_EduTurmasProfRadioButtonWebForm1_xtabPeriodosLetivos_xpnlTurmaDisciplina_I3i0_"]/span').click()
                        # ctl24_EduTurmasProfRadioButtonWebForm1_xtabPeriodosLetivos_xpnlTurmaDisciplina_GHC4
                        pagina.locator(
                            f"text= - {a3} >> input[name=\"rdTurma\"]").check()


                    elif a2 in unid_curr[1]:
                        pagina.locator(
                            f'xpath=//*[@id="ctl24_EduTurmasProfRadioButtonWebForm1_xtabPeriodosLetivos_xpnlTurmaDisciplina_{gh2}"]/span').click()
                        #pagina.locator('xpath=//*[@id="ctl24_EduTurmasProfRadioButtonWebForm1_xtabPeriodosLetivos_xpnlTurmaDisciplina_I3i0_"]/span').click()
                        pagina.locator(
                            f"text= - {a3} >> input[name=\"rdTurma\"]").check()


                    elif a2 in unid_curr[2]:

                        pagina.locator(
                            f'xpath=//*[@id="ctl24_EduTurmasProfRadioButtonWebForm1_xtabPeriodosLetivos_xpnlTurmaDisciplina_{gh3}"]/span').click()
                        pagina.locator(
                            f"text= - {a3} >> input[name=\"rdTurma\"]").click()
                        #f"text=HT-ETT-008-N-02 - {INSTALAÇÕES ELÉTRICAS INDUSTRIAIS} >> input[name=\"rdTurma\"]").click()

                    elif a2 in unid_curr[3]:

                        pagina.locator(
                            f'xpath=//*[@id="ctl24_EduTurmasProfRadioButtonWebForm1_xtabPeriodosLetivos_xpnlTurmaDisciplina_{gh4}"]/span').click()
                        pagina.locator(
                            f"text= - {a3} >> input[name=\"rdTurma\"]").click()

                    elif a2 in unid_curr[4]:

                        pagina.locator(
                            f'xpath=//*[@id="ctl24_EduTurmasProfRadioButtonWebForm1_xtabPeriodosLetivos_xpnlTurmaDisciplina_{gh5}"]/span').click()
                        pagina.locator(
                            f"text= - {a3} >> input[name=\"rdTurma\"]").click()


                except Exception:

                    sg.popup_error('Unidade Curricular não encontrada')
                    sl(5)

                    pagina.close()


                # ENTRANDO NO PLANO DE AULA

                pagina.locator('xpath=//*[@id="ctl24_EduToolBarFuncProf1_xbtPlanoAula_CD"]/span').click()

                pagina.locator("input[name=\"ctl24\\$xcbEtapaFalta\"]").press("CapsLock")

                # ESCOLHENDO MÊS E ANO
                pagina.locator("input[name=\"ctl24\\$xcbEtapaFalta\"]").fill(f"{mes}/{ano}")  # USAR MAIÚSCULA
                pagina.locator("input[name=\"ctl24\\$xcbEtapaFalta\"]").fill(f"{mes}/{ano}")
                #pagina.locator('xpath=//*[@id="MainContainer"]/table[3]/tbody/tr/td[1]/fieldset').click()
                sl(1)
                pagina.locator("input[name=\"ctl24\\$xcbEtapaFalta\"]").click()
                sl(1)
                pagina.locator("input[name=\"ctl24\\$xdpDe\"]").click()
                # Fill input[name="ctl24\$xdpDe"]
                pagina.locator("input[name=\"ctl24\\$xdpDe\"]").fill(f"{d1}/{mes1}/{ano}")
                # Click input[name="ctl24\$xdpAte"]
                pagina.locator("input[name=\"ctl24\\$xdpAte\"]").click()
                # Fill input[name="ctl24\$xdpAte"]
                pagina.locator("input[name=\"ctl24\\$xdpAte\"]").fill(f"{d2}/{mes1}/{ano}")

                # /html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/div/table[3]/tbody/tr/td[1]/fieldset/div/div/div/input
                ##ctl24_xbtSelecionar_I
                pagina.locator('xpath=//*[@id="ctl24_xbtSelecionar_CD"]/span').click()


                for i in range(d1, d2):

                    pagina.locator(f'#ctl24_xgvPlanoAula_DXCBtn{c}_CD').click()
                    sl(7)
                    pagina.locator(
                        f"textarea[name=\"ctl24\\$xgvPlanoAula\\$DXPEForm\\$ef{c}\\$xmConteudoEfet\"]").click()
                    # Fill textarea[name="ctl24\$xgvPlanoAula\$DXPEForm\$ef1\$xmConteudoEfet"]
                    pagina.locator(f"textarea[name=\"ctl24\\$xgvPlanoAula\\$DXPEForm\\$ef{c}\\$xmConteudoEfet\"]").fill(
                        f"{capacidade}")
                    pagina.locator("span:has-text(\"Salvar\")").click()

                    sl(5)
                    pagina.locator(f'xpath=//*[@id="ctl24_xgvPlanoAula_DXSelBtn{c}_D"]').click()
                    sl(1)
                    pagina.locator('xpath=//*[@id="ctl24_xmnuOpcao_DXI0_T"]/span').click()
                    sl(1)
                    pagina.locator('xpath=//*[@id="ctl24_xmnuOpcao_DXI0i5_T"]/span').click()
                    c += 5



            sg.popup_ok('Processo Finalizado\nConfira seu SGE')
            pagina.close()
            
            


    def conf_ghe(self):
        unid_curr = []

        with open('UCS.txt', 'r+', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                unid_curr.append(linha.split())

        if len(unid_curr) == 1:
            self.uni1 = unid_curr[0]
        else:
            self.uni1 = ' '

        if len(unid_curr) == 2:
            self.uni1 = unid_curr[0]
            self.uni2 = unid_curr[1]
        else:
            self.uni2 = ' '

        if len(unid_curr) == 3:
            self.uni1 = unid_curr[0]
            self.uni2 = unid_curr[1]
            self.uni3 = unid_curr[2]
        else:
            uni3 = ' '

        if len(unid_curr) == 4:
            self.uni1 = unid_curr[0]
            self.uni2 = unid_curr[1]
            self.uni3 = unid_curr[2]
            self.uni4 = unid_curr[3]
        else:
            self.uni4 = ' '

        if len(unid_curr) == 5:
            self.uni1 = unid_curr[0]
            self.uni2 = unid_curr[1]
            self.uni3 = unid_curr[2]
            self.uni4 = unid_curr[3]
            self.uni5 = unid_curr[4]
        else:
            self.uni5 = ' '

        self.janela_ghe = self.janelaconf()

    def salvar_ghe(self, valores):

        ghe1 = valores['-CT1-']
        ghe2 = valores['-CT2-']
        ghe3 = valores['-CT3-']
        ghe4 = valores['-CT4-']
        ghe5 = valores['-CT5-']

        with open('GHEsave.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(f'{ghe1} {ghe2} {ghe3} {ghe4} {ghe5}')

        sg.popup_ok('GHE cadastrado com sucesso')
        self.janela_ghe.close()


    # JANELA DE LOGUIN INICIAL

    def janela_loguin():

        sg.theme('Reds')
        layout = [

            [sg.Push(), sg.Text('DADOS PARA LOGUIN INICIAL', font=('arial', 11)), sg.Push()],
            [sg.Text('Nome de Usuário:'), sg.Input(size=(35, 1), key='-Usu-')],
            [sg.Text('Senha:                '), sg.Input(size=(10, 1), key='-Sen-', password_char='*')],
            [sg.Button('Continuar'), sg.Button('Novo Cadastro'),sg.Push(), sg.Text('By RickSilva - ver.1.0_beta', font=('Century Schoolbook', 8))],
        ]

        return sg.Window('LOGUIN', layout=layout, finalize=True)
        # janela_log

    # JANELA DE REQUISIÇÃO DE SENHA PARA NOVO CADASTRO

    def janela_apenassenha(self):
        sg.theme('Reds')
        layout = [

            [sg.Text('Digite a senha antiga'), sg.Input(size=(10, 1), key='-ANSENHA-')],
            [sg.Button('Continuar')],
        ]

        return sg.Window('Confirmação NOVO CADASTRO', layout=layout, finalize=True)

        # janela_apsenha

    # JANELA PARA CADASTRO DE USUÁRIO
    def janela_cadastrousuario(self):

        sg.theme('Reds')
        layout = [

            [sg.Push(), sg.Text('DADOS PARA LOGUIN INICIAL', font=('arial', 11)), sg.Push()],
            [sg.Text('Nome de Usuário:'), sg.Input(size=(35, 1), key='-NU-')],
            [sg.Text('Senha:                '), sg.Input(size=(10, 1), key='-S1-')],
            [sg.Text('Repita a Senha:   '), sg.Input(size=(10, 1), key='-S2-'), sg.Push(),
             sg.Button('CADASTRAR DADOS DO SGE', font=('times', 8))],
            [sg.Button('Cadastrar'), sg.Button('Cancelar')],
        ]

        return sg.Window('Cadastro Inicial', layout=layout, finalize=True)
        # janela_usu

    # JANELA PARA CADASTRO DO LOGUIN SGE
    def janela_cadastrosge(self):

        sg.theme('Reds')
        layout = [
            [sg.Push(), sg.Text('DADOS PARA lOGUIN NO SGE'), sg.Push()],
            [sg.Text('E-mail SGE:'), sg.Input(size=(35, 1), key='-MSGE-')],
            [sg.Text('Senha SGE:'), sg.Input(size=(10, 1), key='-SSGE-')],
            [sg.Button('Salvar'), sg.Button('Cancelar')],
        ]

        return sg.Window('Cadastro Loguin SGE', layout=layout, finalize=True)
        # janela_cadsge

    def sge_tela(self):

        unid_curr1 = []
        with open('UCS.txt', 'r+', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                unid_curr1.append(linha.split())
        a = str(unid_curr1).replace('_', ' ')
        
        with open('Capacidades.txt', 'r', encoding='utf-8')as cap:
            capac = cap.read()

         # LAYOUT DA TELA

        sg.theme('Reds')

        layout = [
            [sg.Text('Nº DO MÊS REFERÊNCIA:'),
             sg.Combo(values=list(range(13)), key='mes', default_value=1, size=(3, 1)), sg.Text(
                '     ANO:'), sg.Combo(values=list(range(2021, 2024)), key='ano', default_value=2022, size=(4, 1))],
            [sg.Text('DIA INICIAL'), sg.Combo(values=list(range(32)), key='d1', default_value=1, size=(3, 1)),
             sg.Text('       DIA FINAL '),
             sg.Combo(values=list(range(32)), key='d2', default_value=1, size=(3, 1)), sg.Push(), sg.CBox('Primeiro Plano', key='-Seg-')],
            [sg.Text('Selecione a UC     '), sg.OptionMenu((unid_curr1), key='ucs', size=(40, 1))],
            [sg.HorizontalSeparator()],
            [sg.Text('Digite ou cole a(s) CAPACIDADE(S) desenvolvida(s) no período')],
            [sg.MLine(default_text=f'{capac}', size=(70, 5), key='cp')],
            [sg.HorizontalSeparator()],
            [sg.Text('Processos...')],
            [sg.Output(size=(70, 3))],
            [sg.Button('Cadastrar UC', font=('times', 8)), sg.Push(),sg.Text('By RickSilva - ver.1.0_beta', font=('Century Schoolbook', 8)),sg.Push(), sg.Button('Rodar'), sg.Button('Cancelar')],
        ]
        return sg.Window('SGE_auto', layout=layout, finalize=True)
        # janela_sge

    def cadastrarUcs(self):

        sg.theme('Reds')

        layout = [
            [sg.Text('ADICIONE UMA NOVA UC OU SUBSTITUA UMA.')],
            [sg.MLine(default_text=f'{self.ucs1}', size=(50, 5), key='-UCS-')],
            [sg.Button('Configurar GHE'), sg.Push(), sg.Button('Salvar'), sg.Button('Cancelar')],
        ]

        return sg.Window('Cadastro de UCs', layout=layout, finalize=True)

        # janela_caducs

    def janelaconf(self):


        sg.theme('Reds')

        layout = [
            [sg.Text('CADASTRO DO GHC', font=20)],
            [sg.Text('Nº do GHC:'), sg.Text(f'{self.uni1}', size=(45, 1)), sg.Push(),
             sg.Input(default_text='GHC', size=(6, 1), key='-CT1-')],
            [sg.Text('', size=(9, 1)), sg.Text(f'{self.uni2}', size=(45, 1)), sg.Push(),
             sg.Input(default_text='GHC', size=(6, 1), key='-CT2-')],
            [sg.Text('', size=(9, 1)), sg.Text(f'{self.uni3}', size=(45, 1)), sg.Push(),
             sg.Input(default_text='GHC', size=(6, 1), key='-CT3-')],
            [sg.Text('', size=(9, 1)), sg.Text(f'{self.uni4}', size=(45, 1)), sg.Push(),
             sg.Input(default_text='GHC', size=(6, 1), key='-CT4-')],
            [sg.Text('', size=(9, 1)), sg.Text(f'{self.uni5}', size=(45, 1)), sg.Push(),
             sg.Input(default_text='GHC', size=(6, 1), key='-CT5-')],
            [sg.Button('Salvar'), sg.Button('Cancelar')]

        ]

        return sg.Window('Configuração Inicial', layout=layout, finalize=True)
        # janela_ghe



    # TELA PARA EXECUSSÃO DA AUTOMAÇÃO

    janela_log, janela_caducs, janela_sge, janela_apsenha, janela_usu, janela_cadsge, janela_ghe = janela_loguin(), None, None, None, None, None, None

    def Iniciar(self):

        while True:
            janela, evento, valores = sg.read_all_windows()
            if janela == self.janela_log and evento == sg.WIN_CLOSED or evento == 'Cancelar':
                break
            elif janela == self.janela_apsenha and evento == sg.WIN_CLOSED or evento == 'Cancelar':
                self.janela_apsenha.close()
            elif janela == self.janela_sge and evento == sg.WIN_CLOSED or evento == 'Cancelar':
                break
            elif janela == self.janela_caducs and evento == sg.WIN_CLOSED or evento == 'Cancelar':
                self.janela_caducs.close()
            elif janela == self.janela_apsenha and evento == sg.WIN_CLOSED or evento == 'Cancelar':
                self.janela_apsenha.close()
            elif janela == self.janela_ghe and evento == sg.WIN_CLOSED or evento == 'Cancelar':
                self.janela_ghe.close()
            elif janela == self.janela_cadsge and evento == sg.WIN_CLOSED or evento == 'Cancelar':
                self.janela_cadsge.close()
            elif janela == self.janela_usu and evento == sg.WIN_CLOSED or evento == 'Cancelar':
                    self.janela_usu.close()
                

            elif janela == self.janela_log and evento == 'Continuar':
                self.verificacao_log(valores)

            elif janela == self.janela_log and evento == 'Novo Cadastro':
                # self.janela_log.hide()
                self.janela_apsenha = self.janela_apenassenha()

            elif janela == self.janela_apsenha and evento == 'Continuar':
                self.req_senhanovocadastro(valores)

            elif janela == self.janela_usu and evento == 'Cadastrar':
                self.verificacao_senha(valores)
            elif janela == self.janela_usu and evento == 'CADASTRAR DADOS DO SGE':
                self.janela_cadsge = self.janela_cadastrosge()

            elif janela == self.janela_sge and evento == 'Cadastrar UC':
                self.listaUcs(valores)
                self.janela_caducs = self.cadastrarUcs()

            elif janela == self.janela_caducs and evento == 'Salvar':
                self.salvar_ucs(valores)

            elif janela == self.janela_cadsge and evento == 'Salvar':
                self.salvar_sge(valores)
                self.salvar_loguin()
            elif janela == self.janela_caducs and evento == 'Configurar GHE':
                self.conf_ghe()

            elif janela == self.janela_ghe and evento == 'Salvar':
                self.salvar_ghe(valores)


            elif janela == self.janela_sge and evento == 'Rodar':
                self.auto_sge(valores)



        print(evento, valores)


loguin = Loguin()
loguin.Iniciar()
