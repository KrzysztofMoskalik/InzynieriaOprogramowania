# -*- coding: utf-8 -*-
import os
import re
#import plików
from Parsers.PhpParser import PhpParser
from Parsers.CppParser import CppParser
from Parsers.PyParser import PyParser

#klasa fileReader
class FileReader:

    #tablica asocjacyjna zależności między plikami
    dependencies = {}

    #tablica parserów z konkretnymi rodzajami plików
    parsers = {
        '.php': PhpParser(),
        '.cpp': CppParser(),
        '.py': PyParser()
    }

#metoda do odczytu plików
    def readFiles(self, files, rootDirectory):

        '''
        dla kazdej nazwy pliku wybieramy ścieżkę do tego pliku i rozszeżenie
        wybranie odpowiedniego parsera w zależności od rozszeżenia pliku
        otworzenie pliku do odczytu
        usunięcie komentarzy w pliku
        znalezienie importów/includów
        sprawdzenie czy pliki istnieją w podenym zestawie plików 
            (czy odwołanie jest do pliku który został podany na wejściu)
        stworzenie tablicy z zależnościami między plikami
        '''
        for fileName in files:
            filepath, extension = os.path.splitext(fileName)

            parser = self.parsers.get(extension)
            if not parser:
                continue

            file = open(fileName, 'r')
            file = parser.removeComments(file.read())
            dependencies = parser.findDependencies(file, rootDirectory)
            dependencies = self.checkFilesExistance(files, dependencies, rootDirectory)
            self.dependencies[fileName] = dependencies
        print (self.dependencies)

    '''
    metoda do sprawdzania czy podany plik istnieje w zestawie plików wejściowych
    '''
    def checkFilesExistance(self, files, dependencies,rootDirectory):
        existedFiles = []
        for dep in dependencies:
            depPath = os.path.join(rootDirectory, dep)
            depPath = os.path.abspath(depPath)
            if depPath in files:
                existedFiles.append(depPath)
        return existedFiles
