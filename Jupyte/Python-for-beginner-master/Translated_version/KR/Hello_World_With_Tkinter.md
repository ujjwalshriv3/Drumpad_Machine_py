# Tkinter�� �Բ��ϴ� Hello World

_����, Tkinter��Ű���� �����ͼ� â�� ����ϴ�_

```python
from tkinter import *
window = Tk()
```

_â�� ������ ���Դϴ�._

```python
window.title("Tkinter�� �Բ��ϴ� Hello World")
```

_format���� â�� label�� �߰��մϴ�._

```python
lbl = Label(window, text="Hello World", font=("Arial Bold", 50))
```


_�׷����� �װ��� ��ġ�� �Բ� grid�Լ��� ����Ͽ� �װ��� ��ġ�� �����մϴ�._

```python
lbl.grid(column=0, row=0)
```
_�׸��� �װ� ���Դϴ�. �츰 �츮���� Hello World�� ������ �ɰ̴ϴ�._



```python
from tkinter import *
 
window = Tk()
 
window.title("LikeGeeks app�� ����ϽŰ� ȯ���մϴ�.")
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
window.mainloop()
```

![](hello.png)




