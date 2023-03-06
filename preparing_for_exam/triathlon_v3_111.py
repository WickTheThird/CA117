#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.news = {}
        self.name = name
        self.tid = tid

    def add_time(self, event, time=0):
        self.news[event] = time

    def get_time(self, input):
        return self.news[input]

    def __add__(self):
        total = 0
        for x in self.news:
            total = total + self.news[x]
        return total

    def __eq__(self, other):
        return self.__add__() == other.__add__()

    def __lt__(self, other):
        return self.__add__() < other.__add__()

    def __gt__(self, other):
        return self.__add__() > other.__add__()

    def __str__(self):
        return 'Name: {}\nID: {}\nRace time: {}'.format(
            self.name, self.tid, self.__add__()
        )

class Triathlon(object):

    def __init__(self):
        self.agenda = {}
        self.race = {}

    def add(self, other):
        self.agenda[other.tid] = other.name
        self.race[other.__add__()] = other.tid

    def remove(self, tid):
        del self.agenda[tid]

    def lookup(self, tid):
        for x in self.agenda:
            if x == tid:
                return Triathlete(self.agenda[x], tid)
        return None

    def best(self):
        return 'Name: {}\nID: {}\nRace time: {}'.format(self.agenda[self.race[min(self.race)]], self.race[min(self.race)], min(self.race))

    def worst(self):
       return 'Name: {}\nID: {}\nRace time: {}'.format(self.agenda[self.race[max(self.race)]], self.race[max(self.race)], max(self.race))
