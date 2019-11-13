# -*- coding: utf-8 -*-
#biblioteka do wyrażeń regularnych i operacji systemowych
import os
import re

class PyParser:

    # regexp do znajdywania komentarzy
    commentPatter = r"# [^\n]*$|[']{3}[\s\S\n]*[']{3}|[\"]{3}[\s\S\n]*[\"]{3}"
    # regexp do znajdywania importów
    linkPattern = r"from[\s]([\S\.]*)[\s]"

    '''
        metody do usuwania komentarzy w plikach i znajdywania w nich zależności
        w podanym pliku zamienia znaleziony komentarz na pusty string w danym ploiku dolowlną ilość razy
            używając szukania w trybie wielolinijkowym
        znajduje wszystkie importy innych plików w danym pliku używając szukania w trybie wielolinijkowym
        
        pyton nie używa typowej ścieżki do pliku tylko listy "modułów" przedzielonej kropkami i w tym miejscu 
            zamieniamy rodzaj importu na ścieżkę do pliku
        '''
    def removeComments(self, file):
        file = re.sub(self.commentPatter, '', file, 0, re.MULTILINE)
        return file

    def findDependencies(self, file, rootDirectory):
        fixedDependencies = []
        dependencies = re.findall(self.linkPattern, file, re.MULTILINE)
        for dependency in dependencies:
            filename = dependency.replace('.', os.path.sep)
            filename = filename + '.py'
            fixedDependencies.append(filename)
        return fixedDependencies