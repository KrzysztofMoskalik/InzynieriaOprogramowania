# -*- coding: utf-8 -*-
#biblioteka do wyrażeń regularnych
import re

class PhpParser:

    #regexp do znajdywania komentarzy
    commentPatter = r"/[\*]{1,2}[^(\*/)]*[\s\S]]*\*/|//[^\n]*$"
    # regexp do znajdywania importóe
    linkPattern = r"(?:require_once|require|include_once|include)[^\n][\s|(]*['|\"]{1}([\s\w\-.()]*)['|\"]{1}"

    '''
    metody do usuwania komentarzy w plikach i znajdywania w nich zależności
    w podanym pliku zamienia znaleziony komentarz na pusty string w danym ploiku dolowlną ilość razy
        używając szukania w trybie wielolinijkowym
    znajduje wszystkie importy innych plików w danym pliku używając szukania w trybie wielolinijkowym
    '''
    def removeComments(self, file):
        file = re.sub(self.commentPatter, '', file, 0, re.MULTILINE)
        return file

    def findDependencies(self, file, rootDirectory):
        dependencies = re.findall(self.linkPattern, file, re.MULTILINE)
        return dependencies