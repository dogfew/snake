# Змея

### Как запустить игру? 
```python main.py``` - запустить игру 

```python main.py level_name``` запустить игру с картой ```level_name.csv``` из папки ```levels```

### Как играть? 

    ВВЕРХ       ВНИЗ      ВЛЕВО       ВПРАВО        ВЫБОР УРОВНЯ
    W           S         A           D             ESC
    UP          DOWN      LEFT        RIGHT         ESC
    
Так же можно перемещать змею с зажатой ЛКМ по направлению курсора. 

### Как создавать уровни?

Уровни создаются как .csv-файлы, со следующими обозначениями:

        Пустота     Стена       Змея
        0           1           5 
    
При создании уровня, достаточно разместить .csv файл с номером, который больше последнего на 1.
Если последний файл -> 8.csv, то новый уровень для корректной работы экрана выбора уровней следует назвать 9.csv 
Больше 10 уровней (0-9), чтобы они были доступны на экране выбора уровней, создать нельзя, однако на уровне можно будет поиграть, при запуске программы с аргументом, соотв. названию уровня. 
