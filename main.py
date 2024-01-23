import flet as ft
import requests
import json

def MeuAplicativo(page: ft.Page):
    page.bgcolor = ft.colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "auto"
    page.expand = True

#<HOME>----------------------------------------------------------------------------------------------------------------------- 

    def home(e):
        page.controls.clear()
        
        def galeria(e):
            page.padding = 50
            page.scroll = False
            page.expand = False
            page.update()

            images = ft.GridView(
                expand=1,
                runs_count=5,
                max_extent=150,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,
            )

            page.add(images)
 
            for i in range(0, 60):
                images.controls.append(
                    ft.Image(
                        src=f"https://picsum.photos/150/150?{i}",
                        fit=ft.ImageFit.NONE,
                        repeat=ft.ImageRepeat.NO_REPEAT,
                        border_radius=ft.border_radius.all(10),
                    )
                )

            page.update()    
            
        
        page.drawer = ft.NavigationDrawer(
            controls=[
                ft.Column(
                    [
                        ft.Container(height=12),
                        ft.Container(
                            content=(
                                ft.TextButton(
                                    text="Olá Joao Vittor",
                                    icon=ft.icons.HOME,
                                    on_click=home
                                )   
                            ),
                            padding=ft.padding.only(top=10, bottom=10), width=400,
                        ),
                        ft.Divider(thickness=2),
                        ft.Container(
                            content=(
                                ft.TextButton(
                                    text="GALERIA",
                                    icon=ft.icons.PHOTO,
                                    on_click=galeria,
                                )   
                            ),
                            width=400,
                        ),
                        ft.Container(
                            content=(
                                ft.TextButton(
                                    text="CALENDARIO",
                                    icon=ft.icons.CALENDAR_MONTH,
                                    # width=400,
                                )   
                            ),
                            width=400,
                        ),
                        ft.Container(
                            content=(
                                ft.TextButton(
                                    text="AVISOS",
                                    icon=ft.icons.WARNING_OUTLINED,
                                    # width=400,
                                )   
                            ),
                            width=400,
                        ),
                        ft.Container(
                            content=(
                                ft.TextButton(
                                    text="ESCALAS",
                                    icon=ft.icons.LINEAR_SCALE,
                                    # width=400,
                                )   
                            ),
                            width=400,
                        ),
                        ft.Container(
                            content=(
                                ft.TextButton(
                                    text="FINANCEIRO",
                                    icon=ft.icons.ATTACH_MONEY,
                                    # width=400,
                                )   
                            ),
                            width=400,
                        ),
                        ft.Container(
                            content=(
                                ft.TextButton(
                                    text="ESCOLA BIBLICA",
                                    icon=ft.icons.SCHOOL,
                                    # width=400,
                                )   
                            ),
                            width=400,
                        ),
                        ft.Container(
                            content=(
                                ft.TextButton(
                                    text="AJUSTES",
                                    icon=ft.icons.SETTINGS,
                                )   
                            ),
                            width=400,
                        ),
                        ft.Container(
                            content=(
                                ft.TextButton(
                                    text="SAIR",
                                    icon=ft.icons.CLOSE,
                                    on_click=limpar_controles_voltar_login,
                                )   
                            ),
                            padding=ft.padding.only(top=200), width=400,
                        ),
                    ],
                    scroll="always", expand=True,
                ),
            ],
        )
        def show_drawer(e):
            page.drawer.open = True
            page.drawer.update()
 
        page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.MENU, on_click=show_drawer)
        page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
        page.bottom_appbar=ft.BottomAppBar(
            
        )
        
        page.update()

#</HOME>-----------------------------------------------------------------------------------------------------------------------     

#<None>----------------------------------------------------------------------------------------------------------------------- 

    # def home(e):
    #     page.controls.clear()
        
        
    #     page.update()

#</None>-----------------------------------------------------------------------------------------------------------------------     

#<AREA DE LOGIN>-----------------------------------------------------------------------------------------------------------------------    
    def limpar_controles_voltar_login(e):
        page.drawer = False
        page.floating_action_button = False
        page.appbar = False
        page.bottom_appbar = False
        page.controls.clear()
        page.update()
        area_login(e=area_login)
        
    def area_login(e):
        page.scroll = False
        page.expand = False
        page.padding = 0
        text_igreja = ft.Text(value="IGREJA BATISTA GETSÊMANI", size=20, color=ft.colors.BLACK, no_wrap=True)
        text_acesso = ft.Text(value="AREA DE ACESSO", size=15, color=ft.colors.BLACK)
        cpf = ft.TextField(label="INSIRA SEU CPF", width=400, text_align=ft.TextAlign.CENTER, border_color=ft.colors.BLUE, border_radius=ft.border_radius.all(10), color=ft.colors.BLUE, bgcolor=ft.colors.WHITE, border_width=3)
        senha = ft.TextField(label="INSIRA SUA SENHA", width=400, text_align=ft.TextAlign.CENTER, password=True, can_reveal_password=True, border_color=ft.colors.BLUE, border_radius=ft.border_radius.all(10), color=ft.colors.BLUE, bgcolor=ft.colors.WHITE, border_width=3)
        
        def validar_login(e):
            cpf_informado = cpf.value
            senha_informada = senha.value
            
            if cpf_informado == "" and senha_informada == "":
                home(e=home)
            
                
        botao_acessar = ft.ElevatedButton(text="ACESSAR", width=170, on_click=validar_login, color=ft.colors.WHITE, bgcolor=ft.colors.BLUE, height=40)        
        
        def cadastro(e):
            page.controls.clear()
            page.padding = ft.padding.only(top=50)
            page.scroll = True
            page.expand = True
            
            def salvar_dados(e):
                link = "https://cadastro-de-membros-72952-default-rtdb.firebaseio.com/"
                dados = {"PRIMEIRO_NOME": primeiro_nome.value, "SEGUNDO_NOME": segundo_nome.value, "DATA_NASCIMENTO": data_nascimento.value,
                         "CPF": cpf_cadastro.value, "SEXO": sexo.value, "TELEFONE": telefone.value, "EMAIL": e_mail.value, "MEMBRO": membro.value, "CEP": cep.value,
                         "ENDERECO": endereco.value, "COMPLEMENTO": complemento.value, "IGREJA": igreja.value, "BATIZADO": check_batizado.value,
                         "DATA_BATISMO": data_batismo.value, "SENHA": confirmar_senha_cadastro.value, "ID_LOGIN": cpf_cadastro.value + "_" + confirmar_senha_cadastro.value}
                requisicao = requests.post(f"{link}/MEMBROS/.json", data=json.dumps(dados))
                print(requisicao)
                print(requisicao.text)
                print(primeiro_nome.value, segundo_nome.value, data_nascimento.value)
            
            
            def yes_click(e):   
                alert.open = False
                page.controls.clear()
                page.update()
                salvar_dados(e=salvar_dados)
                area_login(e=area_login)

            def no_click(e):
                alert.open = False
                page.update()    
            
            
            primeiro_nome = ft.TextField(label="PRIMEIRO NOME", text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE)
            segundo_nome = ft.TextField(label="SEGUNDO NOME", text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE)
            data_nascimento = ft.TextField(label="Ex: 01/01/2024", text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE)
            
            campo_data_nascimento = ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            ft.Text(value="DATA NASCIMENTO :"),
                        ),
                        ft.Container(
                            width=150,
                            height=50,
                            content=data_nascimento,
                        ),
                    ]
                )
            )
            
            cpf_cadastro = ft.TextField(label="CPF", text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE)
            sexo_check_sim = ft.Radio(label="MASCULINO", value="M")
            sexo_check_nao = ft.Radio(label="FEMININO", value="F")
            sexo = ft.RadioGroup(
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(value="SEXO :"),
                        ),
                        ft.Container(
                            content=sexo_check_sim,
                        ),
                        ft.Container(
                            content=sexo_check_nao,
                        ),
                    ],
                    wrap=True, expand=True, scroll="always",
                )    
            )
            telefone = ft.TextField(label="TELEFONE", text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE)
            e_mail = ft.TextField(label="E-MAIL", text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE)
            membro_check_sim = ft.Radio(label="SOU MEMBRO", value="SIM")
            membro_check_nao = ft.Radio(label="NAO SOU MEMBRO", value="NAO")
            membro = ft.RadioGroup(
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(value="MEMBRO :", no_wrap=True),
                        ),
                        ft.Container(
                            content=membro_check_sim,
                        ),
                        ft.Container(
                            content=membro_check_nao,
                        ),
                    ],
                    wrap=True, expand=True, scroll="always",
                )    
            )
            cep = ft.TextField(label="CEP", text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE)
            endereco = ft.TextField(label="ENDEREÇO", text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE)
            complemento = ft.TextField(label="COMPLEMENTO", text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE)
            igreja = ft.Dropdown(
                label="IGREJA",
                color=ft.colors.BLUE,
                options=[
                    ft.dropdown.Option("IGREJA BATISTA GETSÊMANI")
                ],
                autofocus=True,
            )
            data_batismo = ft.TextField(label="Ex: 01/01/2024", text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE)
            
            campo_data_batismo = ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            ft.Text(value="DATA BATISMO :"),
                        ),
                        ft.Container(
                            width=150,
                            height=50,
                            content=data_batismo,
                        )    
                    ],
                    # wrap=True, expand=True, scroll="always",
                )
            )
            
            batizado_field = ft.Text(value="BATIZADO :")
            batizado_check_sim = ft.Radio(label="SIM", value="SIM")
            batizado_check_nao = ft.Radio(label="NAO", value="NAO")
            check_batizado = ft.RadioGroup(
                content=ft.Row(
                    [
                        ft.Container(
                            content=batizado_field,
                        ),
                        ft.Container(
                            content=batizado_check_sim,
                        ),
                        ft.Container(
                            content=batizado_check_nao,
                        ),
                    ]
                )    
            )
            cadastrar_senha = ft.TextField(label="DIGITE SUA SENHA", text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE, password=True, can_reveal_password=True)
            confirmar_senha_cadastro = ft.TextField(label="CONFIRME SUA SENHA", text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE, password=True, can_reveal_password=True)
            
            def open_alert(e):
                nome_informado = primeiro_nome.value
                sobrenome_informado = segundo_nome.value
                nascimento_informado = data_nascimento.value
                cpf_cadastro_informado = cpf_cadastro.value
                membro_informado = membro.value
                sexo_informado = sexo.value
                igreja_informada = igreja.value
                batismo_informado = check_batizado.value
                batismo_informado_data = data_batismo.value
                cadastrar_senha_informada = cadastrar_senha.value
                confirmar_senha_cadastro_informada = confirmar_senha_cadastro.value
                erro_alert = ft.AlertDialog(
                        title=ft.Text(value="CAMPOS OBRIGATORIOS"),
                        content=ft.Text(value="PRIMEIRO NOME, SEGUNDO NOME, DATA NASCIMENTO, CPF, SEXO e IGREJA.  --VERIFIQUE ALGUNS DOS CAMPOS--"),
                )
                def open_dlg(e):
                    page.dialog = erro_alert
                    erro_alert.open = True
                    page.update()
                    
                if not nome_informado:
                    open_dlg(e=open_dlg)
                    page.update()
                elif not sobrenome_informado:
                    open_dlg(e=open_dlg)
                    page.update()
                elif not nascimento_informado:
                    open_dlg(e=open_dlg)
                    page.update()
                elif not cpf_cadastro_informado:
                    open_dlg(e=open_dlg)
                    page.update()
                elif not sexo_informado:
                    open_dlg(e=open_dlg)
                    page.update()
                elif not membro_informado:
                    open_dlg(e=open_dlg)
                    page.update()
                elif not igreja_informada:
                    open_dlg(e=open_dlg)
                    page.update()
                elif not cadastrar_senha_informada:
                    cadastrar_senha.error_text = "Informe uma senha valida"
                    page.update()
                elif not confirmar_senha_cadastro_informada:
                    confirmar_senha_cadastro.error_text = "Confirme a senha para proceguir"
                elif cadastrar_senha_informada != confirmar_senha_cadastro_informada: 
                    confirmar_senha_cadastro.error_text = "ATENCAO! SENHAS NAO CONFEREM."
                else:
                    page.dialog=alert
                    alert.open=True
                    page.update()
                    
                page.update()
            botao_cadastrar = ft.IconButton(icon=ft.icons.SAVE_ROUNDED, on_click=open_alert, width=150)
            botao_voltar_login = ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT_ROUNDED, on_click=limpar_controles_voltar_login, width=180, icon_size=40)
            
            dados_cadastrais = ft.Container(
                padding=10,
                alignment=ft.alignment.center,
                content=ft.Column(
                    [
                        ft.Container(
                            content=ft.Text(value="INSIRA SEUS DADOS PARA CADASTRO",size=15, color=ft.colors.BLUE),
                            padding=ft.padding.only(top=15, bottom=15)
                        ),
                        ft.Container(
                            content=primeiro_nome,
                        ),
                        ft.Container(
                            content=segundo_nome,
                        ),
                        ft.Container(
                            content=campo_data_nascimento,
                        ),
                        ft.Container(
                            content=cpf_cadastro,
                        ),
                        ft.Container(
                            content=sexo,
                        ),
                        ft.Container(
                            content=telefone,
                        ),
                        ft.Container(
                            content=e_mail,
                        ),
                        ft.Container(
                            content=membro,
                        ),
                        ft.Container(
                            content=cep,
                        ),
                        ft.Container(
                            content=endereco,
                        ),
                        ft.Container(
                            content=complemento,
                        ),
                        ft.Container(
                            content=igreja,
                        ),
                        ft.Container(
                            content=check_batizado,
                        ),
                        ft.Container(
                            content=campo_data_batismo,
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=ft.Text(value="CADASTRE SUA SENHA"),
                            padding=ft.padding.only(top=15),
                            border=ft.border.only(bottom=ft.border.BorderSide(1, "black")),
                            width=700,
                        ),
                        ft.Container(
                            content=cadastrar_senha,
                        ),
                        ft.Container(
                            content=confirmar_senha_cadastro,
                            padding=ft.padding.only(bottom=15),
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
            
            botoes_cadastro=ft.Container(
                ft.Row(
                    controls=[
                        botao_cadastrar,
                        ft.Container(expand=True),
                        botao_voltar_login,
                    ]
                ),padding=25,    
            )
            
            alert = ft.AlertDialog(
                modal=True,
                title=ft.Text(value="CONFIRMA DADOS?"),
                # content=ft.Column(
                    
                # )
                actions=[
                    ft.ElevatedButton("Confirmar", on_click=yes_click),
                    ft.OutlinedButton("Voltar", on_click=no_click)
                    ]
                )
            
            
            page.add(dados_cadastrais,
                     botoes_cadastro)
            page.update()
                     
        botao_seja_membro = ft.TextButton("Seja membro", icon=ft.icons.GROUP_ADD_OUTLINED, on_click=cadastro)
        
        infors = ft.Container(
            
            # bgcolor=ft.colors.GREY_500,
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(10),
            width=400,
            
            content=ft.Column(
                [
                    ft.Container(
                        content=text_igreja,
                        padding=ft.padding.only(top=200)
                    ),
                    ft.Container(
                        content=text_acesso,
                        padding=ft.padding.only(bottom=50, top=50),
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        area_de_acesso = ft.Container(
            
            padding=10,
            # bgcolor=ft.colors.GREY_500,
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(10),
            width=400,
            
            content=ft.Column(
                [
                    ft.Container(
                        content=cpf,
                    ),
                    ft.Container(
                        content=senha,
                    ),
                    ft.Container(
                        content=botao_acessar,
                        padding=ft.padding.only(top=15)
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
            
        cadastrar = ft.Column(
            [
                ft.Container(
                    alignment=ft.alignment.center,
                    content=botao_seja_membro,
                    padding=ft.padding.only(top=50),
                )
            ]
        )
        
        page.add(
            infors,
            area_de_acesso,
            cadastrar)
        
        page.update()
        
    area_login(e=area_login)

#</AREA DE LOGIN>-----------------------------------------------------------------------------------------------------------------------      
    
ft.app(target=MeuAplicativo)