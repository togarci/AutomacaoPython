from src.SeleniumMode import SeleniumMode

print('''
    ###########################################################
    #               Thyago Odorico Garcia                     #
    #                                                         #
    # Teste de progracao proposto pela BPA                    #
    #                                                         #
    # Requisitos: Python3.7, Chrome Browser                   #
    #                                                         #
    # Dependencia: realize a instalacao das dependencias      #
    # necessarias atravez do comando:                         #
    # python3.7 -m pip install -r requiriments.txt            #
    #                                                         #
    # Execucao: python3.7 main.py                             #
    #                                                         #
    ###########################################################
''')

seleniumExc = SeleniumMode()
seleniumExc.getAmazon('iphone')