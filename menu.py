import pygame as pg
from buttons import Button
from pathlib import Path
import sys
from main import main
from lives import Lives


def menu_screen():

    pg.init()
    screen = pg.display.set_mode((672, 672))

    pg.mixer.music.load(Path('assets','menu_sound.mp3'))
    pg.mixer.music.set_volume(0.7)
    pg.mixer.music.play(-1)
    
    botoes = []

    foto_botao_play = pg.image.load(Path('assets','button4.png'))
    foto_botao_play = pg.transform.scale(foto_botao_play, (250, 100))

    botao_play = Button(foto_botao_play, 336, 295, 'PLAY')
    botao_story = Button(foto_botao_play, 336, 405, 'STORY')
    botao_htp = Button(foto_botao_play, 336, 515, 'HOW TO PLAY')
    botao_quit = Button(foto_botao_play, 336, 625, 'QUIT')

    botoes.append(botao_play)
    botoes.append(botao_story)
    botoes.append(botao_htp)
    botoes.append(botao_quit)

    
    while True:
        mouseX, mouseY = pg.mouse.get_pos()
        screen.blit(pg.image.load(Path('assets', 'background_menu.png')), (0, 0))
        pg.display.set_caption('Menu')

        for botao in botoes:
            Button.draw(botao, screen)
        for botao in botoes:
            Button.hoover(botao, mouseX, mouseY)



        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                for botao in botoes:
                    if Button.verifica_clique(botao, mouseX, mouseY) == True:
                        if botao == botao_quit:
                            pg.quit()
                            sys.exit()
                        elif botao == botao_play:
                            preview_jogo()
                        elif botao == botao_story:
                            story_screen()
                        elif botao == botao_htp:
                            instruction_screen()



        pg.display.flip()

# Fontes
pg.font.init()
title_font = pg.font.Font(Path('assets', 'RAGE.TTF'), 55)
names_font = pg.font.Font(Path('assets', 'RAGE.TTF'), 30)
text_font = pg.font.SysFont('Arial', 25)
points_font = pg.font.SysFont('monospace', 50) #Fonte que vai mostrar a pontuação final do jogador


def story_screen():

    pg.init()
    screen = pg.display.set_mode((672, 672))

    foto_botao = pg.image.load(Path('assets','button4.png'))
    foto_botao = pg.transform.scale(foto_botao, (250, 100))

    foto_silvio = pg.image.load(Path('assets','personagem_com_inseticida-2.png'))
    foto_silvio = pg.transform.scale(foto_silvio, (90, 90))

    foto_bug = pg.image.load(Path('assets','bug_simples.png'))
    foto_bug = pg.transform.scale(foto_bug, (65, 65))

    botao_menu = Button(foto_botao, 336, 625, 'MENU')

    while True:
        mouseX, mouseY = pg.mouse.get_pos()
        #Background image com título, texto e imagens já incorporados
        screen.blit(pg.image.load(Path('assets', 'story_screen3.png')), (0, 0))
        pg.display.set_caption('Story')


        Button.draw(botao_menu, screen)
        Button.hoover(botao_menu, mouseX, mouseY)

        for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if Button.verifica_clique(botao_menu, mouseX, mouseY) == True:
                        menu_screen()



        pg.display.flip()

# How to play screen
def instruction_screen():
    pg.init()
    screen = pg.display.set_mode((672, 672))
    pg.display.set_caption('How to Play')

    foto_botao = pg.image.load(Path('assets','button4.png'))
    foto_botao = pg.transform.scale(foto_botao, (250, 100))

    botao_menu = Button(foto_botao, 336, 625, 'MENU')

    while True:
        mouseX, mouseY = pg.mouse.get_pos()
        screen.blit(pg.image.load(Path('assets', 'howtoplay_screen7.png')), (0, 0))

        Button.draw(botao_menu, screen)
        Button.hoover(botao_menu, mouseX, mouseY)

        for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if Button.verifica_clique(botao_menu, mouseX, mouseY) == True:
                            menu_screen()

        pg.display.flip()




def preview_jogo():

    pg.init()
    screen = pg.display.set_mode((672, 672))
    font = pg.font.get_default_font()
    font_game = pg.font.SysFont(font, 30)
    font_game_2 = pg.font.Font(Path('assets', 'STARZONE.ttf'), 16)

    itens_coletados = {'coffee': 0,
                    'energy_drink': 0,
                    'inseticide': 0,
                    'bit_0': 0,
                    'bit_1': 0,
                    'bugs': 0}

    while True:
        screen.fill((255, 255, 255))
        screen.blit(pg.image.load(Path('assets', 'background.png')), (0, 0))
        
        live_points = Lives(screen)
        live_points.draw()

        

        text_pontuacao = font_game.render(
            f'Pontuação: {(itens_coletados["bit_0"] + itens_coletados["bit_1"])*5 + itens_coletados["bugs"]}', 1, (255, 255, 255))

        screen.blit(text_pontuacao, (270, 10))

        screen.blit(pg.transform.scale(pg.image.load(Path('assets','bug_simples.png')), (40, 35)), (20, 65))

        screen.blit(pg.transform.scale(pg.image.load(Path('assets', 'battery-0.png')), (90, 90)), (5, 85))



        mensagem = font_game_2.render('APERTE EM QUALQUER LUGAR DA TELA PARA COMEÇAR', True, (0, 0, 0))
        screen.blit(mensagem, (43, 336))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                main()

    
        pg.display.flip()


#Tela de erro
def error(pontos):

    pg.init()
    screen = pg.display.set_mode((672, 672))

    pg.mixer.music.load(Path('assets','game_sounds','error_sound.mp3'))
    pg.mixer.music.set_volume(0.7)
    pg.mixer.music.play()

    counter = 0

    while True:
        pg.display.set_caption('Game Over')
        counter += 1

        if counter < 150:
            screen.blit(pg.image.load(Path('assets', 'error_screen.png')), (0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

        else:
            game_over(pontos)
    
        pg.display.flip()

#Tela de Game Over
def game_over(pontos):

    pg.init()
    screen = pg.display.set_mode((672, 672))

    pg.mixer.music.load(Path('assets','game_sounds','gameover_music.mp3'))
    pg.mixer.music.set_volume(0.7)
    pg.mixer.music.play(-1)

    foto_botao_play = pg.image.load(Path('assets','button4.png'))
    foto_botao_play = pg.transform.scale(foto_botao_play, (250, 100))
    
    botoes = []

    botao_restart = Button(foto_botao_play, 336, 545, 'RESTART')
    botao_menu = Button(foto_botao_play, 336, 625, 'MENU')

    botoes.append(botao_restart)
    botoes.append(botao_menu)

    text_points = points_font.render(f'Pontuação:{pontos}', True, 'White')
    text_points_rect = text_points.get_rect(midtop=(336, 260))

    while True:
        mouseX, mouseY = pg.mouse.get_pos()
        pg.display.set_caption('Game Over')

        screen.blit(pg.image.load(Path('assets', 'gameover_screen3.png')), (0, 0)) #Background com título e texto já incorporados
        screen.blit(text_points, text_points_rect)

        for botao in botoes:
            Button.draw(botao, screen)
        for botao in botoes:
            Button.hoover(botao, mouseX, mouseY)

        for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    for botao in botoes:
                        if Button.verifica_clique(botao, mouseX, mouseY) == True:
                            if botao == botao_restart:
                                preview_jogo()
                            elif botao == botao_menu:
                                menu_screen()
        
        pg.display.flip()