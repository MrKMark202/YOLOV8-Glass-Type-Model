# YOLOV8 Glass Type Model
 Model za prepoznavanje vrsta čaša

<p>
    Model je prvobitno rađen na google colab platformi.
</p>

## UČITAVANJE GOOGLE COLABA I DOPUŠTENJE

```
    from google.colab import drive

    drive.mount('/content/gdrive')
```

## UTF-8 za locale

```
    import locale
    def getpreferredencoding(do_setlocale = True):
    return "UTF-8"
    locale.getpreferredencoding = getpreferredencoding
```

<p>
    Ovo je za neke stvari bilo potrebno napraviti jer je javljalo pogrešku da se izvodine negdje drugdje.
</p>

## Potrebne biblioteke python-a

```
    pip install ultralytics
    pip install opencv-python-headless
    pip install opencv-python
    pip install numpy
    pip install torch
    pip install torchvision
```

## Treniranje i izrada modela

<p>
    Prije početka rada sa YOLOV8 modelom, bilo je potrebno kreirati novi, pa zatim ga trenirati po nekim slikama koje ste samostalno odabrali. Što je više slika, epoha i klasa, to će model biti bolji i precizniji.
</p>


## Načini detekcije

<p>
    Za detekciju vrsta čaša sam koristio modele za prepoznavanje preko jedne slike, preko više slika putem foldera, renderiranje videozapisa i preko kamere.
</p>

## YOUTUBE LINK

### RH: Ovo je link za videoprezentaciju projekta (Na enkleskom jeziku)
### EN: This is videopresentation about this project.

<a>https://www.youtube.com/watch?v=DPrIBf7aF3Q</a>