#!/usr/bin/env python3

bookDictionary = {}
pointsDictionary = {} 

def generateNumberedListOfBooks(listOfBooks):
    print("\nBook choices, numbered: ")
    bookId=1
    for book in listOfBooks: 
        book = book.strip()
        print(f"{bookId}. {book}")
        bookDictionary[bookId] = book
        pointsDictionary[bookId] = 0
        bookId = bookId+1

def addPoints(bookRanking):
    index = 1
    for ranking in bookRanking:
        pointsDictionary[int(ranking)] = pointsDictionary[int(ranking)] + index
        index = index+1

def collectRankings(listOfAttendees):
    for attendee in listOfAttendees:    
        bookRanking = input (f"\nBook choices ranked for {attendee}: ").split()
        addPoints(bookRanking)

def calculateBookChoice():
    sortedPoints = sorted(pointsDictionary.items(), key=lambda x: x[1])
    topBook = sortedPoints[0][0]
    print("______________________________________________")
    print("\nThe top choice is: " + bookDictionary[int(topBook)])
    print("______________________________________________")

    print(f"\n\nSorted Points = {sortedPoints}")
    print(f"Book dictionary = {bookDictionary}")
    print(f"Points dictionary = {pointsDictionary}")

def main():
    listOfBooks = input ("Suggested books: ").split(";")
    listOfAttendees = input ("\nAttendees: ").split(";")

    generateNumberedListOfBooks(listOfBooks)
    collectRankings(listOfAttendees)
    calculateBookChoice()

main()
 