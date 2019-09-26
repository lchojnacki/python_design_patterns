import collections

class IteratorKazdy:
    def __init__(self, obiekt_do_iteracji):
        self.obiekt = obiekt_do_iteracji
        self.current_index = 0
    
    def first(self):
        self.current_index = 0

    def next(self):
        self.current_index += 1

    def is_done(self):
        return self.current_index >= len(self.obiekt)

    def current_item(self):
        return self.obiekt[self.current_index]

    

class IteratorNiezerowy:
    def __init__(self, obiekt_do_iteracji):
        self.obiekt = obiekt_do_iteracji
        self.first()
        self.temp_index = self.current_index
    
    def first(self):
        self.current_index = 0
        if self.obiekt[self.current_index] == 0:
            while (self.obiekt[self.current_index] == 0):
                self.current_index += 1

    def next(self):
        self.current_index += 1
        if not self.is_done():
            if self.obiekt[self.current_index] == 0:
                self.next()

    def is_done(self):
        return self.current_index >= len(self.obiekt)

    def current_item(self):
        return self.obiekt[self.current_index]

class MyList:
    def __init__(self, elementy = []):
        if type(elementy) == type([]):
            self.lista = elementy
    
    def __str__(self):
        return str(self.lista)

    def __len__(self):
        return len(self.lista)

    def __getitem__(self, index):
        try:
            return self.lista[index]
        except IndexError as e:
            print(e)

    def dodaj(self, element):
        if isinstance(element, collections.Iterable):
            for e in element:
                self.lista.append(e)
        else:
            self.lista.append(element)


if __name__ == "__main__":
    
    list_1 = MyList([3, 0, 4, 0, 5])

    print("\nIterator 1 dla tablicy " + str(list_1) + ":\n")
    
    iter1 = IteratorKazdy(list_1)
    iter1.first()
    
    while not iter1.is_done():
        print(iter1.current_item())
        iter1.next()
    
    print("\nIterator 2 dla tablicy " + str(list_1) + "; niezerowy:\n")
    iter2 = IteratorNiezerowy(list_1)
    iter2.first()

    while not iter2.is_done():
        print(iter2.current_item())
        iter2.next()

    list_2 = MyList([0, 0, 0, 1, 0, 0, 2, 0, 3, 0])
    print("\nIterator 3 dla tablicy " + str(list_2) + "; niezerowy:\n")

    iter3 = IteratorNiezerowy(list_2)
    iter3.first()

    while not iter3.is_done():
        print(iter3.current_item())
        iter3.next()

    print("\ncurrent_index iteratora 3 po przejściu pętli:")
    print(iter3.current_index)