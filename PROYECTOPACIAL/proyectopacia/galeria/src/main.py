import flet as ft


def main(page: ft.Page):
    page.title="Galeria"
    page.bgcolor=ft.Colors.BLACK45
    
    personajes= [
        {
            "titulo": "Katsuki Bakugo (爆豪 勝己)",
            "autor": "Kohei Horikoshi",
            "edad": 17,
            "descripcion": "Orgulloso, explosivo y decidido, estudiante de héroes con gran talento.",
            "imagen": "https://raw.githubusercontent.com/valadezmolinadulcemaria-del/proyectopacial/refs/heads/main/bakugo_katsuk.png"
        },
        {
            "titulo": "Dokuro Mitsukai (ドクロ・ミツカイ)",
            "autor": "Okayu (ilustrador de la novela ligera Bokusatsu Tenshi Dokuro-chan",
            "edad": 16,
            "descripcion": "Ángel violento y dulce, usa un garrote mágico, temperamental pero protectora.",
            "imagen": "https://raw.githubusercontent.com/valadezmolinadulcemaria-del/proyectopacial/refs/heads/main/dokuro_mitsukai.png"
        },
        {
            "titulo": "Beryl",
            "autor": "Luma (artista independiente)",
            "edad": 20,
            "descripcion": "Guerrero fuerte, de cabello rojo, con aire melancólico",
            "imagen": "https://raw.githubusercontent.com/valadezmolinadulcemaria-del/proyectopacial/refs/heads/main/beryl.png"
        },
        {
            "titulo": "Sky (Friday Night Funkin’)",
            "autor": "Originalmente por un fan (mod creado por bbpanzu)",
            "edad": 18 ,
            "descripcion": "Chica enérgica, extrovertida y obsesionada con BF.",
            "imagen": "https://raw.githubusercontent.com/valadezmolinadulcemaria-del/proyectopacial/refs/heads/main/sky_fnf.png"
        },
        {
            "titulo": "Hinata Hyuga",
            "autor": "Masashi Kishimoto",
            "edad": 17 ,
            "descripcion": "Ninja tímida, amable y valiente, pertenece al Clan Hyuga.",
            "imagen": "https://raw.githubusercontent.com/valadezmolinadulcemaria-del/proyectopacial/refs/heads/main/hinata_hyuga.png"
        },
        {
            "titulo": "Randal Ivory",
            "autor": "Capitán Howdie",
            "edad": 17,
            "descripcion": "Puede encariñarse mucho con diferentes personas y amigos, y generalmente quienes las reciben no quieren saber nada de él",
            "imagen": "https://raw.githubusercontent.com/valadezmolinadulcemaria-del/proyectopacial/refs/heads/main/randal_lvory.png"
        },
        {
            "titulo": "Sanemi Shinazugawa",
            "autor": "Koyoharu Gotouge (Kimetsu no Yaiba)",
            "edad": 21,
            "descripcion": "Pilar del viento, impulsivo y rudo, pero de gran corazón.",
            "imagen": "https://raw.githubusercontent.com/valadezmolinadulcemaria-del/proyectopacial/refs/heads/main/sanemi_shinazugawa.png"
        },
        {
            "titulo": "Satoru Tsukada",
            "autor": "Capitán Howdie",
            "edad": 17,
            "descripcion": "es una entidad onírica que parece amigable, tranquila y con una sonrisa amable",
            "imagen": "https://raw.githubusercontent.com/valadezmolinadulcemaria-del/proyectopacial/refs/heads/main/satoru.png"
        },
        {
            "titulo": "Yeo Taeju",
            "autor": "Lee Hae-nal (manhwa Perfect Hybrid)",
            "edad": 20 ,
            "descripcion": "Hombre elegante, calculador y misterioso",
            "imagen": "https://raw.githubusercontent.com/valadezmolinadulcemaria-del/proyectopacial/refs/heads/main/yeotaeju.png"
        },
        {
            "titulo": "Kendrick",
            "autor": "NACHIOBOY",
            "edad": 21,
            "descripcion": " es hombre cual tiene un viru algo curioso,es amable ,resevado ,misterioso",
            "imagen": "https://raw.githubusercontent.com/valadezmolinadulcemaria-del/proyectopacial/refs/heads/main/kendrick.png"
        },
    ]
   
    indice_actua=[0]
   
    contenedor=ft.Container(
       content=ft.Column([]),
       width=400,
       height=500,
       bgcolor=ft.Colors.BROWN_50,
       alignment=ft.alignment.center,
       padding=20
    )
   
    boton_siguiente=ft.ElevatedButton(text="siguiente pintura")
    
    def montrar_personaje():
        personaje=personajes[indice_actua[0]]
        contenedor.content=ft.Column([
            ft.Image(src=personaje["imagen"],width=300,height=300,fit=ft.ImageFit.CONTAIN),
            ft.Text(personaje["titulo"],size=20,weight=ft.FontWeight.BOLD),
            ft.Text(f"Autor: {personaje['autor']}",size=16),
            ft.Text(f"Edad: {personaje['edad']}",size=16),
            ft.Text(personaje["descripcion"],size=14,italic=True)
        ],alignment=ft.MainAxisAlignment.CENTER)
        
        if indice_actua[0]==len(personajes)- 1:
            boton_siguiente.text="volver al inicio"
        else:
            boton_siguiente.text="siguiente personaje"
        page.update()

    def siguiente_click(e):
        indice_actua[0]=(indice_actua[0]+1)%len(personajes)
        montrar_personaje()
    boton_siguiente.on_click=siguiente_click
   
   
   
    page.add(
        ft.Container(
            content=ft.Column([
                contenedor,
                boton_siguiente
            ],alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
        ),
            alignment=ft.alignment.center,
            expand=True
        )
    )
    montrar_personaje()

ft.app(main)
