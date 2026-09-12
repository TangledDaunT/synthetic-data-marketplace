from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'dev-key-for-demo'

# Mock data for dataset catalog
DATASETS = [
    {
        'id': 1,
        'name': 'Satellite Crop Health',
        'description': 'Normalized Difference Vegetation Index (NDVI) time series for major agricultural regions.',
        'category': 'Geospatial',
        'privacy_level': 'Synthetic',
        'size_mb': 120,
        'price_per_query': 0.02
    },
    {
        'id': 2,
        'name': 'Anonymized Mobility Traces',
        'description': 'Aggregated vehicle trajectories from urban areas, preserving travel patterns while ensuring differential privacy.',
        'category': 'Transportation',
        'privacy_level': 'Synthetic',
        'size_mb': 85,
        'price_per_query': 0.015
    },
    {
        'id': 3,
        'name': 'Synthetic Electronic Health Records',
        'description': 'Patient visit histories with conditions, medications, and outcomes, generated to mimic real EHR distributions.',
        'category': 'Healthcare',
        'privacy_level': 'Synthetic',
        'size_mb': 210,
        'price_per_query': 0.05
    }
]

@app.route('/')
def index():
    return render_template('index.html', datasets=DATASETS)

@app.route('/request', methods=['POST'])
def request_data():
    dataset_id = int(request.form.get('dataset_id'))
    use_case = request.form.get('use_case', '')
    # In real system, trigger generation job and notify user
    flash(f'Request submitted for dataset #{dataset_id}. We will notify you when synthetic data is ready.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Run on all interfaces so tailscale can reach it
    app.run(host='0.0.0.0', port=5000, debug=True)