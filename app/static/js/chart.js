document.addEventListener('DOMContentLoaded', function() {
    fetchDataAndRenderChart();
});

function fetchDataAndRenderChart() {
    fetch('/graph-data')
        .then(response => response.json())
        .then(data => {
            const labels = data.labels;
            const values = data.values;

            const ctx = document.getElementById('canva-dash').getContext('2d');

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Tickets por Cliente',
                        data: values,
                        backgroundColor: 'rgba(54, 162, 235, 0.6)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                    }]
                },
                options: {
                    responsive: false,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching data:', error));
}
