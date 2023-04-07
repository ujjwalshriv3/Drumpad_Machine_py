## �Ұ�

������ tkinter�� ����Ͽ� Python���� �ۼ��� ������ GUI (�׷��� ����� �������̽�)�� ����� ���Դϴ�.

## tkinter �Ұ�

Tkinter�� Tk GUI ��Ŷ���� ǥ�� Python �������̽��Դϴ�. �ڼ��� ����� ��ü ���̺귯�� ������ ������ [����] https://docs.python.org/3/library/tkinter.html�� �̵��Ͻʽÿ�.

## ����

```python
from tkinter import Button, Tk, messagebox

def greet():
    # �̰��� tkinter���� ������ �˾� ���ڸ� ����� ����Դϴ�
    # ù ��° �Ű� ������ box�� �����̸� �� ��° �Ű� ������ ������ ��Ÿ���ϴ�.
    messagebox.showinfo('Greetings', 'Hello, world!')

# ���⿡�� `root`�� ���̺�, ��ư ��� ���� GUI�� ��ü�� �߰��ϴµ� ����� �� �ִ� �߰��� ����� �ֿ� ��ü�Դϴ�.
root = Tk()

# ���� GUI���� ��ư�� ����ϴ�
# ���⼭ ��� �� ���ڴ� ������ �ǹ��մϴ�.
#    1. `master` = �θ� â (�츮�� ���`root`)
#    2. `text` = ��ư�� ���Ե� �ؽ�Ʈ
#    3. `width` = ��ư�� ��
#    4. `command` = ��ư�� ������ �� ����� ����Դϴ�.
button = Button(master=root, text='Press me!', width=10, command=greet)
# �� �޼ҵ带 ȣ���ϸ� ���߰� GUI�� �߰��˴ϴ�.
button.pack()

# GUI ������ �����մϴ�
root.mainloop()
```

