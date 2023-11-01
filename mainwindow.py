import random
import time

import threading
from unittest.mock import patch

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QMainWindow, QPushButton, QLineEdit, QPlainTextEdit, QSpinBox, QFrame, QLabel, QProgressBar

from ui_mainwindow import Ui_MainWindow

from produccion import *

MAX_QUEUE_SIZE = 20
TIME_INTERVAL = 1000 # Intervalo de tiempo en milisegundos (1 segundo)


def select_turn():
    # 1 para productor / 2 para consumidor
    turn = random.randint(1, 2)
    return turn


def calculate_num_products():
    num = random.randint(4, 7)
    return num


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.circular_queue = CircularQueue(MAX_QUEUE_SIZE)
        self.producer = Producer()
        self.customer = Customer()
        
        self.hilo = None # Hilo de ejecucion
        self.pause_condition = threading.Condition() # Condicion de pausa
        
        # Crear un QTimer para actualizar la interfaz cada 1 segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_interfaz)
        self.timer.start(TIME_INTERVAL)  # Intervalo en milisegundos (1 segundo)

        # Actualizacion datos de la interfaz:
        self.texto_p_estado = "Dormido"
        self.texto_p_num = "0"
        self.texto_p_posicion = "0"
        self.texto_c_estado = "Dormido"
        self.texto_c_num = "0"
        self.texto_c_posicion = "0"
        self.texto_turno = "Productor"
        self.texto_cantidad = "0"
        self.texto_pgbar = "0"
        self.lista_taco = [] 
        # ----------------------------------------------------------------|
        # - Banderas - automaticas
        self.continuar = True
        self.en_ejecucion = False
        # - Banderas - pulsaciones
        self.bandera_p = False
        self.bandera_c = False
        # ----------------------------------------------------------------|
        # Definicion de widgets
        # ----------------------------------------------------------------|
        # PgBar
        self.progressBar = self.findChild(QProgressBar, "progressBar")
        # Label´s 
        # (animacion de tacos) 
        self.labels_taco = []   # Lista de labels de tacos
        for i in range(20): # 20 labels de tacos (MAX_QUEUE_SIZE) En la interfaz son 20 fijos 
            label_name = "tacos_" + str(i)
            label = self.findChild(QLabel, label_name)
            label.setVisible(False)  # Inicialmente, todos los labels están ocultos
            self.labels_taco.append(label)
                
        # (animacion de Productor)
        self.label_p_work = self.findChild(QLabel, "lbl_p_work")
        self.label_p_sleep = self.findChild(QLabel, "lbl_p_sleep")
        self.label_p_sleep.setVisible(False)
        # (animacion de Consumidor)
        self.label_c_work = self.findChild(QLabel, "lbl_c_work")
        self.label_c_work.setVisible(False)
        self.label_c_sleep = self.findChild(QLabel, "lbl_c_sleep")
        # Animacion de pausa/continuar
        self.label_play = self.findChild(QLabel, "lbl_play")
        self.label_pause = self.findChild(QLabel, "lbl_pausa")
        self.label_pause.setVisible(False)
        
        # Boton
        self.btn_start = self.findChild(QPushButton, "btn_start")

        # LineEdit
        self.le_p_state = self.findChild(QLineEdit, "ledt_p_state")
        self.le_p_num = self.findChild(QLineEdit, "ledt_p_number")
        self.le_p_position = self.findChild(QLineEdit, "ledt_p_position")
        self.le_c_state = self.findChild(QLineEdit, "ledt_c_state")
        self.le_c_num = self.findChild(QLineEdit, "ledt_c_number")
        self.le_c_position = self.findChild(QLineEdit, "ledt_c_position")
        self.le_turn = self.findChild(QLineEdit, "ledt_turn")
        self.le_amount = self.findChild(QLineEdit, "ledt_number_products")
        
        # ----------------------------------------------------------------------------------------|
        # Eventos
        # -------------------------------------------------------------------------|
        # Ejecutar
        self.btn_start.clicked.connect(self.back_end)
        # -------------------------------------------------------------------------|

    # Funciones
    # -----------------------------------------------------------------------------------
    def reiniciar_programa(self):
        self.circular_queue.reset()
        self.lista_taco.clear()
        self.update_pg_bar(self.circular_queue.length)

    def releaseMemory(self):
        self.circular_queue.clear()
        self.lista_taco.clear()
        self.update_pg_bar(self.circular_queue.length)
        
        self.le_p_num.setText("0")
        self.le_c_num.setText("0")
        self.le_turn.setText(" ")
        self.le_amount.setText("0")
        self.actualizar_interfaz()
    
    def closeEvent(self, event):  # Detectar si se va a cerrar el programa y protegerlo
        if self.en_ejecucion and self.continuar:
            self.continuar = False  # Detiene el ciclo de ejecución
            event.ignore()  # Evita que la ventana se cierre
            # time.sleep(1)   # Espera a que el hilo termine de manera ordenada
        else:
            if self.bandera_p:
                with self.pause_condition:
                    self.pause_condition.notify()
            self.releaseMemory()
            event.accept()  # Permite que la ventana se cierre

    def keyPressEvent(self, event):
        texto_tecla = str(event.text())
        if texto_tecla == 'p':
            self.label_pause.setVisible(True)
            self.label_play.setVisible(False)
            self.bandera_p = True
        elif texto_tecla == 'c':
            self.label_pause.setVisible(False)
            self.label_play.setVisible(True)
            self.bandera_p = False
            with self.pause_condition:
                self.pause_condition.notify()
                
    def actualizar_interfaz(self):
        # This function is called every time the QTimer is triggered (1s)
        # LE Producer/Consumer
        self.le_p_state.setText(self.texto_p_estado) 
        self.le_p_num.setText(self.texto_p_num)
        self.le_p_position.setText(self.texto_p_posicion)
        self.le_c_state.setText(self.texto_c_estado)
        self.le_c_num.setText(self.texto_c_num)
        self.le_c_position.setText(self.texto_c_posicion)
        
        # Buffer text´s
        self.le_turn.setText(self.texto_turno)
        if self.texto_turno is "Productor":
            self.le_amount.setText(self.texto_p_num)
        else:
            self.le_amount.setText(self.texto_c_num)
        self.progressBar.setValue(int(self.texto_pgbar))
        
        # Animation icon Producer/Consumer
        if self.texto_turno is "Productor":
            self.label_p_work.setVisible(True)      # Etiqueta de trabajo Productor
            self.label_p_sleep.setVisible(False)    # Etiqueta de dormido Productor
            self.label_c_work.setVisible(False)     # Etiqueta de trabajo Consumidor
            self.label_c_sleep.setVisible(True)     # Etiqueta de dormido Consumidor
        else:
            self.label_c_work.setVisible(True)      # Etiqueta de trabajo Consumidor
            self.label_c_sleep.setVisible(False)    # Etiqueta de dormido Consumidor
            self.label_p_work.setVisible(False)     # Etiqueta de trabajo Productor
            self.label_p_sleep.setVisible(True)     # Etiqueta de dormido Productor

        # Taco Icons animation
        for i in range(20):
            if i in self.lista_taco:
                self.labels_taco[i].setVisible(True)
            else:
                self.labels_taco[i].setVisible(False)
        
                        

    def terminar_hilo(self):
        if self.en_ejecucion:
            self.en_ejecucion = False
            self.reiniciar_programa()
            # self.hilo.join()  # Espera a que el hilo termine de manera ordenada

    def back_end(self):
        if not self.en_ejecucion:
            if self.hilo:
                self.hilo.join()
            self.en_ejecucion = True
            self.continuar = True
            self.hilo = threading.Thread(target=self.production)
            self.hilo.start()
            
    # -----------------------------------------------------------------------------------

    def update_state(self, turn):
        if turn == 1: # Turno del productor
            if not self.circular_queue.isfull():    # Queue is not full, producer's turn
                self.producer.state = "working"
                self.customer.state = "sleeping"
                self.texto_turno = "Productor"
            else:                                   # Queue is full, customer's turn
                self.producer.state = "sleeping"
                self.customer.state = "working"
                self.texto_turno = "Consumidor"
                
        else: # Turno del consumidor
            if not self.circular_queue.isempty():   # Queue is not empty, customer's turn
                self.producer.state = "sleeping"
                self.customer.state = "working"
                self.texto_turno = "Consumidor"
            else:                                   # Queue is empty, producer's turn
                self.producer.state = "working"
                self.customer.state = "sleeping"
                self.texto_turno = "Productor"

    def update_producer(self):
        self.producer.number_products -= 1
        self.texto_p_num = str(self.producer.number_products)
        self.texto_p_estado = str(self.producer.state)
        
    
    def update_customer(self):
        self.customer.number_products -= 1
        self.texto_c_num = str(self.customer.number_products)
        self.texto_c_estado = str(self.customer.state)
        
        
    def update_pg_bar(self, num):
        percentage = int((100 / MAX_QUEUE_SIZE) * num)
        self.texto_pgbar = str(percentage)
    
    def pause(self):
        if self.bandera_p:
            with self.pause_condition:
                self.pause_condition.wait()
    
    def production(self):
        idx_producer = 0
        idx_customer = 0
        # Ciclo de produccion(1) / consumo(2)
        while self.continuar:
            # Seleccionar turno
            self.pause()
            self.update_state(select_turn())
            if self.producer.state is "working":
                self.producer.number_products = calculate_num_products()
                while not self.circular_queue.isfull() and self.producer.number_products > 0 and self.continuar:
                    self.pause()
                    self.update_producer()
                    self.circular_queue.enqueue(self.producer.get_element())    # Agregar elemento a la cola e incrementarlo (en produccion.py)
                    self.update_pg_bar(self.circular_queue.length)
                    self.lista_taco.append(idx_producer)
                    idx_producer = (idx_producer + 1) % MAX_QUEUE_SIZE  # Asegura que el índice se mantenga dentro de 0-19
                    self.texto_p_posicion = str(idx_producer)
                    time.sleep(1)
                self.producer.number_products = 0 # Reiniciar contador
                self.texto_p_num = str(self.producer.number_products)
                time.sleep(1)
            else:
                self.customer.number_products = calculate_num_products()
                while not self.circular_queue.isempty() and self.customer.number_products > 0 and self.continuar:
                    self.pause()
                    self.update_customer()
                    self.circular_queue.dequeue()
                    self.update_pg_bar(self.circular_queue.length)
                    self.lista_taco.pop(0)  # Eliminar el primer elemento de la lista
                    idx_customer = (idx_customer + 1) % MAX_QUEUE_SIZE  # Asegura que el índice se mantenga dentro de 0-19
                    self.texto_c_posicion = str(idx_customer)
                    time.sleep(1)
                self.customer.number_products = 0 # Reiniciar contador 
                self.texto_c_num = str(self.customer.number_products)
                time.sleep(1)
        self.texto_p_posicion = "0"
        self.texto_c_posicion = "0"
        self.terminar_hilo()
