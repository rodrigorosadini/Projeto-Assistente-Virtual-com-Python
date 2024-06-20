import speech_recognition as sr
import re
import pyttsx3
import webbrowser
import subprocess
import os


init = True
nome = ''
google = 'https://www.google.com'


while (init):
  mic = sr.Recognizer()

  with sr.Microphone() as source:
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.luciana')

    mic.adjust_for_ambient_noise(source)

    print('Vamos começar, fale alguma coisa...')

    audio = mic.listen(source)

    try:
      frase = mic.recognize_google(audio, language='pt-BR').lower()

      #SAIR DO PROGRAMA
      print('Voce falou: ' + frase)
      if (re.search(r'\b' + "sair do programa" + r'\b', format(frase))):
        engine.say('Saindo do programa')
        engine.runAndWait()
        print('Saindo do programa')
        init = False

      #ABRIR NAVEGADOR
      if (re.search(r'\b' + "abra o navegador" + r'\b', format(frase))):
        engine.say('Abrindo seu navegador')
        engine.runAndWait()
        webbrowser.open(google)

      #ABRIR BLOCO DE NOTAS
      if (re.search(r'\b' + "abra o bloco de notas" + r'\b', format(frase))):
        engine.say('Abrindo o bloco de notas')
        engine.runAndWait()
        blocoNotasAberto = subprocess.Popen(['notepad.exe'])

      #FECHAR BLOCO DE NOTAS
      if (re.search(r'\b' + "feche o bloco de notas" + r'\b', format(frase))):
        engine.say('Fechando o bloco de notas')
        engine.runAndWait()
        os.kill(blocoNotasAberto.pid, 9)
      
      #FALAR O NOME
      if (re.search(r'\b' + "meu nome é" + r'\b', format(frase))):
        t = re.search('meu nome é (.*)',format(frase))
        nome = t.group(1)
        engine.say('Olá' + nome)
        engine.runAndWait()
        print('Olá', nome)

    except sr.UnknownValueError:
      print('Ops, algo deu errado')