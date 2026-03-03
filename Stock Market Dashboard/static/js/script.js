function renderStockChart(data, chartId='stockChart', label='Closing Price', color='#2ecc71'){
    const ctx = document.getElementById(chartId).getContext('2d');
    const labels = data.map(d => d.Date);
    const values = data.map(d => d.Close);

    return new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: values,
                borderColor: color,
                backgroundColor: color+'33', // semi-transparent fill
                fill: true,
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: true } },
            scales: {
                x: { display: true, title: { display: true, text: 'Date' } },
                y: { display: true, title: { display: true, text: 'Price ($)' } }
            }
        }
    });
}