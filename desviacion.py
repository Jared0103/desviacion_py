import math
import csv

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def get_values(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values

def read_data_from_csv(file_path):
    linked_list = LinkedList()
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for value in row:
                    try:
                        number = float(value)
                        linked_list.append(number)
                    except ValueError:
                        print(f"Advertencia: '{value}' no es un número válido y será ignorado.")
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
        return None
    return linked_list

def calculate_mean(linked_list):
    values = linked_list.get_values()
    if not values:
        return 0
    return sum(values) / len(values)

def calculate_standard_deviation(linked_list, mean):
    values = linked_list.get_values()
    if not values:
        return 0
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

def display_results(mean, std_dev):
    print(f"Media: {mean}")
    print(f"Desviación Estándar: {std_dev}")

def main():
    file_path = input("Ingrese la ruta del archivo CSV: ")
    linked_list = read_data_from_csv(file_path)
    if linked_list is not None:
        mean = calculate_mean(linked_list)
        std_dev = calculate_standard_deviation(linked_list, mean)
        display_results(mean, std_dev)

if __name__ == "__main__":
    main()
