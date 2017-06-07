btn3=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="3", bg="blue", command=lambda:btnClick(3)).grid(row=3, column=2)

Multiplicacion=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="x", bg="blue", command=lambda:btnClick("*")).grid(row=3, column=3)

#===============================================================================
btn0=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="0", bg="blue", command=lambda:btnClick(0)).grid(row=4, column=0)

btnlimpiar=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="C", bg="blue", command= btnLimpiarTexto).grid(row=4, column=1)

btnIgual=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="=", bg="blue", command=botonIgual).grid(row=4, column=2)

Division=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="/", bg="blue", command=lambda:btnClick("/")).grid(row=4, column=3)