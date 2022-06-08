from datetime import datetime
import pandas
import os

class Export:
    def printInfo(self, nameFile):
        print(f'''
    ###########################################################
    #                                                         #
    # O arquivo {nameFile} foi       #  
    # criado na pasta ExcelExports                            #
    #                                                         #
    ###########################################################
        ''')

    def setNameFile(self):
        os.chdir(f'{os.getcwd()}/ExcelExports')
        dateStr = datetime.today().strftime('%Y-%m-%d_%H:%M:%S')
        return f'ExportFile-{dateStr}.xlsx'

    def createExcel(self, data):
        dataFrame = pandas.DataFrame(data)
        nameFile = self.setNameFile()
        file = pandas.ExcelWriter(nameFile, engine='xlsxwriter')

        dataFrame.to_excel(file, sheet_name='Sheet1', index=False)
        file.save()

        self.printInfo(nameFile)