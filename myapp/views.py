from django.shortcuts import render

# Create your views here.

import pandas as pd
from django.shortcuts import render
from .forms import CSVUploadForm
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
import base64

def index(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            data = pd.read_csv(csv_file)

            # Handle missing values
            missing_values = data.isnull().sum().to_dict()

            # Perform data analysis
            summary_stats = data.describe().to_html()
            first_rows = data.head().to_html()

            # Generate histograms
            plots = []
            for column in data.select_dtypes(include=['float', 'int']).columns:
                plt.figure()
                sns.histplot(data[column].dropna(), kde=True)
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                plt.close()
                buf.seek(0)
                image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                plots.append(image_base64)

            context = {
                'form': form,
                'summary_stats': summary_stats,
                'first_rows': first_rows,
                'missing_values': missing_values,
                'plots': plots,
            }
            return render(request, 'myapp/results.html',context)
    else:
        form = CSVUploadForm()

    return render(request, 'myapp/index.html', {'form': form})
