import pygame
import copy
import random
pygame.init()

# array initialization
l = [9, 8, 6, 7, 4, 9, 2, 1, 5, 6, 7, 4, 6, 3, 8, 2, 7, 2, 3]
duplicate = copy.deepcopy(l)

# window intialization
winX = 600
winY = 600
winSize = (winX, winY)
winColor = (153, 204, 255)
win = pygame.display.set_mode(winSize)
pygame.display.set_caption("Sorting Algorithms")
icon = pygame.image.load("sort.png")
pygame.display.set_icon(icon)

# running status
run = True

# Define Font for text
smallfont = pygame.font.Font('freesansbold.ttf', 13)
font = pygame.font.Font('freesansbold.ttf', 18)
midfont = pygame.font.Font('freesansbold.ttf', 32)
bigfont = pygame.font.Font('freesansbold.ttf', 48)

# Boolean for Various Sorting Window
runbubble = False
runselection = False
runinsertion = False
runmerge = False
runquick = False
runshuffle = False
runcount = False
runradix = False

# Number of sort status
sort = 0


# Bubble Sort
def bubblesort(array, img):
    n = len(array)
    for _ in range(n - 1):
        for i in range(n - 1):
            # selecting bar
            win.fill(winColor)
            drawline(array, 503)
            showlist(array, 500)
            win.blit(img, (145, 100))
            drawbox(array[i], i, 500, "red")
            drawbox(array[i + 1], i + 1, 500, "red")
            pygame.display.update()
            pygame.time.delay(100)
            if array[i] > array[i + 1]:
                # showing swapping of number
                win.fill(winColor)
                drawline(array, 503)
                showlist(array, 500)
                win.blit(img, (145, 100))
                drawbox(array[i], i, 500, "green")
                drawbox(array[i + 1], i + 1, 500, "green")
                pygame.display.update()
                pygame.time.delay(200)
                # swapping
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                # updating window
                win.fill(winColor)
                drawline(array, 503)
                showlist(array, 500)
                win.blit(img, (145, 100))
                drawbox(array[i], i, 500, "green")
                drawbox(array[i + 1], i + 1, 500, "green")
                pygame.display.update()
                pygame.time.delay(200)


# selection Sort
def selectionsort(array, img):
    n = len(array)
    for id in range(n):
        win.fill(winColor)
        drawline(array, 503)
        showlist(array, 500)
        win.blit(img, (145, 100))
        idx = id
        drawbox(array[id], id, 500, "red")
        pointerline(id, 400, 53)
        pygame.display.update()
        pygame.time.delay(200)
        for i in range(id + 1, n):
            win.fill(winColor)
            drawline(array, 503)
            showlist(array, 500)
            win.blit(img, (145, 100))
            drawbox(array[id], id, 500, "black")
            drawbox(array[i], i, 500, "red")
            pointerline(id, 400, 53)
            pygame.display.update()
            pygame.time.delay(200)
            # Set idx = i if array[i]<array[idx]
            if array[idx] > array[i]:
                idx = i
        if idx != id:
            swap = midfont.render("Swap: " + str(array[idx]) + " and " + str(array[id]), True, (0, 0, 150))
            win.blit(swap, (150, 550))
            pointerline(id, 400, 53)
            pygame.display.update()
            pygame.time.delay(500)
        else:
            noswap = font.render("No Swap as " + str(array[idx]) + " is lowest in unsorted array", True, (0, 0, 150))
            win.blit(noswap, (110, 550))
            pointerline(id, 400, 53)
            pygame.display.update()
            pygame.time.delay(1000)
        win.fill(winColor)
        drawline(array, 503)
        showlist(array, 500)
        win.blit(img, (145, 100))
        drawbox(array[idx], idx, 500, "green")
        drawbox(array[id], id, 500, "green")
        pointerline(id, 400, 53)
        temp = array[idx]
        array[idx] = array[id]
        array[id] = temp
        pygame.display.update()
        pygame.time.delay(1000)


# Insertion Sort
def insertionsort(array, img):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        win.fill(winColor)
        drawline(array, 503)
        showlist(array, 500)
        win.blit(img, (145, 100))
        drawbox(array[i - 1], i - 1, 500, "black")
        drawbox(array[i], i, 500, "blue")
        pointerline(i, 400, 53)
        pygame.display.update()
        pygame.time.delay(1000)
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            drawbox(array[j], j, 500, "blue")
            pygame.display.update()
            pygame.time.delay(500)
            j -= 1
        if j >= 0:
            drawbox(array[j], j, 500, "red")
            pygame.display.update()
            pygame.time.delay(500)
        array[j + 1] = key
        win.fill(winColor)
        drawline(array, 503)
        showlist(array, 500)
        win.blit(img, (145, 100))
        drawbox(array[j + 1], j + 1, 500, "green")
        pointerline(i, 400, 53)
        pygame.display.update()
        pygame.time.delay(500)


# Merge sort
def mergesort(array, arraycopy):
    if len(array) > 1:
        m = len(array) // 2

        L = array[:m]
        R = array[m:]

        win.fill(winColor)
        drawline(arraycopy, 103)
        showlist(arraycopy, 100, width=-10)
        drawline(array, 253)
        showlist(array, 250, width=-10)
        drawline(L, 403)
        showlist(L, 400, width=-10)
        drawline([], 553)
        for id in range(len(L)):
            drawbox(L[id], id, 250, "blue", width=-10)
            drawbox(L[id], id, 400, "blue", width=-10)
        dividing = font.render("Dividing current Array in two Subsets of size " + str(len(L)) + " and " + str(len(R)),
                               True, (0, 0, 150))
        win.blit(dividing, (80, 450))
        pygame.display.update()
        pygame.time.delay(1200)

        win.fill(winColor)
        drawline(arraycopy, 103)
        showlist(arraycopy, 100, width=-10)
        drawline(array, 253)
        showlist(array, 250, width=-10)
        drawline(R, 403)
        showlist(R, 400, width=-10)
        drawline([], 553)
        s = len(L) * 30
        for id in range(len(R)):
            drawbox(R[id], id, 250, "blue", start=s, width=-10)
            drawbox(R[id], id, 400, "blue", width=-10)
        dividing = font.render("Dividing current Array in two Subsets of size " + str(len(L)) + " and " + str(len(R)),
                               True, (0, 0, 150))
        win.blit(dividing, (80, 450))
        pygame.display.update()
        pygame.time.delay(1200)

        # recursive calling
        mergesort(L, arraycopy)
        mergesort(R, arraycopy)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):

            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            k += 1
            i += 1

        while j < len(R):
            array[k] = R[j]
            k += 1
            j += 1
        win.fill(winColor)
        drawline(arraycopy, 103)
        showlist(arraycopy, 100, width=-10)
        sorting = font.render('"Merging" two sorted sub arrays with sorting', True, (0, 0, 150))
        win.blit(sorting, (100, 250))
        drawline(L, 403)
        showlist(L, 400, width=-10)
        s = len(L) * 30
        drawline(R, 403, start=s + 5)
        showlist(R, 400, start=s, width=-10)
        pointerline(len(L), 310, 54)
        drawline(array, 553)
        showlist(array, 550, width=-10)
        for id in range(len(array)):
            drawbox(array[id], id, 550, "green", width=-10)
        pygame.display.update()
        pygame.time.delay(2000)


# Quick Sort
def q_partition(array, arrmin, arrmax):
    i = arrmin - 1
    pivot = array[arrmax]

    win.fill(winColor)
    drawline(array, 503)
    showlist(array, 500)
    drawbox(pivot, arrmax, 500, "black")
    pygame.display.update()
    pygame.time.delay(500)

    for j in range(arrmin, arrmax):
        win.fill(winColor)
        drawline(array, 503)
        showlist(array, 500)
        drawbox(pivot, arrmax, 500, "black")
        if i > 0:
            drawbox(array[i], i, 500, "blue")
        drawbox(array[j], j, 500, "green")
        pygame.display.update()
        pygame.time.delay(500)
        if array[j] < pivot:
            i += 1

            win.fill(winColor)
            drawline(array, 503)
            showlist(array, 500)
            drawbox(pivot, arrmax, 500, "black")
            drawbox(array[j], j, 500, "green")
            drawbox(array[i], i, 500, "blue")
            swap = font.render("Swap " + str(array[i]) + " and " + str(array[j]), True,
                               (0, 0, 150))
            win.blit(swap, (200, 550))
            pygame.display.update()
            pygame.time.delay(500)

            temp = array[j]
            array[j] = array[i]
            array[i] = temp

            win.fill(winColor)
            drawline(array, 503)
            showlist(array, 500)
            drawbox(pivot, arrmax, 500, "black")
            drawbox(array[j], j, 500, "green")
            drawbox(array[i], i, 500, "blue")
            swap = font.render("Swap " + str(array[i]) + " and " + str(array[j]), True,
                               (0, 0, 150))
            win.blit(swap, (200, 550))
            pygame.display.update()
            pygame.time.delay(500)

    win.fill(winColor)
    drawline(array, 503)
    showlist(array, 500)
    drawbox(pivot, arrmax, 500, "black")
    # drawbox(array[j], j, 500, "green")
    drawbox(array[i + 1], i + 1, 500, "blue")
    swap = font.render("Swap i (Blue Bar) and Pivot (Black Bar)", True, (0, 0, 150))
    win.blit(swap, (100, 550))
    pygame.display.update()
    pygame.time.delay(1000)

    # Placing Pivot at its place and returning its index for partitioning around it
    temp = array[i + 1]
    array[i + 1] = array[arrmax]
    array[arrmax] = temp

    win.fill(winColor)
    drawline(array, 503)
    showlist(array, 500)
    drawbox(array[i + 1], i + 1, 500, "black")
    # drawbox(array[j], j, 500, "green")
    drawbox(array[arrmax], arrmax, 500, "blue")
    swap = font.render("Swap i (Blue Bar) and Pivot (Black Bar)", True, (0, 0, 150))
    win.blit(swap, (100, 550))
    pygame.display.update()
    pygame.time.delay(1000)

    return i + 1


def quicksort(array, arrmin, arrmax):
    if arrmin < arrmax:
        # Array[partition] at its required place
        partition = q_partition(array, arrmin, arrmax)

        # Recursive Call around Partition
        quicksort(array, arrmin, partition - 1)
        quicksort(array, partition + 1, arrmax)


# Counting Sort
def countsort(array):
    n = max(array)
    count = [0 for i in range(n + 1)]
    output = [0 for i in range(len(array))]
    index = [i for i in range(len(count))]
    for i in range(len(array)):
        count[array[i]] += 1
        win.fill(winColor)
        drawline(count, 203)
        drawline(index, 220, w=0)
        showlist(count, 200, width=-5)
        drawbox(count[array[i]], array[i], 200, "blue", width=-5)
        drawline(array, 353)
        showlist(array, 350, width=-5)
        drawbox(array[i], i, 350, "green", width=-5)
        indx = font.render("-> Counting Number of occurence of each element in Array", True, (0, 0, 150))
        win.blit(indx, (20, 50))
        arr1 = font.render("Counting Array (above)", True, (0, 0, 150))
        win.blit(arr1, (20, 250))
        arr2 = font.render("Original Array (above)", True, (0, 0, 150))
        win.blit(arr2, (20, 380))
        pygame.display.update()
        pygame.time.delay(500)

    for i in range(1, len(count)):
        count[i] += count[i - 1]
        win.fill(winColor)
        drawline(count, 203)
        showlist(count, 200, width=-5)
        drawline(index, 220, w=0)
        drawbox(count[i], i, 200, "blue", width=-5)
        drawbox(count[i - 1], i - 1, 200, "black", width=-5)
        indx = smallfont.render(
            "-> Modify Count Array so that every element of each index stores sum of previous index", True, (0, 0, 150))
        win.blit(indx, (20, 50))
        drawline(array, 353)
        showlist(array, 350, width=-5)
        arr1 = font.render("Counting Array (above)", True, (0, 0, 150))
        win.blit(arr1, (20, 250))
        arr2 = font.render("Original Array (above)", True, (0, 0, 150))
        win.blit(arr2, (20, 380))
        pygame.display.update()
        pygame.time.delay(500)

    for i in range(len(array)):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        win.fill(winColor)
        drawline(count, 203)
        showlist(count, 200, width=-5)
        drawbox(count[array[i]], array[i], 200, "blue", width=-5)
        drawline(index, 220, w=0)
        drawline(array, 353)
        showlist(array, 350, width=-5)
        drawbox(array[i], i, 350, "green", width=-5)
        drawline(output, 503)
        showlist(output, 500, width=-5)
        arr1 = font.render("Counting Array (above)", True, (0, 0, 150))
        win.blit(arr1, (20, 250))
        arr2 = font.render("Original Array (above)", True, (0, 0, 150))
        win.blit(arr2, (20, 380))
        arr3 = font.render("Output Array (above)", True, (0, 0, 150))
        win.blit(arr3, (20, 530))
        pygame.display.update()
        pygame.time.delay(500)
    return output


# Radix sort
def radixcount(array, d):
    count = [0 for i in range(10)]
    output = [0 for i in range(len(array))]

    for i in range(len(array)):
        j = array[i] // d
        count[j % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
    i = len(array) - 1
    while i >= 0:
        j = (array[i] // d) % 10
        output[count[j] - 1] = array[i]
        count[j] -= 1
        i -= 1

    i = len(array) - 1
    while i >= 0:
        array[i] = output[i]
        i -= 1


def radixsort(array):
    maxx = max(array)
    d = 1
    while (maxx / d) > 1:
        radixcount(array, d)
        win.fill(winColor)
        drawline(l, 503, start=0)
        showlist(l, 500, width=-1)
        if d==1:
            sorting = midfont.render("Sorting according to "+str(d)+"'s digit" , True, (0, 0, 150))
            win.blit(sorting, (80, 100))
        else:
            sorting = midfont.render("Sorting according to " + str(d) + "'th digit", True, (0, 0, 150))
            win.blit(sorting, (50, 100))
        note=smallfont.render("Note: Array is changed to bigger digit for better representation of Radix sort", True, (0, 0, 150))
        win.blit(note, (20, 580))
        pygame.display.update()
        pygame.time.delay(2000)
        d = d * 10


# Pointer Line
def pointerline(x, y, start=0):
    pline = pygame.draw.line(win, (150, 0, 0), (start + (30 * (x - 1)), y), (start + (30 * (x - 1)), y + 100), 3)


# Display list
def showlist(array, y, start=0, width=-20):
    j = 1
    for i in (array):
        arraybar = pygame.draw.rect(win, (255, 255, 0), (start + (30 * j), y, 20, width * i))
        j += 1


# Draw axis Line for Bar
def drawline(array, y, start=5, w=4):
    x = 30
    start += 30
    pygame.draw.line(win, (0, 0, 255), (0, y), (winX, y), w)
    if len(array) != 0:
        for i in range(len(array)):
            num = font.render(str(array[i]), True, (0, 0, 150))
            win.blit(num, (start + x * i, y + 10))


# Draw outline Box
def drawbox(x, i, y, color, width=-20, start=0):
    if color == "red":
        color = (255, 0, 0)
    elif color == "green":
        color = (0, 150, 0)
    elif color == "blue":
        color = (0, 0, 255)
    elif color == "black":
        color = (0, 0, 0)
    box = pygame.draw.rect(win, color, (start + 30 * (i + 1), y, 20, width * x), 3)


# Draw grid
def drawgrid():
    x = 75
    # Horizontal Lines
    for i in range(3):
        pygame.draw.line(win, (0, 0, 100), (0, 375 + x * i), (winX, 375 + x * i), 5)
    x = 150
    # Vertical Lines
    for i in range(5):
        pygame.draw.line(win, (0, 0, 100), (0 + x * i, 375), (0 + x * i, 525), 5)


# Write Names
def writename():
    nameBubble = font.render("Bubble Sort", True, (0, 0, 150))
    win.blit(nameBubble, (15, 400))
    nameSelection = font.render("Selection Sort", True, (0, 0, 150))
    win.blit(nameSelection, (160, 400))
    nameInsertion = font.render("Insertion Sort", True, (0, 0, 150))
    win.blit(nameInsertion, (310, 400))
    nameMerge = font.render("Merge Sort", True, (0, 0, 150))
    win.blit(nameMerge, (470, 400))
    nameQuick = font.render("Quick Sort", True, (0, 0, 150))
    win.blit(nameQuick, (15, 475))
    nameCount = font.render("Counting Sort", True, (0, 0, 150))
    win.blit(nameCount, (160, 475))
    nameRadix = font.render("Radix Sort", True, (0, 0, 150))
    win.blit(nameRadix, (315, 475))
    nameRead = font.render("Random Shuffle", True, (0, 0, 150))
    win.blit(nameRead, (455, 475))


# Mouse Click: Select Algorithm
def mouseclick(position):
    global runbubble, runselection, runinsertion, runmerge, runquick, runshuffle, runcount, runradix
    if 0 < position[0] < 150 and 375 < position[1] < 450:
        runbubble = True
    elif 150 < position[0] < 300 and 375 < position[1] < 450:
        runselection = True
    elif 300 < position[0] < 450 and 375 < position[1] < 450:
        runinsertion = True
    elif 450 < position[0] < 600 and 375 < position[1] < 450:
        runmerge = True
    elif 0 < position[0] < 150 and 450 < position[1] < 525:
        runquick = True
    elif 150 < position[0] < 300 and 450 < position[1] < 525:
        runcount = True
    elif 300 < position[0] < 450 and 450 < position[1] < 525:
        runradix = True
    elif 450 < position[0] < 600 and 450 < position[1] < 525:
        runshuffle = True


while run:
    win.fill(winColor)
    drawgrid()
    writename()
    drawline(l, 303)
    showlist(l, 300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouseclick(pos)

    # if Bubble Sort is selected
    if runbubble:
        pygame.display.set_caption("Bubble Sort")
        sort = 0
        while runbubble:
            win.fill(winColor)
            drawline(l, 503)
            showlist(l, 500)
            sortimg = bigfont.render("Bubble Sort", True, (0, 0, 150))
            win.blit(sortimg, (145, 100))
            pygame.display.update()
            if sort == 0:
                bubblesort(l, sortimg)
                sort += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runbubble = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        runbubble = False
                        pygame.display.set_caption("Sorting Algorithms")
                        l = copy.deepcopy(duplicate)

    # if Selection Sort is selected
    if runselection:
        pygame.display.set_caption("Selection Sort")
        sort = 0
        while runselection:
            win.fill(winColor)
            drawline(l, 503)
            showlist(l, 500)
            sortimg = bigfont.render("Selection Sort", True, (0, 0, 150))
            win.blit(sortimg, (145, 100))
            pygame.display.update()
            if sort == 0:
                selectionsort(l, sortimg)
                sort += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runselection = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        runselection = False
                        pygame.display.set_caption("Sorting Algorithms")
                        l = copy.deepcopy(duplicate)

    # if Insertion Sort is selected
    if runinsertion:
        pygame.display.set_caption("Insertion Sort")
        sort = 0
        while runinsertion:
            win.fill(winColor)
            drawline(l, 503)
            showlist(l, 500)
            sortimg = bigfont.render("Insertion Sort", True, (0, 0, 150))
            win.blit(sortimg, (145, 100))
            pygame.display.update()
            if sort == 0:
                insertionsort(l, sortimg)
                sort += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runinsertion = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        runinsertion = False
                        pygame.display.set_caption("Sorting Algorithms")
                        l = copy.deepcopy(duplicate)

    # if Merge Sort is selected
    if runmerge:
        pygame.display.set_caption("Merge Sort")
        sort = 0
        while runmerge:
            win.fill(winColor)
            drawline(l, 503)
            showlist(l, 500)
            sortimg = bigfont.render("Merge Sort", True, (0, 0, 150))
            win.blit(sortimg, (145, 100))
            pygame.display.update()
            mergeduplicate = copy.deepcopy(l)
            if sort == 0:
                mergesort(l, mergeduplicate)
                sort += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runmerge = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        runmerge = False
                        pygame.display.set_caption("Sorting Algorithms")
                        l = copy.deepcopy(duplicate)

    # if Quick Sort is selected
    if runquick:
        pygame.display.set_caption("Quick Sort")
        sort = 0
        while runquick:
            win.fill(winColor)
            drawline(l, 503)
            showlist(l, 500)
            sortimg = bigfont.render("Quick Sort", True, (0, 0, 150))
            win.blit(sortimg, (145, 100))
            pygame.display.update()
            if sort == 0:
                quicksort(l, 0, len(l) - 1)
                sort += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runquick = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        runquick = False
                        pygame.display.set_caption("Sorting Algorithms")
                        l = copy.deepcopy(duplicate)

    # if Counting sort is selected
    if runcount:
        pygame.display.set_caption("Counting Sort")
        sort = 0
        while runcount:
            win.fill(winColor)
            drawline(l, 503)
            showlist(l, 500)
            sortimg = bigfont.render("Counting Sort", True, (0, 0, 150))
            win.blit(sortimg, (145, 100))
            pygame.display.update()
            if sort == 0:
                l = countsort(l)
                sort += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runcount = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        runcount = False
                        pygame.display.set_caption("Sorting Algorithms")
                        l = copy.deepcopy(duplicate)
    if runradix:
        l=[20,15,94,5,33,54,74,92,74,62,69,29,38,22,82,10,49,50,123]
        pygame.display.set_caption("Radix Sort")
        sort = 0
        while runradix:
            win.fill(winColor)
            drawline(l, 503,start=0)
            showlist(l, 500,width=-1)
            sortimg = bigfont.render("Radix Sort", True, (0, 0, 150))
            win.blit(sortimg, (145, 100))
            note = smallfont.render("Note: Array is changed to bigger digits for better representation of Radix sort",
                                    True, (0, 0, 150))
            win.blit(note, (20, 580))
            pygame.display.update()
            if sort == 0:
                radixsort(l)
                sort += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runradix = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        runradix = False
                        pygame.display.set_caption("Sorting Algorithms")
                        l = copy.deepcopy(duplicate)
    # Shuffling List
    if runshuffle:
        random.shuffle(l)
        runshuffle=False

    pygame.display.update()

pygame.quit()
