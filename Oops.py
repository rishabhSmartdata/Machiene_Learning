{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "HP, its your brand\n",
      "25\n",
      "True\n",
      "25335.5\n",
      "1 in Laptop\n",
      "hello its static\n"
     ]
    }
   ],
   "source": [
    "class Laptop:\n",
    "    discount = 10\n",
    "    count_instance = 0\n",
    "    def __init__(self,name,model,price):\n",
    "        Laptop.count_instance += 1\n",
    "        self.name = name\n",
    "        self.model = model\n",
    "        self.price = price\n",
    "        self.brand = name+' '+'9tu'\n",
    "    \n",
    "    @classmethod\n",
    "    def count_instances(cls):\n",
    "        return f'{cls.count_instance} in {cls.__name__}'\n",
    "    \n",
    "    @staticmethod\n",
    "    def hello():\n",
    "        return 'hello its static'\n",
    "        \n",
    "    def full_name(self):\n",
    "        print(Laptop.discount)\n",
    "        return f'{self.name}, its your brand'\n",
    "    \n",
    "    def ageCalculate(self,num):\n",
    "        print(num)\n",
    "        if(num> 18):\n",
    "            return True\n",
    "        \n",
    "    def discount1(self):\n",
    "        \n",
    "        return (Laptop.discount/100)*self.price\n",
    "\n",
    "p1 = Laptop('HP','G6',253355)\n",
    "print(p1.full_name())\n",
    "print(p1.ageCalculate(25))\n",
    "print(p1.discount1())\n",
    "print(Laptop.count_instances())\n",
    "print(Laptop.hello())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import ttk\n",
    "win = tk.Tk()\n",
    "name_label = ttk.Label(win,text=\"Enter your name\")\n",
    "name_label.grid(row=0,column=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arrlist = [1,2,3,4,5]\n",
    "npaaray = np.array(arrlist)\n",
    "print(npaaray)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
