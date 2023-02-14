#!/usr/bin/env python
# coding: utf-8
""" Module listes.py - fonctions de listes """

class EmptyListError(Exception):
    pass


def vide(l):
    """
        renvoie True/False selon que la liste l est vide ou non
    """
    return l == []


def prem(l):
    """
        renvoie le premier élément de l pour toute liste l non vide
    """
    if l:
        return l[0]
    else:
        raise EmptyListError("Cannot get 1st element from an empty list")
    
    
def reste(l):
    """
        renvoie le reste de l pour toute liste l non vide
    """
    if l:
        return l[1:]
    else:
        raise EmptyListError("Cannot get remaining elements from an empty list")
