import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()  # Aquí usas plt
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    plt.savefig('pie.png')  # Guarda el gráfico como imagen
    plt.close()  # Cierra la figura después de guardarla
