from django.shortcuts import render
from .models import DataPoint
import matplotlib.pyplot as plt
import io
import urllib, base64

def generate_graph(request):
    data_points = DataPoint.objects.all()
    x = [point.x_value for point in data_points]
    y = [point.y_value for point in data_points]

    plt.plot(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Graph Title')
    plt.grid(True)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graph = base64.b64encode(image_png).decode('utf-8')
    return render(request, 'graph.html', {'graph': graph})
